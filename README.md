# 🔐 Real-Time Intrusion Detection & Threat Alert System

A lightweight yet powerful **Real-Time Intrusion Detection System (IDS)** built using  
**Python, Scapy, Flask, Socket.IO, and MySQL**.  
It captures live network packets, detects suspicious activity (DoS, Port Scans, Flooding), logs incidents,  
and alerts the admin through a real-time dashboard and optional Email/Telegram notifications.

---

## 🚀 Features

- ✔️ Live Packet Capture (Scapy)
- ✔️ Real-Time Threat Detection
- ✔️ High Packet Rate (DoS) Detection
- ✔️ Port Scan Detection
- ✔️ Flooding Pattern Detection
- ✔️ Alerts via Web Dashboard, Email & Telegram
- ✔️ MySQL Database Logging
- ✔️ Real-Time Dashboard using Flask + Socket.IO
- ✔️ Clean and Modular Codebase

---

## 📁 Project Structure


⚙️ Setup Guide (Windows)

Follow these steps exactly:

1️⃣ Clone or Download the Repository
git clone https://github.com/yourusername/real-time-ids.git
cd real-time-ids


Or download ZIP → Extract.

2️⃣ Create and Configure .env File

Inside project root, create a file named .env:

MYSQL_HOST=localhost
MYSQL_USER=ids_user
MYSQL_PASSWORD=StrongPassword123
MYSQL_DB=ids_system

# Alerts (optional)
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_app_password
ALERT_EMAIL_FROM=your_email@gmail.com
ALERT_EMAIL_TO=admin@example.com

TELEGRAM_TOKEN=YOUR_BOT_TOKEN
TELEGRAM_CHAT_ID=YOUR_CHAT_ID


3️⃣ MySQL Database Setup

Open MySQL Command Line / Workbench

Run:

CREATE DATABASE ids_system;

CREATE USER 'ids_user'@'localhost' IDENTIFIED BY 'StrongPassword123';

GRANT ALL PRIVILEGES ON ids_system.* TO 'ids_user'@'localhost';

FLUSH PRIVILEGES;


Initialize the table using Python:

python db.py


This creates the incidents table.

▶️ Running the Project
4️⃣ Start the Real-Time Detector

Run (as Administrator):

python detector.py


This starts:

Packet capture

Detection engine

Auto logging

Real-time alerts

5️⃣ Run the Dashboard (admin UI)


---

## 🧰 Tech Stack

| Component | Technology |
|----------|------------|
| **Programming Language** | Python 3 |
| **Packet Capture** | Scapy |
| **Backend Framework** | Flask |
| **Real-Time Communication** | Flask-SocketIO |
| **Database** | MySQL |
| **Notifications** | SMTP (email), Telegram Bot API |
| **Frontend** | HTML, CSS, JavaScript |
| **Platform** | Windows |

---

## 🖥️ Requirements

Install the following:

- Python 3.10+  
- Git  
- MySQL Server  
- Pip dependencies:

```bash
pip install -r requirements.txt

Open another terminal:

cd dashboard
python app.py


Visit:

👉 http://localhost:5000

You will see alerts in real-time.

6️⃣ Test the IDS (Optional)
from scapy.all import IP, UDP, send

for i in range(300):
    send(IP(dst="127.0.0.1")/UDP(dport=1234), verbose=False)


This generates:

HIGH_PACKET_RATE alert


Visible in:

Dashboard

MySQL database
