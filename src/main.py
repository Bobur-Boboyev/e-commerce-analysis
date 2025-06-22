from data_analyzer import most_sold
from vizulization import vizualization
from save_data import save_csv, save_excel, save_json

while True:
    print("\nMENU:")
    print("\n1 - Top 5 best-selling products")
    print("2 - Visualize top 5 products")
    print("3 - Save Top 5 to csv")
    print("0 - Exit")
    choice = input("Enter a choice: ")

    if choice == '1':
        top_5 = most_sold()
        print("\nTop 5 Best-Selling Products:\n")
        print("{:<45} {:>10}".format("Product Name", "Quantity"))
        print("-" * 58)
        
        for name, quantity in top_5:
             print("{:<45} {:>10}".format(name, quantity))

    elif choice == '2':
        vizualization()

    elif choice == '3':
        print("\n1 - to csv")
        print("2 - to excel")
        print("3 - to json")
        
        choice2 = input("\nEnter a choice: ")

        if choice2 == '1':
            save_csv()
            print("\nFile saved!")
        
        elif choice2 == '2':
            save_excel()
            print("\nFile saved!")

        elif choice2 == '3':
            save_json()
            print("\nFile saved!")
        
        else:
            print("\nWrong format choice")
    elif choice == '0':
        break
    else:
        print('\nWrong choice!')

