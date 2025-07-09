# 🌐 Cloud-Native Microservices Platform (Local Kubernetes)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?logo=Prometheus&logoColor=white)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/Grafana-F46800?logo=grafana&logoColor=white)](https://grafana.com)
[![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?logo=mongodb&logoColor=white)](https://www.mongodb.com/)

This project simulates a production-grade cloud-native platform on your local machine using Docker, Kubernetes (Minikube), Prometheus, and Grafana. It's a complete system with API, frontend, database, and monitoring.

## 🧱 Features

- ✅ Python Flask API with MongoDB connection  
- ✅ NGINX frontend (static or React)  
- ✅ MongoDB with persistent storage  
- ✅ Full Kubernetes deployments  
- ✅ Monitoring with Prometheus & Grafana  
- ✅ Automated CI/CD via GitHub Actions  

## ⚙️ Stack

| Component       | Technology          |
|----------------|---------------------|
| Containers     | Docker              |
| Orchestration  | Kubernetes (Minikube)|
| API            | Python Flask        |
| Frontend       | NGINX               |
| Database       | MongoDB             |
| Monitoring     | Prometheus + Grafana|
| CI/CD          | GitHub Actions      |

## 🚀 Full Setup Commands

### 🐳 Start Minikube with Docker Driver
```bash
minikube start --driver=docker
eval $(minikube -p minikube docker-env)
```

### 🏗️ Build Docker Images Locally
```bash
docker build -t local/api:v1 ./docker/api
docker build -t local/frontend:v1 ./docker/frontend
```

### 🚢 Deploy to Kubernetes
```bash
kubectl apply -f k8s/base/
```
### 🌐 Enable Ingress & Configure DNS
```bash
minikube addons enable ingress
echo "$(minikube ip) api.local frontend.local" | sudo tee -a /etc/hosts
```
```bash
kubectl apply -f k8s/base/ingress.yaml
```

### 🔗 Access The App
Frontend: http://frontend.local

API: http://api.local

## 📊 Monitoring with Prometheus & Grafana
### 📦 Install Monitoring Stack with Helm
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install monitoring prometheus-community/kube-prometheus-stack
```

### 🖥️ Access Grafana Dashboard
```bash
kubectl port-forward svc/monitoring-grafana 3000:80
```
Open http://localhost:3000

Login: admin / prom-operator

### 📈 Import Dashboards
In Grafana → "+" → Import, use:

Import these IDs:

| Dashboard Name                | ID      |
| ----------------------------- | ------- |
| Kubernetes Cluster Monitoring | `315`   |
| Prometheus + K8s Cluster      | `12784` |
| Node Exporter Full            | `1860`  |

## 🔁 GitHub Actions CI (Docker Build & Push)
This repo includes a CI pipeline using GitHub Actions that:

- Builds `api` and `frontend` Docker images

- Pushes them to Docker Hub on every push to `main`



## 🧠 What You’ll Learn

- Kubernetes core objects: Deployments, Services, Ingress 

- Docker image creation and multi-service architecture

- Prometheus and Grafana real-time metrics collection

- GitHub Actions automation for container builds
