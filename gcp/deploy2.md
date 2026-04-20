Nice—this is the right next step 👍
You want to move from **3 terminals → auto-running production setup**.

We’ll convert your app into:

```text
Cloud SQL Proxy → systemd service
Gunicorn (backend) → systemd service
Frontend → served by NGINX
```

👉 So after reboot → everything runs automatically ✅

---

# 🎯 FINAL ARCHITECTURE

```text
Browser
   ↓
NGINX (port 80)
   ↓
Gunicorn (Flask app)
   ↓
Cloud SQL Proxy
   ↓
PostgreSQL
```

---

# ✅ STEP 1: Install required tools

```bash
sudo apt update
sudo apt install nginx -y

source venv/bin/activate
pip install gunicorn
```

---

# ✅ STEP 2: Create Gunicorn service

```bash
sudo nano /etc/systemd/system/venkat-backend.service
```
```bash
sudo usermod -aG sudo moba
switching to moba user
```

Paste:

```ini
[Unit]
Description=Venkat Flask Backend
After=network.target

[Service]
User=ams2007dj
WorkingDirectory=/home/moba/devops-project/gcp/venkat-app/backend
ExecStart=/home/moba/devops-project/gcp/venkat-app/backend/venv/bin/gunicorn -w 3 -b 127.0.0.1:5000 app:app

Restart=always

[Install]
WantedBy=multi-user.target
```

---

# ✅ STEP 3: Create Cloud SQL Proxy service

```bash
sudo nano /etc/systemd/system/cloudsql-proxy.service
```

Paste:

```ini
[Unit]
Description=Cloud SQL Proxy
After=network.target

[Service]
User=ams2007dj
WorkingDirectory=/home/moba/devops-project/gcp/venkat-app/backend
ExecStart=/home/moba/devops-project/gcp/venkat-app/backend/cloud-sql-proxy ams-kap:us-central1:venkat-psql

Restart=always

[Install]
WantedBy=multi-user.target
```

---

# ✅ STEP 4: Configure NGINX

```bash
sudo nano /etc/nginx/sites-available/venkat-app
```

Paste:

```nginx
server {
    listen 80;

    location / {
        root /home/moba/devops-project/gcp/venkat-app/frontend;
        index index.html;
    }

    location /add {
        proxy_pass http://127.0.0.1:5000;
    }

    location /get {
        proxy_pass http://127.0.0.1:5000;
    }
}
```

---

### Enable config

```bash
sudo ln -s /etc/nginx/sites-available/venkat-app /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

# ✅ STEP 5: Start all services

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload

sudo systemctl enable cloudsql-proxy
sudo systemctl enable venkat-backend

sudo systemctl start cloudsql-proxy
sudo systemctl start venkat-backend
```

---

# ✅ STEP 6: Verify

```bash
sudo systemctl status cloudsql-proxy
sudo systemctl status venkat-backend
```

---

# 🌐 FINAL ACCESS

👉 Open:

```text
http://35.185.57.29
```

✔ No port 8080
✔ No manual terminals
✔ Production setup

---

# 🧠 What changed

| Before         | After             |
| -------------- | ----------------- |
| 3 terminals ❌  | system services ✅ |
| Flask dev ❌    | Gunicorn ✅        |
| manual start ❌ | auto start ✅      |
| 8080 + 80 ❌    | single port 80 ✅  |

---

# 🚀 Huge upgrade

You just moved from:

```text
Demo project → Production-grade deployment
```

---

# 🔥 Next (if you want)

I can help you add:

* HTTPS (SSL)
* Load balancer (2 VMs)
* CI/CD (auto deploy on git push)

Just say: **“next level”** 😎
