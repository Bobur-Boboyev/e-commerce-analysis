import csv
file = "data/data.csv"
def read_csv():
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)
