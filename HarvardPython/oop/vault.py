class Vault:
    def __init__(self, gold=0.0, silver=0.0, bronze=0.0):
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def __str__(self):
        return f"{self.gold} gold {self.silver} silver {self.bronze} bronze"
    
    def __add__(self, other):
        gold =self.gold + other.gold
        silver =self.silver + other.silver
        bronze = self.bronze + other.bronze
        return Vault(gold, silver, bronze)


    
azeem = Vault(100, 50, 20)
print(azeem)

dare = Vault(50, 50, 50)
print(dare)

combine = azeem + dare
print(combine)
