const api = "http://localhost:5000/events";
let isEditing = false;
let editEventId = null;

document.getElementById("eventForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const event = {
    title: document.getElementById("title").value,
    description: document.getElementById("description").value,
    start_time: document.getElementById("start_time").value,
    end_time: document.getElementById("end_time").value,
    recurring: document.getElementById("recurring").value,
    email: document.getElementById("email").value
  };

  if (isEditing) {
    // UPDATE
    await fetch(`${api}/${editEventId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(event)
    });
    isEditing = false;
    editEventId = null;
    document.querySelector("#eventForm button").textContent = "Add Event";
  } else {
    // CREATE
    await fetch(api, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(event)
    });
  }

  e.target.reset();
  loadEvents();
});

async function loadEvents() {
  const res = await fetch(api);
  const events = await res.json();
  displayEvents(events);
  showReminders(events);
}


function displayEvents(events) {
  const list = document.getElementById("eventList");
  list.innerHTML = "";
  events.forEach(e => {
    const div = document.createElement("div");
    div.className = "event";
    div.innerHTML = `
      <strong>${e.title}</strong> (${e.start_time} to ${e.end_time})<br>
      ${e.description}<br>
      Recurring: ${e.recurring || 'No'}<br>
      Email: ${e.email || 'None'}<br>
      <button onclick="editEvent('${e.id}')">✏️ Edit</button>
      <button onclick="deleteEvent('${e.id}')">🗑️ Delete</button>
    `;
    list.appendChild(div);
  });
}

async function deleteEvent(id) {
  await fetch(`${api}/${id}`, { method: "DELETE" });
  loadEvents();
}

async function editEvent(id) {
  const res = await fetch(`${api}`);
  const events = await res.json();
  const e = events.find(ev => ev.id === id);
  if (!e) return alert("Event not found");

  document.getElementById("title").value = e.title;
  document.getElementById("description").value = e.description;
  document.getElementById("start_time").value = e.start_time;
  document.getElementById("end_time").value = e.end_time;
  document.getElementById("recurring").value = e.recurring || "";
  document.getElementById("email").value = e.email || "";

  isEditing = true;
  editEventId = id;
  document.querySelector("#eventForm button").textContent = "Update Event";
}

function showReminders(events) {
  const now = new Date();
  const soon = new Date(now.getTime() + 60 * 60 * 1000);
  const due = events.filter(e => {
    const start = new Date(e.start_time);
    return start > now && start <= soon;
  });

  const reminderBox = document.getElementById("reminders");
  reminderBox.innerHTML = due.length
    ? `🔔 Upcoming in next 1 hour: ${due.map(e => e.title).join(", ")}`
    : "";
}

document.getElementById("searchBox").addEventListener("input", async (e) => {
  const query = e.target.value;
  const res = await fetch(`http://localhost:5000/events/search?q=${query}`);
  const results = await res.json();
  displayEvents(results);
});

setInterval(loadEvents, 60000);
loadEvents();
