import yfinance as yf
import requests

tickers = ["BKSL.JK", "BNBR.JK", "BULL.JK", "BUMI.JK", "COAL.JK", "CPRO.JK", "DEWA.JK", "DMAS.JK",	"ELTY.JK", "ESIP.JK", "IATA.JK", "INET.JK", "IRSX.JK", "KIJA.JK", "KOTA.JK", "KRYA.JK",	"MBMA.JK", "MINA.JK", "PSAB.JK", "WMUU.JK", "ZATA.JK"]

data = []
for t in tickers:
    stock = yf.Ticker(t)
    hist = stock.history(period="2d")  # ambil 2 hari terakhir
    info = stock.info                  # ambil info valuasi & fundamental

    if len(hist) >= 2:
        change = (hist['Close'].iloc[-1] - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2] * 100
        volume = hist['Volume'].iloc[-1]   # volume perdagangan hari terakhir
        market_cap = info.get("marketCap", "N/A")   # valuasi market cap
        pe_ratio = info.get("trailingPE", "N/A")    # PE ratio
        eps = info.get("trailingEps", "N/A")        # EPS (Earnings Per Share)

        data.append((t, change, volume, market_cap, pe_ratio, eps))

# Urutkan dari terbesar ke terkecil
sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

# Format pesan
message_lines = []
for t, change, volume, market_cap, pe_ratio, eps in sorted_data:
    kategori = "📈 Gainer" if change > 0 else "📉 Loser"
    message_lines.append(
        f"{kategori}: {t} ({change:.2f}%) | Vol: {volume:,} | MC: {market_cap:,} | PE: {pe_ratio} | EPS: {eps}"
    )

message = "\n".join(message_lines)

# Kirim ke Telegram
telegram_url = "https://api.telegram.org/bot8389454308:AAH7iiQ5WG9fCxYhZQsxfWd74TpcpEQOfhQ/sendMessage"
params = {"chat_id": "1670726615", "text": message}
requests.post(telegram_url, params=params)
