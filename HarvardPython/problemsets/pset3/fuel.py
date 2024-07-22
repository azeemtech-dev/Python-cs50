def main():
    fraction = input("Fraction (x/y): ")
    print(get_fraction(fraction))




def get_fraction(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if y == 0:
                raise ZeroDivisionError
            elif x > y:
                raise ValueError

            percentage = round((x / y) * 100)
            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return f"{percentage}%"

        except (ValueError, ZeroDivisionError):
            fraction = input("Fraction(x/y): ")

if __name__ == "__main__":
    main()
