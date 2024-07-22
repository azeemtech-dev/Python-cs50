deep = input("What is the Answer to the Great Question of life, the Universe, and Everything? ")
match deep:
    case "42":
        print("Yes")
    case "Forty_Two":
        print("Yes")
    case "forty two":
        print("Yes")
    case _:
        print("No")