from data_read import read_csv
data = read_csv()

def most_sold():
    products = {}
    for row in data:
        description = row["Description"]
        quantity = int(row['Quantity'])

        if description in products.keys():
            products[description] += quantity
        else:
            products[description] = quantity
    sorted_products = sorted(products.items(), key=lambda x: x[1], reverse=True)
    return sorted_products[:5]