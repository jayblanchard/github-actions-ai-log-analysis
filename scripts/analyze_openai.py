import json
import os
import sys
import urllib.request

if len(sys.argv) < 2:
    print("Usage: python analyze_openai.py <logfile>")
    sys.exit(1)

log_file = sys.argv[1]

with open(log_file, "r") as f:
    log_text = f.read()

prompt = f"""
You are analyzing a GitHub Actions workflow log.

Your job is to:
1. Identify the most likely root cause of the failure
2. Ignore unrelated noise when possible
3. Highlight only the most relevant log lines
4. Suggest 3 to 5 practical next steps

Rules:
- Be concise and direct
- Only suggest fixes supported by the log
- If a suggestion is less certain, label it as "Possible additional check"
- Prefer actionable steps over explanations

Output format:

Summary:
<one or two sentences>

Likely Cause:
<most likely cause>

Relevant Log Lines:
- <line 1>
- <line 2>

Suggested Fixes:
1. <fix 1>
2. <fix 2>
3. <fix 3>

Here is the log:

{log_text}
"""

payload = {
    "model": "gpt-4.1",
    "input": [
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": prompt
                }
            ]
        }
    ]
}

req = urllib.request.Request(
    "https://api.openai.com/v1/responses",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"
    },
    method="POST"
)

with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())

parts = []
for item in data.get("output", []):
    for content in item.get("content", []):
        if content.get("type") == "output_text":
            parts.append(content.get("text", ""))

print("\n".join(parts))
