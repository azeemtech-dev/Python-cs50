'''import csv
students = []

with open("student.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home":row["home"]})

for student in sorted(students, key = lambda student:student["name"]):
    print(f"{student['name']} is from {student['home']}")
'''

import csv

name = input("what's your name? ")
home = input("where is your home? ")

with open("student.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name": name, "home": home})
