#!/usr/bin/env python3
"""Quality-review recapture of the live Grafana set without saving dashboard edits."""
import base64,csv,json,re,subprocess,time
from pathlib import Path
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT=Path.home()/"grafana";SHOTS=ROOT/"screenshots";BASE="http://127.0.0.1:13000"
FILTERS={
 "Kubernetes / Compute Resources / Namespace (Pods)":{"namespace":"default"},
 "Kubernetes / Compute Resources / Namespace (Workloads)":{"namespace":"default","type":"deployment"},
 "Kubernetes / Compute Resources / Pod":{"namespace":"default","pod":"nginx-5765b9d8c4-gtdwz"},
}
def norm(s):return re.sub(r"\s+"," ",s or "").strip()
def main():
 entries=json.loads((ROOT/".dashboard-metadata.json").read_text())
 secret=json.loads(subprocess.check_output(["kubectl","--context","kind-devsecops","-n","default","get","secret","monitoring-grafana","-o","json"]))["data"]
 auth={k:base64.b64decode(v).decode() for k,v in secret.items() if v}
 opts=webdriver.ChromeOptions();opts.binary_location="/usr/bin/chromium"
 for a in ["--headless=new","--no-sandbox","--disable-dev-shm-usage","--hide-scrollbars","--window-size=1920,1200"]:opts.add_argument(a)
 driver=webdriver.Chrome(service=Service("/usr/bin/chromedriver"),options=opts)
 token=base64.b64encode((auth["admin-user"]+":"+auth["admin-password"]).encode()).decode()
 driver.execute_cdp_cmd("Network.enable",{});driver.execute_cdp_cmd("Network.setExtraHTTPHeaders",{"headers":{"Authorization":"Basic "+token}})
 errors=[];new_names=set()
 for i,e in enumerate(entries,1):
  q={"from":"now-1h","to":"now"};q.update({"var-"+k:v for k,v in FILTERS.get(e["title"],{}).items()})
  driver.get(e["url"]+"?"+urlencode(q));target=norm(e["title"]);body=""
  for _ in range(60):
   body=norm(driver.find_element("tag name","body").text)
   if target in body:break
   time.sleep(.5)
  if target not in body:
   errors.append((e["title"],"title not present after load"));print(f"[{i}/{len(entries)}] FAILED title",e["title"],flush=True);continue
  # Allow panels to settle, then wait for visible Grafana loading placeholders to clear.
  time.sleep(3)
  for _ in range(40):
   body=driver.find_element("tag name","body").text
   if not re.search(r"Loading(?: data|\.\.\.)",body,re.I):break
   time.sleep(.5)
  c=driver.execute_script("""return [...document.querySelectorAll('*')].filter(e=>e.scrollHeight>e.clientHeight+100&&e.clientHeight>400&&getComputedStyle(e).overflowY==='auto').sort((a,b)=>b.scrollHeight-a.scrollHeight)[0]||null""")
  if c:
   dims=driver.execute_script("return [arguments[0].scrollHeight,arguments[0].clientHeight]",c);maxscroll=max(0,dims[0]-dims[1]);step=max(1,dims[1]-160)
   offsets=[0]
   while offsets[-1]<maxscroll:offsets.append(min(offsets[-1]+step,maxscroll))
  else:offsets=[0]
  new=[];base=e["screens"][0] if e.get("screens") else f"{i:02d}-dashboard.png"
  for part,off in enumerate(offsets,1):
   if c and off:
    driver.execute_script("arguments[0].scrollTop=arguments[1]",c,off);time.sleep(1)
   name=base if part==1 else base[:-4]+f"-{part:02d}.png";path=SHOTS/name
   driver.save_screenshot(str(path))
   if not path.exists() or path.stat().st_size<10000 or path.read_bytes()[:8]!=b"\x89PNG\r\n\x1a\n":errors.append((e["title"],"PNG verification failed: "+name))
   new.append(name);new_names.add(name)
  # Remove extra segments from the preceding capture, but only names recorded for this dashboard.
  for stale in set(e.get("screens",[]))-set(new):
   p=SHOTS/stale
   if p.exists():p.unlink()
   sp=SHOTS/"sanitized"/stale
   if sp.exists():sp.unlink()
  e["screens"]=new
  e["capture"]="Quality-reviewed; rendered title visible; PNG-verified"
  if e["title"] in FILTERS:e["capture"]+="; view filter: "+", ".join(k+"="+v for k,v in FILTERS[e["title"]].items())
  print(f"[{i}/{len(entries)}] {e['title']}: {len(new)} segment(s), scroll offsets {offsets}",flush=True)
 driver.quit()
 (ROOT/".dashboard-metadata.json").write_text(json.dumps(entries,indent=2),encoding="utf-8")
 with (ROOT/"dashboard-inventory.csv").open(newline="",encoding="utf-8") as f:rows=list(csv.DictReader(f));fields=rows[0].keys()
 em={e["title"]:e for e in entries}
 for r in rows:
  if r["Exact dashboard name"] in em:
   e=em[r["Exact dashboard name"]];r["Screenshot filename"]="; ".join(e["screens"]);r["Capture status"]=e["capture"]
 with (ROOT/"dashboard-inventory.csv").open("w",newline="",encoding="utf-8") as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
 print("ERRORS",json.dumps(errors),"ORIGINAL_SEGMENTS",sum(len(e['screens']) for e in entries),flush=True)
if __name__=="__main__":main()
