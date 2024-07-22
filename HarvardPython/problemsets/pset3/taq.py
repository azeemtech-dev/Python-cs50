def main():


    print("Welcome to our online shop! please place your order")
    while True:
        try:
            text = input("Item: ").title().strip()
            price = get_taq(text)
            if price is not None:
                print(f"price: ${price:.2f}")
        except EOFError:
            print("Thanks for your patronage!!!")
            break # press ctrl-d or (ctrl-z for windows) to break out of the loop




menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}



def get_taq(text):
    if text in menu:
        return menu[text]
    else:
        print(f"{text} is not in menu.")
        return None
    





if __name__=="__main__":
    main()


