def main():
    x = get_int("input value for x ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
             x=int(input(prompt))
        except ValueError:
            """ print("x is not an integer")"""
            pass
        else:
            return x

main()