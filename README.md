# Real-Time Bot Detection System

## Overview
This project is a real-time bot detection system built on Linux that monitors Apache access logs and detects automated traffic based on request-rate behavior.

The system uses sliding time windows and rate-based heuristics, similar to basic Web Application Firewalls (WAFs).

---

## Features
- Real-time Apache log monitoring
- Sliding window traffic analysis (1 second)
- Immediate bot detection on traffic bursts
- Machine learning pipeline for behavioral analysis
- Linux-native streaming using `tail -F`

---

## Tech Stack
- OS: Linux
- Web Server: Apache
- Language: Python 3
- ML Library: scikit-learn
- Traffic Generator: ApacheBench (`ab`)

---

## Architecture

HTTP Requests
↓
Apache Server
↓
access.log
↓
tail -F
↓
Python Detector
↓
BOT ALERT


---

## Dataset Creation
- Human traffic simulated using Python scripts with delays
- Bot traffic generated using ApacheBench
- Feature used: requests per time window
- Labels:
  - 0 → Human
  - 1 → Bot

---

## Real-Time Detection

### Run detector:
```bash
sudo tail -F /var/log/apache2/access.log | python3 -u realtime_detector.py

Generate bot traffic:
ab -n 200 -c 20 http://localhost/

Sample Output:
BOT DETECTED — high request rate

Project Structure:
autobot/
├── human_traffic.py
├── bot.py
├── human.log
├── bot.log
├── dataset.csv
├── build_dataset.py
├── train_model.py
├── bot_model.pkl
├── realtime_detector.py
└── README.md


Limitations:

Requires access to server logs

Designed for controlled environments

Focuses on rate-based bot detection


Resume Description:

Built a real-time bot detection system on Linux that monitors Apache access logs and detects automated traffic using sliding-window analysis and machine learning

Disclaimer

This project is for educational purposes only. Deploy only on systems you own or have permission to monitor.
