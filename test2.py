import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression

# Daftar emiten IDX
tickers = ["BBCA.JK", "TLKM.JK", "BBRI.JK", "ASII.JK"]

results = []

for ticker in tickers:
    data = yf.download(ticker, period="6mo", interval="1d")
    data["Target"] = data["Close"].shift(-1)
    data = data.dropna()

    X = data[["Close", "Volume"]]
    y = data["Target"]

    model = LinearRegression()
    model.fit(X, y)

    last_row = data.iloc[-1][["Close", "Volume"]].values.reshape(1, -1)
    predicted_price = model.predict(last_row)[0]

    results.append({
        "Ticker": ticker,
        "Last_Close": data.iloc[-1]["Close"],
        "Predicted_Next": predicted_price
    })

df_results = pd.DataFrame(results)
print(df_results)

