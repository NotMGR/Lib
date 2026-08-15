# Lib

**Lib** is a desktop application for managing **NIKKE Union Raid** groups. It is designed to help raid organizers coordinate their Union by keeping track of users, Nikkes, teams, raid bosses, mock damage, attempts, rankings, and overall raid progress.

Lib is intended to be used by multiple members of Union management through a shared backend server.

> **Note:** Lib is currently a work in progress. The project is under active development and features, APIs, database models, and UI elements may change as development continues.

## Current Status

The current version consists of:

* A functional **PySide6 desktop client**
* A **FastAPI REST API**
* A **PostgreSQL database**
* **SQLAlchemy** ORM models
* **Alembic** database migrations
* A **Docker Compose** setup for the backend and database
* Server connection and connection testing from the desktop client
* NIKKE image management
* Raid, team, user, mock damage, and attempt management

The project is currently focused on building out the backend and connecting the desktop client to it.

## Features

* User management
* Union management
* NIKKE management
* Raid management
* Team management
* Mock damage tracking
* Damage rankings
* Attempt tracking
* NIKKE image management
* Server selection and connection testing
* REST API backend
* PostgreSQL database
* SQLAlchemy ORM
* Alembic database migrations
* Dockerized backend
* Dockerized PostgreSQL database

## Architecture

Lib uses a client-server architecture.

The desktop client communicates with the FastAPI backend over HTTP. The backend handles application logic and database access, while PostgreSQL stores persistent application data.

```text
┌─────────────────────┐
│    Lib Desktop      │
│    PySide6 Client   │
└──────────┬──────────┘
           │
           │ HTTP / REST
           ▼
┌─────────────────────┐
│    FastAPI Backend  │
└──────────┬──────────┘
           │
           │ SQLAlchemy
           ▼
┌─────────────────────┐
│     PostgreSQL      │
└─────────────────────┘
```

## Technology Stack

### Client

* Python
* PySide6
* Qt Designer
* Requests
* PyInstaller

### Backend

* Python
* FastAPI
* SQLAlchemy
* Alembic
* PostgreSQL
* Uvicorn

### Infrastructure

* Docker
* Docker Compose

## Project Structure

```text
Lib/
├── Backend/
│   ├── alembic/
│   │   ├── versions/
│   │   └── ...
│   ├── Dockerfile
│   ├── compose.yaml
│   ├── requirements.txt
│   └── ...
│
├── Client/
│   ├── GUI/
│   ├── logic/
│   ├── images/
│   ├── Lib.spec
│   └── ...
│
└── README.md
```

# Running the Backend

The Lib backend uses Docker Compose to run both the FastAPI application and PostgreSQL.

You do not need to install PostgreSQL or the backend Python dependencies manually.

## Requirements

Install:

* [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* Git (optional, but recommended)

Verify Docker is installed:

```powershell
docker --version
docker compose version
```

Both commands should return a version number.

## 1. Clone the Repository

Clone the repository and enter the project directory:

```powershell
git clone <repository-url>
cd Lib
```

Alternatively, download the repository as a ZIP file from GitHub.

## 2. Configure the Backend

Enter the backend directory:

```powershell
cd Backend
```

Create a `.env` file based on the provided environment configuration.

For example:

```env
POSTGRES_DB=ur_manager
POSTGRES_USER=ur_manager
POSTGRES_PASSWORD=change_this_password

Note: For simplicity, avoid using characters such as $ or @ in the PostgreSQL password, as they may require additional escaping depending on how the environment variable is interpreted.

DATABASE_URL=postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}

API_URL=http://127.0.0.1:8000


> **Important:** Do not commit your `.env` file or real credentials to GitHub.

A `.env.example` file is recommended for development so that the required variables are documented without exposing credentials.
Alternatively, copy .env.example to .env and replace the placeholder values with your own configuration.

## 3. Start the Backend

From the `Backend` directory:

```powershell
docker compose up -d --build
```

Docker Compose will:

1. Create the PostgreSQL container.
2. Create the backend container.
3. Create the required Docker volumes.
4. Wait for PostgreSQL to become healthy.
5. Start the FastAPI application.

The first startup may take longer while Docker downloads the required images and builds the backend image.

## 4. Check the Containers

Run:

```powershell
docker compose ps
```

You should see both services running.

The database should report a healthy status similar to:

```text
Up (healthy)
```

Check backend logs with:

```powershell
docker compose logs backend
```

A successful startup should contain a message similar to:

```text
Application startup complete.
Uvicorn running on http://0.0.0.0:8000
```

## 5. Database Migrations

Lib uses **Alembic** to manage database schema changes.

To check the current migration:

```powershell
docker compose exec backend alembic current
```

To apply pending migrations:

```powershell
docker compose exec backend alembic upgrade head
```

To check whether the SQLAlchemy models and database schema are synchronized:

```powershell
docker compose exec backend alembic check
```

A correctly synchronized database should report:

```text
No new upgrade operations detected.
```

## 6. Access the API

Once the backend is running, the FastAPI application is available at:

```text
http://localhost:8000
```

FastAPI's interactive API documentation is available at:

```text
http://localhost:8000/docs
```

This can be used to inspect and test the available API endpoints.


# Running the Client

The desktop client communicates with the backend using the configured server address.

For local development, this may be:

```text
http://127.0.0.1:8000
```

When connecting to a backend running on another computer on the network, use that computer's local IP address instead:

```text
http://192.168.1.100:8000
```

The backend computer must allow incoming connections on port `8000`.

# Building the Client

The Windows desktop client can be packaged into a standalone executable using PyInstaller.

From the `Client` directory:

```powershell
pyinstaller Lib.spec
```

The generated executable will be placed in:

```text
Client/dist/
```

The generated `build/` and `dist/` directories are not included in the Git repository.

## Client Development Environment

To install the client dependencies manually:

```powershell
cd Client

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

# Backend Development

The backend dependencies are installed inside the Docker image.

To rebuild the backend after changing dependencies or Docker configuration:

```powershell
docker compose up -d --build
```

To enter the running backend container:

```powershell
docker compose exec backend bash
```

If Bash is unavailable:

```powershell
docker compose exec backend sh
```

Useful commands include:

```powershell
docker compose exec backend alembic current
docker compose exec backend alembic upgrade head
docker compose exec backend alembic check
```

# Stopping the Backend

To stop the containers:

```powershell
docker compose down
```

This stops the containers without deleting the PostgreSQL data stored in the Docker volume.

To start the server again:

```powershell
docker compose up -d
```

> **Warning:** Avoid using `docker compose down -v` unless you intentionally want to delete the Docker volumes. Removing the PostgreSQL volume can permanently delete the database and its data.

# Development Roadmap

Planned development includes:

* Expanding the REST API
* Completing client/backend integration
* Authentication and authorization
* Improved Union management
* Improved raid management
* More comprehensive validation
* Automated tests
* Improved error handling
* API documentation
* Production deployment
* Additional client versions that do not require users to manage their own server

The roadmap may change as development continues.

# Contributing

Lib is currently a personal work-in-progress project.

The project is primarily being developed as a learning project while exploring:

* Backend development
* REST APIs
* Database design
* SQLAlchemy
* PostgreSQL
* Database migrations
* Docker
* Client-server architecture
* Desktop application development

Suggestions, bug reports, and improvements are welcome as the project develops.

# License

This project is currently provided without a specified open-source license.
