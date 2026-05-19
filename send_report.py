import requests

BOT_TOKEN = "8389454308:AAH7iiQ5WG9fCxYhZQsxfWd74TpcpEQOfhQ"
CHAT_ID = "1670726615"

message = "Tes kirim pesan dari GitHub Actions 🚀"

telegram_url = f"https://api.telegram.org/bot8389454308:AAH7iiQ5WG9fCxYhZQsxfWd74TpcpEQOfhQ/sendMessage"
params = {"1670726615": CHAT_ID, "text": message}
requests.post(telegram_url, params=params)
