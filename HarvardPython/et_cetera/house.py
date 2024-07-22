students = [
    {"name": "azeem", "house":"onipan"},
    {"name":"damilare", "house":"yaba" },
    {"name":"malik", "house":"sango"},
    {"name": "ilu", "house":"ajilete"},
    {"name": "sunday", "house":"oke_ore"},
    {"name": "sulu", "house":"oke_ore"},
    {"name": "raman", "house":"oke_ore"}
    ]

houses =set()#[]
for student in students:
    houses.add(student["house"])
'''    if student ["house"] not in houses:
        houses.append(student["house"])'''
    

for house in sorted(houses):
    print(house)