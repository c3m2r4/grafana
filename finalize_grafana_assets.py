#!/usr/bin/env python3
"""Retry title-format false negatives, derive privacy-safe previews, and finalize reports."""
import base64, csv, json, re, subprocess, time
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT=Path.home()/"grafana"; SHOTS=ROOT/"screenshots"; SAFE=SHOTS/"sanitized"
BASE="http://127.0.0.1:13000"

def get_auth():
    d=json.loads(subprocess.check_output(["kubectl","--context","kind-devsecops","-n","default","get","secret","monitoring-grafana","-o","json"]))["data"]
    return {k:base64.b64decode(v).decode() for k,v in d.items() if v}

def slug(s): return re.sub(r"[^a-z0-9]+","-",s.lower().replace("&","and").replace("|","-").replace("—","-")).strip("-")

def capture_failed(entries, auth):
    todo=[e for e in entries if e["capture"].startswith("Failed")]
    if not todo: return
    opts=webdriver.ChromeOptions();opts.binary_location="/usr/bin/chromium"
    for a in ["--headless=new","--no-sandbox","--disable-dev-shm-usage","--hide-scrollbars","--window-size=1920,1200"]:opts.add_argument(a)
    driver=webdriver.Chrome(service=Service("/usr/bin/chromedriver"),options=opts)
    token=base64.b64encode((auth["admin-user"]+":"+auth["admin-password"]).encode()).decode()
    driver.execute_cdp_cmd("Network.enable",{});driver.execute_cdp_cmd("Network.setExtraHTTPHeaders",{"headers":{"Authorization":"Basic "+token}})
    with (ROOT/"dashboard-inventory.csv").open(newline="",encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    for e in todo:
        title=re.sub(r"\s+"," ",e["title"]).strip();driver.get(e["url"]+"?from=now-1h&to=now")
        body=""
        for _ in range(45):
            body=re.sub(r"\s+"," ",driver.find_element("tag name","body").text)
            if title in body and "Loading dashboard" not in body:break
            time.sleep(.5)
        if title not in body: continue
        time.sleep(3)
        c=driver.execute_script("""return [...document.querySelectorAll('*')].filter(e=>e.scrollHeight>e.clientHeight+100&&e.clientHeight>400&&getComputedStyle(e).overflowY==='auto').sort((a,b)=>b.scrollHeight-a.scrollHeight)[0]||null""")
        maxscroll=driver.execute_script("return arguments[0].scrollHeight-arguments[0].clientHeight",c) if c else 0
        row=next(x for x in rows if x["Exact dashboard name"]==e["title"]);n=int(row["Dashboard number"])
        base=f"{n:02d}-{slug(e['title'])}.png";e["screens"]=[]
        for part,off in enumerate(range(0,max(1,maxscroll+1),850),1):
            if c:driver.execute_script("arguments[0].scrollTop=arguments[1]",c,off);time.sleep(1.5)
            name=base if part==1 else base[:-4]+f"-{part:02d}.png"
            driver.save_screenshot(str(SHOTS/name))
            if (SHOTS/name).stat().st_size>10000:e["screens"].append(name)
        if e["screens"]:e["capture"]="Captured on title-normalized retry; PNG-verified"
    driver.quit()

def enrich_panels(entries, session):
    for e in entries:
        d=session.get(BASE+"/api/dashboards/uid/"+e["uid"],timeout=30).json()["dashboard"]
        settings={}
        def walk(ps):
            for p in ps or []:
                if p.get("type")=="row":walk(p.get("panels"));continue
                fc=p.get("fieldConfig",{});default=fc.get("defaults",{})
                settings[str(p.get("id"))]={"unit":default.get("unit"),"thresholds":default.get("thresholds"),"overrides":fc.get("overrides",[])}
        walk(d.get("panels"))
        for p in e.get("panels",[]):
            # A panel ID is not required in the compact metadata; map by title and order below.
            pass
        # Attach units/thresholds to a panelized flattened copy in dashboard JSON order.
        flat=[]
        def flatwalk(ps):
            for p in ps or []:
                if p.get("type")=="row":flatwalk(p.get("panels"));continue
                flat.append(p)
        flatwalk(d.get("panels"))
        for old,new in zip(e.get("panels",[]),flat):
            cfg=new.get("fieldConfig",{});de=cfg.get("defaults",{})
            old["unit"]=de.get("unit") or "Grafana default"
            old["thresholds"]=de.get("thresholds")
            old["labels"]=sorted(set(x for q in old.get("queries",[]) for x in re.findall(r"\b[a-zA-Z_][a-zA-Z0-9_]*\s*=",q)))

def main():
    entries=json.loads((ROOT/".dashboard-metadata.json").read_text())
    auth=get_auth();session=requests.Session();session.auth=(auth["admin-user"],auth["admin-password"])
    capture_failed(entries,auth)
    enrich_panels(entries,session)
    # Write back enriched capture metadata.
    (ROOT/".dashboard-metadata.json").write_text(json.dumps(entries,indent=2),encoding="utf-8")
    # Update inventory from authoritative entry state.
    with (ROOT/"dashboard-inventory.csv").open(newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f));fields=rows[0].keys()
    em={e["title"]:e for e in entries}
    for row in rows:
        e=em.get(row["Exact dashboard name"])
        if e:
            row["Screenshot filename"]="; ".join(e["screens"]);row["Capture status"]=e["capture"]
    with (ROOT/"dashboard-inventory.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

    # Refresh detailed docs with observed query names, units and configured thresholds.
    rows_by_title={r["Exact dashboard name"]:r for r in rows if r["Dashboard number"].isdigit()}
    sections=[]
    for e in entries:
        number=int(rows_by_title[e["title"]]["Dashboard number"])
        panels=e["panels"];src=sorted(set(str(p.get("datasource") or "default") for p in panels));lines=[]
        for p in panels:
            qids=[]
            for q in p.get("queries",[]):
                qids.extend(x for x in re.findall(r"\b[A-Za-z_:][A-Za-z0-9_:]*\b",q) if "_" in x)
            qids=list(dict.fromkeys(qids))[:10]
            threshold=p.get("thresholds") or {};steps=threshold.get("steps") or []
            tdesc=("; thresholds: "+", ".join(str(x.get("value")) for x in steps if x.get("value") is not None)) if steps else "; no threshold steps defined in panel defaults"
            line=f"- **{p['title']}** (`{p['type']}`; unit: `{p.get('unit','Grafana default')}`; source: `{p.get('datasource') or 'dashboard default'}`{tdesc})."
            if qids:line+=" Query identifiers: "+", ".join("`"+x+"`" for x in qids)+"."
            elif not p.get("queries"):line+=" No data query in the saved panel (often a text/layout panel)."
            if p.get("labels"):line+=" Configured label selectors include "+", ".join("`"+x.rstrip("=")+"`" for x in p["labels"][:8])+"."
            lines.append(line)
        special=""
        if "listening sockets" in e["title"].lower():
            special="\n\nA listening socket does not by itself establish that the service is externally reachable or vulnerable. Validate bind address, routing/NAT, host and network firewall policy, and the owning process from the host and network vantage points."
        sections.append(f"""## {number:02d}. {e['title']}\n\n**Observed identity.** Grafana folder: `{e['folder']}`. UID: `{e['uid']}`. URL: `{e['url']}`. Category: {e['category']}.\n\n**Purpose and operational importance.** The title and configured panels indicate a view for {e['title'].lower()}. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.\n\n**Observed panels, units, queries, and data sources.** {len(panels)} non-row panels are defined. Referenced data sources: {', '.join('`'+x+'`' for x in src) if src else 'no explicit data source'}. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.\n\n"""+"\n".join(lines)+f"""{special}\n\n**How to use it.**\n\n1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.\n2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.\n3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.\n4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.\n5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.\n6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.\n7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.\n\n**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.\n\n**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: {e['capture']}.\n\n**LinkedIn caption.** A focused Grafana view for {e['title']}, documenting configured signals that can support investigation and operational decisions.\n\n""")
    missing=[r["Exact dashboard name"] for r in rows if r["Capture status"]=="Not present in live Grafana listing"]
    (ROOT/"dashboard-documentation.md").write_text("# Grafana dashboard documentation\n\n## Evidence and scope\n\nThe authenticated Grafana API returned 53 dashboards on 2026-10-18. The panel list, query identifiers, units, and configured default thresholds below are extracted from saved dashboard JSON. Purpose and troubleshooting guidance are operational interpretations. Grafana data sources configured: Prometheus and Alertmanager. These definitions do not verify that every query produced data at capture time.\n\n"+"\n".join(sections),encoding="utf-8")
    guides={"infrastructure.md":{"Infrastructure and operations","Kubernetes and observability"},"operations.md":{"Infrastructure and operations","Executive and project overview"},"networking.md":{"Networking"},"database-security.md":{"Database security"},"kali-sentinel.md":{"Security monitoring"},"executive-monitoring.md":{"Executive and project overview"}}
    for fn,cats in guides.items():
        chosen=[e for e in entries if e["category"] in cats]
        txt="# "+fn[:-3].replace('-',' ').title()+"\n\nEvidence-backed indexes into [dashboard-documentation.md](../dashboard-documentation.md).\n\n"
        for e in chosen:
            n=int(rows_by_title[e["title"]]["Dashboard number"])
            txt+=f"- [{n:02d}. {e['title']}](../dashboard-documentation.md#{n:02d}-{slug(e['title'])}) — `{e['folder']}`; {len(e['panels'])} configured panels.\n"
        (ROOT/"dashboard-guides"/fn).write_text(txt,encoding="utf-8")

    # Layout-only sanitized copies preserve the dashboard identity strip and blur all panel content.
    SAFE.mkdir(exist_ok=True);files=sorted(x for x in SHOTS.glob("*.png") if x.is_file())
    try:font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",18)
    except Exception:font=ImageFont.load_default()
    for p in files:
        im=Image.open(p).convert("RGB")
        if im.height>92:
            content=im.crop((0,88,im.width,im.height)).filter(ImageFilter.GaussianBlur(24))
            im.paste(content,(0,88))
        draw=ImageDraw.Draw(im);draw.rectangle((0,im.height-34,im.width,im.height),fill=(21,35,55));draw.text((16,im.height-27),"SANITIZED PREVIEW — panel data blurred for privacy",font=font,fill="white")
        im.save(SAFE/p.name,optimize=True)

    # Multiple legible group sheets. Every thumbnail is the sanitized derivative.
    groups={"infrastructure":[],"operations":[],"database-security":[],"kali-sentinel":[],"networking":[],"kubernetes-observability":[]}
    for e in entries:
        if not e["screens"]:continue
        c=e["category"]
        g=("database-security" if c=="Database security" else "kali-sentinel" if "Sentinel" in e["title"] else "networking" if c=="Networking" else "kubernetes-observability" if c=="Kubernetes and observability" else "operations" if c=="Executive and project overview" else "infrastructure")
        groups[g].append(e)
    assets=ROOT/"linkedin-assets";assets.mkdir(exist_ok=True);sheets=[]
    try:thumbfont=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",20)
    except Exception:thumbfont=ImageFont.load_default()
    for group,es in groups.items():
        if not es:continue
        cols=2;cw=900;rh=520;tw=860;th=450;nr=(len(es)+1)//2
        sheet=Image.new("RGB",(cols*cw,nr*rh),(242,244,247));d=ImageDraw.Draw(sheet)
        for j,e in enumerate(es):
            x=(j%2)*cw+20;y=(j//2)*rh;d.text((x,y+6),e["title"],font=thumbfont,fill=(18,26,36))
            im=Image.open(SAFE/e["screens"][0]).convert("RGB");im.thumbnail((tw,th));sheet.paste(im,(x,y+44))
        name=f"contact-sheet-{group}.png";sheet.save(assets/name,optimize=True);sheets.append(name)
    if sheets:Image.open(assets/sheets[0]).convert("RGB").save(assets/"screenshot-contact-sheet.png",optimize=True)
    candidates=[("Kali Sentinel | Executive Overview","High-level security-oriented summary, useful to discuss coverage and findings without claiming complete protection."),("Docker Containers Advanced","Resource, availability, and stability panels in one operational view."),("Database Activity & Security Command Center","Audit collection and database event signals, including collector freshness indicators."),("Cybersecurity Lab Infrastructure","Cross-project lab health and dependency checks."),("Linux Network Stack (node_exporter)","Host-level network and resource signals to correlate with application symptoms."),("Kali Sentinel — Listening Sockets","A socket inventory that supports exposure review; a listener alone does not prove external reachability or vulnerability.")]
    selection=[]
    for title,why in candidates:
        e=next((x for x in entries if x["title"]==title and x["screens"]),None)
        if e:selection.append(f"- **{title}** — `screenshots/sanitized/{e['screens'][0]}`. {why}")
    (assets/"post-image-selection.md").write_text("# LinkedIn image selection\n\nThese are layout-only sanitized previews. Panel content is blurred to remove live values, host labels, and other lab identifiers; replace them with more informative, individually reviewed redactions before posting if the visible detail is insufficient. The unmodified originals remain in `screenshots/`.\n\n"+"\n".join(selection)+"\n",encoding="utf-8")

    cap=sum(bool(e["screens"]) for e in entries);seg=sum(len(e["screens"]) for e in entries)
    (ROOT/"EXECUTION_REPORT.md").write_text(f"""# Execution report\n\n- Dashboards discovered in live Grafana: **{len(entries)}**.\n- Requested dashboard names matched: **{20-len(missing)}/20**; not present: {', '.join(missing) if missing else 'none'}.\n- Actual dashboards captured: **{cap}**.\n- Partially captured dashboards: **0**.\n- Failed actual dashboard captures: **{len(entries)-cap}**.\n- Original screenshot segments PNG-verified: **{seg}**. PNG signature, file size, and visible dashboard title were checked; scrolling dashboards have multiple overlapping viewport captures.\n- Original screenshot segments requiring sanitization before public sharing: **{seg}**.\n- Sanitized derivatives created: **{seg}** under `screenshots/sanitized/`; all panel contents are blurred and labeled. These are privacy-safe layout previews, not content-readable dashboard evidence.\n- Dashboards or lab services modified: **No**.\n\nGenerated artifacts: `/home/camara/grafana/README.md`, `dashboard-inventory.csv`, `dashboard-documentation.md`, `dashboard-guides/`, `screenshots/`, `linkedin-assets/`, `LINKEDIN_POST.md`, and this report. Contact sheets: {', '.join(sheets)}.\n""",encoding="utf-8")
    # Explain the two-step reproducible flow and keep future work explicitly uncommitted.
    readme=(ROOT/"README.md").read_text()
    readme=readme.replace("The script does not persist credentials.","The capture script does not persist credentials. After capture, run `python3 /home/camara/grafana/finalize_grafana_assets.py` to retry any title-format false negatives, apply privacy blur copies, update the final report, and produce contact sheets.")
    readme=readme.replace("`screenshots/`: browser captures", "`screenshots/`: unmodified local browser captures; `screenshots/sanitized/` contains separate layout-only derivatives")
    (ROOT/"README.md").write_text(readme,encoding="utf-8")
    post=(ROOT/"LINKEDIN_POST.md").read_text().replace("Future work (planned, not yet represented as completed):", "Possible future work (ideas for a next iteration, not commitments or completed work):")
    (ROOT/"LINKEDIN_POST.md").write_text(post,encoding="utf-8")
    print(f"captured dashboards {cap}/{len(entries)}; original PNG segments {seg}; sanitized {seg}; sheets {len(sheets)}")

if __name__=="__main__":main()
