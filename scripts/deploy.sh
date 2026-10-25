#!/bin/bash
set -e

echo "Building Docker image..."
docker build -t k8s-observability-platform:latest .

echo "Loading image into Minikube (if using Minikube)..."
# minikube image load k8s-observability-platform:latest

echo "Applying Kubernetes manifests..."
kubectl apply -f k8s/

echo "Deployment complete. Check with: kubectl get pods"
echo "Service: kubectl get svc observability-platform"