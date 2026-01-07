import pandas as pd
import numpy as np

ROWS = 1_000_000  # ~200MB CSV

data = {
    "transaction_id": [f"TXN{i}" for i in range(ROWS)],
    "merchant_id": np.random.choice(
        ["M001", "M002", "M003", None], ROWS, p=[0.3, 0.3, 0.3, 0.1]
    ),
    "customer_id": [f"CUST{i%50000}" for i in range(ROWS)],
    "amount": np.random.choice(
        [100, 250, 500, 1000, None], ROWS, p=[0.25, 0.25, 0.25, 0.15, 0.10]
    ),
    "currency": np.random.choice(["INR", "USD"], ROWS),
    "transaction_date": pd.date_range(
        start="2024-01-01", periods=ROWS, freq="min"
    ).astype(str),
    "status": np.random.choice(
        ["SUCCESS", "FAILED", "PENDING"], ROWS, p=[0.85, 0.10, 0.05]
    ),
    "country": np.random.choice(
        ["IN", "US", "SG"], ROWS, p=[0.7, 0.2, 0.1]
    ),
}

df = pd.DataFrame(data)

df.to_csv("payments_200mb.csv", index=False)
print("✅ 200MB dataset generated")
