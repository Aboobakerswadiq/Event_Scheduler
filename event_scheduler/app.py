from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
import json
import os
import uuid
from apscheduler.schedulers.background import BackgroundScheduler
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)
DATA_FILE = 'events.json'

# ========== Persistence ==========


def load_events():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_events(events):
    with open(DATA_FILE, 'w') as f:
        json.dump(events, f, indent=4)

# ========== Create ==========


@app.route('/events', methods=['POST'])
def create_event():
    data = request.json
    new_event = {
        "id": str(uuid.uuid4()),
        "title": data["title"],
        "description": data["description"],
        "start_time": data["start_time"],
        "end_time": data["end_time"],
        "recurring": data.get("recurring", ""),
        "email": data.get("email", "")
    }
    events = load_events()
    events.append(new_event)
    save_events(events)
    return jsonify(new_event), 201

# ========== Read ==========


@app.route('/events', methods=['GET'])
def get_events():
    events = load_events()
    events.sort(key=lambda e: e['start_time'])
    return jsonify(events)

# ========== Update ==========


@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.json
    events = load_events()
    for e in events:
        if e["id"] == event_id:
            e.update(data)
            save_events(events)
            return jsonify(e)
    return jsonify({"error": "Event not found"}), 404

# ========== Delete ==========


@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    events = load_events()
    updated_events = [e for e in events if e["id"] != event_id]
    save_events(updated_events)
    return jsonify({"message": "Event deleted"}), 200

# ========== Search ==========


@app.route('/events/search', methods=['GET'])
def search_events():
    query = request.args.get("q", "").lower()
    events = load_events()
    filtered = [e for e in events if query in e['title'].lower()
                or query in e['description'].lower()]
    return jsonify(filtered)

# ========== Reminder & Email Notification ==========


def send_email(email, subject, body):
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = "your_email_id"
        msg["To"] = email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("your_email@gmail.com", "App Password")
            smtp.send_message(msg)
    except Exception as e:
        print("Failed to send email:", e)


def handle_reminders():
    now = datetime.now()
    upcoming = now + timedelta(hours=1)
    events = load_events()
    for event in events:
        start_time = datetime.fromisoformat(event["start_time"])
        if now < start_time <= upcoming:
            print(f"🔔 Reminder: {event['title']} at {event['start_time']}")
            if event.get("email"):
                send_email(
                    event["email"],
                    f"Event Reminder: {event['title']}",
                    f"Your event '{event['title']}' is scheduled at {event['start_time']}\n\nDescription: {event['description']}"
                )

        # Handle recurring events
        if start_time < now and event.get("recurring"):
            delta = {"daily": 1, "weekly": 7, "monthly": 30}
            days = delta.get(event["recurring"], 0)
            new_start = start_time + timedelta(days=days)
            new_end = datetime.fromisoformat(
                event["end_time"]) + timedelta(days=days)

            event["start_time"] = new_start.isoformat()
            event["end_time"] = new_end.isoformat()
            print(
                f"🔁 Recurring event updated: {event['title']} ({event['recurring']})")

    save_events(events)


scheduler = BackgroundScheduler()
scheduler.add_job(handle_reminders, 'interval', minutes=1)
scheduler.start()

# ========== Run Server ==========
if __name__ == '__main__':
    app.run(debug=True)
