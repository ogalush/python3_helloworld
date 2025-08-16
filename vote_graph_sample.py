import matplotlib.pyplot as plt
import pandas as pd
import datetime

# サンプルデータ (独自データに置き換えてください)
data = {
    "date": [
        "2024-02-20", "2024-02-21", "2024-02-22", "2024-02-23", "2024-02-24"
    ],
    "brand_A": [10, 15, 20, 25, 30],
    "brand_B": [5, 7, 14, 20, 28],
    "brand_C": [2, 8, 12, 18, 22],
}

# DataFrame に変換
df = pd.DataFrame(data)

# 日付を datetime 型に変換
df["date"] = pd.to_datetime(df["date"])

# グラフ作成
plt.figure(figsize=(10, 5))
for brand in df.columns[1:]:  # 最初の列（date）を除く
    plt.plot(df["date"], df[brand], marker="o", label=brand)

# グラフの装飾
plt.xlabel("日付")
plt.ylabel("投票数")
plt.title("銘柄ごとの投票数推移")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # X軸の日付を見やすくする
plt.tight_layout()

# 表示
plt.show()