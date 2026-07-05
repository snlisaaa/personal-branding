import json
import re

log_file = r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\.system_generated\logs\transcript.jsonl"

with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('type') == 'USER_INPUT':
                print(f"--- Step {data.get('step_index')} ---")
                # Look for media filenames in the whole JSON line
                matches = re.findall(r'media__\d+\.(?:png|jpg)', line)
                if matches:
                    print("Found media keys in line:", set(matches))
                else:
                    print("No media keys found in this line.")
        except Exception as e:
            pass
