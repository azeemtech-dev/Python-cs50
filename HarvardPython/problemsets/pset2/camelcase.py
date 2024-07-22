variable = input("Camel case: ")

snake_case = ""

for char in variable:
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char
    '''if camel_case.startswith("_"):
        camel_case = camel_case[1:]'''
    snake_case = snake_case.lstrip("_")

print(f"Snake case: {snake_case}")

