# Discord Bot Rate Limit Check

A simple Python script to check and interpret a Discord bot’s current API rate limit status.

---

## 🔧 Requirements

- Python 3.6 or higher
- A `bot_token.txt` file in the same directory, containing your Discord **bot token** (in plaintext)

---

## 🚀 How to Use

1. Save your bot token in a file named `bot_token.txt`:
   ```
   MTAx...your_token_here...nA
   ```

2. Run the script:
   ```bash
   python check_rate_limit.py
   ```

⚠️ If you use this script with Relo's Discord Bot, simply put the script into the same directory as the bot's main.py file, which also contains a bot_token.txt file already.

---

## 🧠 What It Does

- Makes a safe request to `GET /users/@me`
- Displays Discord rate limit response headers:
  - `X-RateLimit-Remaining`
  - `X-RateLimit-Reset`
  - `Retry-After`
- Interprets the output to tell you:
  - ✅ If your bot is **not** rate-limited
  - ⚠️ If it's **currently rate-limited**
  - ⏳ How long until the limit resets (in seconds/minutes)

---

## 📘 Reference

Based on Discord’s official rate limit documentation:  
[https://discord.com/developers/docs/topics/rate-limits](https://discord.com/developers/docs/topics/rate-limits)