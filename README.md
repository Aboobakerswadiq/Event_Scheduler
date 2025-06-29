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

## 🧑‍💻 Installation, Setup & API Testing (One Command Block)

```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-username/event-scheduler.git
cd event-scheduler

# 2️⃣ Install all required dependencies
pip install flask flask_cors apscheduler pytest

# Optional (for email notifications)
pip install secure-smtplib

# 3️⃣ Run the Flask backend
python app.py

# 4️⃣ Open the frontend
# Just open index.html in your browser (double-click or use VS Code Live Server)

# 5️⃣ [Optional] Test API using Postman
# Example POST Request to create an event:
# URL: http://localhost:5000/events
# Method: POST
# Headers: Content-Type: application/json
# Body:
# {
#   "title": "Meeting with Team",
#   "description": "Project planning",
#   "start_time": "2025-07-01T10:00:00",
#   "end_time": "2025-07-01T11:00:00",
#   "recurring": "weekly",
#   "email": "your-email@gmail.com"
# }

# Example GET to list all events:
# URL: http://localhost:5000/events
# Method: GET

# Example PUT to update an event:
# URL: http://localhost:5000/events/<event_id>
# Method: PUT
# (same JSON format as POST)

# Example DELETE:
# URL: http://localhost:5000/events/<event_id>
# Method: DELETE


