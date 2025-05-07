import random

street_names = ["Main St", "Elm St", "Maple Ave", "Oak Rd"]
cities = ["New York", "Los Angeles", "Chicago", "Houston"]
states = ["NY", "CA", "IL", "TX"]
zip_codes = ["10001", "90001", "60601", "77001"]

def generate_address():
    street = random.randint(100, 9999)
    street_name = random.choice(street_names)
    city = random.choice(cities)
    state = random.choice(states)
    zip_code = random.choice(zip_codes)
    return f"{street} {street_name}, {city}, {state} {zip_code}"
