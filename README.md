# Task Manager REST API (Django)

A production-ready RESTful API for managing tasks, built using Django REST Framework with JWT authentication, role-based access, pagination, global exception handling, Swagger documentation, and unit tests.

---

## 🚀 Features

- User authentication using JWT (SimpleJWT)
- Role-based access (Admin / Regular user)
- Task CRUD APIs (Create, Read, Update, Delete)
- Pagination (environment-based configuration)
- Global exception handling
- Interactive API documentation (Swagger & ReDoc)
- Unit tests for core APIs

---

## 🛠 Tech Stack

- Python 3.12  
- Django 4.2  
- Django REST Framework  
- SimpleJWT  
- SQLite (can be replaced with PostgreSQL/MySQL)  
- drf-yasg (Swagger & ReDoc)

---

## 📁 Project Structure
# Task Manager REST API (Django)

A production-ready RESTful API for managing tasks, built using Django REST Framework with JWT authentication, role-based access, pagination, global exception handling, Swagger documentation, and unit tests.

---

## 🚀 Features

- User authentication using JWT (SimpleJWT)
- Role-based access (Admin / Regular user)
- Task CRUD APIs (Create, Read, Update, Delete)
- Pagination (environment-based configuration)
- Global exception handling
- Interactive API documentation (Swagger & ReDoc)
- Unit tests for core APIs
- Clean & scalable project structure

---

## 🛠 Tech Stack

- Python 3.12  
- Django 4.2  
- Django REST Framework  
- SimpleJWT  
- SQLite (can be replaced with PostgreSQL/MySQL)  
- drf-yasg (Swagger & ReDoc)

---

## 📁 Project Structure
```text
task-manager-api/
├── apps/
│   ├── accounts/
│   └── tasks/
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── permissions.py
│       └── tests.py
├── common/
│   ├── pagination.py
│   └── exceptions.py
├── config/
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/task-manager-api.git
cd task-manager-api
```

---

### 2. Create & activate virtual environment

```bash
python -m venv venv
```

**Windows**
```bash
venv\Scripts\activate
```

**Mac / Linux**
```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Environment variables (.env)

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key

DEFAULT_PAGE_SIZE=5
MAX_PAGE_SIZE=100
```

---

### 5. Database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Create superuser

```bash
python manage.py createsuperuser
```

---

### 7. Run the server

```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication (JWT)

### Register new user

```
POST /api/register
```

**Request body**
```json
{
  "username": "admin",
  "password": "password"
}
```
---


### Login

```
POST /api/auth/login/
```

**Request body**
```json
{
  "username": "admin",
  "password": "password"
}
```

**Response**
```json
{
  "access": "<jwt_access_token>",
  "refresh": "<jwt_refresh_token>"
}
```

---

### Refresh token

```
POST /api/auth/refresh/
```

---

## 📌 Task APIs

Base URL:

```
/api/tasks/
```

| Method | Endpoint | Description |
|------|--------|-------------|
| GET | `/api/tasks/` | List tasks (paginated) |
| POST | `/api/tasks/` | Create task |
| GET | `/api/tasks/{id}/` | Retrieve task |
| PATCH | `/api/tasks/{id}/` | Update task |
| DELETE | `/api/tasks/{id}/` | Delete task |

All endpoints require JWT authentication.

---

## 📄 API Documentation

Swagger UI:
```
http://127.0.0.1:8000/swagger/
```

ReDoc:
```
http://127.0.0.1:8000/redoc/
```

To authorize in Swagger:

```
Bearer <access_token>
```

---

## ❗ Error Handling

All API errors follow a consistent format:

```json
{
  "success": false,
  "message": "Validation error",
  "errors": {
    "title": ["This field is required."]
  }
}
```

Handled centrally using a global exception handler.

---

## 🧪 Running Unit Tests

```bash
python manage.py test
```

Tests cover:
- Authentication protection
- Task CRUD operations
- Permissions
- Pagination compatibility

---

## 🧠 Best Practices Followed

- DRF ModelViewSet for CRUD APIs
- Environment-based configuration
- Centralized exception handling
- JWT best practices (short-lived access tokens)
- Clean commit history
- Scalable project structure

---

## 📤 Submission Notes

- Codebase shared via GitHub repository
- README includes setup, usage, and testing

---

## 👨‍💻 Author

Akash Singhal 
Backend Developer – Django / Django REST Framework
