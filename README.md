# 🏗️ k8s-lab

> **Note:** This project is a hands-on learning lab built to practice Kubernetes, Helm, and GitOps fundamentals in a local environment. It is not production-ready — the goal is to understand the concepts by doing.

## 🛠️ Tech Stack

| Tool       | Purpose                        |
| ---------- | ------------------------------ |
| Python 3   | Basic App                      |
| Docker     | Container runtime              |
| Kubernetes | Cluster                        |
| Helm       | Package manager for Kubernetes |

---

## 🚀 Getting Started

### Prerequisites

- [Helm](https://helm.sh/docs/intro/install/) >= v4.1.3
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Setup

**1. Clone the repo**

```bash
git clone https://github.com/Syenta-Elf/k8s-lab.git
cd k8s-lab
```

**2. Run Helm template for verify**

```bash
helm template k8s-lab-chart
```

**3. Deploy with Helm**

```bash
helm install k8s-lab k8s-lab-chart
```

**4. Verify**

```bash
kubectl get pod,svc
```

### Teardown

```bash
helm uninstall k8s-lab
```

---

## 📁 Project Structure

```
.
├── Dockerfile
├── k8s
│   ├── deployment.yaml
│   └── service.yaml
├── k8s-lab-chart
│   ├── Chart.yaml
│   ├── charts
│   ├── templates
│   │   ├── _helpers.tpl
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── values.yaml
├── main.py
├── README.md
└── requirements.txt
```

---

## 💡 Key Concepts Practiced

- Kubernetes Deployment, Service, liveness/readiness probes
- Helm chart templating, install, upgrade, rollback
- Multi-replica pod management

---

## 🗺️ Roadmap

- [x] FastAPI app + Dockerize
- [x] Kubernetes manifests
- [x] Helm chart
- [ ] ArgoCD GitOps
- [ ] Prometheus + Grafana monitoring

## 📜 License

MIT
