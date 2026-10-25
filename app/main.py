from fastapi import FastAPI
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
import time
import random

app = FastAPI(title="Observability Platform Service", version="1.0.0")

# Metrics
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP requests", ["method", "endpoint"])
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "Request latency")

@app.get("/health")
def health():
    return {"status": "healthy", "service": "k8s-observability-platform"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/api/data")
def get_data():
    start = time.time()
    REQUEST_COUNT.labels(method="GET", endpoint="/api/data").inc()
    
    # Simulate some work
    time.sleep(random.uniform(0.01, 0.1))
    
    REQUEST_LATENCY.observe(time.time() - start)
    return {"message": "Platform data", "value": random.randint(1, 100)}

@app.get("/")
def root():
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()
    return {"message": "Kubernetes Observability Platform API", "docs": "/docs"}