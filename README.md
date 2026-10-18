# Grafana dashboard documentation and captures

## Purpose

This package records the live Grafana dashboards discoverable in the local Kubernetes lab, their configured panels and query identifiers, and local browser screenshots. It does not modify dashboards, Grafana, or lab services.

## Screenshot gallery

Browse [all dashboard screenshots](SCREENSHOTS.md), including every scroll segment. Complete original contact sheets are in [`linkedin-assets/unblurred/contact-sheets/`](linkedin-assets/unblurred/contact-sheets/).

## Inventory

The live Grafana API returned **53 dashboards** on 2026-10-18. The requested list matched **19** current titles; `05 - Kali Operations` was not found. The inventory also includes dashboards beyond the 20 names in the supplied list.

- `dashboard-inventory.csv`: current live dashboard names, folders, URLs/UIDs, panel names, screenshot segments, and capture status.
- `dashboard-documentation.md`: observed panel definitions and query metric identifiers, with investigation guidance distinguished from observed configuration.
- `dashboard-guides/`: category indexes into the complete documentation.
- `screenshots/`: unmodified local browser captures; `screenshots/sanitized/` contains separate layout-only derivatives of live Grafana pages, split into overlapping scroll segments where needed.
- `linkedin-assets/`: six grouped contact sheets made from layout-only blurred previews, the combined `screenshot-contact-sheet.png`, and candidate image selections. Original screenshots remain unmodified and contain live lab details.
- `LINKEDIN_POST.md`: evidence-qualified portfolio draft.
- `EXECUTION_REPORT.md`: capture counts and verification details.
- `.dashboard-metadata.json`: local panel metadata used to generate the inventory and documentation; it contains no Grafana credentials.
- `capture_and_document.py`, `review_and_recapture.py`, and `finalize_grafana_assets.py`: read-only capture, quality review, and asset-generation scripts.

## Reproduce

The read-only capture script uses the running port-forward at `http://127.0.0.1:13000`, reads Grafana credentials at runtime from the Kubernetes Secret `monitoring-grafana` in context `kind-devsecops`, retrieves dashboards and datasource references through the Grafana API, and opens each dashboard in headless Chromium at a one-hour range. It captures the scrollable dashboard viewport and checks the PNG signature and file size.

Run `python3 /home/camara/grafana/capture_and_document.py`, then `python3 /home/camara/grafana/review_and_recapture.py` for full scroll coverage and useful existing Kubernetes filter selections, then `python3 /home/camara/grafana/finalize_grafana_assets.py` to apply privacy blur copies, update the final report, and produce contact sheets. Requirements: `kubectl`, `requests`, Selenium, Chromium, ChromeDriver, and Pillow. The capture scripts do not persist credentials or save dashboard edits.

## Known limitations

The screenshot is a point-in-time capture. Query definitions establish what panels are configured, not whether every source returned data. A saved query or empty panel is not proof of monitoring coverage. The local Grafana API requires authentication and the capture depends on its local port-forward. Original screenshot files contain live lab details and should not be posted as-is. Generated contact sheets are layout-only blurred previews; use separately reviewed, selectively redacted images if readable panel detail is needed publicly.


## LinkedIn image assets

`linkedin-assets/unblurred/dashboard-screenshots/` contains full-resolution, unblurred screenshots selected for editorial review. They are not sanitized and may include lab identifiers and live values. `screenshots/sanitized/` contains separate blurred layout previews. See `linkedin-assets/unblurred/dashboard-screenshots/README.md` for the original image index.
