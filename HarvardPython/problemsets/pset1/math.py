def main():
    expression = input("Enter number (eg: 1 + 1): ").strip()
    x,y,z =expression.split(" ")
    x = int(x)
    z = int(z)
    result = math(x,y,z)
    print(f"Result is equal to {result:.1f}")




def math(x,y,z):

    if y == "+":
        return x+z
    elif y == "-":
        return x-z
    elif y== "*":
        return x*z
    elif y == "/":
        return x/z
    elif y == "%":
        return x%z
    
    
if __name__ == "__main__":
    main()
