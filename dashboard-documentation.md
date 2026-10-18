# Grafana dashboard documentation

## Evidence and scope

The authenticated Grafana API returned 53 dashboards on 2026-10-18. The panel list, query identifiers, units, and configured default thresholds below are extracted from saved dashboard JSON. Purpose and troubleshooting guidance are operational interpretations. Grafana data sources configured: Prometheus and Alertmanager. These definitions do not verify that every query produced data at capture time.

## 01. Docker Containers Advanced

**Observed identity.** Grafana folder: `04 - Container Operations`. UID: `docker-containers-overview`. URL: `http://127.0.0.1:13000/d/docker-containers-overview/docker-containers-advanced`. Category: Infrastructure and operations.

**Purpose and operational importance.** The title and configured panels indicate a view for docker containers advanced. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 16 non-row panels are defined. Referenced data sources: `Dashboard default / not explicit`, `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Total containers** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `docker_container_info`. Configured label selectors include `name`.
- **Running containers** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `docker_container_running`. Configured label selectors include `name`.
- **Stopped containers** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `docker_container_info`, `docker_container_running`. Configured label selectors include `name`.
- **Memory in use** (`stat`; unit: `bytes`; source: `prometheus`; thresholds: ). Query identifiers: `docker_container_memory_usage_bytes`. Configured label selectors include `name`.
- **CPU usage by container** (`timeseries`; unit: `percent`; source: `prometheus`; thresholds: ). Query identifiers: `docker_container_cpu_percent`. Configured label selectors include `name`.
- **Memory usage by container** (`timeseries`; unit: `bytes`; source: `prometheus`; thresholds: ). Query identifiers: `docker_container_memory_usage_bytes`. Configured label selectors include `name`.
- **Memory limit used by container** (`timeseries`; unit: `percent`; source: `prometheus`; thresholds: ). Query identifiers: `docker_container_memory_percent`. Configured label selectors include `name`.
- **Network receive rate** (`timeseries`; unit: `Bps`; source: `prometheus`; thresholds: ). Query identifiers: `docker_container_network_receive_bytes_total`, `__rate_interval`. Configured label selectors include `name`.
- **Network transmit rate** (`timeseries`; unit: `Bps`; source: `prometheus`; thresholds: ). Query identifiers: `docker_container_network_transmit_bytes_total`, `__rate_interval`. Configured label selectors include `name`.
- **Block device read rate** (`timeseries`; unit: `Bps`; source: `prometheus`; thresholds: ). Query identifiers: `docker_container_block_read_bytes_total`, `__rate_interval`. Configured label selectors include `name`.
- **Block device write rate** (`timeseries`; unit: `Bps`; source: `prometheus`; thresholds: ). Query identifiers: `docker_container_block_write_bytes_total`, `__rate_interval`. Configured label selectors include `name`.
- **Container inventory and state** (`table`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `docker_container_info`. Configured label selectors include `name`.
- **Sources and drill-down** (`text`; unit: `Grafana default`; source: `Dashboard default / not explicit`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).
- **Docker daemon status** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `kali_cc_docker_daemon_available`.
- **Host metrics snapshot age** (`stat`; unit: `s`; source: `prometheus`; thresholds: 30, 120). Query identifiers: `kali_cc_metrics_snapshot_timestamp_seconds`.
- **Containers outside running state** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1, 3). Query identifiers: `docker_container_info`. Configured label selectors include `name`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Layout updated; dashboard title visible and screenshots PNG-verified.

**LinkedIn caption.** A focused Grafana view for Docker Containers Advanced, documenting configured signals that can support investigation and operational decisions.


## 03. Alerts and Reliability

**Observed identity.** Grafana folder: `05 - Kali Operations`. UID: `kali-alerts-reliability`. URL: `http://127.0.0.1:13000/d/kali-alerts-reliability/alerts-and-reliability`. Category: Infrastructure and operations.

**Purpose and operational importance.** The title and configured panels indicate a view for alerts and reliability. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 12 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Firing alerts** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Configured label selectors include `alertstate`.
- **Scrape targets down** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Configured label selectors include `up `.
- **Failed service probes** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_cc_health_check_up`. Configured label selectors include `kali_cc_health_check_up `.
- **Projects needing attention** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1, 3). Query identifiers: `kali_cc_project_state`. Configured label selectors include `state`.
- **Containers stopped** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_cc_container_running`. Configured label selectors include `kali_cc_container_running `.
- **Prometheus head series** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `prometheus_tsdb_head_series`.
- **Active alert details** (`table`; unit: `short`; source: `prometheus`; thresholds: ). Configured label selectors include `alertstate`.
- **Scrape health by job** (`state-timeline`; unit: `short`; source: `prometheus`; thresholds: 1).
- **Service probe status** (`table`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_cc_health_check_up`.
- **Project attention details** (`table`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `kali_cc_project_state`. Configured label selectors include `state`.
- **Containers not running** (`table`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `kali_cc_container_running`. Configured label selectors include `kali_cc_container_running `.
- **Prometheus TSDB head series** (`timeseries`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `prometheus_tsdb_head_series`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Alerts and Reliability, documenting configured signals that can support investigation and operational decisions.


## 04. Cybersecurity Lab Infrastructure

**Observed identity.** Grafana folder: `05 - Kali Operations`. UID: `kali-security-lab`. URL: `http://127.0.0.1:13000/d/kali-security-lab/cybersecurity-lab-infrastructure`. Category: Infrastructure and operations.

**Purpose and operational importance.** The title and configured panels indicate a view for cybersecurity lab infrastructure. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 9 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Lab projects healthy** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `kali_cc_project_state`. Configured label selectors include `project`, `state`.
- **Projects needing attention** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1, 3). Query identifiers: `kali_cc_project_state`. Configured label selectors include `project`.
- **Lab containers stopped** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_cc_container_running`. Configured label selectors include `project`.
- **Failed lab checks** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_cc_health_check_up`. Configured label selectors include `project`.
- **VMware running VMs** (`stat`; unit: `short`; source: `prometheus`; thresholds: -1). Query identifiers: `kali_cc_vmware_running_vms`.
- **Docker daemon** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_cc_docker_daemon_available`.
- **Lab project health state** (`state-timeline`; unit: `short`; source: `prometheus`; thresholds: 2, 3, 4). Query identifiers: `kali_cc_project_state`. Configured label selectors include `project`, `state`.
- **Lab container status** (`table`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_cc_container_running`. Configured label selectors include `project`.
- **Lab endpoint checks** (`table`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_cc_health_check_up`. Configured label selectors include `project`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Cybersecurity Lab Infrastructure, documenting configured signals that can support investigation and operational decisions.


## 05. Kali System Performance

**Observed identity.** Grafana folder: `05 - Kali Operations`. UID: `kali-system-performance`. URL: `http://127.0.0.1:13000/d/kali-system-performance/kali-system-performance`. Category: Infrastructure and operations.

**Purpose and operational importance.** The title and configured panels indicate a view for kali system performance. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 6 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **CPU by mode** (`timeseries`; unit: `percent`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `netdata_system_cpu_percentage_average`.
- **Load average** (`timeseries`; unit: `short`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `netdata_system_load_load_average`.
- **RAM and swap** (`timeseries`; unit: `mebibytes`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `netdata_system_ram_MiB_average`.
- **Disk I/O** (`timeseries`; unit: `Bps`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `netdata_disk_io_KiB_persec_average`.
- **Network throughput** (`timeseries`; unit: `Bps`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `netdata_system_net_kilobits_persec_average`.
- **Filesystem used percent** (`timeseries`; unit: `percent`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `mount_point`, `netdata_disk_space_GiB_average`. Configured label selectors include `dimension`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kali System Performance, documenting configured signals that can support investigation and operational decisions.


## 06. Network and Connectivity

**Observed identity.** Grafana folder: `05 - Kali Operations`. UID: `kali-network-connectivity`. URL: `http://127.0.0.1:13000/d/kali-network-connectivity/network-and-connectivity`. Category: Networking.

**Purpose and operational importance.** The title and configured panels indicate a view for network and connectivity. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 5 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Network traffic** (`timeseries`; unit: `Bps`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `netdata_system_net_kilobits_persec_average`.
- **Network packet errors** (`timeseries`; unit: `short`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `netdata_system_softnet_stat_events_persec_average`.
- **Local endpoint availability** (`state-timeline`; unit: `short`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `kali_cc_health_check_up`.
- **Endpoint response time** (`timeseries`; unit: `s`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `kali_cc_health_check_response_seconds`.
- **Prometheus target health** (`table`; unit: `short`; source: `prometheus`; thresholds: 70, 90).

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Layout updated; dashboard title visible and screenshots PNG-verified.

**LinkedIn caption.** A focused Grafana view for Network and Connectivity, documenting configured signals that can support investigation and operational decisions.


## 07. Project Command Center

**Observed identity.** Grafana folder: `05 - Kali Operations`. UID: `kali-project-command-center`. URL: `http://127.0.0.1:13000/d/kali-project-command-center/project-command-center`. Category: Executive and project overview.

**Purpose and operational importance.** The title and configured panels indicate a view for project command center. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 10 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Project state** (`state-timeline`; unit: `short`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `kali_cc_project_state`.
- **Explicit local health checks** (`table`; unit: `short`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `kali_cc_health_check_up`.
- **Probe response time** (`timeseries`; unit: `s`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `kali_cc_health_check_response_seconds`.
- **Health check last success** (`table`; unit: `dateTimeAsIso`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `kali_cc_health_check_last_success_timestamp_seconds`.
- **Project disk footprint** (`barchart`; unit: `bytes`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `kali_cc_project_size_bytes`.
- **Git tracked working tree dirty** (`table`; unit: `short`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `kali_cc_project_git_dirty`.
- **Discovered unconfigured projects** (`table`; unit: `short`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `kali_cc_discovered_project_info`.
- **Container associations** (`table`; unit: `short`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `kali_cc_container_state`.
- **Latest HTTP status code** (`table`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kali_cc_health_check_status_code`.
- **Current health check errors** (`table`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kali_cc_health_check_error`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Project Command Center, documenting configured signals that can support investigation and operational decisions.


## 08. Services and Ports

**Observed identity.** Grafana folder: `05 - Kali Operations`. UID: `kali-services-ports`. URL: `http://127.0.0.1:13000/d/kali-services-ports/services-and-ports`. Category: Infrastructure and operations.

**Purpose and operational importance.** The title and configured panels indicate a view for services and ports. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 8 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Observed local systemd unit state** (`table`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kali_cc_systemd_unit_state`.
- **Registered local container state** (`table`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kali_cc_container_state`.
- **Explicit endpoint check result** (`state-timeline`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kali_cc_health_check_up`.
- **HTTP response code (HTTP checks only)** (`table`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kali_cc_health_check_status_code`. Configured label selectors include `type`.
- **Endpoint response time** (`timeseries`; unit: `s`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kali_cc_health_check_response_seconds`.
- **Last successful check time** (`table`; unit: `dateTimeAsIso`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kali_cc_health_check_last_success_timestamp_seconds`.
- **Failed system services** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kali_cc_systemd_failed_units`.
- **Prometheus scrape target health** (`table`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults).

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Services and Ports, documenting configured signals that can support investigation and operational decisions.


## 09. Storage and Project Capacity

**Observed identity.** Grafana folder: `05 - Kali Operations`. UID: `kali-storage-capacity`. URL: `http://127.0.0.1:13000/d/kali-storage-capacity/storage-and-project-capacity`. Category: Infrastructure and operations.

**Purpose and operational importance.** The title and configured panels indicate a view for storage and project capacity. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 11 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Filesystem used percent** (`timeseries`; unit: `percent`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `mount_point`, `netdata_disk_space_GiB_average`. Configured label selectors include `dimension`.
- **Filesystem free GiB** (`timeseries`; unit: `gibibytes`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `netdata_disk_space_GiB_average`. Configured label selectors include `dimension`.
- **Project directory sizes** (`barchart`; unit: `bytes`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `kali_cc_project_size_bytes`.
- **Filesystem inode utilization** (`table`; unit: `percent`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `mount_point`, `netdata_disk_inodes_inodes_average`. Configured label selectors include `dimension`.
- **Disk read/write throughput** (`timeseries`; unit: `Bps`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `netdata_disk_io_KiB_persec_average`.
- **Project size scan status** (`table`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kali_cc_project_size_known`.
- **Projected root filesystem used in 7 days** (`timeseries`; unit: `gibibytes`; source: `prometheus`; thresholds: 190, 210). Query identifiers: `predict_linear`, `netdata_disk_space_GiB_average`, `mount_point`. Configured label selectors include `dimension`, `mount_point`.
- **Root storage alerts** (`table`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Configured label selectors include `alertname`.
- **Prometheus TSDB compacted blocks** (`timeseries`; unit: `bytes`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `prometheus_tsdb_storage_blocks_bytes`.
- **Prometheus WAL size** (`timeseries`; unit: `bytes`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `prometheus_tsdb_wal_storage_size_bytes`.
- **Prometheus active head series** (`timeseries`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `prometheus_tsdb_head_series`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Layout updated; dashboard title visible and screenshots PNG-verified.

**LinkedIn caption.** A focused Grafana view for Storage and Project Capacity, documenting configured signals that can support investigation and operational decisions.


## 10. Database Activity & Security Command Center

**Observed identity.** Grafana folder: `06 - Database Security`. UID: `db-dam-command-center`. URL: `http://127.0.0.1:13000/d/db-dam-command-center/database-activity-and-security-command-center`. Category: Database security.

**Purpose and operational importance.** The title and configured panels indicate a view for database activity & security command center. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 21 non-row panels are defined. Referenced data sources: `${datasource}`, `Dashboard default / not explicit`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Coverage, interpretation, and drilldowns** (`text`; unit: `Grafana default`; source: `Dashboard default / not explicit`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).
- **DAM events retained** (`stat`; unit: `short`; source: `${datasource}`; thresholds: 1). Query identifiers: `dbcc_dam_events_stored`.
- **Counter increase observed by Prometheus in selected range** (`stat`; unit: `short`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `dbcc_dam_events_total`, `__range`. Configured label selectors include `engine`.
- **Audit records observed by collector** (`stat`; unit: `short`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `dbcc_dam_collector_records_seen`.
- **Prometheus scrape target** (`stat`; unit: `short`; source: `${datasource}`; thresholds: 1). Configured label selectors include `job`.
- **Collector heartbeat current** (`stat`; unit: `short`; source: `${datasource}`; thresholds: 1). Query identifiers: `dbcc_dam_source_configured`, `dbcc_dam_collector_heartbeat_timestamp_seconds`. Configured label selectors include `dbcc_dam_source_configured `.
- **Heartbeat age** (`stat`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `dbcc_dam_collector_heartbeat_timestamp_seconds`.
- **Failures / denials / interruptions** (`stat`; unit: `short`; source: `${datasource}`; thresholds: 1). Query identifiers: `dbcc_dam_events_total`. Configured label selectors include `engine`, `outcome`.
- **Authentication failures** (`stat`; unit: `short`; source: `${datasource}`; thresholds: 1). Query identifiers: `dbcc_dam_events_total`, `event_type`, `authentication_failure`. Configured label selectors include `engine`, `event_type`.
- **Privilege changes** (`stat`; unit: `short`; source: `${datasource}`; thresholds: 1). Query identifiers: `dbcc_dam_events_total`, `event_type`, `privilege_change`. Configured label selectors include `engine`, `event_type`.
- **DDL / data changes for review** (`stat`; unit: `short`; source: `${datasource}`; thresholds: 1). Query identifiers: `dbcc_dam_events_total`, `event_type`, `data_change`. Configured label selectors include `engine`, `event_type`.
- **Configuration changes** (`stat`; unit: `short`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `dbcc_dam_events_total`, `event_type`, `configuration_change`. Configured label selectors include `engine`, `event_type`.
- **Audit tampering events** (`stat`; unit: `short`; source: `${datasource}`; thresholds: 1). Query identifiers: `dbcc_dam_events_total`, `event_type`, `audit_tampering`. Configured label selectors include `engine`, `event_type`.
- **Successful logins** (`stat`; unit: `short`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `dbcc_dam_events_total`, `event_type`. Configured label selectors include `engine`, `event_type`, `outcome`.
- **Failed / denied privilege changes** (`stat`; unit: `short`; source: `${datasource}`; thresholds: 1). Query identifiers: `dbcc_dam_events_total`, `event_type`, `privilege_change`. Configured label selectors include `engine`, `event_type`, `outcome`.
- **Event volume by category** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `event_type`, `dbcc_dam_events_total`, `__rate_interval`. Configured label selectors include `engine`.
- **Unsuccessful activity by category** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `event_type`, `dbcc_dam_events_total`, `__rate_interval`. Configured label selectors include `engine`, `outcome`.
- **Authentication activity by type and outcome** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `event_type`, `dbcc_dam_events_total`, `authentication_failure`, `__rate_interval`. Configured label selectors include `engine`, `event_type`.
- **Configuration, DDL, and data-change activity** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `event_type`, `dbcc_dam_events_total`, `configuration_change`, `data_change`, `__rate_interval`. Configured label selectors include `engine`, `event_type`.
- **All event totals by type and outcome** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `event_type`, `dbcc_dam_events_total`. Configured label selectors include `engine`.
- **Investigation leads by category and outcome** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `event_type`, `dbcc_dam_events_total`, `authentication_failure`, `audit_tampering`, `privilege_change`, `configuration_change`, `data_change`. Configured label selectors include `engine`, `event_type`, `outcome`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Database Activity & Security Command Center, documenting configured signals that can support investigation and operational decisions.


## 11. Kali Sentinel | Application & API Security

**Observed identity.** Grafana folder: `07 - Kali Sentinel`. UID: `kali-sentinel-appsec`. URL: `http://127.0.0.1:13000/d/kali-sentinel-appsec/kali-sentinel-7c-application-and-api-security`. Category: Security monitoring.

**Purpose and operational importance.** The title and configured panels indicate a view for kali sentinel | application & api security. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 12 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Evidence limits** (`text`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).
- **Monitored checks** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `kali_cc_health_check_up`. Configured label selectors include `check`, `project`, `type`.
- **Failing checks** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_cc_health_check_up`. Configured label selectors include `check`, `project`, `type`.
- **HTTP 5xx checks** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_cc_health_check_status_code`. Configured label selectors include `check`, `project`, `type`.
- **Container restarts / 1h** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1, 5). Query identifiers: `kube_pod_container_status_restarts_total`.
- **Active alert instances** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1, 5). Configured label selectors include `alertstate`.
- **Reachability by discovered check** (`table`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_cc_health_check_up`. Configured label selectors include `check`, `project`, `type`.
- **HTTP response codes by check** (`timeseries`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `kali_cc_health_check_status_code`. Configured label selectors include `check`, `project`, `type`.
- **Health-check latency** (`timeseries`; unit: `s`; source: `prometheus`; thresholds: 1, 2). Query identifiers: `kali_cc_health_check_response_seconds`. Configured label selectors include `check`, `project`, `type`.
- **Container restarts (last hour)** (`timeseries`; unit: `short`; source: `prometheus`; thresholds: 1, 2). Query identifiers: `kube_pod_container_status_restarts_total`.
- **Firing alert instances by severity** (`timeseries`; unit: `short`; source: `prometheus`; thresholds: 1, 2). Configured label selectors include `alertstate`.
- **Current firing alert details** (`table`; unit: `short`; source: `prometheus`; thresholds: 1). Configured label selectors include `alertstate`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kali Sentinel | Application & API Security, documenting configured signals that can support investigation and operational decisions.


## 12. Kali Sentinel | Audit & Monitoring Health

**Observed identity.** Grafana folder: `07 - Kali Sentinel`. UID: `kali-sentinel-audit-health`. URL: `http://127.0.0.1:13000/d/kali-sentinel-audit-health/kali-sentinel-7c-audit-and-monitoring-health`. Category: Security monitoring.

**Purpose and operational importance.** The title and configured panels indicate a view for kali sentinel | audit & monitoring health. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 10 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Read this first** (`text`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).
- **Prometheus targets** (`stat`; unit: `short`; source: `prometheus`; thresholds: ).
- **Unhealthy targets** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Configured label selectors include `up `.
- **DBCC scrape target** (`stat`; unit: `short`; source: `prometheus`; thresholds: 0, 1). Configured label selectors include `job`.
- **DAM collector heartbeat** (`stat`; unit: `short`; source: `prometheus`; thresholds: 0, 1). Query identifiers: `dbcc_dam_source_configured`. Configured label selectors include `job`.
- **Collector heartbeat age** (`stat`; unit: `s`; source: `prometheus`; thresholds: 60, 90). Query identifiers: `dbcc_dam_collector_heartbeat_timestamp_seconds`. Configured label selectors include `job`.
- **DAM events stored (total)** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `dbcc_dam_events_stored`. Configured label selectors include `job`.
- **Prometheus target health** (`table`; unit: `short`; source: `prometheus`; thresholds: 1).
- **Active firing alerts** (`table`; unit: `short`; source: `prometheus`; thresholds: 1). Configured label selectors include `alertstate`.
- **Coverage and operational gaps** (`text`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kali Sentinel | Audit & Monitoring Health, documenting configured signals that can support investigation and operational decisions.


## 13. Kali Sentinel | Database Activity Monitoring

**Observed identity.** Grafana folder: `07 - Kali Sentinel`. UID: `kali-sentinel-dam`. URL: `http://127.0.0.1:13000/d/kali-sentinel-dam/kali-sentinel-7c-database-activity-monitoring`. Category: Database security.

**Purpose and operational importance.** The title and configured panels indicate a view for kali sentinel | database activity monitoring. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 8 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Interpretation** (`text`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).
- **DBCC scrape target** (`stat`; unit: `short`; source: `prometheus`; thresholds: 0, 1). Configured label selectors include `job`.
- **Normalized events stored (total)** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `dbcc_dam_events_stored`. Configured label selectors include `job`.
- **Collector heartbeat age** (`stat`; unit: `s`; source: `prometheus`; thresholds: 60, 90). Query identifiers: `dbcc_dam_collector_heartbeat_timestamp_seconds`. Configured label selectors include `job`.
- **Collector heartbeat current (not source verification)** (`stat`; unit: `short`; source: `prometheus`; thresholds: 0, 1). Query identifiers: `dbcc_dam_source_configured`. Configured label selectors include `job`.
- **Observed event rate by category** (`timeseries`; unit: `ops`; source: `prometheus`; thresholds: 1, 2). Query identifiers: `event_type`, `dbcc_dam_events_total`. Configured label selectors include `engine`, `job`.
- **Events by category in selected period** (`timeseries`; unit: `short`; source: `prometheus`; thresholds: 1, 2). Query identifiers: `event_type`, `dbcc_dam_events_total`, `__range`. Configured label selectors include `engine`, `job`.
- **Investigation** (`text`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kali Sentinel | Database Activity Monitoring, documenting configured signals that can support investigation and operational decisions.


## 14. Kali Sentinel | Database Fleet

**Observed identity.** Grafana folder: `07 - Kali Sentinel`. UID: `kali-sentinel-db-fleet`. URL: `http://127.0.0.1:13000/d/kali-sentinel-db-fleet/kali-sentinel-7c-database-fleet`. Category: Database security.

**Purpose and operational importance.** The title and configured panels indicate a view for kali sentinel | database fleet. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 11 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Database fleet coverage** (`text`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).
- **DB performance exporters** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Configured label selectors include `job`.
- **Database/broker sockets** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `kali_socket_inventory_last_seen_timestamp_seconds`, `socket_state`, `local_port`. Configured label selectors include `local_port`, `protocol`, `socket_state`.
- **Wildcard-bound sockets** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1, 3). Query identifiers: `kali_socket_inventory_last_seen_timestamp_seconds`, `socket_state`, `local_port`. Configured label selectors include `exposure`, `local_port`, `protocol`, `socket_state`.
- **DBCC metrics scrape** (`stat`; unit: `short`; source: `prometheus`; thresholds: 0, 1). Configured label selectors include `job`.
- **DAM events stored (total)** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `dbcc_dam_events_stored`. Configured label selectors include `job`.
- **Collector heartbeat age** (`stat`; unit: `short`; source: `prometheus`; thresholds: 60, 90). Query identifiers: `dbcc_dam_collector_heartbeat_timestamp_seconds`. Configured label selectors include `job`.
- **Observed database and broker listeners** (`table`; unit: `dateTimeAsIso`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kali_socket_inventory_last_seen_timestamp_seconds`, `socket_state`, `local_port`. Configured label selectors include `local_port`, `protocol`, `socket_state`.
- **DAM event rate by category** (`timeseries`; unit: `ops`; source: `prometheus`; thresholds: ). Query identifiers: `event_type`, `dbcc_dam_events_total`. Configured label selectors include `engine`, `job`.
- **DAM events by category in selected period** (`timeseries`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `event_type`, `dbcc_dam_events_total`, `__range`. Configured label selectors include `engine`, `job`.
- **Observed binds and data limits** (`text`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kali Sentinel | Database Fleet, documenting configured signals that can support investigation and operational decisions.


## 15. Kali Sentinel | Executive Overview

**Observed identity.** Grafana folder: `07 - Kali Sentinel`. UID: `kali-sentinel-overview`. URL: `http://127.0.0.1:13000/d/kali-sentinel-overview/kali-sentinel-7c-executive-overview`. Category: Security monitoring.

**Purpose and operational importance.** The title and configured panels indicate a view for kali sentinel | executive overview. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 10 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Evidence and coverage** (`text`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).
- **Host CPU utilization** (`timeseries`; unit: `percent`; source: `prometheus`; thresholds: 70, 85). Query identifiers: `netdata_system_cpu_percentage_average`, `guest_nice`.
- **Host memory utilization** (`timeseries`; unit: `percent`; source: `prometheus`; thresholds: 75, 90). Query identifiers: `netdata_system_ram_MiB_average`. Configured label selectors include `dimension`.
- **Critical and high alerts** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1, 3). Configured label selectors include `alertstate`, `severity`.
- **Unhealthy Prometheus targets** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1, 3). Configured label selectors include `up `.
- **Failing application health checks** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1, 2). Query identifiers: `kali_cc_health_check_up`. Configured label selectors include `kali_cc_health_check_up `.
- **DBCC metrics scrape** (`stat`; unit: `short`; source: `prometheus`; thresholds: 0, 1). Configured label selectors include `job`.
- **Database activity volume (observed categories)** (`timeseries`; unit: `ops`; source: `prometheus`; thresholds: 1, 2). Query identifiers: `event_type`, `dbcc_dam_events_total`.
- **Disk usage by mount point** (`timeseries`; unit: `percent`; source: `prometheus`; thresholds: 75, 90). Query identifiers: `mount_point`, `netdata_disk_space_GiB_average`. Configured label selectors include `dimension`.
- **Known gaps** (`text`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kali Sentinel | Executive Overview, documenting configured signals that can support investigation and operational decisions.


## 16. Kali Sentinel | File Integrity

**Observed identity.** Grafana folder: `07 - Kali Sentinel`. UID: `kali-sentinel-file-integrity`. URL: `http://127.0.0.1:13000/d/kali-sentinel-file-integrity/kali-sentinel-7c-file-integrity`. Category: Security monitoring.

**Purpose and operational importance.** The title and configured panels indicate a view for kali sentinel | file integrity. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 4 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **File integrity coverage and evidence limits** (`text`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).
- **Prometheus targets related to audit and file integrity** (`table`; unit: `short`; source: `prometheus`; thresholds: 0, 1). Configured label selectors include `job`.
- **Host collector observations (last checked)** (`text`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).
- **Collection scope and next evidence needed** (`text`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kali Sentinel | File Integrity, documenting configured signals that can support investigation and operational decisions.


## 17. Kali Sentinel | Privileged Activity

**Observed identity.** Grafana folder: `07 - Kali Sentinel`. UID: `kali-sentinel-privileged-audit`. URL: `http://127.0.0.1:13000/d/kali-sentinel-privileged-audit/kali-sentinel-7c-privileged-activity`. Category: Security monitoring.

**Purpose and operational importance.** The title and configured panels indicate a view for kali sentinel | privileged activity. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 3 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Collection status: not yet evidenced** (`text`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).
- **Audit-related scrape targets** (`table`; unit: `short`; source: `prometheus`; thresholds: 1, 2). Configured label selectors include `job`.
- **Evidence required** (`text`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kali Sentinel | Privileged Activity, documenting configured signals that can support investigation and operational decisions.


## 18. Kali Sentinel | Service Catalog & Health

**Observed identity.** Grafana folder: `07 - Kali Sentinel`. UID: `kali-sentinel-services`. URL: `http://127.0.0.1:13000/d/kali-sentinel-services/kali-sentinel-7c-service-catalog-and-health`. Category: Security monitoring.

**Purpose and operational importance.** The title and configured panels indicate a view for kali sentinel | service catalog & health. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 6 non-row panels are defined. Referenced data sources: `Dashboard default / not explicit`, `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Catalog scope** (`text`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).
- **Service health checks** (`table`; unit: `short`; source: `prometheus`; thresholds: 1, 2). Query identifiers: `kali_cc_health_check_up`.
- **HTTP status from instrumented health checks** (`table`; unit: `short`; source: `prometheus`; thresholds: 1, 2). Query identifiers: `kali_cc_health_check_status_code`. Configured label selectors include `type`.
- **Health-check response time** (`timeseries`; unit: `s`; source: `prometheus`; thresholds: 1, 2). Query identifiers: `kali_cc_health_check_response_seconds`.
- **Port-forwarded monitoring interfaces** (`text`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).
- **Discovered services and verified browser URLs** (`text`; unit: `Grafana default`; source: `Dashboard default / not explicit`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kali Sentinel | Service Catalog & Health, documenting configured signals that can support investigation and operational decisions.


## 19. Kali Sentinel — Listening Sockets

**Observed identity.** Grafana folder: `07 - Kali Sentinel`. UID: `kali-sentinel-sockets`. URL: `http://127.0.0.1:13000/d/kali-sentinel-sockets/kali-sentinel-e28094-listening-sockets`. Category: Security monitoring.

**Purpose and operational importance.** The title and configured panels indicate a view for kali sentinel — listening sockets. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 24 non-row panels are defined. Referenced data sources: `Dashboard default / not explicit`, `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Collection and evidence limits** (`text`; unit: `Grafana default`; source: `Dashboard default / not explicit`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).
- **TCP LISTEN** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `kali_socket_inventory_sockets`, `socket_state`. Configured label selectors include `protocol`, `socket_state`.
- **UDP sockets** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `kali_socket_inventory_sockets`. Configured label selectors include `protocol`.
- **Unique ports** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `local_port`, `kali_socket_inventory_last_seen_timestamp_seconds`, `socket_state`. Configured label selectors include `protocol`, `socket_state`.
- **Unique processes** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `process_name`, `kali_socket_inventory_last_seen_timestamp_seconds`.
- **Loopback services** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `kali_socket_inventory_last_seen_timestamp_seconds`. Configured label selectors include `exposure`.
- **Wildcard services** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_socket_inventory_last_seen_timestamp_seconds`. Configured label selectors include `exposure`.
- **New listeners (15m)** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_socket_listener_change`. Configured label selectors include `change`.
- **Disappeared (15m)** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_socket_listener_change`. Configured label selectors include `change`.
- **Failed application health checks** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_socket_inventory_application_health`, `kali_cc_health_check_up`. Configured label selectors include `kali_cc_health_check_up `, `kali_socket_inventory_application_health `.
- **Exporter scrape** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_socket_inventory_scrape_success`.
- **Process metadata available** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_socket_inventory_process_metadata_available`.
- **Inventory snapshot truncated** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_socket_inventory_truncated`.
- **TCP / UDP distribution** (`piechart`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_socket_inventory_sockets`.
- **Listening ports by process** (`barchart`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `process_name`, `local_port`, `kali_socket_inventory_last_seen_timestamp_seconds`, `socket_state`. Configured label selectors include `socket_state`.
- **Services by interface** (`barchart`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_socket_inventory_last_seen_timestamp_seconds`.
- **Port activity over time** (`timeseries`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `socket_state`, `kali_socket_inventory_sockets`.
- **Newly discovered listeners** (`table`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_socket_listener_change`. Configured label selectors include `change`.
- **Wildcard-bound exposure review** (`table`; unit: `dateTimeAsIso`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_socket_inventory_last_seen_timestamp_seconds`. Configured label selectors include `exposure`.
- **Important service availability** (`table`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_socket_listener_expected_up`.
- **Availability / last seen inventory** (`table`; unit: `dateTimeAsIso`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_socket_inventory_last_seen_timestamp_seconds`, `local_port`, `process_name`, `local_address`. Configured label selectors include `exposure`, `local_address`, `local_port`, `process_name`, `protocol`.
- **HTTP(S) application health checks** (`table`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kali_socket_inventory_application_health`.
- **Recent listener changes (15m)** (`table`; unit: `dateTimeAsIso`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kali_socket_listener_change_timestamp_seconds`.
- **Change tracking baseline** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_socket_inventory_baseline_initialized`.

A listening socket does not by itself establish that the service is externally reachable or vulnerable. Validate bind address, routing/NAT, host and network firewall policy, and the owning process from the host and network vantage points.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kali Sentinel — Listening Sockets, documenting configured signals that can support investigation and operational decisions.


## 20. Linux Network Stack (node_exporter)

**Observed identity.** Grafana folder: `07 - Kali Sentinel`. UID: `linux-net-stack-nodeexp`. URL: `http://127.0.0.1:13000/d/linux-net-stack-nodeexp/linux-network-stack-node-exporter`. Category: Security monitoring.

**Purpose and operational importance.** The title and configured panels indicate a view for linux network stack (node_exporter). It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 43 non-row panels are defined. Referenced data sources: `${datasource}`, `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Conntrack usage** (`gauge`; unit: `percent`; source: `prometheus`; thresholds: 70, 85, 95). Query identifiers: `node_nf_conntrack_entries`, `node_nf_conntrack_entries_limit`. Configured label selectors include `instance`, `job`.
- **Conntrack entries** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `node_nf_conntrack_entries`. Configured label selectors include `instance`, `job`.
- **Conntrack limit** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `node_nf_conntrack_entries_limit`. Configured label selectors include `instance`, `job`.
- **TCP established** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `node_netstat_Tcp_CurrEstab`. Configured label selectors include `instance`, `job`.
- **UDP sockets in use** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `node_sockstat_UDP_inuse`. Configured label selectors include `instance`, `job`.
- **Softnet drops /s** (`stat`; unit: `ops`; source: `prometheus`; thresholds: 0.01). Query identifiers: `node_softnet_dropped_total`, `__rate_interval`. Configured label selectors include `instance`, `job`.
- **Conntrack entries vs limit** (`timeseries`; unit: `short`; source: `${datasource}`; thresholds: ). Query identifiers: `node_nf_conntrack_entries`, `node_nf_conntrack_entries_limit`. Configured label selectors include `instance`, `job`.
- **Conntrack failures /s** (`timeseries`; unit: `ops`; source: `prometheus`; thresholds: ). Query identifiers: `node_nf_conntrack_stat_insert_failed`, `__rate_interval`, `node_nf_conntrack_stat_drop`, `node_nf_conntrack_stat_early_drop`, `node_nf_conntrack_stat_invalid`. Configured label selectors include `instance`, `job`.
- **Conntrack activity /s** (`timeseries`; unit: `ops`; source: `${datasource}`; thresholds: ). Query identifiers: `node_nf_conntrack_stat_insert`, `__rate_interval`, `node_nf_conntrack_stat_found`, `node_nf_conntrack_stat_ignore`, `node_nf_conntrack_stat_search_restart`. Configured label selectors include `instance`, `job`.
- **Interface status** (`table`; unit: `none`; source: `prometheus`; thresholds: ). Query identifiers: `node_network_up`, `node_network_carrier`, `node_network_receive_bytes_total`, `__rate_interval`, `node_network_transmit_bytes_total`, `node_network_receive_packets_total`, `node_network_transmit_packets_total`, `node_network_receive_drop_total`, `node_network_transmit_drop_total`, `node_network_receive_errs_total`. Configured label selectors include `device`, `instance`, `job`.
- **Throughput (bits/s)  RX above / TX below** (`timeseries`; unit: `bps`; source: `${datasource}`; thresholds: ). Query identifiers: `node_network_receive_bytes_total`, `__rate_interval`, `node_network_transmit_bytes_total`. Configured label selectors include `device`, `instance`, `job`.
- **Packets /s  RX above / TX below** (`timeseries`; unit: `pps`; source: `prometheus`; thresholds: ). Query identifiers: `node_network_receive_packets_total`, `__rate_interval`, `node_network_transmit_packets_total`. Configured label selectors include `device`, `instance`, `job`.
- **RX multicast /s** (`timeseries`; unit: `pps`; source: `prometheus`; thresholds: ). Query identifiers: `node_network_receive_multicast_total`, `__rate_interval`. Configured label selectors include `device`, `instance`, `job`.
- **Errors /s** (`timeseries`; unit: `ops`; source: `${datasource}`; thresholds: ). Query identifiers: `node_network_receive_errs_total`, `__rate_interval`, `node_network_transmit_errs_total`. Configured label selectors include `device`, `instance`, `job`.
- **Drops /s** (`timeseries`; unit: `ops`; source: `prometheus`; thresholds: ). Query identifiers: `node_network_receive_drop_total`, `__rate_interval`, `node_network_transmit_drop_total`. Configured label selectors include `device`, `instance`, `job`.
- **FIFO, frame, collisions & carrier /s** (`timeseries`; unit: `ops`; source: `prometheus`; thresholds: ). Query identifiers: `node_network_receive_fifo_total`, `__rate_interval`, `node_network_receive_frame_total`, `node_network_transmit_fifo_total`, `node_network_transmit_colls_total`, `node_network_transmit_carrier_total`. Configured label selectors include `device`, `instance`, `job`.
- **CPU utilisation by mode (avg of selected CPUs)** (`timeseries`; unit: `percent`; source: `prometheus`; thresholds: ). Query identifiers: `node_cpu_seconds_total`, `__rate_interval`. Configured label selectors include `cpu`, `instance`, `job`.
- **softirq & hardirq time (avg of selected CPUs)** (`timeseries`; unit: `percent`; source: `${datasource}`; thresholds: ). Query identifiers: `node_cpu_seconds_total`, `__rate_interval`. Configured label selectors include `cpu`, `instance`, `job`, `mode`.
- **softirq time by CPU (%)** (`timeseries`; unit: `percent`; source: `${datasource}`; thresholds: ). Query identifiers: `node_cpu_seconds_total`, `__rate_interval`. Configured label selectors include `cpu`, `instance`, `job`, `mode`.
- **hardirq time by CPU (%)** (`timeseries`; unit: `percent`; source: `${datasource}`; thresholds: ). Query identifiers: `node_cpu_seconds_total`, `__rate_interval`. Configured label selectors include `cpu`, `instance`, `job`, `mode`.
- **Packets processed /s by CPU** (`timeseries`; unit: `pps`; source: `${datasource}`; thresholds: ). Query identifiers: `node_softnet_processed_total`, `__rate_interval`. Configured label selectors include `cpu`, `instance`, `job`.
- **Dropped /s by CPU (softnet backlog full)** (`timeseries`; unit: `pps`; source: `${datasource}`; thresholds: ). Query identifiers: `node_softnet_dropped_total`, `__rate_interval`. Configured label selectors include `cpu`, `instance`, `job`.
- **Time squeezed /s by CPU** (`timeseries`; unit: `ops`; source: `${datasource}`; thresholds: ). Query identifiers: `node_softnet_times_squeezed_total`, `__rate_interval`. Configured label selectors include `cpu`, `instance`, `job`.
- **Backlog length by CPU (packets)** (`timeseries`; unit: `short`; source: `${datasource}`; thresholds: ). Query identifiers: `node_softnet_backlog_len`. Configured label selectors include `cpu`, `instance`, `job`.
- **RPS packets received /s by CPU** (`timeseries`; unit: `ops`; source: `${datasource}`; thresholds: ). Query identifiers: `node_softnet_received_rps_total`, `__rate_interval`. Configured label selectors include `cpu`, `instance`, `job`.
- **Flow limit hits /s by CPU** (`timeseries`; unit: `ops`; source: `${datasource}`; thresholds: ). Query identifiers: `node_softnet_flow_limit_count_total`, `__rate_interval`. Configured label selectors include `cpu`, `instance`, `job`.
- **NIC hardware interrupts /s by CPU** (`timeseries`; unit: `ops`; source: `${datasource}`; thresholds: ). Query identifiers: `node_interrupts_total`, `__rate_interval`. Configured label selectors include `cpu`, `devices`, `instance`, `job`.
- **NIC interrupts per CPU (now)** (`bargauge`; unit: `ops`; source: `${datasource}`; thresholds: ). Query identifiers: `sort_desc`, `node_interrupts_total`, `__rate_interval`. Configured label selectors include `cpu`, `devices`, `instance`, `job`.
- **NIC interrupts /s by IRQ vector** (`timeseries`; unit: `ops`; source: `${datasource}`; thresholds: ). Query identifiers: `node_interrupts_total`, `__rate_interval`. Configured label selectors include `cpu`, `devices`, `instance`, `job`.
- **RX packets per NIC interrupt** (`timeseries`; unit: `short`; source: `${datasource}`; thresholds: ). Query identifiers: `node_network_receive_packets_total`, `__rate_interval`, `node_interrupts_total`. Configured label selectors include `cpu`, `device`, `devices`, `instance`, `job`.
- **NIC interrupt matrix: CPU x IRQ vector (current rate, /s)** (`table`; unit: `ops`; source: `${datasource}`; thresholds: ). Query identifiers: `node_interrupts_total`, `__rate_interval`. Configured label selectors include `cpu`, `devices`, `instance`, `job`.
- **TCP segments /s** (`timeseries`; unit: `ops`; source: `${datasource}`; thresholds: ). Query identifiers: `node_netstat_Tcp_InSegs`, `__rate_interval`, `node_netstat_Tcp_OutSegs`, `node_netstat_Tcp_RetransSegs`. Configured label selectors include `instance`, `job`.
- **TCP retransmit ratio (%)** (`timeseries`; unit: `percent`; source: `${datasource}`; thresholds: 1, 5). Query identifiers: `node_netstat_Tcp_RetransSegs`, `__rate_interval`, `node_netstat_Tcp_OutSegs`. Configured label selectors include `instance`, `job`.
- **TCP connection establishment /s** (`timeseries`; unit: `ops`; source: `prometheus`; thresholds: ). Query identifiers: `node_netstat_Tcp_ActiveOpens`, `__rate_interval`, `node_netstat_Tcp_PassiveOpens`. Configured label selectors include `instance`, `job`.
- **Listen queue overflows & drops /s** (`timeseries`; unit: `ops`; source: `${datasource}`; thresholds: ). Query identifiers: `node_netstat_TcpExt_ListenOverflows`, `__rate_interval`, `node_netstat_TcpExt_ListenDrops`. Configured label selectors include `instance`, `job`.
- **SYN cookies /s** (`timeseries`; unit: `ops`; source: `${datasource}`; thresholds: ). Query identifiers: `node_netstat_TcpExt_SyncookiesSent`, `__rate_interval`, `node_netstat_TcpExt_SyncookiesRecv`, `node_netstat_TcpExt_SyncookiesFailed`. Configured label selectors include `instance`, `job`.
- **TCP timeouts, SYN retransmits, RSTs & bad segments /s** (`timeseries`; unit: `ops`; source: `prometheus`; thresholds: ). Query identifiers: `node_netstat_TcpExt_TCPTimeouts`, `__rate_interval`, `node_netstat_TcpExt_TCPSynRetrans`, `node_netstat_Tcp_OutRsts`, `node_netstat_Tcp_InErrs`. Configured label selectors include `instance`, `job`.
- **UDP datagrams /s** (`timeseries`; unit: `ops`; source: `${datasource}`; thresholds: ). Query identifiers: `node_netstat_Udp_InDatagrams`, `__rate_interval`, `node_netstat_Udp_OutDatagrams`. Configured label selectors include `instance`, `job`.
- **UDP errors /s** (`timeseries`; unit: `ops`; source: `prometheus`; thresholds: ). Query identifiers: `node_netstat_Udp_NoPorts`, `__rate_interval`, `node_netstat_Udp_InErrors`, `node_netstat_Udp_RcvbufErrors`, `node_netstat_Udp_SndbufErrors`. Configured label selectors include `instance`, `job`.
- **ICMP messages /s** (`timeseries`; unit: `ops`; source: `prometheus`; thresholds: ). Query identifiers: `node_netstat_Icmp_InMsgs`, `__rate_interval`, `node_netstat_Icmp_OutMsgs`, `node_netstat_Icmp_InErrors`. Configured label selectors include `instance`, `job`.
- **Sockets in use** (`timeseries`; unit: `short`; source: `${datasource}`; thresholds: ). Query identifiers: `node_sockstat_sockets_used`, `node_sockstat_TCP_inuse`, `node_sockstat_TCP_alloc`, `node_sockstat_UDP_inuse`. Configured label selectors include `instance`, `job`.
- **TCP orphaned & TIME_WAIT sockets** (`timeseries`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `node_sockstat_TCP_orphan`, `node_sockstat_TCP_tw`. Configured label selectors include `instance`, `job`.
- **Socket buffer memory** (`timeseries`; unit: `bytes`; source: `prometheus`; thresholds: ). Query identifiers: `node_sockstat_TCP_mem_bytes`, `node_sockstat_UDP_mem_bytes`, `node_sockstat_FRAG_memory`. Configured label selectors include `instance`, `job`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Layout updated; dashboard title visible and screenshots PNG-verified.

**LinkedIn caption.** A focused Grafana view for Linux Network Stack (node_exporter), documenting configured signals that can support investigation and operational decisions.


## 21. DevSecOps Control Plane Advanced

**Observed identity.** Grafana folder: `01 - Command Centers`. UID: `devsecops-control-plane-advanced`. URL: `http://127.0.0.1:13000/d/devsecops-control-plane-advanced/devsecops-control-plane-advanced`. Category: Infrastructure and operations.

**Purpose and operational importance.** The title and configured panels indicate a view for devsecops control plane advanced. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 21 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Ready nodes** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `kube_node_status_condition`. Configured label selectors include `cluster`, `condition`, `status`.
- **Running pods** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `kube_pod_status_phase`. Configured label selectors include `cluster`, `phase`.
- **Prometheus targets up (%)** (`stat`; unit: `percent`; source: `prometheus`; thresholds: ). Query identifiers: `clamp_min`. Configured label selectors include `cluster`.
- **Firing alerts** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Configured label selectors include `alertstate`.
- **Critical image vulnerabilities** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `trivy_image_vulnerabilities`. Configured label selectors include `cluster`, `severity`.
- **High image vulnerabilities** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `trivy_image_vulnerabilities`. Configured label selectors include `cluster`, `severity`.
- **Falco rule matches/sec** (`stat`; unit: `ops`; source: `prometheus`; thresholds: ). Query identifiers: `falcosecurity_falco_rules_matches_total`. Configured label selectors include `cluster`.
- **Running Docker containers** (`stat`; unit: `short`; source: `prometheus`; thresholds: ). Query identifiers: `docker_container_running`. Configured label selectors include `cluster`.
- **CPU usage by namespace** (`timeseries`; unit: `cores`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `container_cpu_usage_seconds_total`, `metrics_path`. Configured label selectors include `cluster`, `job`, `metrics_path`.
- **Memory working set by namespace** (`timeseries`; unit: `bytes`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `container_memory_working_set_bytes`, `metrics_path`. Configured label selectors include `cluster`, `job`, `metrics_path`.
- **API server request rate by code** (`timeseries`; unit: `ops`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `apiserver_request_total`. Configured label selectors include `cluster`.
- **CoreDNS responses by code** (`timeseries`; unit: `ops`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `coredns_dns_responses_total`. Configured label selectors include `cluster`.
- **Pod scheduling attempts/sec** (`timeseries`; unit: `ops`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `scheduler_schedule_attempts_total`. Configured label selectors include `cluster`.
- **etcd database size** (`timeseries`; unit: `bytes`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `etcd_mvcc_db_total_size_in_bytes`. Configured label selectors include `cluster`.
- **Kubernetes network receive by namespace** (`timeseries`; unit: `Bps`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `metrics_path`. Configured label selectors include `cluster`, `job`, `metrics_path`.
- **Kubernetes network transmit by namespace** (`timeseries`; unit: `Bps`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_bytes_total`, `metrics_path`. Configured label selectors include `cluster`, `job`, `metrics_path`.
- **Trivy vulnerabilities by severity** (`timeseries`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `trivy_image_vulnerabilities`. Configured label selectors include `cluster`.
- **Falco events by rule** (`timeseries`; unit: `ops`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `falcosecurity_falco_rules_matches_total`. Configured label selectors include `cluster`.
- **Docker CPU by container** (`timeseries`; unit: `percent`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `docker_container_cpu_percent`. Configured label selectors include `cluster`, `name`.
- **Docker memory by container** (`timeseries`; unit: `bytes`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `docker_container_memory_usage_bytes`. Configured label selectors include `cluster`, `name`.
- **Docker container inventory** (`table`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `docker_container_info`. Configured label selectors include `cluster`, `name`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for DevSecOps Control Plane Advanced, documenting configured signals that can support investigation and operational decisions.


## 22. Kali Linux Executive Overview

**Observed identity.** Grafana folder: `01 - Command Centers`. UID: `kali-executive-overview`. URL: `http://127.0.0.1:13000/d/kali-executive-overview/kali-linux-executive-overview`. Category: Executive and project overview.

**Purpose and operational importance.** The title and configured panels indicate a view for kali linux executive overview. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 9 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Host CPU utilization** (`timeseries`; unit: `percent`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `netdata_system_cpu_percentage_average`, `guest_nice`.
- **Memory available** (`timeseries`; unit: `mebibytes`; source: `prometheus`; thresholds: 2048, 4096). Query identifiers: `netdata_system_ram_MiB_average`. Configured label selectors include `dimension`.
- **Filesystem utilization** (`timeseries`; unit: `percent`; source: `prometheus`; thresholds: 70, 90). Query identifiers: `mount_point`, `netdata_disk_space_GiB_average`. Configured label selectors include `dimension`.
- **Docker containers running** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `docker_container_running`. Configured label selectors include `docker_container_running `.
- **Configured project status** (`table`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kali_cc_project_state`.
- **Prometheus scrape targets** (`timeseries`; unit: `short`; source: `prometheus`; thresholds: 1).
- **Failed systemd units** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_cc_systemd_failed_units`.
- **Configured local checks** (`state-timeline`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `kali_cc_health_check_up`.
- **Docker containers stopped** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `docker_container_running`. Configured label selectors include `docker_container_running `.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kali Linux Executive Overview, documenting configured signals that can support investigation and operational decisions.


## 23. Alertmanager / Overview

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `alertmanager-overview`. URL: `http://127.0.0.1:13000/d/alertmanager-overview/alertmanager-overview`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for alertmanager / overview. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 4 non-row panels are defined. Referenced data sources: `$datasource`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Alerts** (`timeseries`; unit: `none`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `alertmanager_alerts`. Configured label selectors include `namespace`, `service`.
- **Alerts receive rate** (`timeseries`; unit: `ops`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `alertmanager_alerts_received_total`, `__rate_interval`, `alertmanager_alerts_invalid_total`. Configured label selectors include `namespace`, `service`.
- **$integration: Notifications Send Rate** (`timeseries`; unit: `ops`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `alertmanager_notifications_total`, `__rate_interval`, `alertmanager_notifications_failed_total`. Configured label selectors include `integration`, `namespace`, `service`.
- **$integration: Notification Duration** (`timeseries`; unit: `s`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `alertmanager_notification_latency_seconds_bucket`, `__rate_interval`, `alertmanager_notification_latency_seconds_sum`, `alertmanager_notification_latency_seconds_count`. Configured label selectors include `integration`, `namespace`, `service`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Alertmanager / Overview, documenting configured signals that can support investigation and operational decisions.


## 24. Alertmanager Advanced

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `eea-9_sik`. URL: `http://127.0.0.1:13000/d/eea-9_sik/alertmanager-advanced`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for alertmanager advanced. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 14 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Alertmanager instances** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `alertmanager_build_info`. Configured label selectors include `cluster`.
- **Active alerts** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `alertmanager_alerts`. Configured label selectors include `cluster`, `state`.
- **Active silences** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `alertmanager_silences`. Configured label selectors include `cluster`, `state`.
- **Configuration reload successful** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `alertmanager_config_last_reload_successful`. Configured label selectors include `cluster`.
- **Alerts by state** (`timeseries`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `alertmanager_alerts`. Configured label selectors include `cluster`.
- **Silences by state** (`timeseries`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `alertmanager_silences`. Configured label selectors include `cluster`.
- **Notification send rate by integration** (`timeseries`; unit: `ops`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `alertmanager_notifications_total`. Configured label selectors include `cluster`.
- **Failed notifications/sec** (`timeseries`; unit: `ops`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `alertmanager_notifications_failed_total`. Configured label selectors include `cluster`.
- **Incoming alerts/sec by status** (`timeseries`; unit: `ops`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `alertmanager_alerts_received_total`. Configured label selectors include `cluster`.
- **Notification latency p95** (`timeseries`; unit: `s`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `alertmanager_notification_latency_seconds_bucket`. Configured label selectors include `cluster`.
- **Alert processing latency p99** (`timeseries`; unit: `s`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `alertmanager_dispatcher_alert_processing_duration_seconds_bucket`. Configured label selectors include `cluster`.
- **Alertmanager HTTP requests/sec** (`timeseries`; unit: `ops`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `alertmanager_http_request_duration_seconds_count`. Configured label selectors include `cluster`.
- **Notification log query errors/sec** (`timeseries`; unit: `ops`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `alertmanager_nflog_query_errors_total`. Configured label selectors include `cluster`.
- **Alertmanager process memory** (`timeseries`; unit: `bytes`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `process_resident_memory_bytes`. Configured label selectors include `cluster`, `job`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Alertmanager Advanced, documenting configured signals that can support investigation and operational decisions.


## 25. CoreDNS

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `vkQ0UHxik`. URL: `http://127.0.0.1:13000/d/vkQ0UHxik/coredns`. Category: Networking.

**Purpose and operational importance.** The title and configured panels indicate a view for coredns. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 12 non-row panels are defined. Referenced data sources: `$datasource`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Requests (total)** (`timeseries`; unit: `pps`; source: `$datasource`; thresholds: 80). Query identifiers: `coredns_dns_request_count_total`, `coredns_dns_requests_total`. Configured label selectors include `cluster`, `instance`, `job`.
- **Requests (by qtype)** (`timeseries`; unit: `pps`; source: `$datasource`; thresholds: 80). Query identifiers: `coredns_dns_request_type_count_total`, `coredns_dns_requests_total`. Configured label selectors include `cluster`, `instance`, `job`.
- **Requests (by zone)** (`timeseries`; unit: `pps`; source: `$datasource`; thresholds: 80). Query identifiers: `coredns_dns_request_count_total`, `coredns_dns_requests_total`. Configured label selectors include `cluster`, `instance`, `job`.
- **Requests (DO bit)** (`timeseries`; unit: `pps`; source: `$datasource`; thresholds: 80). Query identifiers: `coredns_dns_request_do_count_total`, `coredns_dns_do_requests_total`, `coredns_dns_request_count_total`, `coredns_dns_requests_total`. Configured label selectors include `cluster`, `instance`, `job`.
- **Requests (size, udp)** (`timeseries`; unit: `bytes`; source: `$datasource`; thresholds: 80). Query identifiers: `histogram_quantile`, `coredns_dns_request_size_bytes`, `coredns_dns_request_size_bytes_bucket`. Configured label selectors include `cluster`, `instance`, `job`, `proto`.
- **Requests (size,tcp)** (`timeseries`; unit: `bytes`; source: `$datasource`; thresholds: 80). Query identifiers: `histogram_quantile`, `coredns_dns_request_size_bytes`, `coredns_dns_request_size_bytes_bucket`. Configured label selectors include `cluster`, `instance`, `job`, `proto`.
- **Responses (by rcode)** (`timeseries`; unit: `pps`; source: `$datasource`; thresholds: 80). Query identifiers: `coredns_dns_response_rcode_count_total`, `coredns_dns_responses_total`. Configured label selectors include `cluster`, `instance`, `job`.
- **Responses (duration)** (`timeseries`; unit: `s`; source: `$datasource`; thresholds: 80). Query identifiers: `histogram_quantile`, `coredns_dns_request_duration_seconds`, `coredns_dns_request_duration_seconds_bucket`. Configured label selectors include `cluster`, `instance`, `job`.
- **Responses (size, udp)** (`timeseries`; unit: `bytes`; source: `$datasource`; thresholds: 80). Query identifiers: `histogram_quantile`, `coredns_dns_response_size_bytes`, `coredns_dns_response_size_bytes_bucket`. Configured label selectors include `cluster`, `instance`, `job`, `proto`.
- **Responses (size, tcp)** (`timeseries`; unit: `bytes`; source: `$datasource`; thresholds: 80). Query identifiers: `histogram_quantile`, `coredns_dns_response_size_bytes`, `coredns_dns_response_size_bytes_bucket`. Configured label selectors include `cluster`, `instance`, `job`, `proto`.
- **Cache (size)** (`timeseries`; unit: `decbytes`; source: `$datasource`; thresholds: 80). Query identifiers: `coredns_cache_size`, `coredns_cache_entries`. Configured label selectors include `cluster`, `instance`, `job`.
- **Cache (hitrate)** (`timeseries`; unit: `pps`; source: `$datasource`; thresholds: 80). Query identifiers: `coredns_cache_hits_total`, `coredns_cache_misses_total`. Configured label selectors include `cluster`, `instance`, `job`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for CoreDNS, documenting configured signals that can support investigation and operational decisions.


## 26. Grafana Overview

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `6be0s85Mk`. URL: `http://127.0.0.1:13000/d/6be0s85Mk/grafana-overview`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for grafana overview. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 5 non-row panels are defined. Referenced data sources: `$datasource`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Firing Alerts** (`stat`; unit: `Grafana default`; source: `$datasource`; thresholds: 80). Query identifiers: `grafana_alerting_result_total`. Configured label selectors include `instance`, `job`, `state`.
- **Dashboards** (`stat`; unit: `Grafana default`; source: `$datasource`; thresholds: 80). Query identifiers: `grafana_stat_totals_dashboard`. Configured label selectors include `instance`, `job`.
- **Build Info** (`table`; unit: `Grafana default`; source: `$datasource`; thresholds: 80). Query identifiers: `grafana_build_info`. Configured label selectors include `instance`, `job`.
- **RPS** (`timeseries`; unit: `reqps`; source: `$datasource`; thresholds: 80). Query identifiers: `status_code`, `grafana_http_request_duration_seconds_count`. Configured label selectors include `instance`, `job`.
- **Request Latency** (`timeseries`; unit: `ms`; source: `$datasource`; thresholds: 80). Query identifiers: `histogram_quantile`, `grafana_http_request_duration_seconds_bucket`, `__rate_interval`, `grafana_http_request_duration_seconds_sum`, `grafana_http_request_duration_seconds_count`. Configured label selectors include `instance`, `job`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Grafana Overview, documenting configured signals that can support investigation and operational decisions.


## 27. Kubernetes / API server

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `09ec8aa1e996d6ffcd6817bbaff4db1b`. URL: `http://127.0.0.1:13000/d/09ec8aa1e996d6ffcd6817bbaff4db1b/kubernetes-api-server`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / api server. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 17 non-row panels are defined. Referenced data sources: `${datasource}`, `-- Mixed --`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Notice** (`text`; unit: `Grafana default`; source: `-- Mixed --`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).
- **Availability (30d) > 99.000%** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `apiserver_request:availability30d`. Configured label selectors include `cluster`, `verb`.
- **Error Budget (30d) > 99.000%** (`timeseries`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `apiserver_request:availability30d`. Configured label selectors include `cluster`, `verb`.
- **Read Availability (30d)** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `apiserver_request:availability30d`. Configured label selectors include `cluster`, `verb`.
- **Read SLI - Requests** (`timeseries`; unit: `reqps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `code_resource:apiserver_request_total:rate5m`. Configured label selectors include `cluster`, `verb`.
- **Read SLI - Errors** (`timeseries`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `code_resource:apiserver_request_total:rate5m`. Configured label selectors include `cluster`, `code`, `verb`.
- **Read SLI - Duration** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `cluster_quantile:apiserver_request_sli_duration_seconds:histogram_quantile`. Configured label selectors include `cluster`, `verb`.
- **Write Availability (30d)** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `apiserver_request:availability30d`. Configured label selectors include `cluster`, `verb`.
- **Write SLI - Requests** (`timeseries`; unit: `reqps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `code_resource:apiserver_request_total:rate5m`. Configured label selectors include `cluster`, `verb`.
- **Write SLI - Errors** (`timeseries`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `code_resource:apiserver_request_total:rate5m`. Configured label selectors include `cluster`, `code`, `verb`.
- **Write SLI - Duration** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `cluster_quantile:apiserver_request_sli_duration_seconds:histogram_quantile`. Configured label selectors include `cluster`, `verb`.
- **Work Queue Add Rate** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `workqueue_adds_total`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.
- **Work Queue Depth** (`timeseries`; unit: `short`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `workqueue_depth`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.
- **Work Queue Latency** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `workqueue_queue_duration_seconds_bucket`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.
- **Memory** (`timeseries`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `process_resident_memory_bytes`. Configured label selectors include `cluster`, `instance`, `job`.
- **CPU usage** (`timeseries`; unit: `short`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `process_cpu_seconds_total`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.
- **Goroutines** (`timeseries`; unit: `short`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `go_goroutines`. Configured label selectors include `cluster`, `instance`, `job`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kubernetes / API server, documenting configured signals that can support investigation and operational decisions.


## 28. Kubernetes / Compute Resources /  Multi-Cluster

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `b59e6c9f2fcbe2e16d77fc492374cc4f`. URL: `http://127.0.0.1:13000/d/b59e6c9f2fcbe2e16d77fc492374cc4f/kubernetes-compute-resources-multi-cluster`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / compute resources /  multi-cluster. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 10 non-row panels are defined. Referenced data sources: `${datasource}`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **CPU Utilisation** (`stat`; unit: `none`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `cluster:node_cpu:ratio_rate5m`.
- **CPU Requests Commitment** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_container_resource_requests`, `kube_node_status_allocatable`. Configured label selectors include `job`, `resource`.
- **CPU Limits Commitment** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_container_resource_limits`, `kube_node_status_allocatable`. Configured label selectors include `job`, `resource`.
- **Memory Utilisation** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_memory_MemAvailable_bytes:sum`, `node_memory_MemTotal_bytes`. Configured label selectors include `job`.
- **Memory Requests Commitment** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_container_resource_requests`, `kube_node_status_allocatable`. Configured label selectors include `job`, `resource`.
- **Memory Limits Commitment** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_container_resource_limits`, `kube_node_status_allocatable`. Configured label selectors include `job`, `resource`.
- **CPU Usage** (`timeseries`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_namespace_pod_container:container_cpu_usage_seconds_total:sum_rate5m`.
- **CPU Quota** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_namespace_pod_container:container_cpu_usage_seconds_total:sum_rate5m`, `kube_pod_container_resource_requests`, `kube_pod_container_resource_limits`. Configured label selectors include `job`, `resource`.
- **Memory Usage (w/o cache)** (`timeseries`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_memory_rss`, `metrics_path`. Configured label selectors include `job`, `metrics_path`.
- **Memory Requests by Cluster** (`table`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_memory_rss`, `metrics_path`, `kube_pod_container_resource_requests`, `kube_pod_container_resource_limits`. Configured label selectors include `job`, `metrics_path`, `resource`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kubernetes / Compute Resources /  Multi-Cluster, documenting configured signals that can support investigation and operational decisions.


## 29. Kubernetes / Compute Resources / Cluster

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `efa86fd1d0c121a26444b636a3f509a8`. URL: `http://127.0.0.1:13000/d/efa86fd1d0c121a26444b636a3f509a8/kubernetes-compute-resources-cluster`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / compute resources / cluster. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 22 non-row panels are defined. Referenced data sources: `${datasource}`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **CPU Utilisation** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `cluster:node_cpu:ratio_rate5m`. Configured label selectors include `cluster`.
- **CPU Requests Commitment** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `namespace_cpu:kube_pod_container_resource_requests:sum`, `kube_node_status_allocatable`. Configured label selectors include `cluster`, `job`, `resource`.
- **CPU Limits Commitment** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `namespace_cpu:kube_pod_container_resource_limits:sum`, `kube_node_status_allocatable`. Configured label selectors include `cluster`, `job`, `resource`.
- **Memory Utilisation** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_memory_MemAvailable_bytes:sum`, `node_memory_MemTotal_bytes`. Configured label selectors include `cluster`, `job`.
- **Memory Requests Commitment** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `namespace_memory:kube_pod_container_resource_requests:sum`, `kube_node_status_allocatable`. Configured label selectors include `cluster`, `job`, `resource`.
- **Memory Limits Commitment** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `namespace_memory:kube_pod_container_resource_limits:sum`, `kube_node_status_allocatable`. Configured label selectors include `cluster`, `job`, `resource`.
- **CPU Usage** (`timeseries`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_namespace_pod_container:container_cpu_usage_seconds_total:sum_rate5m`. Configured label selectors include `cluster`.
- **CPU Quota** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_owner`, `namespace_workload_pod:kube_pod_owner:relabel`, `node_namespace_pod_container:container_cpu_usage_seconds_total:sum_rate5m`, `namespace_cpu:kube_pod_container_resource_requests:sum`, `namespace_cpu:kube_pod_container_resource_limits:sum`. Configured label selectors include `cluster`, `job`.
- **Memory** (`timeseries`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_memory_rss`, `metrics_path`. Configured label selectors include `cluster`, `job`, `metrics_path`.
- **Memory Requests by Namespace** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_owner`, `namespace_workload_pod:kube_pod_owner:relabel`, `container_memory_rss`, `metrics_path`, `namespace_memory:kube_pod_container_resource_requests:sum`, `namespace_memory:kube_pod_container_resource_limits:sum`. Configured label selectors include `cluster`, `job`, `metrics_path`.
- **Current Network Usage** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `metrics_path`, `__rate_interval`, `container_network_transmit_bytes_total`, `container_network_receive_packets_total`, `container_network_transmit_packets_total`, `container_network_receive_packets_dropped_total`, `container_network_transmit_packets_dropped_total`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`.
- **Receive Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`.
- **Transmit Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_bytes_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`.
- **Average Container Bandwidth by Namespace: Received** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`.
- **Average Container Bandwidth by Namespace: Transmitted** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_bytes_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`.
- **Rate of Received Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_packets_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`.
- **Rate of Transmitted Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_packets_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`.
- **Rate of Received Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_packets_dropped_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`.
- **Rate of Transmitted Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_packets_dropped_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`.
- **IOPS(Reads+Writes)** (`timeseries`; unit: `iops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_fs_reads_total`, `metrics_path`, `__rate_interval`, `container_fs_writes_total`. Configured label selectors include `cluster`, `device`, `job`, `metrics_path`.
- **ThroughPut(Read+Write)** (`timeseries`; unit: `Bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_fs_reads_bytes_total`, `metrics_path`, `__rate_interval`, `container_fs_writes_bytes_total`. Configured label selectors include `cluster`, `device`, `job`, `metrics_path`.
- **Current Storage IO** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_fs_reads_total`, `metrics_path`, `__rate_interval`, `container_fs_writes_total`, `container_fs_reads_bytes_total`, `container_fs_writes_bytes_total`. Configured label selectors include `cluster`, `device`, `job`, `metrics_path`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kubernetes / Compute Resources / Cluster, documenting configured signals that can support investigation and operational decisions.


## 30. Kubernetes / Compute Resources / Namespace (Pods)

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `85a562078cdf77779eaa1add43ccec1e`. URL: `http://127.0.0.1:13000/d/85a562078cdf77779eaa1add43ccec1e/kubernetes-compute-resources-namespace-pods`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / compute resources / namespace (pods). It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 18 non-row panels are defined. Referenced data sources: `${datasource}`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **CPU Utilisation (from requests)** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_namespace_pod_container:container_cpu_usage_seconds_total:sum_rate5m`, `kube_pod_container_resource_requests`. Configured label selectors include `cluster`, `job`, `namespace`, `resource`.
- **CPU Utilisation (from limits)** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_namespace_pod_container:container_cpu_usage_seconds_total:sum_rate5m`, `kube_pod_container_resource_limits`. Configured label selectors include `cluster`, `job`, `namespace`, `resource`.
- **Memory Utilisation (from requests)** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_memory_working_set_bytes`, `metrics_path`, `kube_pod_container_resource_requests`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `resource`.
- **Memory Utilisation (from limits)** (`stat`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_memory_working_set_bytes`, `metrics_path`, `kube_pod_container_resource_limits`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `resource`.
- **CPU Usage** (`timeseries`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_namespace_pod_container:container_cpu_usage_seconds_total:sum_rate5m`, `kube_resourcequota`. Configured label selectors include `cluster`, `namespace`, `resource`, `type`.
- **CPU Quota** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_namespace_pod_container:container_cpu_usage_seconds_total:sum_rate5m`, `cluster:namespace:pod_cpu:active:kube_pod_container_resource_requests`, `cluster:namespace:pod_cpu:active:kube_pod_container_resource_limits`. Configured label selectors include `cluster`, `namespace`.
- **Memory Usage (w/o cache)** (`timeseries`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_memory_working_set_bytes`, `metrics_path`, `kube_resourcequota`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `resource`, `type`.
- **Memory Quota** (`table`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_memory_working_set_bytes`, `metrics_path`, `cluster:namespace:pod_memory:active:kube_pod_container_resource_requests`, `cluster:namespace:pod_memory:active:kube_pod_container_resource_limits`, `container_memory_rss`, `container_memory_cache`, `container_memory_swap`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`.
- **Current Network Usage** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `metrics_path`, `__rate_interval`, `container_network_transmit_bytes_total`, `container_network_receive_packets_total`, `container_network_transmit_packets_total`, `container_network_receive_packets_dropped_total`, `container_network_transmit_packets_dropped_total`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`.
- **Receive Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `__rate_interval`. Configured label selectors include `cluster`, `namespace`.
- **Transmit Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_bytes_total`, `__rate_interval`. Configured label selectors include `cluster`, `namespace`.
- **Rate of Received Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_packets_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`.
- **Rate of Transmitted Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_packets_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`.
- **Rate of Received Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_packets_dropped_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`.
- **Rate of Transmitted Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_packets_dropped_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`.
- **IOPS(Reads+Writes)** (`timeseries`; unit: `iops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_fs_reads_total`, `__rate_interval`, `container_fs_writes_total`. Configured label selectors include `cluster`, `device`, `namespace`.
- **ThroughPut(Read+Write)** (`timeseries`; unit: `Bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_fs_reads_bytes_total`, `__rate_interval`, `container_fs_writes_bytes_total`. Configured label selectors include `cluster`, `device`, `namespace`.
- **Current Storage IO** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_fs_reads_total`, `metrics_path`, `__rate_interval`, `container_fs_writes_total`, `container_fs_reads_bytes_total`, `container_fs_writes_bytes_total`. Configured label selectors include `cluster`, `device`, `job`, `metrics_path`, `namespace`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified; view filter: namespace=default.

**LinkedIn caption.** A focused Grafana view for Kubernetes / Compute Resources / Namespace (Pods), documenting configured signals that can support investigation and operational decisions.


## 31. Kubernetes / Compute Resources / Namespace (Workloads)

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `a87fb0d919ec0ea5f6543124e16c42a5`. URL: `http://127.0.0.1:13000/d/a87fb0d919ec0ea5f6543124e16c42a5/kubernetes-compute-resources-namespace-workloads`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / compute resources / namespace (workloads). It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 13 non-row panels are defined. Referenced data sources: `${datasource}`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **CPU Usage** (`timeseries`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_namespace_pod_container:container_cpu_usage_seconds_total:sum_rate5m`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`, `kube_resourcequota`. Configured label selectors include `cluster`, `namespace`, `resource`, `type`, `workload_type`.
- **CPU Quota** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `namespace_workload_pod:kube_pod_owner:relabel`, `workload_type`, `node_namespace_pod_container:container_cpu_usage_seconds_total:sum_rate5m`, `group_left`, `kube_pod_container_resource_requests`, `kube_pod_container_resource_limits`. Configured label selectors include `cluster`, `job`, `namespace`, `resource`, `workload_type`.
- **Memory Usage** (`timeseries`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_memory_working_set_bytes`, `metrics_path`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`, `kube_resourcequota`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `resource`, `type`, `workload_type`.
- **Memory Quota** (`table`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `namespace_workload_pod:kube_pod_owner:relabel`, `workload_type`, `container_memory_working_set_bytes`, `metrics_path`, `group_left`, `kube_pod_container_resource_requests`, `kube_pod_container_resource_limits`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `resource`, `workload_type`.
- **Current Network Usage** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`, `container_network_transmit_bytes_total`, `container_network_receive_packets_total`, `container_network_transmit_packets_total`, `container_network_receive_packets_dropped_total`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload_type`.
- **Receive Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Transmit Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_bytes_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Average Container Bandwidth by Workload: Received** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Average Container Bandwidth by Workload: Transmitted** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_bytes_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Rate of Received Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_packets_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Rate of Transmitted Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_packets_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Rate of Received Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_packets_dropped_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Rate of Transmitted Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_packets_dropped_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified; view filter: namespace=default, type=deployment.

**LinkedIn caption.** A focused Grafana view for Kubernetes / Compute Resources / Namespace (Workloads), documenting configured signals that can support investigation and operational decisions.


## 32. Kubernetes / Compute Resources / Node (Pods)

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `200ac8fdbfbb74b39aff88118e4d1c2c`. URL: `http://127.0.0.1:13000/d/200ac8fdbfbb74b39aff88118e4d1c2c/kubernetes-compute-resources-node-pods`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / compute resources / node (pods). It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 5 non-row panels are defined. Referenced data sources: `${datasource}`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **CPU Usage** (`timeseries`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kube_node_status_capacity`, `kube_node_status_allocatable`, `node_namespace_pod_container:container_cpu_usage_seconds_total:sum_rate5m`. Configured label selectors include `cluster`, `job`, `node`, `resource`.
- **CPU Quota** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_namespace_pod_container:container_cpu_usage_seconds_total:sum_rate5m`, `cluster:namespace:pod_cpu:active:kube_pod_container_resource_requests`, `cluster:namespace:pod_cpu:active:kube_pod_container_resource_limits`. Configured label selectors include `cluster`, `node`.
- **Memory Usage (w/cache)** (`timeseries`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kube_node_status_capacity`, `kube_node_status_allocatable`, `node_namespace_pod_container:container_memory_working_set_bytes`. Configured label selectors include `cluster`, `job`, `node`, `resource`.
- **Memory Usage (w/o cache)** (`timeseries`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kube_node_status_capacity`, `kube_node_status_allocatable`, `node_namespace_pod_container:container_memory_rss`. Configured label selectors include `cluster`, `job`, `node`, `resource`.
- **Memory Quota** (`table`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_namespace_pod_container:container_memory_working_set_bytes`, `cluster:namespace:pod_memory:active:kube_pod_container_resource_requests`, `cluster:namespace:pod_memory:active:kube_pod_container_resource_limits`, `node_namespace_pod_container:container_memory_rss`, `node_namespace_pod_container:container_memory_cache`, `node_namespace_pod_container:container_memory_swap`. Configured label selectors include `cluster`, `node`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kubernetes / Compute Resources / Node (Pods), documenting configured signals that can support investigation and operational decisions.


## 33. Kubernetes / Compute Resources / Pod

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `6581e46e4e5c7ba40a07646395ef7b23`. URL: `http://127.0.0.1:13000/d/6581e46e4e5c7ba40a07646395ef7b23/kubernetes-compute-resources-pod`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / compute resources / pod. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 16 non-row panels are defined. Referenced data sources: `${datasource}`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **CPU Usage** (`timeseries`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_namespace_pod_container:container_cpu_usage_seconds_total:sum_rate5m`, `kube_pod_container_resource_requests`, `kube_pod_container_resource_limits`. Configured label selectors include `cluster`, `job`, `namespace`, `pod`, `resource`.
- **CPU Throttling** (`timeseries`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_cpu_cfs_throttled_periods_total`, `metrics_path`, `__rate_interval`, `container_cpu_cfs_periods_total`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `pod`.
- **CPU Quota** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_namespace_pod_container:container_cpu_usage_seconds_total:sum_rate5m`, `cluster:namespace:pod_cpu:active:kube_pod_container_resource_requests`, `cluster:namespace:pod_cpu:active:kube_pod_container_resource_limits`. Configured label selectors include `cluster`, `namespace`, `pod`.
- **Memory Usage (WSS)** (`timeseries`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_memory_working_set_bytes`, `metrics_path`, `kube_pod_container_resource_requests`, `kube_pod_container_resource_limits`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `pod`, `resource`.
- **Memory Quota** (`table`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_memory_working_set_bytes`, `metrics_path`, `cluster:namespace:pod_memory:active:kube_pod_container_resource_requests`, `cluster:namespace:pod_memory:active:kube_pod_container_resource_limits`, `container_memory_rss`, `container_memory_cache`, `container_memory_swap`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `pod`.
- **Receive Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `pod`.
- **Transmit Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_bytes_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `pod`.
- **Rate of Received Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_packets_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `pod`.
- **Rate of Transmitted Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_packets_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `pod`.
- **Rate of Received Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_packets_dropped_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `pod`.
- **Rate of Transmitted Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_packets_dropped_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `pod`.
- **IOPS (Pod)** (`timeseries`; unit: `iops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_fs_reads_total`, `metrics_path`, `__rate_interval`, `container_fs_writes_total`. Configured label selectors include `cluster`, `device`, `job`, `metrics_path`, `namespace`, `pod`.
- **ThroughPut (Pod)** (`timeseries`; unit: `Bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_fs_reads_bytes_total`, `metrics_path`, `__rate_interval`, `container_fs_writes_bytes_total`. Configured label selectors include `cluster`, `device`, `job`, `metrics_path`, `namespace`, `pod`.
- **IOPS (Containers)** (`timeseries`; unit: `iops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_fs_reads_total`, `metrics_path`, `__rate_interval`, `container_fs_writes_total`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `pod`.
- **ThroughPut (Containers)** (`timeseries`; unit: `Bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_fs_reads_bytes_total`, `metrics_path`, `__rate_interval`, `container_fs_writes_bytes_total`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `pod`.
- **Current Storage IO** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_fs_reads_total`, `metrics_path`, `__rate_interval`, `container_fs_writes_total`, `container_fs_reads_bytes_total`, `container_fs_writes_bytes_total`. Configured label selectors include `cluster`, `device`, `job`, `metrics_path`, `namespace`, `pod`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified; view filter: namespace=default, pod=nginx-5765b9d8c4-gtdwz.

**LinkedIn caption.** A focused Grafana view for Kubernetes / Compute Resources / Pod, documenting configured signals that can support investigation and operational decisions.


## 34. Kubernetes / Compute Resources / Workload

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `a164a7f0339f99e89cea5cb47e9be617`. URL: `http://127.0.0.1:13000/d/a164a7f0339f99e89cea5cb47e9be617/kubernetes-compute-resources-workload`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / compute resources / workload. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 13 non-row panels are defined. Referenced data sources: `${datasource}`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **CPU Usage** (`timeseries`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_namespace_pod_container:container_cpu_usage_seconds_total:sum_rate5m`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `namespace`, `workload`, `workload_type`.
- **CPU Quota** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_namespace_pod_container:container_cpu_usage_seconds_total:sum_rate5m`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`, `kube_pod_container_resource_requests`, `kube_pod_container_resource_limits`. Configured label selectors include `cluster`, `job`, `namespace`, `resource`, `workload`, `workload_type`.
- **Memory Usage** (`timeseries`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_memory_working_set_bytes`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `namespace`, `workload`, `workload_type`.
- **Memory Quota** (`table`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_memory_working_set_bytes`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`, `kube_pod_container_resource_requests`, `kube_pod_container_resource_limits`. Configured label selectors include `cluster`, `job`, `namespace`, `resource`, `workload`, `workload_type`.
- **Current Network Usage** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`, `container_network_transmit_bytes_total`, `container_network_receive_packets_total`, `container_network_transmit_packets_total`, `container_network_receive_packets_dropped_total`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Receive Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Transmit Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_bytes_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Average Container Bandwidth by Pod: Received** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Average Container Bandwidth by Pod: Transmitted** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_bytes_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Rate of Received Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_packets_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Rate of Transmitted Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_packets_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Rate of Received Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_packets_dropped_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Rate of Transmitted Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_packets_dropped_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kubernetes / Compute Resources / Workload, documenting configured signals that can support investigation and operational decisions.


## 35. Kubernetes / Controller Manager

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `72e0e05bef5099e5f049b05fdc429ed4`. URL: `http://127.0.0.1:13000/d/72e0e05bef5099e5f049b05fdc429ed4/kubernetes-controller-manager`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / controller manager. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 10 non-row panels are defined. Referenced data sources: `${datasource}`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Up** (`stat`; unit: `none`; source: `${datasource}`; no threshold steps defined in panel defaults). Configured label selectors include `cluster`, `job`.
- **Work Queue Add Rate** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `workqueue_adds_total`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.
- **Work Queue Depth** (`timeseries`; unit: `short`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `workqueue_depth`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.
- **Work Queue Latency** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `workqueue_queue_duration_seconds_bucket`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.
- **Kube API Request Rate** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `rest_client_requests_total`, `__rate_interval`. Configured label selectors include `code`, `instance`, `job`.
- **Post Request Latency 99th Quantile** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `rest_client_request_duration_seconds_bucket`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`, `verb`.
- **Get Request Latency 99th Quantile** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `rest_client_request_duration_seconds_bucket`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`, `verb`.
- **Memory** (`timeseries`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `process_resident_memory_bytes`. Configured label selectors include `cluster`, `instance`, `job`.
- **CPU usage** (`timeseries`; unit: `short`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `process_cpu_seconds_total`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.
- **Goroutines** (`timeseries`; unit: `short`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `go_goroutines`. Configured label selectors include `cluster`, `instance`, `job`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kubernetes / Controller Manager, documenting configured signals that can support investigation and operational decisions.


## 36. Kubernetes / Kubelet

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `3138fa155d5915769fbded898ac09fd9`. URL: `http://127.0.0.1:13000/d/3138fa155d5915769fbded898ac09fd9/kubernetes-kubelet`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / kubelet. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 24 non-row panels are defined. Referenced data sources: `${datasource}`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Running Kubelets** (`stat`; unit: `none`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kubelet_node_name`, `metrics_path`. Configured label selectors include `cluster`, `job`, `metrics_path`.
- **Running Pods** (`stat`; unit: `none`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kubelet_running_pods`, `metrics_path`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **Running Containers** (`stat`; unit: `none`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kubelet_running_containers`, `metrics_path`, `container_state`. Configured label selectors include `cluster`, `container_state`, `instance`, `job`, `metrics_path`.
- **Actual Volume Count** (`stat`; unit: `none`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `volume_manager_total_volumes`, `metrics_path`, `actual_state_of_world`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`, `state`.
- **Desired Volume Count** (`stat`; unit: `none`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `volume_manager_total_volumes`, `metrics_path`, `desired_state_of_world`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`, `state`.
- **Config Error Count** (`stat`; unit: `none`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kubelet_node_config_error`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **Operation Rate** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kubelet_runtime_operations_total`, `metrics_path`, `__rate_interval`, `operation_type`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **Operation Error Rate** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kubelet_runtime_operations_errors_total`, `metrics_path`, `__rate_interval`, `operation_type`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **Operation Duration 99th quantile** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `kubelet_runtime_operations_duration_seconds_bucket`, `metrics_path`, `__rate_interval`, `operation_type`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **Pod Start Rate** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kubelet_pod_start_duration_seconds_count`, `metrics_path`, `__rate_interval`, `kubelet_pod_worker_duration_seconds_count`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **Pod Start Duration** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `kubelet_pod_start_duration_seconds_bucket`, `metrics_path`, `__rate_interval`, `kubelet_pod_worker_duration_seconds_bucket`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **Storage Operation Rate** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `storage_operation_duration_seconds_count`, `metrics_path`, `__rate_interval`, `operation_name`, `volume_plugin`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **Storage Operation Error Rate** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `storage_operation_errors_total`, `metrics_path`, `__rate_interval`, `operation_name`, `volume_plugin`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **Storage Operation Duration 99th quantile** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `storage_operation_duration_seconds_bucket`, `metrics_path`, `__rate_interval`, `operation_name`, `volume_plugin`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **Cgroup manager operation rate** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kubelet_cgroup_manager_duration_seconds_count`, `metrics_path`, `__rate_interval`, `operation_type`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **Cgroup manager 99th quantile** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `kubelet_cgroup_manager_duration_seconds_bucket`, `metrics_path`, `__rate_interval`, `operation_type`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **PLEG relist rate** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kubelet_pleg_relist_duration_seconds_count`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **PLEG relist interval** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `kubelet_pleg_relist_interval_seconds_bucket`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **PLEG relist duration** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `kubelet_pleg_relist_duration_seconds_bucket`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **RPC rate** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `rest_client_requests_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `code`, `instance`, `job`, `metrics_path`.
- **Request duration 99th quantile** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `rest_client_request_duration_seconds_bucket`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **Memory** (`timeseries`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `process_resident_memory_bytes`, `metrics_path`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **CPU usage** (`timeseries`; unit: `short`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `process_cpu_seconds_total`, `metrics_path`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.
- **Goroutines** (`timeseries`; unit: `short`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `go_goroutines`, `metrics_path`. Configured label selectors include `cluster`, `instance`, `job`, `metrics_path`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kubernetes / Kubelet, documenting configured signals that can support investigation and operational decisions.


## 37. Kubernetes / Networking / Cluster

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `ff635a025bcfea7bc3dd4f508990a3e9`. URL: `http://127.0.0.1:13000/d/ff635a025bcfea7bc3dd4f508990a3e9/kubernetes-networking-cluster`. Category: Networking.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / networking / cluster. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 13 non-row panels are defined. Referenced data sources: `${datasource}`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Current Rate of Bits Received** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`.
- **Current Rate of Bits Transmitted** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`.
- **Current Status** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`, `container_network_transmit_bytes_total`, `container_network_receive_packets_total`, `container_network_transmit_packets_total`, `container_network_receive_packets_dropped_total`, `container_network_transmit_packets_dropped_total`. Configured label selectors include `cluster`, `host_network`.
- **Average Rate of Bits Received** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`.
- **Average Rate of Bits Transmitted** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`.
- **Receive Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`.
- **Transmit Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`.
- **Rate of Received Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_packets_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`.
- **Rate of Transmitted Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_packets_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`.
- **Rate of Received Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_packets_dropped_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`.
- **Rate of Transmitted Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_packets_dropped_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`.
- **Rate of TCP Retransmits out of all sent segments** (`timeseries`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_netstat_Tcp_RetransSegs`, `__rate_interval`, `node_netstat_Tcp_OutSegs`. Configured label selectors include `cluster`.
- **Rate of TCP SYN Retransmits out of all retransmits** (`timeseries`; unit: `percentunit`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `node_netstat_TcpExt_TCPSynRetrans`, `__rate_interval`, `node_netstat_Tcp_RetransSegs`. Configured label selectors include `cluster`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kubernetes / Networking / Cluster, documenting configured signals that can support investigation and operational decisions.


## 38. Kubernetes / Networking / Namespace (Pods)

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `8b7a8b326d7a6f1f04244066368c67af`. URL: `http://127.0.0.1:13000/d/8b7a8b326d7a6f1f04244066368c67af/kubernetes-networking-namespace-pods`. Category: Networking.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / networking / namespace (pods). It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 9 non-row panels are defined. Referenced data sources: `${datasource}`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Current Rate of Bits Received** (`gauge`; unit: `bps`; source: `${datasource}`; thresholds: 5000000000, 7000000000). Query identifiers: `container_network_receive_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`, `namespace`.
- **Current Rate of Bits Transmitted** (`gauge`; unit: `bps`; source: `${datasource}`; thresholds: 5000000000, 7000000000). Query identifiers: `container_network_transmit_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`, `namespace`.
- **Current Network Usage** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`, `container_network_transmit_bytes_total`, `container_network_receive_packets_total`, `container_network_transmit_packets_total`, `container_network_receive_packets_dropped_total`, `container_network_transmit_packets_dropped_total`. Configured label selectors include `cluster`, `host_network`, `namespace`.
- **Receive Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`, `namespace`.
- **Transmit Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`, `namespace`.
- **Rate of Received Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_packets_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`, `namespace`.
- **Rate of Transmitted Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_packets_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`, `namespace`.
- **Rate of Received Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_packets_dropped_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`.
- **Rate of Transmitted Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_packets_dropped_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`. Configured label selectors include `cluster`, `host_network`, `namespace`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kubernetes / Networking / Namespace (Pods), documenting configured signals that can support investigation and operational decisions.


## 39. Kubernetes / Networking / Namespace (Workload)

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `bbb2a765a623ae38130206c7d94a160f`. URL: `http://127.0.0.1:13000/d/bbb2a765a623ae38130206c7d94a160f/kubernetes-networking-namespace-workload`. Category: Networking.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / networking / namespace (workload). It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 11 non-row panels are defined. Referenced data sources: `${datasource}`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Current Rate of Bits Received** (`bargauge`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_receive_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `host_network`, `namespace`, `workload`, `workload_type`.
- **Current Rate of Bits Transmitted** (`bargauge`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_transmit_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `host_network`, `namespace`, `workload`, `workload_type`.
- **Current Status** (`table`; unit: `Grafana default`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `workload_type`, `container_network_receive_bytes_total`, `__rate_interval`, `kube_pod_info`, `host_network`, `group_left`, `namespace_workload_pod:kube_pod_owner:relabel`, `container_network_transmit_bytes_total`, `container_network_receive_packets_total`. Configured label selectors include `cluster`, `host_network`, `namespace`, `workload`, `workload_type`.
- **Receive Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_receive_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `host_network`, `namespace`, `workload`, `workload_type`.
- **Transmit Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_transmit_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `host_network`, `namespace`, `workload`, `workload_type`.
- **Average Container Bandwidth by Workload: Received** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_receive_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `host_network`, `namespace`, `workload`, `workload_type`.
- **Average Container Bandwidth by Workload: Transmitted** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_transmit_bytes_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `host_network`, `namespace`, `workload`, `workload_type`.
- **Rate of Received Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_receive_packets_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `host_network`, `namespace`, `workload`, `workload_type`.
- **Rate of Transmitted Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_transmit_packets_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `host_network`, `namespace`, `workload`, `workload_type`.
- **Rate of Received Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_receive_packets_dropped_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `host_network`, `namespace`, `workload`, `workload_type`.
- **Rate of Transmitted Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_transmit_packets_dropped_total`, `__rate_interval`, `group_left`, `kube_pod_info`, `host_network`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `host_network`, `namespace`, `workload`, `workload_type`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kubernetes / Networking / Namespace (Workload), documenting configured signals that can support investigation and operational decisions.


## 40. Kubernetes / Networking / Pod

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `7a18067ce943a40ae25454675c19ff5c`. URL: `http://127.0.0.1:13000/d/7a18067ce943a40ae25454675c19ff5c/kubernetes-networking-pod`. Category: Networking.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / networking / pod. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 8 non-row panels are defined. Referenced data sources: `${datasource}`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Current Rate of Bits Received** (`gauge`; unit: `bps`; source: `${datasource}`; thresholds: 5000000000, 7000000000). Query identifiers: `container_network_receive_bytes_total`, `__rate_interval`. Configured label selectors include `cluster`, `namespace`, `pod`.
- **Current Rate of Bits Transmitted** (`gauge`; unit: `bps`; source: `${datasource}`; thresholds: 5000000000, 7000000000). Query identifiers: `container_network_transmit_bytes_total`, `__rate_interval`. Configured label selectors include `cluster`, `namespace`, `pod`.
- **Receive Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_bytes_total`, `__rate_interval`. Configured label selectors include `cluster`, `namespace`, `pod`.
- **Transmit Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_bytes_total`, `__rate_interval`. Configured label selectors include `cluster`, `namespace`, `pod`.
- **Rate of Received Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_packets_total`, `__rate_interval`. Configured label selectors include `cluster`, `namespace`, `pod`.
- **Rate of Transmitted Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_packets_total`, `__rate_interval`. Configured label selectors include `cluster`, `namespace`, `pod`.
- **Rate of Received Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_receive_packets_dropped_total`, `__rate_interval`. Configured label selectors include `cluster`, `namespace`, `pod`.
- **Rate of Transmitted Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `container_network_transmit_packets_dropped_total`, `__rate_interval`. Configured label selectors include `cluster`, `namespace`, `pod`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kubernetes / Networking / Pod, documenting configured signals that can support investigation and operational decisions.


## 41. Kubernetes / Networking / Workload

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `728bf77cc1166d2f3133bf25846876cc`. URL: `http://127.0.0.1:13000/d/728bf77cc1166d2f3133bf25846876cc/kubernetes-networking-workload`. Category: Networking.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / networking / workload. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 10 non-row panels are defined. Referenced data sources: `${datasource}`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Current Rate of Bits Received** (`bargauge`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_receive_bytes_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Current Rate of Bits Transmitted** (`bargauge`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_transmit_bytes_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Average Rate of Bits Received** (`bargauge`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_receive_bytes_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Average Rate of Bits Transmitted** (`bargauge`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_transmit_bytes_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Receive Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_receive_bytes_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Transmit Bandwidth** (`timeseries`; unit: `bps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_transmit_bytes_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Rate of Received Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_receive_packets_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Rate of Transmitted Packets** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_transmit_packets_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Rate of Received Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_receive_packets_dropped_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.
- **Rate of Transmitted Packets Dropped** (`timeseries`; unit: `pps`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `container_network_transmit_packets_dropped_total`, `metrics_path`, `__rate_interval`, `group_left`, `workload_type`, `namespace_workload_pod:kube_pod_owner:relabel`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `workload`, `workload_type`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kubernetes / Networking / Workload, documenting configured signals that can support investigation and operational decisions.


## 42. Kubernetes / Persistent Volumes

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `919b92a8e8041bd567af9edab12c840c`. URL: `http://127.0.0.1:13000/d/919b92a8e8041bd567af9edab12c840c/kubernetes-persistent-volumes`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / persistent volumes. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 4 non-row panels are defined. Referenced data sources: `${datasource}`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Volume Space Usage** (`timeseries`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kubelet_volume_stats_capacity_bytes`, `metrics_path`, `kubelet_volume_stats_available_bytes`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `persistentvolumeclaim`.
- **Volume Space Usage** (`gauge`; unit: `percent`; source: `${datasource}`; thresholds: 0, 80, 90). Query identifiers: `kubelet_volume_stats_capacity_bytes`, `metrics_path`, `kubelet_volume_stats_available_bytes`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `persistentvolumeclaim`.
- **Volume inodes Usage** (`timeseries`; unit: `none`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kubelet_volume_stats_inodes_used`, `metrics_path`, `kubelet_volume_stats_inodes`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `persistentvolumeclaim`.
- **Volume inodes Usage** (`gauge`; unit: `percent`; source: `${datasource}`; thresholds: 0, 80, 90). Query identifiers: `kubelet_volume_stats_inodes_used`, `metrics_path`, `kubelet_volume_stats_inodes`. Configured label selectors include `cluster`, `job`, `metrics_path`, `namespace`, `persistentvolumeclaim`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kubernetes / Persistent Volumes, documenting configured signals that can support investigation and operational decisions.


## 43. Kubernetes / Proxy

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `632e265de029684c40b21cb76bca4f94`. URL: `http://127.0.0.1:13000/d/632e265de029684c40b21cb76bca4f94/kubernetes-proxy`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / proxy. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 11 non-row panels are defined. Referenced data sources: `${datasource}`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Up** (`stat`; unit: `none`; source: `${datasource}`; no threshold steps defined in panel defaults). Configured label selectors include `cluster`, `job`.
- **Rules Sync Rate** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kubeproxy_sync_proxy_rules_duration_seconds_count`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.
- **Rules Sync Latency 99th Quantile** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `kubeproxy_sync_proxy_rules_duration_seconds_bucket`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.
- **Network Programming Rate** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `kubeproxy_network_programming_duration_seconds_count`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.
- **Network Programming Latency 99th Quantile** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `kubeproxy_network_programming_duration_seconds_bucket`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.
- **Kube API Request Rate** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `rest_client_requests_total`, `__rate_interval`. Configured label selectors include `cluster`, `code`, `instance`, `job`.
- **Post Request Latency 99th Quantile** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `rest_client_request_duration_seconds_bucket`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`, `verb`.
- **Get Request Latency 99th Quantile** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `rest_client_request_duration_seconds_bucket`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`, `verb`.
- **Memory** (`timeseries`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `process_resident_memory_bytes`. Configured label selectors include `cluster`, `instance`, `job`.
- **CPU usage** (`timeseries`; unit: `short`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `process_cpu_seconds_total`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.
- **Goroutines** (`timeseries`; unit: `short`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `go_goroutines`. Configured label selectors include `cluster`, `instance`, `job`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kubernetes / Proxy, documenting configured signals that can support investigation and operational decisions.


## 44. Kubernetes / Scheduler

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `2e6b6a3b4bddf1427b3a55aa1311c656`. URL: `http://127.0.0.1:13000/d/2e6b6a3b4bddf1427b3a55aa1311c656/kubernetes-scheduler`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes / scheduler. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 9 non-row panels are defined. Referenced data sources: `${datasource}`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Up** (`stat`; unit: `none`; source: `${datasource}`; no threshold steps defined in panel defaults). Configured label selectors include `cluster`, `job`.
- **Scheduling Rate** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `scheduler_scheduling_attempt_duration_seconds_count`, `__rate_interval`, `scheduler_pod_scheduling_sli_duration_seconds_count`, `scheduler_scheduling_algorithm_duration_seconds_count`, `scheduler_volume_scheduling_duration_seconds_count`. Configured label selectors include `cluster`, `instance`, `job`.
- **Scheduling latency 99th Quantile** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `scheduler_scheduling_attempt_duration_seconds_bucket`, `__rate_interval`, `scheduler_pod_scheduling_sli_duration_seconds_bucket`, `scheduler_scheduling_algorithm_duration_seconds_bucket`, `scheduler_volume_scheduling_duration_seconds_bucket`. Configured label selectors include `cluster`, `instance`, `job`.
- **Kube API Request Rate** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `rest_client_requests_total`, `__rate_interval`. Configured label selectors include `cluster`, `code`, `instance`, `job`.
- **Post Request Latency 99th Quantile** (`timeseries`; unit: `ops`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `rest_client_request_duration_seconds_bucket`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`, `verb`.
- **Get Request Latency 99th Quantile** (`timeseries`; unit: `s`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `rest_client_request_duration_seconds_bucket`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`, `verb`.
- **Memory** (`timeseries`; unit: `bytes`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `process_resident_memory_bytes`. Configured label selectors include `cluster`, `instance`, `job`.
- **CPU usage** (`timeseries`; unit: `short`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `process_cpu_seconds_total`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.
- **Goroutines** (`timeseries`; unit: `short`; source: `${datasource}`; no threshold steps defined in panel defaults). Query identifiers: `go_goroutines`. Configured label selectors include `cluster`, `instance`, `job`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kubernetes / Scheduler, documenting configured signals that can support investigation and operational decisions.


## 45. Kubernetes Cluster (Prometheus)

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `4XuMd2Iiz`. URL: `http://127.0.0.1:13000/d/4XuMd2Iiz/kubernetes-cluster-prometheus`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for kubernetes cluster (prometheus). It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 29 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Cluster Pod Usage** (`stat`; unit: `percentunit`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_status_phase`, `kube_node_status_allocatable`. Configured label selectors include `phase`, `resource`, `unit`.
- **Cluster CPU Usage** (`stat`; unit: `percentunit`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_container_resource_requests`, `kube_node_status_allocatable`. Configured label selectors include `node`, `resource`, `unit`.
- **Cluster Memory Usage** (`stat`; unit: `percentunit`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_container_resource_requests`, `kube_node_status_allocatable`. Configured label selectors include `node`, `resource`, `unit`.
- **Cluster Disk Usage** (`stat`; unit: `percentunit`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `node_filesystem_size_bytes`, `node_uname_info`, `node_filesystem_avail_bytes`. Configured label selectors include `nodename`.
- **Cluster Pod Capacity** (`timeseries`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_node_status_allocatable`, `kube_node_status_capacity`, `kube_pod_status_phase`. Configured label selectors include `node`, `phase`, `resource`.
- **Cluster CPU Capacity** (`timeseries`; unit: `cores`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_node_status_capacity`, `kube_node_status_allocatable`, `kube_pod_container_resource_requests`. Configured label selectors include `node`, `resource`, `unit`.
- **Cluster Mem Capacity** (`timeseries`; unit: `bytes`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_node_status_allocatable`, `kube_node_status_capacity`, `kube_pod_container_resource_requests`. Configured label selectors include `node`, `resource`, `unit`.
- **Cluster Disk Capacity** (`timeseries`; unit: `bytes`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `node_filesystem_size_bytes`, `node_uname_info`, `node_filesystem_avail_bytes`. Configured label selectors include `nodename`.
- **Deployment Replicas - Up To Date** (`table`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_deployment_status_replicas`. Configured label selectors include `namespace`.
- **Deployment Replicas** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_deployment_status_replicas`. Configured label selectors include `namespace`.
- **Deployment Replicas - Updated** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_deployment_status_replicas_updated`. Configured label selectors include `namespace`.
- **Deployment Replicas - Unavailable** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_deployment_status_replicas_unavailable`. Configured label selectors include `namespace`.
- **Number Of Nodes** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_node_info`. Configured label selectors include `node`.
- **Nodes Under Disk Pressure** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_node_status_condition`. Configured label selectors include `condition`, `node`, `status`.
- **Nodes Not Ready** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_node_status_condition`. Configured label selectors include `condition`, `node`, `status`.
- **Pods Running** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_status_phase`. Configured label selectors include `namespace`, `phase`.
- **Pods Pending** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_status_phase`. Configured label selectors include `namespace`, `phase`.
- **Pods Failed** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_status_phase`. Configured label selectors include `namespace`, `phase`.
- **Pods Succeeded** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_status_phase`. Configured label selectors include `namespace`, `phase`.
- **Pods Unknown** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_status_phase`. Configured label selectors include `namespace`, `phase`.
- **Containers Running** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_container_status_running`. Configured label selectors include `namespace`.
- **Containers Waiting** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_container_status_waiting`. Configured label selectors include `namespace`.
- **Containers Terminated** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_container_status_terminated`. Configured label selectors include `namespace`.
- **Containers Restarts (Last 30 Minutes)** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_container_status_restarts_total`. Configured label selectors include `namespace`.
- **CPU Cores Requested by Containers** (`stat`; unit: `cores`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_container_resource_requests`. Configured label selectors include `namespace`, `node`, `resource`, `unit`.
- **Memory Requested By Containers** (`stat`; unit: `bytes`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_pod_container_resource_requests`. Configured label selectors include `namespace`, `node`, `resource`, `unit`.
- **Jobs Succeeded** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_job_status_succeeded`. Configured label selectors include `namespace`.
- **Jobs Active** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_job_status_active`. Configured label selectors include `namespace`.
- **Jobs Failed** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `kube_job_status_failed`. Configured label selectors include `namespace`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Kubernetes Cluster (Prometheus), documenting configured signals that can support investigation and operational decisions.


## 46. Node Exporter / AIX

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `7e0a61e486f727d763fb1d86fdd629c2`. URL: `http://127.0.0.1:13000/d/7e0a61e486f727d763fb1d86fdd629c2/node-exporter-aix`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for node exporter / aix. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 8 non-row panels are defined. Referenced data sources: `$datasource`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **CPU Usage** (`timeseries`; unit: `percentunit`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_cpu_seconds_total`, `__rate_interval`, `group_left`. Configured label selectors include `cluster`, `instance`, `job`, `mode`.
- **Load Average** (`timeseries`; unit: `short`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_load1`, `node_load5`, `node_load15`, `node_cpu_seconds_total`. Configured label selectors include `cluster`, `instance`, `job`, `mode`.
- **Memory Usage** (`timeseries`; unit: `bytes`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_memory_total_bytes`, `node_memory_available_bytes`. Configured label selectors include `cluster`, `instance`, `job`.
- **Memory Usage** (`gauge`; unit: `percent`; source: `$datasource`; thresholds: 80, 90). Query identifiers: `node_memory_available_bytes`, `node_memory_total_bytes`. Configured label selectors include `cluster`, `instance`, `job`.
- **Disk I/O** (`timeseries`; unit: `Grafana default`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_disk_read_bytes_total`, `__rate_interval`, `node_disk_written_bytes_total`, `node_disk_io_time_seconds_total`. Configured label selectors include `cluster`, `device`, `instance`, `job`.
- **Disk Space Usage** (`table`; unit: `decbytes`; source: `$datasource`; thresholds: 0.8, 0.9). Query identifiers: `node_filesystem_size_bytes`, `node_filesystem_avail_bytes`. Configured label selectors include `cluster`, `instance`, `job`.
- **Network Received** (`timeseries`; unit: `bps`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_network_receive_bytes_total`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.
- **Network Transmitted** (`timeseries`; unit: `bps`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_network_transmit_bytes_total`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Node Exporter / AIX, documenting configured signals that can support investigation and operational decisions.


## 47. Node Exporter / MacOS

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `629701ea43bf69291922ea45f4a87d37`. URL: `http://127.0.0.1:13000/d/629701ea43bf69291922ea45f4a87d37/node-exporter-macos`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for node exporter / macos. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 8 non-row panels are defined. Referenced data sources: `$datasource`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **CPU Usage** (`timeseries`; unit: `percentunit`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_cpu_seconds_total`, `__rate_interval`, `group_left`. Configured label selectors include `cluster`, `instance`, `job`, `mode`.
- **Load Average** (`timeseries`; unit: `short`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_load1`, `node_load5`, `node_load15`, `node_cpu_seconds_total`. Configured label selectors include `cluster`, `instance`, `job`, `mode`.
- **Memory Usage** (`timeseries`; unit: `bytes`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_memory_total_bytes`, `node_memory_internal_bytes`, `node_memory_purgeable_bytes`, `node_memory_wired_bytes`, `node_memory_compressed_bytes`. Configured label selectors include `cluster`, `instance`, `job`.
- **Memory Usage** (`gauge`; unit: `percent`; source: `$datasource`; thresholds: 80, 90). Query identifiers: `node_memory_internal_bytes`, `node_memory_purgeable_bytes`, `node_memory_wired_bytes`, `node_memory_compressed_bytes`, `node_memory_total_bytes`. Configured label selectors include `cluster`, `instance`, `job`.
- **Disk I/O** (`timeseries`; unit: `Grafana default`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_disk_read_bytes_total`, `__rate_interval`, `node_disk_written_bytes_total`, `node_disk_io_time_seconds_total`. Configured label selectors include `cluster`, `device`, `instance`, `job`.
- **Disk Space Usage** (`table`; unit: `decbytes`; source: `$datasource`; thresholds: 0.8, 0.9). Query identifiers: `node_filesystem_size_bytes`, `node_filesystem_avail_bytes`. Configured label selectors include `cluster`, `instance`, `job`.
- **Network Received** (`timeseries`; unit: `bps`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_network_receive_bytes_total`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.
- **Network Transmitted** (`timeseries`; unit: `bps`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_network_transmit_bytes_total`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Node Exporter / MacOS, documenting configured signals that can support investigation and operational decisions.


## 48. Node Exporter / Nodes

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `7d57716318ee0dddbac5a7f451fb7753`. URL: `http://127.0.0.1:13000/d/7d57716318ee0dddbac5a7f451fb7753/node-exporter-nodes`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for node exporter / nodes. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 8 non-row panels are defined. Referenced data sources: `$datasource`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **CPU Usage** (`timeseries`; unit: `percentunit`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_cpu_seconds_total`, `__rate_interval`, `group_left`. Configured label selectors include `cluster`, `instance`, `job`, `mode`.
- **Load Average** (`timeseries`; unit: `short`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_load1`, `node_load5`, `node_load15`, `node_cpu_seconds_total`. Configured label selectors include `cluster`, `instance`, `job`, `mode`.
- **Memory Usage** (`timeseries`; unit: `bytes`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_memory_MemTotal_bytes`, `node_memory_MemFree_bytes`, `node_memory_Buffers_bytes`, `node_memory_Cached_bytes`. Configured label selectors include `cluster`, `instance`, `job`.
- **Memory Usage** (`gauge`; unit: `percent`; source: `$datasource`; thresholds: 80, 90). Query identifiers: `node_memory_MemAvailable_bytes`, `node_memory_MemTotal_bytes`. Configured label selectors include `cluster`, `instance`, `job`.
- **Disk I/O** (`timeseries`; unit: `Grafana default`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_disk_read_bytes_total`, `__rate_interval`, `node_disk_written_bytes_total`, `node_disk_io_time_seconds_total`. Configured label selectors include `cluster`, `device`, `instance`, `job`.
- **Disk Space Usage** (`table`; unit: `decbytes`; source: `$datasource`; thresholds: 0.8, 0.9). Query identifiers: `node_filesystem_size_bytes`, `node_filesystem_avail_bytes`. Configured label selectors include `cluster`, `instance`, `job`.
- **Network Received** (`timeseries`; unit: `bps`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_network_receive_bytes_total`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.
- **Network Transmitted** (`timeseries`; unit: `bps`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_network_transmit_bytes_total`, `__rate_interval`. Configured label selectors include `cluster`, `instance`, `job`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Node Exporter / Nodes, documenting configured signals that can support investigation and operational decisions.


## 49. Node Exporter / USE Method / Cluster

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `3e97d1d02672cdd0861f4c97c64f89b2`. URL: `http://127.0.0.1:13000/d/3e97d1d02672cdd0861f4c97c64f89b2/node-exporter-use-method-cluster`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for node exporter / use method / cluster. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 9 non-row panels are defined. Referenced data sources: `$datasource`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **CPU Utilisation** (`timeseries`; unit: `percentunit`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `instance:node_cpu_utilisation:rate5m`, `instance:node_num_cpu:sum`. Configured label selectors include `cluster`, `job`.
- **CPU Saturation (Load1 per CPU)** (`timeseries`; unit: `percentunit`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `instance:node_load1_per_cpu:ratio`. Configured label selectors include `cluster`, `job`.
- **Memory Utilisation** (`timeseries`; unit: `percentunit`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `instance:node_memory_utilisation:ratio`. Configured label selectors include `cluster`, `job`.
- **Memory Saturation (Major Page Faults)** (`timeseries`; unit: `rds`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `instance:node_vmstat_pgmajfault:rate5m`. Configured label selectors include `cluster`, `job`.
- **Network Utilisation (Bytes Receive/Transmit)** (`timeseries`; unit: `Bps`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `instance:node_network_receive_bytes_excluding_lo:rate5m`, `instance:node_network_transmit_bytes_excluding_lo:rate5m`. Configured label selectors include `cluster`, `job`.
- **Network Saturation (Drops Receive/Transmit)** (`timeseries`; unit: `Bps`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `instance:node_network_receive_drop_excluding_lo:rate5m`, `instance:node_network_transmit_drop_excluding_lo:rate5m`. Configured label selectors include `cluster`, `job`.
- **Disk IO Utilisation** (`timeseries`; unit: `percentunit`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `instance_device:node_disk_io_time_seconds:rate5m`. Configured label selectors include `cluster`, `job`.
- **Disk IO Saturation** (`timeseries`; unit: `percentunit`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `instance_device:node_disk_io_time_weighted_seconds:rate5m`. Configured label selectors include `cluster`, `job`.
- **Disk Space Utilisation** (`timeseries`; unit: `percentunit`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `node_filesystem_size_bytes`, `node_filesystem_avail_bytes`. Configured label selectors include `cluster`, `job`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Node Exporter / USE Method / Cluster, documenting configured signals that can support investigation and operational decisions.


## 50. Node Exporter / USE Method / Node

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `fac67cfbe174d3ef53eb473d73d9212f`. URL: `http://127.0.0.1:13000/d/fac67cfbe174d3ef53eb473d73d9212f/node-exporter-use-method-node`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for node exporter / use method / node. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 9 non-row panels are defined. Referenced data sources: `$datasource`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **CPU Utilisation** (`timeseries`; unit: `percentunit`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `instance:node_cpu_utilisation:rate5m`. Configured label selectors include `cluster`, `instance`, `job`.
- **CPU Saturation (Load1 per CPU)** (`timeseries`; unit: `percentunit`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `instance:node_load1_per_cpu:ratio`. Configured label selectors include `cluster`, `instance`, `job`.
- **Memory Utilisation** (`timeseries`; unit: `percentunit`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `instance:node_memory_utilisation:ratio`. Configured label selectors include `cluster`, `instance`, `job`.
- **Memory Saturation (Major Page Faults)** (`timeseries`; unit: `rds`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `instance:node_vmstat_pgmajfault:rate5m`. Configured label selectors include `cluster`, `instance`, `job`.
- **Network Utilisation (Bytes Receive/Transmit)** (`timeseries`; unit: `Bps`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `instance:node_network_receive_bytes_physical:rate5m`, `instance:node_network_transmit_bytes_physical:rate5m`. Configured label selectors include `cluster`, `instance`, `job`.
- **Network Saturation (Drops Receive/Transmit)** (`timeseries`; unit: `Bps`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `instance:node_network_receive_drop_physical:rate5m`, `instance:node_network_transmit_drop_physical:rate5m`. Configured label selectors include `cluster`, `instance`, `job`.
- **Disk IO Utilisation** (`timeseries`; unit: `percentunit`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `instance_device:node_disk_io_time_seconds:rate5m`. Configured label selectors include `cluster`, `instance`, `job`.
- **Disk IO Saturation** (`timeseries`; unit: `percentunit`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `instance_device:node_disk_io_time_weighted_seconds:rate5m`. Configured label selectors include `cluster`, `instance`, `job`.
- **Disk Space Utilisation** (`timeseries`; unit: `percentunit`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `sort_desc`, `node_filesystem_avail_bytes`, `node_filesystem_size_bytes`. Configured label selectors include `cluster`, `instance`, `job`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Node Exporter / USE Method / Node, documenting configured signals that can support investigation and operational decisions.


## 51. Prometheus / Overview

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `9fa0d141-d019-4ad7-8bc5-42196ee308bd`. URL: `http://127.0.0.1:13000/d/9fa0d141-d019-4ad7-8bc5-42196ee308bd/prometheus-overview`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for prometheus / overview. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 10 non-row panels are defined. Referenced data sources: `$datasource`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Prometheus Stats** (`table`; unit: `short`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `prometheus_build_info`, `process_start_time_seconds`. Configured label selectors include `cluster`, `instance`, `job`.
- **Target Sync** (`timeseries`; unit: `ms`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `prometheus_target_sync_length_seconds_sum`, `scrape_job`. Configured label selectors include `cluster`, `instance`, `job`.
- **Targets** (`timeseries`; unit: `short`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `prometheus_sd_discovered_targets`. Configured label selectors include `cluster`, `instance`, `job`.
- **Average Scrape Interval Duration** (`timeseries`; unit: `ms`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `prometheus_target_interval_length_seconds_sum`, `prometheus_target_interval_length_seconds_count`. Configured label selectors include `cluster`, `instance`, `job`.
- **Scrape failures** (`timeseries`; unit: `short`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `prometheus_target_scrapes_exceeded_body_size_limit_total`, `prometheus_target_scrapes_exceeded_sample_limit_total`, `prometheus_target_scrapes_sample_duplicate_timestamp_total`, `prometheus_target_scrapes_sample_out_of_bounds_total`, `prometheus_target_scrapes_sample_out_of_order_total`. Configured label selectors include `cluster`, `instance`, `job`.
- **Appended Samples** (`timeseries`; unit: `short`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `prometheus_tsdb_head_samples_appended_total`. Configured label selectors include `cluster`, `instance`, `job`.
- **Head Series** (`timeseries`; unit: `short`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `prometheus_tsdb_head_series`. Configured label selectors include `cluster`, `instance`, `job`.
- **Head Chunks** (`timeseries`; unit: `short`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `prometheus_tsdb_head_chunks`. Configured label selectors include `cluster`, `instance`, `job`.
- **Query Rate** (`timeseries`; unit: `short`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `prometheus_engine_query_duration_seconds_count`, `inner_eval`. Configured label selectors include `cluster`, `instance`, `job`, `slice`.
- **Stage Duration** (`timeseries`; unit: `ms`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `prometheus_engine_query_duration_seconds`. Configured label selectors include `cluster`, `instance`, `job`, `quantile`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Prometheus / Overview, documenting configured signals that can support investigation and operational decisions.


## 52. etcd

**Observed identity.** Grafana folder: `02 - Kubernetes & Observability`. UID: `c2f4e12cdf69feb95caa41a5a1b423d9`. URL: `http://127.0.0.1:13000/d/c2f4e12cdf69feb95caa41a5a1b423d9/etcd`. Category: Kubernetes and observability.

**Purpose and operational importance.** The title and configured panels indicate a view for etcd. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 13 non-row panels are defined. Referenced data sources: `$datasource`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Up** (`stat`; unit: `Grafana default`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `etcd_server_has_leader`. Configured label selectors include `job`.
- **RPC rate** (`timeseries`; unit: `ops`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `grpc_server_started_total`, `grpc_type`, `__rate_interval`, `grpc_server_handled_total`, `grpc_code`. Configured label selectors include `grpc_code`, `grpc_type`, `job`.
- **Active streams** (`timeseries`; unit: `Grafana default`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `grpc_server_started_total`, `grpc_service`, `grpc_type`, `bidi_stream`, `grpc_server_handled_total`. Configured label selectors include `grpc_service`, `grpc_type`, `job`.
- **DB size** (`timeseries`; unit: `bytes`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `etcd_mvcc_db_total_size_in_bytes`. Configured label selectors include `job`.
- **Disk sync duration** (`timeseries`; unit: `s`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `etcd_disk_wal_fsync_duration_seconds_bucket`, `__rate_interval`, `etcd_disk_backend_commit_duration_seconds_bucket`. Configured label selectors include `job`.
- **Memory** (`timeseries`; unit: `bytes`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `process_resident_memory_bytes`. Configured label selectors include `job`.
- **Client traffic in** (`timeseries`; unit: `Bps`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `etcd_network_client_grpc_received_bytes_total`, `__rate_interval`. Configured label selectors include `job`.
- **Client traffic out** (`timeseries`; unit: `Bps`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `etcd_network_client_grpc_sent_bytes_total`, `__rate_interval`. Configured label selectors include `job`.
- **Peer traffic in** (`timeseries`; unit: `Bps`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `etcd_network_peer_received_bytes_total`, `__rate_interval`. Configured label selectors include `job`.
- **Peer traffic out** (`timeseries`; unit: `Bps`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `etcd_network_peer_sent_bytes_total`, `__rate_interval`. Configured label selectors include `job`.
- **Raft proposals** (`timeseries`; unit: `Grafana default`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `etcd_server_leader_changes_seen_total`. Configured label selectors include `job`.
- **Total leader elections per day** (`timeseries`; unit: `Grafana default`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `etcd_server_leader_changes_seen_total`. Configured label selectors include `job`.
- **Peer round trip time** (`timeseries`; unit: `s`; source: `$datasource`; no threshold steps defined in panel defaults). Query identifiers: `histogram_quantile`, `etcd_network_peer_round_trip_time_seconds_bucket`, `__rate_interval`. Configured label selectors include `job`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for etcd, documenting configured signals that can support investigation and operational decisions.


## 53. Falco Dashboard

**Observed identity.** Grafana folder: `03 - Security Operations`. UID: `FvUFlfuZz`. URL: `http://127.0.0.1:13000/d/FvUFlfuZz/falco-dashboard`. Category: Security monitoring.

**Purpose and operational importance.** The title and configured panels indicate a view for falco dashboard. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 10 non-row panels are defined. Referenced data sources: `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Falco rule matches (24h)** (`stat`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `falcosecurity_falco_rules_matches_total`.
- **Current event rate** (`stat`; unit: `ops`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `falcosecurity_falco_rules_matches_total`.
- **Kernel event drops (24h)** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `falcosecurity_scap_n_drops_total`.
- **Falco CPU usage** (`stat`; unit: `percentunit`; source: `prometheus`; thresholds: 0.8, 0.95). Query identifiers: `falcosecurity_falco_cpu_usage_ratio`.
- **Falco uptime** (`stat`; unit: `s`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `falcosecurity_falco_start_timestamp_nanoseconds`.
- **Falco metrics scrape** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Configured label selectors include `job`.
- **Event rate by Falco rule** (`timeseries`; unit: `ops`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `rule_name`, `falcosecurity_falco_rules_matches_total`.
- **Falco rule matches by rule (24h)** (`table`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `rule_name`, `falcosecurity_falco_rules_matches_total`.
- **Falco RSS memory** (`timeseries`; unit: `bytes`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `falcosecurity_falco_memory_rss_bytes`.
- **Falco CPU usage trend** (`timeseries`; unit: `percent`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `falcosecurity_falco_cpu_usage_ratio`.

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Falco Dashboard, documenting configured signals that can support investigation and operational decisions.


## 54. Trivy Operator Security Posture & Vulnerability Intelligence

**Observed identity.** Grafana folder: `03 - Security Operations`. UID: `trivy-operator-overview`. URL: `http://127.0.0.1:13000/d/trivy-operator-overview/b8875f1`. Category: Security monitoring.

**Purpose and operational importance.** The title and configured panels indicate a view for trivy operator security posture & vulnerability intelligence. It gives an operator a focused place to review the named system domain, identify unusual states or trends, and decide what to investigate next. This is an interpretation of the saved dashboard definition, not a report of an incident.

**Observed panels, units, queries, and data sources.** 19 non-row panels are defined. Referenced data sources: `Dashboard default / not explicit`, `prometheus`. Units and threshold steps below are taken from panel defaults; thresholds may also be set by overrides or value mappings. A saved query does not prove that it returned data during capture.

- **Critical** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `trivy_image_vulnerabilities`, `exported_namespace`, `container_name`, `image_repository`. Configured label selectors include `container_name`, `exported_namespace`, `image_repository`, `severity`.
- **High** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1, 10). Query identifiers: `trivy_image_vulnerabilities`, `exported_namespace`, `container_name`, `image_repository`. Configured label selectors include `container_name`, `exported_namespace`, `image_repository`, `severity`.
- **Medium** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1). Query identifiers: `trivy_image_vulnerabilities`, `exported_namespace`, `container_name`, `image_repository`. Configured label selectors include `container_name`, `exported_namespace`, `image_repository`, `severity`.
- **Low** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1, 10). Query identifiers: `trivy_image_vulnerabilities`, `exported_namespace`, `container_name`, `image_repository`. Configured label selectors include `container_name`, `exported_namespace`, `image_repository`, `severity`.
- **Critical + High** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1, 10). Query identifiers: `trivy_image_vulnerabilities`, `exported_namespace`, `container_name`, `image_repository`. Configured label selectors include `container_name`, `exported_namespace`, `image_repository`, `severity`.
- **Affected images** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1, 5). Query identifiers: `image_digest`, `trivy_image_vulnerabilities`, `exported_namespace`, `container_name`, `image_repository`. Configured label selectors include `container_name`, `exported_namespace`, `image_repository`, `severity`.
- **Configuration audit failures** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1, 10). Query identifiers: `trivy_resource_configaudits`, `exported_namespace`. Configured label selectors include `exported_namespace`, `severity`.
- **Exposed secrets** (`stat`; unit: `short`; source: `prometheus`; thresholds: 1, 10). Query identifiers: `trivy_image_exposedsecrets`, `exported_namespace`, `container_name`, `image_repository`. Configured label selectors include `container_name`, `exported_namespace`, `image_repository`, `severity`.
- **Image vulnerability findings by severity** (`barchart`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `trivy_image_vulnerabilities`, `exported_namespace`, `container_name`, `image_repository`. Configured label selectors include `container_name`, `exported_namespace`, `image_repository`, `severity`.
- **Critical and high findings by namespace** (`barchart`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `exported_namespace`, `trivy_image_vulnerabilities`, `container_name`, `image_repository`. Configured label selectors include `container_name`, `exported_namespace`, `image_repository`, `severity`.
- **Image vulnerability severity mix** (`piechart`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `trivy_image_vulnerabilities`, `exported_namespace`, `container_name`, `image_repository`. Configured label selectors include `container_name`, `exported_namespace`, `image_repository`, `severity`.
- **Highest-risk images · critical and high** (`table`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `exported_namespace`, `container_name`, `image_registry`, `image_repository`, `image_tag`, `image_digest`, `trivy_image_vulnerabilities`. Configured label selectors include `container_name`, `exported_namespace`, `image_repository`, `severity`.
- **Vulnerability findings by workload and severity** (`table`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `exported_namespace`, `resource_kind`, `resource_name`, `container_name`, `image_repository`, `image_tag`, `trivy_image_vulnerabilities`. Configured label selectors include `container_name`, `exported_namespace`, `image_repository`, `severity`.
- **Configuration audit failures by namespace and severity** (`barchart`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `exported_namespace`, `trivy_resource_configaudits`. Configured label selectors include `exported_namespace`, `severity`.
- **Cluster compliance checks · pass vs fail** (`barchart`; unit: `short`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `trivy_cluster_compliance`.
- **Infrastructure assessment findings by resource** (`table`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `exported_namespace`, `resource_kind`, `resource_name`, `trivy_resource_infraassessments`. Configured label selectors include `exported_namespace`, `severity`.
- **RBAC assessment findings by resource** (`table`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `exported_namespace`, `resource_kind`, `trivy_role_rbacassessments`. Configured label selectors include `exported_namespace`, `severity`.
- **Images with exposed secret findings** (`table`; unit: `Grafana default`; source: `prometheus`; no threshold steps defined in panel defaults). Query identifiers: `exported_namespace`, `container_name`, `image_repository`, `image_tag`, `trivy_image_exposedsecrets`. Configured label selectors include `container_name`, `exported_namespace`, `image_repository`, `severity`.
- **CVE, package, fix version and advisory drill-down** (`text`; unit: `Grafana default`; source: `Dashboard default / not explicit`; no threshold steps defined in panel defaults). No data query in the saved panel (often a text/layout panel).

**How to use it.**

1. Open when investigating a symptom in the named domain; set a time range that brackets the symptom.
2. Start with summary/stat panels if present, then inspect detailed tables and time series listed above.
3. Check sustained changes, unexpected states, missing series, stale data, or threshold crossings. Confirm that a gap is not a query, variable, or collection problem.
4. Correlate panels over the same time window and use only labels and filters configured in the displayed queries.
5. Validate the signal in the source system and consult logs, audit records, service state, or configuration as appropriate.
6. Remediate only after confirming cause and scope; escalate through the owner or incident process when needed.
7. Recheck the affected signal and related health panels over a suitable interval to verify recovery.

**Hypothetical scenario.** If one panel changes while a related health or activity panel changes in the same time window, compare their labels and confirm the condition at the source before changing configuration. This example is hypothetical.

**Limitations.** The panels and queries above are what the saved dashboard defines. No source result, telemetry completeness, event coverage, or alerting behavior is inferred from query text alone. Empty or unavailable panels need source-side validation. Current capture status: Quality-reviewed; rendered title visible; PNG-verified.

**LinkedIn caption.** A focused Grafana view for Trivy Operator Security Posture & Vulnerability Intelligence, documenting configured signals that can support investigation and operational decisions.



## Layout review (2026-10-18)

Four dashboards had their panel positions reorganized to remove overlapping or poorly aligned rows: Docker Containers Advanced, Network and Connectivity, Storage and Project Capacity, and Linux Network Stack (node_exporter). Only panel grid positions changed; queries and data sources were preserved. Updated screenshots are listed in `dashboard-inventory.csv`.
