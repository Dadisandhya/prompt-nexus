Prompt Nexus

A full-stack backend project built with Django, Redis, and Docker.
This application allows users to create, view, and manage prompts, with real-time view tracking using Redis.

---
Tech Stack

* **Backend:** Django (Python)
* **Database:** SQLite (default)
* **Cache:** Redis (for view count)
* **Containerization:** Docker & Docker Compose

---

Features

* Create prompts (title, content, complexity)
* Fetch all prompts
* Fetch single prompt by ID
* Track `view_count` using Redis (increments on each view)
* Django Admin panel for easy management
* Fully Dockerized setup

---

Project Structure

```
prompt-nexus/
│
├── backend/
│   ├── prompts/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── redis_client.py
│   │
│   ├── config/
│   ├── manage.py
│   ├── Dockerfile
│
├── docker-compose.yml
└── README.md
```

---

Setup Instructions

### 🔹 Option 1: Run using Docker (Recommended)

```bash
docker compose up --build
```

---

 Access Application

* API: http://localhost:8000/prompts/
* Admin: http://localhost:8000/admin/

---

Sample API Endpoints

### 🔹 Get All Prompts

```
GET /prompts/
```

### 🔹 Create Prompt

```
POST /prompts/create/
```

**Request Body:**

```json
{
  "title": "Sample Prompt",
  "content": "This is a test prompt",
  "complexity": 5
}
```

---

### 🔹 Get Single Prompt (with view count)

```
GET /prompts/<uuid>/
```

**Response:**

```json
{
  "id": "...",
  "title": "Sample Prompt",
  "content": "This is a test prompt",
  "complexity": 5,
  "view_count": 3
}
```

---

##  Redis Integration

* Each time a prompt is accessed, Redis increments a counter:

```
prompt:<id>:views
```

* This ensures fast and scalable tracking of views.

---

## Docker Setup

### docker-compose.yml includes:

* Django backend service
* Redis service

Run everything with:

```bash
docker compose up --build
```

---

##  Future Improvements

* JWT Authentication
* User-based prompt ownership
* Angular/React frontend
* Deployment to cloud (Render / Railway)

---

## Author

**Dadi sandhya**

---

##  Notes

This project demonstrates backend development, caching, and DevOps skills, suitable for real-world scalable applications.
