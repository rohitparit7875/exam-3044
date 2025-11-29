import re

password = input("Enter a password: ")

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!#%*?&]).{8,}$"

if re.match(pattern, password):
    print("Strong password ✔")
else:
    print("Weak password ❌ — use uppercase, lowercase, numbers & symbols")
