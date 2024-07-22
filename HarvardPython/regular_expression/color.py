import re

def main():
    color = input("hexadecimal color code: ")
    pattern = r"^#[a-fA_F0-9]{6}$"
    if match := re.search(pattern, color):
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid")

main()