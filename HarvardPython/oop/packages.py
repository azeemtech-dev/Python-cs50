class Package:
    def __init__(self, number,sender, recipent, weight):
        self.number = number
        self.sender = sender
        self.recipent = recipent
        self.weight = weight
    
    def __str__(self) -> str:
        return f"Package {self.number}: {self.sender} to {self.recipent}, {self.weight}"

    def calculate_cost(self, cost_per_kg):
        return self.weight*cost_per_kg


def main():
    packages  = [
        Package(number=1, recipent="Azeem", sender="dare", weight=145),
        Package(number=2, recipent="sule", sender="kabir", weight=15)
    ]
    for package in packages:
        print(f"{package} cost{package.calculate_cost(cost_per_kg=2)}")

main()