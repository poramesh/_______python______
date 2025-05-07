import random

domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]

def generate_email():
    username = "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=10))
    domain = random.choice(domains)
    return f"{username}@{domain}"
