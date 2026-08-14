# Lib

Lib is a Nikke Union Raid manager for keeping track of your teammates mock damage numbers, attempts used, rankings and overall raid status. It's a work in progress, so there's many improvements that can be made. 

## Features

- User management
- Nikke management
- Team creation and management
- Raid and boss management
- Mock damage tracking
- Damage rankings
- Nikke image management
- REST API backend
- PostgreSQL database
- Dockerized backend

### Client
- Python
- PySide6
- Qt Designer

### Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL

### Infrastructure
- Docker
- Docker Compose

## Architecture

The application uses a desktop client communicating with a REST API.


PySide6 Client
      |
      | HTTP / REST
      v
   FastAPI
      |
      | SQLAlchemy
      v
 PostgreSQL