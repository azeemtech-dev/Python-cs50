'''for _ in range(3):
    print("#")'''

def main():
    h = int(input("enter height: "))
    print_column(h)


def print_column (height):
   ''' for _ in range(height):
        print("#")'''
   print("#\n" *height, end="")


main()

#<<<<<<<<<<<>>>>>>>>>>>>

def main():
    w = int(input("How many row do you want? "))
    print_row(w)

def print_row(width):
    print("?" *width)



main()

