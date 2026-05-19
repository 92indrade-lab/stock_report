import yfinance as yf
import pandas as pd

# Ambil data saham (contoh BBCA)
ticker = "BBCA.JK"
data = yf.download(ticker, period="6mo", interval="1d")

# Hitung moving average
data["MA5"] = data["Close"].rolling(5).mean()
data["MA20"] = data["Close"].rolling(20).mean()

# Deteksi volume spike (volume > 1.5x rata-rata 20 hari)
data["VolSpike"] = data["Volume"] > 1.5 * data["Volume"].rolling(20).mean()

# Sinyal sederhana: MA5 > MA20 dan volume spike
data["Signal"] = (data["MA5"] > data["MA20"]) & data["VolSpike"]

print(data.tail(10)[["Close", "MA5", "MA20", "Volume", "VolSpike", "Signal"]])
