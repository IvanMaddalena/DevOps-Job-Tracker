# 📊 DevOps Job Tracker API

Track your tech job applications, interviews, and outcomes with this clean, fast, and lightweight API.  
Built using **FastAPI**, **SQLite**, and **SQLAlchemy**, and ready for cloud deployment or frontend integration. 🚀

---

## 🔍 Features

- 📝 Track jobs you've applied for (company, position, date)
- 💼 Add and manage interviews by stage and feedback
- 📈 Easily query all jobs and interviews
- 🛡️ Interactive API docs via Swagger UI

---

## ⚙️ Tech Stack

| Layer       | Technology                 |
|-------------|----------------------------|
| API         | FastAPI                    |
| ORM         | SQLAlchemy                 |
| DB          | SQLite                     |
| Models      | Pydantic                   |
| Config      | dotenv                     |

---

## 📁 Project Structure

```
devops-job-tracker/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI app
│   ├── models.py          # SQLAlchemy models
│   ├── schemas.py         # Pydantic schemas
│   ├── routes.py          # API endpoints
│   └── database.py        # DB engine and session
├── .env                   # Environment config
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/devops-job-tracker.git
cd devops-job-tracker
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
uvicorn app.main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

---

## 📌 API Overview

### Jobs
- `POST /jobs/` → Create a job entry
- `GET /jobs/` → List all jobs

### Interviews
- `POST /interviews/` → Add an interview for a job
- `GET /interviews/` → List all interviews

---

## 👤 Author

Developed by **Ivan Maddalena**  
📫 Contact: ivan.maddalena00@gmail.com  
🔗 [GitHub Profile](https://github.com/IvanMaddalena)

---

## 📜 License

This project is licensed under the MIT License.