import joblib
import re
import pandas as pd
import sys
import time
from datetime import datetime

# ===============================
# Load model
# ===============================
model = joblib.load("bot_model.pkl")

# ===============================
# Config
# ===============================
LOG_TIME_FORMAT = "%d/%b/%Y:%H:%M:%S"
WINDOW_SIZE = 1          # seconds
RATE_THRESHOLD = 20      # immediate bot cutoff

# ===============================
# State
# ===============================
current_window = None
request_count = 0

def extract_timestamp(line):
    match = re.search(r"\[(.*?)\]", line)
    if not match:
        return None
    time_str = match.group(1).split()[0]
    return datetime.strptime(time_str, LOG_TIME_FORMAT)

print("[*] Real-time bot detector started...", flush=True)

for line in sys.stdin:
    ts = extract_timestamp(line)
    if not ts:
        continue

    epoch = int(ts.timestamp())

    if current_window is None:
        current_window = epoch

    # New window → reset
    if epoch != current_window:
        current_window = epoch
        request_count = 0

    request_count += 1

    # 🔥 IMMEDIATE DETECTION (NO WAITING)
    if request_count >= RATE_THRESHOLD:
        print(f"🚨 BOT DETECTED — {request_count} requests in {WINDOW_SIZE}s", flush=True)

