import yfinance as yf
import requests

# Daftar emiten
tickers = ["BBCA.JK", "TLKM.JK", "ASII.JK", "BMRI.JK", "ICBP.JK"]

data = []
for t in tickers:
    stock = yf.Ticker(t)
    hist = stock.history(period="2d")  # ambil 2 hari terakhir
    if len(hist) >= 2:
        change = (hist['Close'].iloc[-1] - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2] * 100
        data.append((t, change))

# Urutkan dari terbesar ke terkecil
sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

# Format pesan semua emiten
message_lines = []
for t, change in sorted_data:
    kategori = "📈 Gainer" if change > 0 else "📉 Loser"
    message_lines.append(f"{kategori}: {t} ({change:.2f}%)")

message = "\n".join(message_lines)

# Kirim ke Telegram
telegram_url = "https://api.telegram.org/bot8389454308:AAH7iiQ5WG9fCxYhZQsxfWd74TpcpEQOfhQ/sendMessage"
params = {"chat_id": "1670726615", "text": message}
requests.post(telegram_url, params=params)
