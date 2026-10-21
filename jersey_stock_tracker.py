import json

def save_stock():
    with open("stock.json", "w") as f:
        json.dump(stock, f)

def load_stock():
    try:
        with open("stock.json", "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return []
    
def add_jersey():
    team = input("Enter team: ")
    season = input("Enter season: ")
    size = input("Enter size: ")
    cost = float(input("Enter purchase cost: "))
    listed_price = float(input("Enter listed price: "))
    jersey = {"team": team, "season": season, "size": size, "cost": cost, "listed_price": listed_price, "sold_price": None}   # Uses a dictionary to store each jersey with its data into the stock list
    stock.append(jersey)
    save_stock()

def view_stock():
    if stock == []:
        print("Stock is empty")  # If stock is empty
        
    else:
        for j in stock:
            if j['sold_price'] is None:
                print(f"{j['team']} | {j['season']} | {j['size']} | Cost: {j['cost']:.2f}   | Listed:  {j['listed_price']:.2f} | UNSOLD")  # Uses f string to print out the stock to user, using 2 decimal points for price and cost, listed price, and unsold/sold status
            else:
                print(f"{j['team']} | {j['season']} | {j['size']} | Cost: {j['cost']:.2f}   | Sold:  {j['sold_price']:.2f} | Profit: {j['sold_price'] - j['cost']:.2f}")
    
def remove_jersey():
    if stock == []:
        print("Cannot proceed as stock is empty. ")
        
    else:
        for num, j in enumerate(stock, start=1):
            print(num, j['team'], j['season'], j['size'])
            
        try:
            num = int(input("Enter list number: "))
        except ValueError:
            print("Please enter a number. ")
            
        else:
            if 1<= num <= len(stock):
                removed = stock.pop(num - 1)
                save_stock()
                print(f"Removed {removed['team']} ")
            else:
                print("Invalid number.")

def mark_sold():
    if stock == []:
        print("Cannot proceed as stock is empty. ")
    else:
        for num, j in enumerate(stock, start=1):
            if j['sold_price'] is None:
                status = "UNSOLD"
            else:
                status = "SOLD"
            print(f"{num} | {j['team']} | {j['season']} | {j['size']} | {status}")
            
        try:
            num = int(input("Enter list number. "))
        except ValueError:
            print("Please enter a number")
            
        else:
            if 1<= num <= len(stock):
                marked = stock[num-1]
                if marked['sold_price'] is not None:
                    print("Already sold")
                else:
                    
                    try:
                        sold = float(input("Enter sold price: "))
                    except ValueError:
                        print("Please enter a valid price.")
                    else:
                        marked['sold_price'] = sold
                        save_stock()
                        print(f"Marked {marked['team']} {marked['season']} as sold for €{sold:.2f} ")
                    
            else:
                print("Invalid number.")
            
def summary():
    sold_count = 0
    unsold_count = 0
    total_profit = 0
    tied_up = 0
    if stock == []:
        print("Cannot proceed as stock is empty.")
    else:
        for j in stock:
            if j['sold_price'] is not None:
                sold_count += 1
                total_profit += j['sold_price'] - j['cost']
            else:
                unsold_count += 1
                tied_up += j['cost']
           
        print(f"Sold: {sold_count} | Total Profit: €{total_profit:.2f}")
        print(f"Unsold: {unsold_count} | Money tied up: €{tied_up:.2f}")        
            
stock = load_stock()

while True:
    print("1. Add Jersey 2. View Stock 3. Remove Jersey 4. Mark as Sold 5. Summary 6. Quit")   # Menu for the user
    choice = input("Choose: ")
    
    if choice == "1":
        add_jersey()
    elif choice == "2":
        view_stock()
    elif choice == "3":
        remove_jersey()
    elif choice == "4":
        mark_sold()
    elif choice == "5":
        summary()
    elif choice == "6":
        break  # To quit the programme
    else:
        print("Invalid choice")  # Catches invalid inputs
        
        