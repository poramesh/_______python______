import random

first_names = ["John", "Jane", "Alice", "Bob", "Charlie"]
last_names = ["Doe", "Smith", "Johnson", "Brown", "Williams"]

def generate_name():
    first = random.choice(first_names)
    last = random.choice(last_names)
    print(first)
    return f"{first} {last}"


