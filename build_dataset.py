import pandas as pd
from datetime import datetime
import re

LOG_TIME_FORMAT = "%d/%b/%Y:%H:%M:%S"
WINDOW_SIZE = 10  # seconds

def parse_log(file, label):
    windows = {}

    with open(file) as f:
        for line in f:
            match = re.search(r"\[(.*?)\]", line)
            if not match:
                continue

            time_str = match.group(1).split()[0]
            timestamp = datetime.strptime(time_str, LOG_TIME_FORMAT)

            window_id = int(timestamp.timestamp()) // WINDOW_SIZE

            windows.setdefault(window_id, 0)
            windows[window_id] += 1

    rows = []
    for count in windows.values():
        rows.append({
            "requests": count,
            "label": label
        })

    return rows


human_rows = parse_log("human.log", 0)
bot_rows   = parse_log("bot.log", 1)

df = pd.DataFrame(human_rows + bot_rows)
df.to_csv("dataset.csv", index=False)

print(f"Dataset built with {len(df)} rows")
