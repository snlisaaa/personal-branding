import json
import re

log_file = r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\.system_generated\logs\transcript.jsonl"

# Read all lines
with open(log_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Search for any line that contains both a media filename and some post metrics/words
for line in lines:
    for filename in re.findall(r'media__\d+\.(?:jpg|png)', line):
        # Print the context around the filename in the line
        idx = line.find(filename)
        start = max(0, idx - 150)
        end = min(len(line), idx + 150)
        print(f"Context for {filename}: ... {line[start:end].strip()} ...")
