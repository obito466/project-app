# Project App

A simple Flask web app containerized with Docker and run with Docker Compose.
It serves a landing page and a small JSON REST API (no database).

## Project structure

```
.
├── app.py               # Flask application
├── requirements.txt     # Python dependencies
├── templates/index.html # Landing page
├── Dockerfile           # Image build instructions
├── docker-compose.yml   # Service definition
└── .dockerignore
```

## Endpoints

| Method | Path                  | Description              |
|--------|-----------------------|--------------------------|
| GET    | `/`                   | Landing page             |
| GET    | `/api/students`       | List of sample students  |
| GET    | `/api/students/<id>`  | Single student (or 404)  |
| GET    | `/health`             | Health check             |

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) with Docker Compose v2

## Run with Docker Compose (recommended)

```bash
docker compose up --build
```

Open http://localhost:5000 in your browser, or:

```bash
curl http://localhost:5000/api/students
```

Run in the background / stop:

```bash
docker compose up -d --build
docker compose down
```

## Run with plain Docker

```bash
docker build -t project-app .
docker run -p 5000:5000 project-app
```

## How it works

**Dockerfile**
1. `python:3.12-slim` – small base image.
2. `requirements.txt` is copied and installed *before* the source code so Docker caches the dependency layer.
3. App code is copied in, and the container runs as a non-root user.
4. `gunicorn` serves the app on port 5000.

**docker-compose.yml**
- `build: .` builds the image from the Dockerfile.
- `ports: "5000:5000"` maps host port 5000 to the container.
- `environment` sets `APP_NAME`, shown on the home page.
- `healthcheck` calls `/health`; `restart: unless-stopped` restarts the container if it crashes.

## Useful commands

```bash
docker compose ps        # service status
docker compose logs -f   # follow logs
docker compose down      # stop and remove containers
```
