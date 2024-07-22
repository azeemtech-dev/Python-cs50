def main():
    fruit = input("Item: ").strip().lower()
    print(f"Calories: {get_fruit_calories(fruit)}")


fruit_calories = {
    "apple": 95,
    "avocado": 234,
    "banana": 105,
    "cantaloupe": 53,
    "grapefruit": 52,
    "grapes": 62,
    "honeydue melon": 61,
    "kiwifruit": 42,
    "lemon": 17,
    "lime": 20,
    "nectarine": 62,
    "orange": 62,
    "peach": 59,
    "pear": 100,
    "pineapple": 50,
    "plums": 30,
    "strawbwrries": 4,
    "sweet cherries": 87,
    "tangerine": 47,
    "watermelon": 86,
}


def get_fruit_calories(fruit):
    if fruit in fruit_calories:
        kalory = fruit_calories[fruit]
        return kalory
    else:
        return


if __name__ == "__main__":
    main()
