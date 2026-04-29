# Event RSVP System

A backend API for creating events and managing RSVPs, built with FastAPI, SQLAlchemy, and PostgreSQL.

## Features

- Create events with an optional flyer image upload
- List all events
- RSVP to an event
- View all RSVPs for an event

## Tech Stack

- **FastAPI** — web framework
- **SQLAlchemy** — ORM
- **PostgreSQL** — database
- **psycopg2** — PostgreSQL driver
- **python-dotenv** — environment variable management

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create the database

In psql or pgAdmin, create a database that matches the name in your `.env`.

### 6. Run the server

```bash
uvicorn main:app --reload
```

Visit **http://127.0.0.1:8000/docs** to explore and test the API interactively.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/events/` | Create a new event (with optional flyer upload) |
| GET | `/events/` | List all events |
| POST | `/events/{event_id}/rsvp` | RSVP to an event |
| GET | `/events/{event_id}/rsvps` | Get all RSVPs for an event |
