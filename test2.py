import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

tickers = ["ESIP.JK", "SICO.JK", "LCKM.JK", "ZATA.JK", "KOTA.JK"]
results = []

for ticker in tickers:
    data = yf.download(ticker, period="6mo", interval="1d")
    data["MA5"] = data["Close"].rolling(5).mean()
    data["MA20"] = data["Close"].rolling(20).mean()
    data["Target"] = data["Close"].shift(-1)
    train = data.iloc[:-1].dropna()

    X = train[["Close", "Volume", "MA5", "MA20"]]
    y = train["Target"]

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    last_row = data.iloc[-1][["Close", "Volume", "MA5", "MA20"]].values.reshape(1, -1)
    predicted_price = model.predict(last_row)[0]

    results.append({
        "Ticker": ticker,
        "Last_Close": data.iloc[-1]["Close"],
        "Predicted_Next": predicted_price,
        "Diff_%": (predicted_price - data.iloc[-1]["Close"]) / data.iloc[-1]["Close"] * 100
    })

df_results = pd.DataFrame(results)
print(df_results)


