import requests
import os
import time
from datetime import datetime, timedelta

def load_token(file_path='bot_token.txt'):
    if not os.path.exists(file_path):
        print("❌ bot_token.txt not found.")
        return None
    with open(file_path, 'r') as f:
        token = f.read().strip()
        if not token:
            print("❌ bot_token.txt is empty.")
            return None
        return f"Bot {token}" if not token.startswith("Bot ") else token

def format_time(seconds):
    return str(timedelta(seconds=round(seconds)))

def check_rate_limit():
    token = load_token()
    if not token:
        return

    url = 'https://discord.com/api/v10/users/@me'
    headers = {'Authorization': token}

    print(f"📡 Sending request to {url}...\n")
    response = requests.get(url, headers=headers)

    print(f"Status Code: {response.status_code}")
    print("Relevant Headers:")
    relevant = {}
    for key, value in response.headers.items():
        if key.lower().startswith("x-ratelimit") or key.lower() == "retry-after":
            print(f"{key}: {value}")
            relevant[key.lower()] = value

    print("\n🔍 Interpretation:")
    remaining = int(relevant.get('x-ratelimit-remaining', 1))
    reset_after = float(relevant.get('x-ratelimit-reset-after', 0))
    retry_after = float(relevant.get('retry-after', 0))
    reset_epoch = float(relevant.get('x-ratelimit-reset', time.time()))

    if response.status_code == 429 or remaining == 0:
        wait_time = retry_after if retry_after else reset_after
        reset_time = datetime.fromtimestamp(reset_epoch)
        now = datetime.utcnow()
        delta = reset_time - now
        print(f"⚠️ You are currently **exceeding** the rate limit.")
        print(f"⏳ Reset after: {format_time(delta.total_seconds())} (at {reset_time} UTC)")
    else:
        print(f"✅ You are **not** currently rate-limited.")
        print(f"🧮 Remaining requests: {remaining}")
        print(f"🔄 Resets in: {format_time(reset_after)} (at {datetime.fromtimestamp(reset_epoch)} UTC)")

if __name__ == "__main__":
    check_rate_limit()