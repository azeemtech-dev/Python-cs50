import re
email = input("what's your email? ").strip()

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(edu|ng|gov|com)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


