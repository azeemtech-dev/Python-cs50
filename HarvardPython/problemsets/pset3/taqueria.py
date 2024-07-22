def main():
    text = input("Item: ").title().strip()
    print(f"Price: ${get_order(text)}")


taqueria = {
    "Beja Taco": 4.25,
    "Burrito": 7.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Quesadilla": 9.50,
    "Super Burrito": 8.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def get_order(text):
    if text in taqueria:
        order = taqueria[text]
        return order
    else:
        return


main()
