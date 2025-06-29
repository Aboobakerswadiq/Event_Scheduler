# 📅 Event Scheduler System

A full-stack Python + HTML/CSS/JavaScript project that lets users create, view, update, delete, and search for events — with reminders and optional email notifications.

---

## 🚀 Features

### ✅ Core Functionalities
- **Create** events with title, description, start & end time
- **View** all scheduled events (sorted earliest first)
- **Update** existing events
- **Delete** events
- **Persistent storage** using a JSON file (no database needed)

### 🆓 Bonus Features
- 🔁 **Recurring events** (Daily, Weekly, Monthly)
- ⏰ **Reminders** for upcoming events (within the next hour)
- 📩 **Email notifications** (requires Gmail App Password)
- 🔍 **Search** by event title or description
- ✅ **Responsive front-end UI** using Flexbox and clean layout
- 🧪 **Unit tests** (via Pytest)

---

## 📦 Tech Stack

| Layer      | Technology                  |
|------------|-----------------------------|
| Backend    | Python (Flask)              |
| Frontend   | HTML, CSS (Flexbox), JS     |
| Storage    | JSON File                   |
| Email      | Gmail SMTP + App Password   |
| Testing    | Pytest (optional)           |

---

## 🧑‍💻 Installation & Setup

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/Aboobakerswadiq/Event_Scheduler.git
cd event-scheduler

**###2️⃣ Install Dependencies**
pip install flask flask_cors apscheduler
pip install secure-smtplib

3️⃣ Run the Backend
python app.py
Runs on: http://localhost:5000

4️⃣ Open Frontend
Just open index.html in your browser.



