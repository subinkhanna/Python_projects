import re

# re.search(pattern, string, flags=0)

email = input("Enter your email address: ").strip()

#if re.search(r"^[^@]+@[^@]+\.edu$", email):
if re.search(r"^[a-zA-Z0-9_][^ @]+@[a-zA-Z0-9_][^ @]+\.edu$", email):
# re.search(r"^\w+@(\w+\.)?\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")