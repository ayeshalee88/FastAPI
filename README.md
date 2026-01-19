
# FastAPI Todo Tutorial 🚀

A beginner-friendly **FastAPI Todo application** that demonstrates how to build a RESTful API using modern Python tooling. This project is designed as a **learning tutorial** and can be extended into a real-world app.

---

## ✨ Features

* ✅ Create, read, update, and delete Todo items (CRUD)
* ⚡ Built with **FastAPI** (high performance, async-ready)
* 📦 Clean project structure
* 🔍 Automatic API docs with **Swagger UI** & **ReDoc**
* 🌐 CORS enabled (ready for frontend integration)
* 🧪 Easy to extend with authentication, database, or UI

---

## 🧠 What You’ll Learn

* How FastAPI works
* Creating API routes
* Request & response models using **Pydantic**
* API testing with Swagger UI
* Project structuring for backend apps
* Preparing an API for deployment

---

## 📁 Project Structure

```text
project/
│
├── src/
│   ├── main.py          # FastAPI app entry point
│   ├── api/
│   │   ├── auth.py      # (optional) auth routes
│   │   └── tasks.py     # Todo routes
│   ├── core/
│   │   └── middleware.py
│   └── models/
│       └── todo.py      # Pydantic models
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ayeshalee88/FastAPI.git
cd FastAPI
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
uvicorn src.main:app --reload
```

App will run at:

```
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI provides interactive docs automatically:

* **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

You can test all Todo endpoints directly from the browser.

---

## 🧪 Example Todo Endpoints

| Method | Endpoint      | Description       |
| ------ | ------------- | ----------------- |
| GET    | `/tasks`      | Get all todos     |
| POST   | `/tasks`      | Create a new todo |
| PUT    | `/tasks/{id}` | Update a todo     |
| DELETE | `/tasks/{id}` | Delete a todo     |

---

## 🚀 Future Improvements

* 🔐 User authentication (JWT)
* 🗄️ Database integration (PostgreSQL / SQLite)
* 🧠 Validation & error handling
* 🎨 Frontend with React / Next.js
* ☁️ Deployment on Railway / Render

---

## 👩‍💻 Author

**Ayesha**
Learning FastAPI, Python backend development, and AI-powered systems.

---

## 📜 License

This project is for **educational purposes**. You are free to use and modify it.

---

⭐ If this tutorial helped you, consider giving the repo a star!
