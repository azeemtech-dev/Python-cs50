amount_due = 50
print(f"Amount Due: {amount_due} ")

while amount_due > 0:
    coin = int(input("Insert Coin: "))

    if coin < amount_due:
        amount_due -= coin
        print(f"Amount Due: {amount_due}")
    else:
        print("Change own: 0")