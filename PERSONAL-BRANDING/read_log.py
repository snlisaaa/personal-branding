import json

log_file = r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\.system_generated\logs\transcript.jsonl"

with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('type') == 'USER_INPUT':
                content = data.get('content', '')
                # Find image paths/filenames in the content
                print(f"Step {data.get('step_index')}: {content[:100]}")
                # Print any mentioned media files
                for key, val in data.items():
                    if 'media' in str(val) or 'media' in str(key):
                        print(f"  {key}: {str(val)[:200]}")
        except Exception as e:
            pass
