Alright Chandu, here’s a **complete end-to-end working setup**—clean, practical, and exactly matching your requirement (GCP VM + Cloud SQL + UI + Flask).

---

# 🧱 1. ARCHITECTURE (VERY CLEAR)

```
Browser
  ↓
http://35.185.57.29:8080  → Frontend (HTML + JS)
  ↓
http://35.185.57.29:80    → Backend (Flask API)
  ↓
Cloud SQL (PostgreSQL via Proxy)
```

---

# 📁 2. PROJECT STRUCTURE (ON VM)

```
venkat-app/
 ├── frontend/
 │    ├── index.html
 │    ├── app.js
 │    └── style.css
 └── backend/
      ├── app.py
      ├── db.py
      └── requirements.txt
```

---

# 🎨 3. FRONTEND CODE

## ✅ `frontend/index.html`

```html
<!DOCTYPE html>
<html>
<head>
  <title>Venkat App</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="container">
  <div class="left-panel">
    <h2>Venkat App</h2>
    <input type="text" id="name" placeholder="Enter Name">
    <input type="text" id="city" placeholder="Enter City">
    <button onclick="saveData()">Save</button>
  </div>

  <div class="right-panel">
    <h2>Saved Data</h2>
    <ul id="result"></ul>
  </div>
</div>

<script src="app.js"></script>
</body>
</html>
```

---

## ✅ `frontend/style.css`

```css
.container {
  display: flex;
  font-family: Arial;
}
.left-panel {
  width: 30%;
  padding: 20px;
  background: #f2f2f2;
}
.right-panel {
  width: 70%;
  padding: 20px;
}
input {
  display: block;
  margin: 10px 0;
  padding: 8px;
}
button {
  padding: 10px;
}
```

---

## ✅ `frontend/app.js`

```javascript
const API_URL = "http://35.185.57.29:80"; // your VM public IP

function saveData() {
  const name = document.getElementById("name").value;
  const city = document.getElementById("city").value;

  fetch(`${API_URL}/add`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ name, city })
  }).then(() => loadData());
}

function loadData() {
  fetch(`${API_URL}/get`)
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("result");
      list.innerHTML = "";
      data.forEach(row => {
        const li = document.createElement("li");
        li.innerText = `${row.name} - ${row.city}`;
        list.appendChild(li);
      });
    });
}

window.onload = loadData;
```

---

# ⚙️ 4. BACKEND CODE

## ✅ `backend/requirements.txt`

```
flask
psycopg2-binary
flask-cors
```

---

## ✅ `backend/db.py`

```python
import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",   # Cloud SQL Proxy
    database="vapp_db",
    user="vapp_user",
    password="Venkat@369",
    port=5432
)
```

---

## ✅ `backend/app.py`

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
from db import conn

app = Flask(__name__)
CORS(app)

@app.route('/add', methods=['POST'])
def add_data():
    data = request.get_json()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO team_tble(name, city) VALUES (%s, %s)",
        (data['name'], data['city'])
    )
    conn.commit()
    cur.close()
    return jsonify({"msg": "Inserted"})

@app.route('/get', methods=['GET'])
def get_data():
    cur = conn.cursor()
    cur.execute("SELECT name, city FROM team_tble")
    rows = cur.fetchall()
    cur.close()

    return jsonify([
        {"name": r[0], "city": r[1]} for r in rows
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
```

---

# ☁️ 5. COMPLETE SETUP STEPS (ON VM)

## 🔹 Step 1: SSH into VM

```bash
ssh <your-user>@35.185.57.29
```

---

## 🔹 Step 2: Install packages

```bash
sudo apt update
sudo apt install python3-pip -y
```

---

## 🔹 Step 3: Create folders

```bash
mkdir -p venkat-app/frontend
mkdir -p venkat-app/backend
cd venkat-app
```

---

## 🔹 Step 4: Paste code into files

Use:

```bash
nano frontend/index.html
nano frontend/app.js
nano frontend/style.css

nano backend/app.py
nano backend/db.py
nano backend/requirements.txt
```

---

## 🔹 Step 5: Open firewall ports

```bash
gcloud compute firewall-rules create allow-http \
  --allow tcp:80,tcp:8080
```

---

## 🔹 Step 6: Setup Cloud SQL Proxy (IMPORTANT)

```bash
cd backend

wget https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.6.0/cloud-sql-proxy.linux.amd64 -O cloud-sql-proxy

chmod +x cloud-sql-proxy

./cloud-sql-proxy ams-kap:us-central1:venkat-psql &
```

---

## 🔹 Step 7: Run backend

```bash
pip3 install -r requirements.txt
sudo python3 app.py
```

---

## 🔹 Step 8: Run frontend

Open another terminal:

```bash
cd venkat-app/frontend
python3 -m http.server 8080
```

---

# 🌐 6. FINAL ACCESS

👉 Open in browser:

```
http://35.185.57.29:8080
```

---

# ✅ WHAT WILL HAPPEN

* Enter **Name + City**
* Click **Save**
* Data → stored in **Cloud SQL (team_tble)**
* Data → displayed instantly on UI

---

# ⚠️ TROUBLESHOOT QUICKLY

If not working:

* Backend running? → `sudo python3 app.py`
* Proxy running? → must be active
* Table exists? → `team_tble`
* Port open? → 80 & 8080
* API URL correct? → public IP only

---

If you want, next I can upgrade this into a **real DevOps project**:

* NGINX (single URL, no 8080)
* Load balancer + 2 backend VMs
* Primary + replica DB
* CI/CD pipeline

That will make this **interview-level strong project**, not just a demo.
