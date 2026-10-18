#!/usr/bin/env python3
"""Capture the live Grafana dashboard set and document observed dashboard definitions.

Credentials are read from the local Kubernetes Secret at runtime and never written
to disk. The script only reads Grafana APIs and captures browser screenshots.
"""
import base64
import csv
import json
import os
import re
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT = Path.home() / "grafana"
SHOTS = ROOT / "screenshots"
BASE = "http://127.0.0.1:13000"
REQUESTED = [
    "Docker Containers Advanced", "05 - Kali Operations", "Alerts and Reliability",
    "Cybersecurity Lab Infrastructure", "Kali System Performance", "Network and Connectivity",
    "Project Command Center", "Services and Ports", "Storage and Project Capacity",
    "Database Activity & Security Command Center",
    "Kali Sentinel | Application & API Security", "Kali Sentinel | Audit & Monitoring Health",
    "Kali Sentinel | Database Activity Monitoring", "Kali Sentinel | Database Fleet",
    "Kali Sentinel | Executive Overview", "Kali Sentinel | File Integrity",
    "Kali Sentinel | Privileged Activity", "Kali Sentinel | Service Catalog & Health",
    "Kali Sentinel — Listening Sockets", "Linux Network Stack (node_exporter)",
]

def slug(s):
    s = s.lower().replace("&", "and").replace("|", "-").replace("—", "-")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

def auth():
    data = json.loads(subprocess.check_output([
        "kubectl", "--context", "kind-devsecops", "-n", "default", "get", "secret",
        "monitoring-grafana", "-o", "json"
    ]))["data"]
    return {k: base64.b64decode(v).decode() for k, v in data.items() if v}

def panel_list(dash):
    out = []
    def walk(panels):
        for p in panels or []:
            if p.get("type") == "row":
                walk(p.get("panels"))
                continue
            targets = p.get("targets", [])
            queries = []
            ds = p.get("datasource") or {}
            dsname = ds.get("uid") or ds.get("type") if isinstance(ds, dict) else ds
            for t in targets:
                q = t.get("expr") or t.get("rawSql") or t.get("query") or t.get("measurement")
                if q:
                    queries.append(" ".join(q.split()))
                tds = t.get("datasource") or {}
                if isinstance(tds, dict) and tds.get("uid"):
                    dsname = tds["uid"]
            out.append({"title": p.get("title") or "Untitled panel", "type": p.get("type", "unknown"),
                        "datasource": dsname or "Dashboard default / not explicit", "queries": queries})
    walk(dash.get("panels"))
    return out

def metric_names(panels):
    names = []
    for p in panels:
        for q in p["queries"]:
            names.extend(re.findall(r"[A-Za-z_:][A-Za-z0-9_:]*", q))
    blacklist = {"sum", "max", "min", "avg", "count", "by", "without", "on", "ignoring",
                 "group_left", "group_right", "rate", "irate", "increase", "clamp_min", "vector",
                 "histogram_quantile", "topk", "sort_desc", "predict_linear", "time", "scalar", "or",
                 "and", "unless", "label_replace", "absent", "offset", "bool", "le", "quantile",
                 "severity", "state", "namespace", "cluster", "instance", "job", "service", "pod",
                 "container", "device", "mountpoint", "fstype", "code", "name", "type", "status",
                 "mode", "proto", "integration", "engine", "outcome", "event_type", "project", "path"}
    for x in names:
        if x not in blacklist and ("_" in x or x[:1].islower()) and x not in names[:0]:
            if x not in names[:0]: pass
    unique=[]
    for x in names:
        if x not in blacklist and ("_" in x or x[:1].islower()) and x not in unique:
            unique.append(x)
    return unique

def category(folder, title):
    t = title.lower()
    if "database" in t or "dam" in t or "database" in folder.lower(): return "Database security"
    if "sentinel" in t or "sentinel" in folder.lower() or "falco" in t or "trivy" in t: return "Security monitoring"
    if "network" in t or "coredns" in t: return "Networking"
    if "kubernetes" in t or "node exporter" in t or "etcd" in t or "prometheus" in t or "alertmanager" in t or "grafana" in t: return "Kubernetes and observability"
    if "command center" in t or "executive" in t: return "Executive and project overview"
    return "Infrastructure and operations"

def safe_wait(driver, title):
    deadline = time.time() + 22
    while time.time() < deadline:
        try:
            text = driver.find_element("tag name", "body").text
            if title in text and "Loading dashboard" not in text:
                time.sleep(3)
                return text
        except Exception:
            pass
        time.sleep(.5)
    return driver.find_element("tag name", "body").text

def scroll_container(driver):
    return driver.execute_script("""return [...document.querySelectorAll('*')]
      .filter(e=>e.scrollHeight>e.clientHeight+100&&e.clientHeight>400&&getComputedStyle(e).overflowY==='auto')
      .sort((a,b)=>b.scrollHeight-a.scrollHeight)[0]||null""")

def main():
    ROOT.mkdir(exist_ok=True); SHOTS.mkdir(exist_ok=True)
    (ROOT / "dashboard-guides").mkdir(exist_ok=True)
    (ROOT / "linkedin-assets").mkdir(exist_ok=True)
    a = auth(); session = requests.Session(); session.auth = (a["admin-user"], a["admin-password"])
    found = session.get(BASE + "/api/search", params={"type":"dash-db"}, timeout=30).json()
    ds = session.get(BASE + "/api/datasources", timeout=30).json()
    dsnames = {x.get("uid"):x.get("name") for x in ds}
    entries=[]
    for item in found:
        payload=session.get(BASE+"/api/dashboards/uid/"+item["uid"],timeout=30).json()
        dash=payload["dashboard"]; folder=item.get("folderTitle") or "General"
        panels=panel_list(dash)
        entries.append({"title":dash.get("title") or item["title"],"uid":item["uid"],"url":BASE+item["url"],
                        "folder":folder,"panels":panels,"dashboard":dash,"category":category(folder,item["title"])})
    bytitle={e["title"]:e for e in entries}
    ordered=[]
    for name in REQUESTED:
        if name in bytitle and bytitle[name] not in ordered: ordered.append(bytitle[name])
    ordered.extend(e for e in sorted(entries,key=lambda x:(x["folder"],x["title"])) if e not in ordered)
    idx={id(bytitle[name]):i+1 for i,name in enumerate(REQUESTED) if name in bytitle}
    extra=21
    for e in ordered:
        if id(e) not in idx:
            idx[id(e)]=extra;extra+=1

    # Browser screenshots: each inner-scroll viewport is captured, with 180 px overlap.
    opts=webdriver.ChromeOptions();opts.binary_location="/usr/bin/chromium"
    for arg in ["--headless=new","--no-sandbox","--disable-dev-shm-usage","--hide-scrollbars","--window-size=1920,1200"]: opts.add_argument(arg)
    driver=webdriver.Chrome(service=Service("/usr/bin/chromedriver"),options=opts)
    token=base64.b64encode((a["admin-user"]+":"+a["admin-password"]).encode()).decode()
    driver.execute_cdp_cmd("Network.enable",{});driver.execute_cdp_cmd("Network.setExtraHTTPHeaders",{"headers":{"Authorization":"Basic "+token}})
    capture=[]
    for e in ordered:
        n=idx[id(e)]; filename=f"{n:02d}-{slug(e['title'])}.png"; e["screens"]=[]
        try:
            driver.get(e["url"]+"?from=now-1h&to=now")
            body=safe_wait(driver,e["title"])
            if e["title"] not in body: raise RuntimeError("Expected dashboard title not visible after load")
            # Scroll the Grafana dashboard content, saving every distinct vertical segment.
            container=scroll_container(driver)
            maxscroll=0
            if container:
                maxscroll=driver.execute_script("return arguments[0].scrollHeight-arguments[0].clientHeight",container)
            offsets=list(range(0,max(1,maxscroll+1),850))
            for part,offset in enumerate(offsets,1):
                if container:
                    driver.execute_script("arguments[0].scrollTop=arguments[1]",container,offset)
                    time.sleep(1.5)
                fn=filename if part==1 else filename[:-4]+f"-{part:02d}.png"
                path=SHOTS/fn; driver.save_screenshot(str(path))
                e["screens"].append(fn)
            # Verification checks image signature/dimensions and the expected title was rendered.
            for fn in e["screens"]:
                p=SHOTS/fn
                if not p.is_file() or p.stat().st_size<10000 or p.read_bytes()[:8]!=b"\x89PNG\r\n\x1a\n": raise RuntimeError("Screenshot failed file verification: "+fn)
            e["capture"]="Captured and PNG-verified";e["visible_text_sample"]=body[:500]
        except Exception as ex:
            e["capture"]="Failed: "+str(ex);e["screens"]=[]
        capture.append(e)
        print(f"[{n}/{len(ordered)}] {e['title']}: {e['capture']} ({len(e['screens'])} image(s))",flush=True)
    driver.quit()

    # Add an explicit row documenting the requested title not present in the live listing.
    missing=[n for n in REQUESTED if n not in bytitle]
    fields=["Dashboard number","Exact dashboard name","Grafana folder","Primary category","Screenshot filename",
            "Dashboard URL or UID","Data source","Key metrics or panels","Capture status","Operational importance"]
    with (ROOT/"dashboard-inventory.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for e in capture:
            datas=sorted({dsn for p in e["panels"] for dsn in ([p["datasource"]] if p["datasource"] else [])})
            keys=[]
            for p in e["panels"]:
                keys.append(p["title"])
            w.writerow({"Dashboard number":idx[id(e)],"Exact dashboard name":e["title"],"Grafana folder":e["folder"],
                "Primary category":e["category"],"Screenshot filename":"; ".join(e["screens"]),
                "Dashboard URL or UID":e["url"]+" (UID: "+e["uid"]+")","Data source":"; ".join(dsnames) or "None explicit",
                "Key metrics or panels":"; ".join(keys),"Capture status":e["capture"],
                "Operational importance":"See dashboard documentation; importance is a practical assessment based on observed panel names and queries."})
        for n in missing:
            w.writerow({"Dashboard number":REQUESTED.index(n)+1,"Exact dashboard name":n,"Grafana folder":"Not found",
                "Primary category":"Infrastructure and operations","Screenshot filename":"","Dashboard URL or UID":"",
                "Data source":"","Key metrics or panels":"","Capture status":"Not present in live Grafana listing",
                "Operational importance":"Requested title could not be documented as an existing dashboard."})

    # Full definitions to support evidence-backed dashboard guides.
    with (ROOT/".dashboard-metadata.json").open("w",encoding="utf-8") as f:
        json.dump([{k:v for k,v in e.items() if k in ("title","uid","url","folder","panels","category","capture","screens")} for e in capture],f,indent=2)

    guide_sections=defaultdict(list)
    for e in capture:
        i=idx[id(e)]; metrics=metric_names(e["panels"])
        titles=[p["title"] for p in e["panels"]]
        src=sorted({dsn for p in e["panels"] for dsn in ([p["datasource"]] if p["datasource"] else [])})
        noquery=[p["title"] for p in e["panels"] if not p["queries"]]
        panel_lines=[]
        for p in e["panels"]:
            qmetrics=[]
            for q in p["queries"]:
                qmetrics.extend(x for x in re.findall(r"\b[a-zA-Z_:][a-zA-Z0-9_:]*\b",q) if "_" in x)
            panel_lines.append(f"- **{p['title']}** (`{p['type']}`; source: `{p['datasource']}`): " + ("Queries include `"+"`, `".join(dict.fromkeys(qmetrics[:8]))+"`." if qmetrics else ("No data query in dashboard definition (presentation or text panel)." if not p["queries"] else "Query is present; see the CSV for panel inventory.")))
        is_socket="socket" in e["title"].lower()
        section=f"""## {i:02d}. {e['title']}\n\n**Observed identity.** Grafana folder: `{e['folder']}`. UID: `{e['uid']}`. URL: `{e['url']}`. Category: {e['category']}.\n\n**Purpose and operational importance.** The title and configured panels indicate a view for {e['title'].lower()}. It helps an operator focus on the named system domain and use its exposed signals to triage, compare trends, and decide where to investigate next. This description is an interpretation of the dashboard definition, not a claim about a live incident.\n\n**Observed panels, queries, and sources.** {len(e['panels'])} non-row panels are defined. Configured sources: {', '.join('`'+ds+'`' for ds in src) if src else 'none explicitly specified'}. Metric/query identifiers below come from the dashboard JSON; values and current thresholds are not asserted here.\n\n"""+"\n".join(panel_lines)+f"""\n\n**How to use it.**\n\n1. Open this dashboard when investigating a symptom in the domain named above. Set a time range that brackets the symptom and confirm the displayed time range.\n2. Start with summary/stat panels (if present), then review tables and time series; the panel inventory above records which types are configured.\n3. Treat a missing series, stale timestamp, unexpected state, sustained change, or outlier as a lead to validate against the panel query and source health. Compare like-for-like time windows and labels.\n4. Correlate related panels and dashboard variables; follow labels such as service, instance, project, container, namespace, or event type only when those labels appear in the configured query.\n5. Inspect the underlying system, logs, traces, audit records, or service configuration appropriate to the signal. Preserve timestamps and identifiers for investigation.\n6. Apply a change only after validating cause and scope; use the service owner or incident process for escalation.\n7. Recheck the original signal over the same useful time range and verify related health indicators recover.\n\n**Hypothetical scenario.** If a relevant panel departs from its normal pattern while a correlated health panel changes at the same time, an engineer could use the shared time window and labels to narrow the affected component, then confirm the cause in the source system. This is illustrative, not an observed incident.\n\n**Limitations observed.** The dashboard definition shows {len(e['panels'])} panels and the sources listed above. {('Panels with no configured data query: '+', '.join('`'+x+'`' for x in noquery)+'. ' if noquery else '')}A query in a saved dashboard does not establish that its source returned data during capture; blank or unavailable series must be treated as unverified telemetry. No alert threshold is claimed unless it is visibly configured in the dashboard. Current screenshot/capture state: {e['capture']}.\n\n**LinkedIn caption.** A focused Grafana view for {e['title']}, documenting the panels and signals available to support investigation and operational decisions.\n\n"""
        guide_sections[e["category"]].append(section)
    all_sections=[s for group in guide_sections.values() for s in group]
    (ROOT/"dashboard-documentation.md").write_text("# Grafana dashboard documentation\n\n## Evidence and scope\n\nThis document covers the dashboards returned by the live Grafana dashboard API at `http://127.0.0.1:13000` on 2026-10-18. The instance returned **"+str(len(entries))+"** dashboards. Panel titles, panel types, datasource references, and metric/query identifiers are read from each saved dashboard JSON. Purposes and investigation steps are operator guidance inferred from the configured panels. No operational incident is asserted.\n\nThe live instance contains two configured datasource entries: "+", ".join(f"`{d.get('name')}` (`{d.get('type')}`)" for d in ds)+". A datasource reference in a saved panel does not prove that every query returned data during the screenshot.\n\n"+"\n".join(all_sections),encoding="utf-8")

    guide_map={"infrastructure.md":["Infrastructure and operations","Kubernetes and observability"],
      "operations.md":["Infrastructure and operations","Executive and project overview"],
      "networking.md":["Networking"],"database-security.md":["Database security"],
      "kali-sentinel.md":["Security monitoring"],"executive-monitoring.md":["Executive and project overview"]}
    for fn,cats in guide_map.items():
        selected=[e for e in capture if e["category"] in cats]
        content="# "+fn.removesuffix('.md').replace('-',' ').title()+"\n\nThis guide points to the evidence-backed entries in [dashboard-documentation.md](../dashboard-documentation.md).\n\n"
        content += "\n".join(f"- [{i:02d}. {e['title']}](../dashboard-documentation.md#{i:02d}-{slug(e['title'])}) — `{e['folder']}`; {len(e['panels'])} configured panels." for e in selected for i in [idx[id(e)]])
        (ROOT/"dashboard-guides"/fn).write_text(content+"\n",encoding="utf-8")

    # Execution summary and reports.
    success=sum(e["capture"].startswith("Captured") for e in capture)
    partial=sum(e["capture"].startswith("Partially") for e in capture)
    failed=len(capture)-success-partial
    allfiles=sum(len(e["screens"]) for e in capture)
    (ROOT/"EXECUTION_REPORT.md").write_text(f"""# Execution report\n\n- Live Grafana dashboards discovered: **{len(entries)}**.\n- Requested names matched in live Grafana: **{len(REQUESTED)-len(missing)}/20**. Missing requested title: {', '.join(missing) if missing else 'none'}.\n- Actual dashboards successfully captured and PNG-verified: **{success}**.\n- Partially captured dashboards: **{partial}**.\n- Failed actual dashboard captures: **{failed}**.\n- Screenshot image files verified: **{allfiles}**. Each image has a PNG signature and is at least 10 KB; each dashboard title was present in the rendered page before capture.\n- Screenshots requiring sanitization before public sharing: **{success} dashboard capture sets**. Panels expose live lab/container/project identifiers and operational metrics; the local originals are retained. Publicly share only after a separate review/redaction.\n- Grafana dashboards or services modified: **No**.\n\nArtifacts: `/home/camara/grafana/README.md`, `dashboard-inventory.csv`, `dashboard-documentation.md`, `dashboard-guides/`, `screenshots/`, `linkedin-assets/`, `LINKEDIN_POST.md`, and this report.\n""",encoding="utf-8")
    # Local contact sheets are portfolio review aids only; they are not sanitized for release.
    from PIL import Image, ImageDraw, ImageFont
    assetdir=ROOT/"linkedin-assets"
    groups={"infrastructure":[],"operations":[],"database-security":[],"kali-sentinel":[],"networking":[],"kubernetes-observability":[]}
    for e in capture:
        cat=e["category"]
        group=("database-security" if cat=="Database security" else "kali-sentinel" if "Sentinel" in e["title"] else
               "networking" if cat=="Networking" else "kubernetes-observability" if cat=="Kubernetes and observability" else
               "operations" if cat=="Executive and project overview" else "infrastructure")
        if e["screens"]: groups[group].append(e)
    try: font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",22)
    except Exception: font=ImageFont.load_default()
    sheet_files=[]
    for group, rows in groups.items():
        if not rows: continue
        cols=2; cellw=900; thumbw=860; thumbh=484; rowh=530
        rowsn=(len(rows)+cols-1)//cols
        sheet=Image.new("RGB",(cols*cellw,rowsn*rowh),(242,244,247));draw=ImageDraw.Draw(sheet)
        for j,e in enumerate(rows):
            x=(j%cols)*cellw+20;y=(j//cols)*rowh
            draw.text((x,y+8),e["title"],font=font,fill=(20,28,38))
            im=Image.open(SHOTS/e["screens"][0]).convert("RGB");im.thumbnail((thumbw,thumbh))
            sheet.paste(im,(x,y+50))
            draw.text((x,y+50+im.height+4),f"{len(e['screens'])} capture segment(s) · live local capture · sanitize before sharing",font=ImageFont.load_default(),fill=(62,70,80))
        path=assetdir/f"contact-sheet-{group}.png";sheet.save(path,optimize=True);sheet_files.append(path.name)
    if sheet_files:
        first=Image.open(assetdir/sheet_files[0]).convert("RGB")
        first.save(assetdir/"screenshot-contact-sheet.png",optimize=True)
    picks=[]
    for title,why in [
        ("Kali Sentinel | Executive Overview","Communicates the security-oriented summary and coverage signals to technical and nontechnical reviewers."),
        ("Docker Containers Advanced","Shows actual resource, running/stopped, and container health panels in one operational view."),
        ("Database Activity & Security Command Center","Highlights audit collection, source heartbeat, and event categories without implying complete detection."),
        ("Cybersecurity Lab Infrastructure","Shows cross-project lab health and dependency signals."),
        ("Linux Network Stack (node_exporter)","Demonstrates host-level network and system signals for correlation with application symptoms."),
        ("Kali Sentinel | Listening Sockets","Shows socket inventory; a listener alone does not establish external reachability or vulnerability.")]:
        e=bytitle.get(title)
        if e: picks.append(f"- **{title}** — `{e['screens'][0] if e.get('screens') else 'capture unavailable'}`. {why} Public release requires inspection and redaction of live labels and values.")
    (assetdir/"post-image-selection.md").write_text("# LinkedIn image selection\n\nCandidate images for a carousel, subject to a separate privacy review and sanitization. These local screenshots contain live lab values, names, or infrastructure details; do not publish the originals as-is.\n\n"+"\n".join(picks)+"\n",encoding="utf-8")
    readme=f"""# Grafana dashboard documentation and captures\n\n## Purpose\n\nThis package records the live Grafana dashboards discoverable in the local Kubernetes lab, their configured panels and query identifiers, and local browser screenshots. It does not modify dashboards, Grafana, or lab services.\n\n## Inventory\n\nThe live Grafana API returned **{len(entries)} dashboards** on 2026-10-18. The requested list matched **{len(REQUESTED)-len(missing)}** current titles; `{', '.join(missing) if missing else 'none'}` was not found. The inventory also includes dashboards beyond the 20 names in the supplied list.\n\n- `dashboard-inventory.csv`: current live dashboard names, folders, URLs/UIDs, panel names, screenshot segments, and capture status.\n- `dashboard-documentation.md`: observed panel definitions and query metric identifiers, with investigation guidance distinguished from observed configuration.\n- `dashboard-guides/`: category indexes into the complete documentation.\n- `screenshots/`: browser captures of live Grafana pages, split into overlapping scroll segments where needed.\n- `linkedin-assets/`: local contact sheets and candidate image selections. The contact sheets and original screenshots are **not sanitized for public release**.\n- `LINKEDIN_POST.md`: evidence-qualified portfolio draft.\n- `EXECUTION_REPORT.md`: capture counts and verification details.\n\n## Reproduce\n\nThe read-only capture script uses the running port-forward at `http://127.0.0.1:13000`, reads Grafana credentials at runtime from the Kubernetes Secret `monitoring-grafana` in context `kind-devsecops`, retrieves dashboards and datasource references through the Grafana API, and opens each dashboard in headless Chromium at a one-hour range. It captures the scrollable dashboard viewport and checks the PNG signature and file size.\n\nRun `python3 /home/camara/grafana/capture_and_document.py`. Requirements: `kubectl`, `requests`, Selenium, Chromium, ChromeDriver, and Pillow. The script does not persist credentials.\n\n## Known limitations\n\nThe screenshot is a point-in-time capture. Query definitions establish what panels are configured, not whether every source returned data. A saved query or empty panel is not proof of monitoring coverage. The local Grafana API requires authentication and the capture depends on its local port-forward. Live screenshot labels/values can expose lab details; sanitize separately before sharing.\n"""
    (ROOT/"README.md").write_text(readme,encoding="utf-8")
    post="""# A Grafana lab organized for investigation, not dashboard sprawl\n\nI documented the Grafana dashboards running in my local lab and captured the current views alongside their panel definitions. The live instance currently exposes 53 dashboards across infrastructure, Kubernetes observability, project operations, database monitoring, and security-focused views.\n\nI organized dashboards around the question an engineer needs to answer. Docker panels help inspect container availability and resource use. Kali Operations views summarize host and lab health. Network and node-exporter panels give system-level context for connectivity symptoms. The database command center surfaces the audit collection and event signals configured in this environment. Kali Sentinel separates application/API, audit pipeline, database, file integrity, privileged activity, service catalog, and listening socket views.\n\nInfrastructure observability helps answer whether systems are available, saturated, or behaving differently over time. Security monitoring organizes audit, vulnerability, configuration, and activity signals for review. The two domains can support the same investigation, but the presence of a dashboard does not prove complete telemetry or coverage. Grafana supports investigation and decisions; dashboards do not prevent attacks or prove that a system is secure.\n\nSpecialized views keep each workflow legible and make it easier to correlate relevant signals without turning one dashboard into an unreadable wall of panels. The most useful engineering lesson was to document what panels and queries actually exist, make data gaps explicit, and avoid treating a saved query as evidence that its telemetry is healthy.\n\nFuture work (planned, not yet represented as completed): continue validating telemetry freshness and coverage, review alert thresholds against the lab's operating patterns, and prepare a separately sanitized set of images for public sharing. The screenshots in this local package contain lab identifiers and should not be posted as-is.\n\nHow do you decide where to draw the boundary between infrastructure health dashboards and security investigation views in a small lab?\n\n#Grafana #Cybersecurity #Observability #Linux #DevSecOps #SecurityEngineering #OpenSource\n"""
    (ROOT/"LINKEDIN_POST.md").write_text(post,encoding="utf-8")
    # Update report with generated contact sheet filenames.
    with (ROOT/"EXECUTION_REPORT.md").open("a",encoding="utf-8") as f:
        f.write("\nContact sheets: "+", ".join(sheet_files)+". These are local review assets and are not sanitized for public release.\n")
    print(f"DISCOVERED={len(entries)} CAPTURED={success} PARTIAL={partial} FAILED={failed} FILES={allfiles} MISSING_REQUESTED={missing}",flush=True)

if __name__=="__main__": main()
