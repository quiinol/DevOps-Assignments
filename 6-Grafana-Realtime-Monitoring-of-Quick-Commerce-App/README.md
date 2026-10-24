# Real-Time Monitoring of a Quick-Commerce Application

## Overview
This project implements real-time monitoring for a simulated quick-commerce delivery application using Python, Docker, Prometheus, Grafana, and Jenkins.

## Objectives
- Generate simulated delivery metrics using Python.
- Expose metrics in Prometheus format.
- Collect and monitor metrics using Prometheus.
- Visualize delivery metrics in Grafana.
- Configure alert rules for delivery conditions.
- Automate Docker image building and endpoint testing using Jenkins.

## Technologies Used
- Python
- Docker
- Prometheus
- Grafana
- Jenkins
- Prometheus Python Client
- Git and GitHub

## Project Structure
```text
6-Grafana-Realtime-Monitoring-of-Quick-Commerce-App/
├── delivery_monitoring/
│   ├── delivery_metrics.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── prometheus.yml
│   └── alert_rules.yml
├── screenshots/
│   ├── grafana-dashboard.png
│   ├── prometheus-targets.png
│   ├── prometheus-metrics.png
│   ├── prometheus-alerts.png
│   ├── jenkins-pipeline-success.png
│   └── jenkins-console-success.png
└── README.md
```

## Application Metrics
The Python application simulates delivery activity and exposes metrics through the `/metrics` endpoint, including:
- Total deliveries
- Pending deliveries
- Deliveries on the way
- Average delivery time

## Docker
Build the image:

```bash
cd delivery_monitoring
docker build -t delivery-metrics .
```

Run a test container:

```bash
docker run -d --name delivery-metrics-test -p 8001:8000 delivery-metrics
```

Test the endpoint:

```bash
curl http://localhost:8001/metrics
```

## Prometheus
Prometheus is configured through `prometheus.yml` to scrape application metrics and load the alert rules from `alert_rules.yml`.

- Prometheus: http://localhost:9090
- Targets: http://localhost:9090/targets
- Query interface: http://localhost:9090/graph
- Alerts: http://localhost:9090/alerts

Example PromQL query:

```promql
total_deliveries
```

The application target should show `UP` when Prometheus successfully scrapes its metrics endpoint.

## Alert Rules
The `alert_rules.yml` file defines alert rules for delivery conditions, including high pending deliveries and average delivery time. Alert states depend on the configured thresholds and current metric values.

## Grafana Dashboard
Grafana visualizes metrics collected by Prometheus. The dashboard includes Stat panels for:
1. Total Deliveries
2. Pending Deliveries
3. On-the-Way Deliveries
4. Average Delivery Time

Grafana: http://localhost:3000

## Jenkins CI Pipeline
The Jenkins pipeline performs these stages:
1. Check Docker availability.
2. Check out the GitHub repository.
3. Build the delivery metrics Docker image.
4. Start a temporary container and test the `/metrics` endpoint.

The successful pipeline returned HTTP status `200`, printed metrics, and removed the temporary test container.

## Screenshots
The `screenshots/` directory contains:
- `grafana-dashboard.png` — Grafana monitoring dashboard.
- `prometheus-targets.png` — Prometheus targets.
- `prometheus-metrics.png` — Prometheus metric query.
- `prometheus-alerts.png` — Prometheus alert rules and states.
- `jenkins-pipeline-success.png` — Successful Jenkins pipeline.
- `jenkins-console-success.png` — Jenkins console output.

## Conclusion
This project demonstrates an integrated monitoring workflow using Python metrics, Docker containerization, Prometheus collection and alert rules, Grafana visualization, and Jenkins-based continuous integration.
