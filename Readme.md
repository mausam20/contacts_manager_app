# 📞 Contact Manager Web App

A simple full-stack contact manager app using **FastAPI** for the backend and **HTML/CSS/JavaScript** for the frontend.

---

## 🚀 Features

- Add new users with name, email, and contact number
- Search users by name or email (
- Delete users by email
- SQLite database (auto-creates table if not exists)
- Proper status codes and validation checks (duplicate users, non-existent deletions)

---

## 🛠 Backend Setup (FastAPI + SQLite)

### 📦 Requirements
```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

### ▶️ Run the Backend
```bash
uvicorn main:app --reload
```
- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

### 🗃 Database
- SQLite is used (`app.db`)
- Auto-creates table `users` if not already present

---

## 🧩 Backend Directory Structure
```
backend/
├── main.py                  # App entrypoint
├── database.py               # Database connection
├── app.py       # FastAPI app deplyment
├── src/
│   └──  app_logic/
│       └── contacts/
│           ├── response_schema.py    # Pydantic request/response models  
            ├── user_controller.py  # CRUD operations  
            ├──database_layer.py   # Database operations  
            ├──user_model.py   # SQLAlchemy user model  
            └── __init__.py  
├── contact_views.py/    # Route definitions
└── requirements.txt  

```

---

## 🌐 Frontend Setup (HTML/CSS/JavaScript)

### 📁 Location
The frontend is a static HTML file (`contact_user_page.html`) located  inside the `/frontend` folder in the root directory.

### ✨ Features
- Simple UI with buttons to add, search, or delete users
- Form for adding user contact
- Search user by name/email 
- Delete user by entering email

Make sure FastAPI backend is running at `http://127.0.0.1:8000`

---

## 🔐 CORS
CORS enabled for all origins in `main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📡 API Endpoints

| Method | Endpoint                 | Description              | Response Code |
|--------|--------------------------|--------------------------|----------------|
| `GET`  | `/users/search/{term}`   | Search by name or email  | 200 OK         |
| `POST` | `/users/save`            | Add a new user           | 201 Created    |
| `GET`  | `/users/delete/{email}`  | Delete a user by email   | 200 OK / 404   |

---

## ✅ Status Codes
- `201`: Created – when a user is added
- `400`: Bad Request – user already exists
- `404`: Not Found – user doesn't exist on delete
- `200`: OK – successful fetch or deletion


