stock = []

while True:
    print("1. Add Jersey 2. View Stock 3. Remove Jersey 4. Quit")   # Menu for the user
    choice = input("Choose: ")
    
    if choice == "1":
        team = input("Enter team: ")
        season = input("Enter season: ")
        size = input("Enter size: ")
        cost = float(input("Enter cost: "))
        price = float(input("Enter price: "))
        jersey = {"team": team, "season": season, "size": size, "cost": cost, "price": price}   # Uses a dictionary to store each jersey with its data into the stock list
        stock.append(jersey)
        
    elif choice == "2":
        if stock == []:
            print("Stock is empty")  # If stock is empty
        
        else:
            for j in stock:
                print(f"{j['team']} | {j['season']} | {j['size']} | {j['cost']:.2f}  | {j['price']:.2f} | Profit: {j['price'] - j['cost']:.2f}") # Uses f string to print out the stock to user, using 2 decimal points for price and cost, and calculates profit

    
    elif choice == "3":
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
                    print(f"Removed {removed['team']} ")
                else:
                    print("Invalid number.")
                
    
    elif choice == "4":
        break  # To quit the programme
        
    else:
        print("Invalid choice")  # Catches invalid inputs
        
        