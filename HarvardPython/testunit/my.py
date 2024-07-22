def main():
    n=int(input("Input amount in naira: "))
    d=int(input("Input amount in dollar: "))
    dollar=dollar_con(n,d)
    print(f"{n} naira is equivalent to {dollar} dollars")
def dollar_con(n,d):
    return n*d
main()

