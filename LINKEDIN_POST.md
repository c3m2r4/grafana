# A Grafana lab organized for investigation, not dashboard sprawl

I documented the Grafana dashboards running in my local lab and captured the current views alongside their panel definitions. The live instance currently exposes 53 dashboards across infrastructure, Kubernetes observability, project operations, database monitoring, and security-focused views.

I organized dashboards around the question an engineer needs to answer. A few examples from the live set:

- **Docker Containers Advanced** brings together total, running, and stopped container counts with CPU and memory use.
- **Alerts and Reliability** summarizes firing alerts, failed probes, unavailable scrape targets, and container/project attention states.
- **Cybersecurity Lab Infrastructure** rolls up project health, stopped lab containers, endpoint checks, VM count, and Docker daemon availability.
- **Database Activity & Security Command Center** exposes collector heartbeat and audit collection signals alongside authentication, privilege, DDL, and configuration activity categories.
- **Kali Sentinel | Executive Overview** places host CPU/memory and disk use next to alert, target, application check, and database activity signals.
- **Linux Network Stack (node_exporter)** includes connection tracking, TCP/UDP, softnet drops, interface traffic/errors, and interrupt/softirq panels.

Other Kali Sentinel dashboards split application/API, audit pipeline, database, file integrity, privileged activity, service catalog, and listening socket monitoring into focused investigations. For example, a listening socket is an inventory clue; its presence alone does not establish external reachability or vulnerability.

Infrastructure observability helps answer whether systems are available, saturated, or behaving differently over time. Security monitoring organizes audit, vulnerability, configuration, and activity signals for review. The two domains can support the same investigation, but the presence of a dashboard does not prove complete telemetry or coverage. Grafana supports investigation and decisions; dashboards do not prevent attacks or prove that a system is secure.

Specialized views keep each workflow legible and make it easier to correlate relevant signals without turning one dashboard into an unreadable wall of panels. The most useful engineering lesson was to document what panels and queries actually exist, make data gaps explicit, and avoid treating a saved query as evidence that its telemetry is healthy.

Possible future work (ideas for a next iteration, not commitments or completed work): continue validating telemetry freshness and coverage, review alert thresholds against the lab's operating patterns, and prepare selectively redacted public images that retain useful panel detail. See [`LINKEDIN_IMAGES.md`](LINKEDIN_IMAGES.md) for the recommended unblurred images and post sequence. The curated images are copies; the full capture archive remains under `screenshots/`.

How do you decide where to draw the boundary between infrastructure health dashboards and security investigation views in a small lab?

#Grafana #Cybersecurity #Observability #Linux #DevSecOps #SecurityEngineering #OpenSource
