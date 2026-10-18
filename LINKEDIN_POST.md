# A Grafana Lab Built for Investigation, Not Dashboard Sprawl

I’ve been documenting and refining the observability and security monitoring views in my local Grafana lab. The current inventory includes **53 dashboards** across infrastructure, Kubernetes, project operations, database monitoring, and security investigations.

The goal is to organize telemetry around the questions engineers need to answer while troubleshooting systems, reviewing activity, and assessing operational health.

A few examples:

🔹 **Docker Containers Advanced** brings together container counts and states with CPU and memory usage to support troubleshooting and resource analysis.

🔹 **Alerts and Reliability** surfaces firing alerts, failed probes, unavailable scrape targets, and other operational attention signals.

🔹 **Cybersecurity Lab Infrastructure** summarizes lab health through container states, endpoint checks, VM counts, and Docker daemon availability.

🔹 **Database Activity & Security Command Center** groups database audit signals with collector health, authentication activity, privilege changes, DDL operations, and configuration events.

🔹 **Kali Sentinel | Executive Overview** combines selected host health indicators with alert, target, application check, and database activity signals.

🔹 **Linux Network Stack (node_exporter)** provides host network visibility across connection tracking, TCP/UDP metrics, interface traffic and errors, softnet drops, interrupts, and softirqs.

The Kali Sentinel dashboards also separate application/API security, audit pipeline health, database activity, file integrity, privileged activity, service inventory, and listening sockets into focused investigation views. A listening socket is a useful inventory clue; it does not by itself establish external reachability or a vulnerability.

**Observability and security monitoring answer related but different questions.** Infrastructure dashboards help assess availability, performance, resource saturation, and changes in system behavior. Security dashboards organize audit events, application activity, configuration signals, and other telemetry for investigation. Both depend on the quality and freshness of the underlying collection and detection pipelines. A dashboard alone does not prove complete coverage or that an environment is secure.

My main takeaway: useful monitoring takes more than attractive charts. It takes understanding what each panel measures, validating the queries behind it, recognizing telemetry gaps, and making the next investigative step clear.

Next, I plan to validate coverage and data freshness, review alert thresholds against lab behavior, and prepare selectively redacted screenshots for public documentation. I’ve organized the screenshots and contact sheets for review; original captures should be checked for internal hostnames, paths, ports, service details, and values before sharing.

**Project and dashboard screenshots:** [GitHub repository](https://github.com/c3m2r4/grafana) · [LinkedIn top-pick screenshots and contact sheet](https://github.com/c3m2r4/grafana/tree/main/linkedin-post-ready/top-picks) · [Complete screenshot gallery](https://github.com/c3m2r4/grafana/blob/main/SCREENSHOTS.md)

**How do you decide which signals belong on infrastructure health dashboards and which deserve dedicated security investigation views in a small environment?**

#Grafana #Cybersecurity #Observability #Linux #DevSecOps #SecurityEngineering #OpenSource
