import random

class Hat:

    houses = ["obalende", "oshodi", "onipan", "lekki"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")