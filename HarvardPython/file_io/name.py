'''name = input("What's your name? ")

with open("name.txt", "a") as file:
    file.write(f"{name}\n")
'''
name = []

with open ("name.txt") as file:
    for line in file:
        name.append(line.rstrip())

for nam in sorted(name, reverse=True):
    print(f"hello, {nam}")