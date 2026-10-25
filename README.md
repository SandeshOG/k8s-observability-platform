# Kubernetes Observability Platform

A production-style cloud-native platform demo built with **Python FastAPI**, **Kubernetes**, and **Prometheus** monitoring.

This project demonstrates skills relevant to Cloud / Platform Software Engineer roles: containerized services, Kubernetes deployments, observability, automation, and operational best practices.

## Architecture

- **FastAPI service** — exposes health, metrics, and business endpoints
- **Kubernetes** — Deployment, Service, ConfigMap, and resource limits
- **Prometheus** — scrapes `/metrics` for observability
- **Automation** — simple scripts for local testing and cluster deployment

## Project Structure

```
k8s-observability-platform/
├── app/
│   ├── main.py
│   └── requirements.txt
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
├── monitoring/
│   └── prometheus-config.yaml
├── Dockerfile
├── scripts/
│   ├── deploy.sh
│   └── local-run.sh
└── README.md
```

## Quick Start

### Local (without Kubernetes)
```bash
cd app
pip install -r requirements.txt
uvicorn main:app --reload
```
Visit: http://localhost:8000/metrics and http://localhost:8000/health

### With Docker
```bash
docker build -t k8s-observability-platform .
docker run -p 8000:8000 k8s-observability-platform
```

### Deploy to Kubernetes (Minikube / Kind / any cluster)
```bash
kubectl apply -f k8s/
```

## Key Features Demonstrated

- Containerized Python service with health checks
- Kubernetes Deployment with resource requests/limits and liveness/readiness probes
- Prometheus metrics exposure (`/metrics`)
- ConfigMap for configuration
- Clean separation of concerns for platform work
- Automation scripts

## Why this project matters for Cloud/Platform roles

- Shows hands-on Kubernetes experience
- Demonstrates observability (Prometheus)
- Uses a modern Python stack (FastAPI)
- Includes operational practices (probes, resource limits, health endpoints)
- Easy to extend with Grafana dashboards, Helm, or CI/CD

## Next Improvements (ideas)

- Add Grafana dashboard
- Helm chart
- GitHub Actions CI/CD
- Horizontal Pod Autoscaler
- Integration with Azure AKS or AWS EKS

---
Built as a portfolio project for cloud platform engineering roles.