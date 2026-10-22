# Counter Service – CI/CD Final Project

A small Flask counter microservice used to demonstrate a CI/CD pipeline with
GitHub Actions (flake8 + nose) and OpenShift Pipelines (Tekton).

## Endpoints
- `POST /counters/<name>` – create a counter
- `GET /counters/<name>` – read a counter
- `PUT /counters/<name>` – increment a counter
- `DELETE /counters/<name>` – delete a counter
