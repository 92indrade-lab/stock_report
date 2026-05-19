import yfinance as yf
import requests

# Daftar emiten (ticker Yahoo Finance, contoh untuk Indonesia bisa pakai .JK)
tickers = ["BBCA.JK", "TLKM.JK", "ASII.JK", "BMRI.JK", "ICBP.JK"]

data = []
for t in tickers:
    stock = yf.Ticker(t)
    hist = stock.history(period="2d")  # ambil 2 hari terakhir
    if len(hist) >= 2:
        change = (hist['Close'][-1] - hist['Close'][-2]) / hist['Close'][-2] * 100
        data.append((t, change))

# Cari top gainer & loser
top_gainer = max(data, key=lambda x: x[1])
top_loser = min(data, key=lambda x: x[1])

# Format pesan
message = (
    f"📈 Top Gainer: {top_gainer[0]} ({top_gainer[1]:.2f}%)\n"
    f"📉 Top Loser: {top_loser[0]} ({top_loser[1]:.2f}%)"
)

# Kirim ke Telegram
telegram_url = f"https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage"
params = {"chat_id": "<YOUR_CHAT_ID>", "text": message}
requests.post(telegram_url, params=params)
