Perfect—now I’ll **upgrade your full setup with Git + proper Python (venv)** so this becomes a **clean DevOps flow (Local → GitHub → VM → Run)**.

---

# 🧱 1. ARCHITECTURE (UPDATED)

```
Local → GitHub → VM
                  ↓
Browser → Frontend (8080)
         ↓
Backend (80)
         ↓
Cloud SQL (Proxy)
```

---

# 📁 2. PROJECT STRUCTURE (GITHUB + VM)

```
devops-project/
 └── gcp/
      └── venkat-app/
           ├── frontend/
           └── backend/
```

---

# 🚀 3. STEP-BY-STEP COMPLETE FLOW

---

# 💻 PART 1: LOCAL → PUSH TO GITHUB

## 🔹 Step 1: Go to root

```bash
cd C:\Users\venkat\Desktop\devops-proj
```

---

## 🔹 Step 2: Initialize git

```bash
git init
git remote add origin https://github.com/venkat-mr369/devops-project.git
```

---

## 🔹 Step 3: Add + Commit

```bash
git add .
git commit -m "Venkat App full setup"
```

---

## 🔹 Step 4: Push

```bash
git branch -M main
git push -f origin main
```

---

# ☁️ PART 2: VM SETUP + GIT CLONE

## 🔹 Step 1: SSH

```bash
ssh ams2007dj@35.185.57.29
```

---

## 🔹 Step 2: Install required packages

```bash
sudo apt update
sudo apt install git python3 python3-pip python3-venv -y
```

---

## 🔹 Step 3: Clone repo

```bash
git clone https://github.com/venkat-mr369/devops-project.git
cd devops-project/gcp/venkat-app
```

---

# ⚙️ PART 3: BACKEND SETUP (CORRECT WAY)

## 🔹 Step 1: Go to backend

```bash
cd backend
```

---

## 🔹 Step 2: Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 🔹 Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔹 Step 4: Start Cloud SQL Proxy

```bash
wget https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.6.0/cloud-sql-proxy.linux.amd64 -O cloud-sql-proxy

chmod +x cloud-sql-proxy

./cloud-sql-proxy ams-kap:us-central1:venkat-psql &
```

---

## 🔹 Step 5: Run backend

```bash
sudo venv/bin/python app.py
```

👉 Runs on:

```
http://35.185.57.29:80
```

---

# 🌐 PART 4: FRONTEND SETUP

Open new terminal:

```bash
cd ~/devops-project/gcp/venkat-app/frontend
python3 -m http.server 8080
```

---

# 🌍 FINAL ACCESS

```
http://35.185.57.29:8080
```

---

# 🔄 PART 5: NEXT TIME (VERY IMPORTANT)

## 🔹 When you update code locally:

```bash
git add .
git commit -m "update"
git push
```

---

## 🔹 On VM:

```bash
cd ~/devops-project
git pull
```

---

## 🔹 Restart backend:

```bash
cd gcp/venkat-app/backend
source venv/bin/activate
sudo venv/bin/python app.py
```

---

# ⚠️ TROUBLESHOOT (UPDATED)

### ❌ pip error

✔ Use venv (already fixed)

### ❌ git pull error

✔ Must be inside repo folder

### ❌ backend not working

✔ Check:

```
ps -ef | grep cloud-sql-proxy
```

### ❌ UI not loading

✔ Check ports:

```
80, 8080 open
```

---

# 🔥 NOW YOU HAVE REAL DEVOPS FLOW

```
Local → GitHub → VM → Run → Browser
```

---

# 🚀 NEXT LEVEL (I strongly recommend)

I can upgrade this into:

* ✅ NGINX (single URL, no 8080)
* ✅ Gunicorn (production backend)
* ✅ systemd (auto start)
* ✅ CI/CD (auto deploy on git push)

👉 That will make this a **10/10 interview project**

Just tell me: **“next level setup”** and I’ll build it for you step-by-step.
