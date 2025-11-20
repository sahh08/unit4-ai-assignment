# BEFORE (repetitive code)
print("Welcome Sahana")
print("Welcome Nisha")
print("Welcome Priya")
print("Welcome Ankita")
print("Welcome Diya")
# Refactor this code
def greet(name):
    print(f"Welcome {name}")
names = ["Sahana", "Nisha", "Priya", "Ankita", "Diya"]
for name in names:
    greet(name)
# AFTER (refactored code)