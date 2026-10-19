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
            print(f"{j['team']} | {j['season']} | {j['size']} | {j['cost']:.2f}  | {j['listed_price']:.2f}") # Uses f string to print out the stock to user, using 2 decimal points for price and cost
    
def remove_jersey():
    if stock == []:
        print("Cannot proceed as stock is empty.")
        
    else:
        for num, j in enumerate(stock, start=1):
            print(num, j['team'], j['season'], j['size'])
            
        try:
            num = int(input("Enter list number: "))
        except ValueError:
            print("Please enter a number.")
            
        else:
            if 1<= num <= len(stock):
                removed = stock.pop(num - 1)
                save_stock()
                print(f"Removed {removed['team']} ")
            else:
                print("Invalid number.")
    

stock = load_stock()

while True:
    print("1. Add Jersey 2. View Stock 3. Remove Jersey 4. Quit")   # Menu for the user
    choice = input("Choose: ")
    
    if choice == "1":
        add_jersey()
    elif choice == "2":
        view_stock()
    elif choice == "3":
        remove_jersey()
    elif choice == "4":
        break  # To quit the programme
    else:
        print("Invalid choice")  # Catches invalid inputs
        
        