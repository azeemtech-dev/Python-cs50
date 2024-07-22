name = input("Input currency name: ").upper()
match name:
    case "DOLLAR":
        print(f" 1 {name} is equivalent to 1400 naira")
    case "GBP":
        print(f" 1 {name} is equivalent to 2000 naira")
    case "EURO":
        print(f" 1 {name} is equivalent to 1700 naira")
    case _:
        print("which currency?")

