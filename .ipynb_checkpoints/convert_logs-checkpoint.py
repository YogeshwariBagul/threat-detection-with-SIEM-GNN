import json
import pandas as pd

# Load JSON file
with open('logs.json', 'r') as f:
    data = json.load(f)

# Check if data is a list of log entries or a single dictionary with a key holding the entries
if isinstance(data, dict):
    # Try to extract logs from the first (or most likely) key
    data = next((v for v in data.values() if isinstance(v, list)), [data])

# Normalize and convert to DataFrame
df = pd.json_normalize(data)

# Save to CSV
df.to_csv('logs.csv', index=False)

print("Converted JSON logs to logs.csv")
