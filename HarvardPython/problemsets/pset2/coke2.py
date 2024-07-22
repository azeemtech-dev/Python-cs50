"""def main():
    cost = 50
    amount_due = cost
    accepted_coins = [25, 10, 5]

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        
        if coin in accepted_coins:
            amount_due -= coin
        else:
            print("Invalid coin. Please insert a coin of 25, 10, or 5 cents.")

    change_owed = abs(amount_due) 

    print(f"Change Owed: {change_owed}")

if __name__ == "__main__":
    main()
"""



amount_due = 50
print(f"Amount Due: {amount_due}")

while amount_due > 0:
    coin = int(input("Insert Coin: "))

    if coin < amount_due:
        amount_due -= coin
        print(f"Amount Due: {amount_due}")
    else:
        change = coin - amount_due
        print(f"Change Owed: {change}")
        amount_due = 0  # exit the loop

















