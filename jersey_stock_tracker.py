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

def get_price(prompt, allow_zero):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a number.")
        else:
            if allow_zero:
                if value >= 0:
                    return value
                print("Price cannot be negative.")
            else:
                if value > 0:
                    return value
                print("Price must be greater than zero.")
            
def get_list_number():
    while True:
        try:
            num = int(input("Enter list number (0 to cancel): "))
        except ValueError:
            print("Please enter a number.")
        else:
            if num == 0:
                return None
            if 1 <= num <= len(stock):
                return num -1
            print("List number must be valid")

def add_jersey():
    team = input("Enter team: ")
    season = input("Enter season: ")
    
    sizes = ["XS", "S", "M", "L", "XL", "XXL"]    # Store valid sizes
    while True:
        size = input("Enter size:").upper()
        if size in sizes:    # Use in tool to check if the entered size is a valid size from our options
            break     # Valid, so leaves loop and carrys on
        print("Invalid size. Choose from XS, S, M, L, XL, XXL")
    
    cost = get_price("Enter purchase cost: ", True)
    listed_price = get_price("Enter listed price: ", False)
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
            
        index = get_list_number()
        if index is None:
            print("Cancelled")
        
        else:
            removed = stock.pop(index)
            save_stock()
            print(f"Removed {removed['team']} ")

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
            
        index = get_list_number()
        if index is None:
            print("Cancelled.")
            
        else:
            marked = stock[index]
            if marked['sold_price'] is not None:
                print("Already sold")
            else:
                sold = get_price("Enter sold price: ", True)
                marked['sold_price'] = sold
                save_stock()
                print(f"Marked {marked['team']} {marked['season']} as sold for €{sold:.2f} ")
            
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
        
        