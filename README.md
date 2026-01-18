# 🚨 Real-Time Bot Detection System

## 📖 Project Overview
This project implements a **real-time bot detection system** on Linux that monitors **Apache web server access logs** and identifies automated (bot-like) traffic based on **behavioral request-rate analysis**.

The system is designed to reflect how **basic Web Application Firewalls (WAFs)** and **intrusion detection systems (IDS)** detect abnormal traffic patterns in production environments.

---

## 🎯 Objectives
- Detect automated bot traffic in real time  
- Analyze live web server logs using sliding time windows  
- Identify abnormal request bursts indicative of automation  
- Demonstrate practical cybersecurity and traffic analysis skills  

---

## ✨ Key Features
- Real-time Apache access log monitoring  
- Sliding window traffic analysis (1-second windows)  
- Immediate detection of high-rate automated traffic  
- Hybrid design: rule-based detection with ML pipeline support  
- Linux-native streaming using `tail -F`  

---

## 🛠️ Technology Stack
- **Operating System**: Linux  
- **Web Server**: Apache HTTP Server  
- **Programming Language**: Python 3  
- **Machine Learning**: scikit-learn (Random Forest)  
- **Traffic Generation / Testing**: ApacheBench (`ab`)  

---

## 🧱 System Architecture

Incoming HTTP Requests
↓
Apache Web Server
↓
access.log (real-time)
↓
tail -F (log stream)
↓
Python Detection Engine
↓
🚨 Bot Detection Alert

yaml
Copy code

---

## 📊 Dataset & Training (Offline Phase)
To support machine learning experimentation, a labeled dataset was generated:

- **Human traffic** simulated using Python scripts with realistic delays  
- **Bot traffic** generated using ApacheBench to create high-rate bursts  
- **Primary feature**: number of requests per time window  
- **Labels**:
  - `0` → Human traffic  
  - `1` → Bot traffic  

A Random Forest classifier was trained to distinguish between normal and automated behavior based on traffic patterns.

---

## ⚡ Real-Time Detection (Online Phase)

### ▶ Start the detector
```bash
sudo tail -F /var/log/apache2/access.log | python3 -u realtime_detector.py
▶ Simulate bot traffic
bash
Copy code
ab -n 200 -c 20 http://localhost/
▶ Example Output
Copy code
🚨 BOT DETECTED — high request rate
Alerts are triggered immediately when request rates exceed defined thresholds, demonstrating real-time detection capability.

📁 Project Structure
graphql
Copy code
autobot/
├── human_traffic.py        # Simulated human traffic generator
├── bot.py                  # Bot traffic generator
├── human.log               # Human traffic logs
├── bot.log                 # Bot traffic logs
├── dataset.csv             # Labeled dataset
├── build_dataset.py        # Dataset generation script
├── train_model.py          # ML training script
├── bot_model.pkl           # Trained ML model
├── realtime_detector.py    # Real-time detection engine
└── README.md               # Project documentation
🔒 Security & Design Considerations
Follows the principle of least privilege

Python detection engine runs as a non-root process

Only log reading requires elevated permissions

Designed for defensive security and monitoring use cases

⚠️ Limitations
Requires access to web server logs

Intended for self-hosted or authorized environments

Current implementation focuses on rate-based bot detection

Advanced bots may require additional behavioral features

🚀 Future Enhancements
Per-IP bot detection

Automatic blocking using firewall rules (iptables)

Support for Nginx, Flask, and Node.js logs

Dashboard integration (Grafana / ELK stack)

Deployment as a background service (daemon)

🧑‍💻 Resume Description
Developed a real-time bot detection system on Linux that monitors Apache access logs, performs sliding-window traffic analysis, and detects automated traffic using rule-based heuristics and machine learning techniques.

📜 Disclaimer
This project is intended solely for educational and defensive security purposes.
Deploy and test this system only on servers you own or have explicit permission to monitor.
