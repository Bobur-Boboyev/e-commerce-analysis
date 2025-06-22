import matplotlib.pyplot as plt
from data_analyzer import most_sold

data = most_sold()
def vizualization():
    x = [x[0] for x in data]
    y = [y[1] for y in data]

    plt.figure(figsize=(12, 6))
    plt.bar(x, y, color="blue")
    plt.title("Top 5 porducts")
    plt.xlabel("Products")
    plt.ylabel("Number sold")
    plt.xticks(size=7)
    plt.yticks(size=8)
    plt.show()