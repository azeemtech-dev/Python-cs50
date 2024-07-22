def main():
    n = int(input("input size: "))
    print_square(n)

    
def print_square(size):
    for i in range(size):
        '''for j in range(size):
         print("#", end="") 
        print()'''
        print("#"*size)

main()              