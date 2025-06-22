import pandas as pd
from data_analyzer import most_sold

top_5 = most_sold()
df = pd.DataFrame(top_5, columns=["Product Name", "Quantity"])

def save_csv():
    df.to_csv("top5.csv", index=False)

def save_excel():
    df.to_excel("top5.xlsx", index=False)

def save_json():
    df.to_json("top5.json", orient='records', indent=4)

