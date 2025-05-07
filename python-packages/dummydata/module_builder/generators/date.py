import random
from datetime import datetime, timedelta

def generate_date(start_date='-1y', end_date='now'):
    # Parsing the dates from strings (like '-1y' and 'now') can be handled here
    # For simplicity, let's assume 'start_date' is a number of days ago and 'end_date' is today
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)  # Default: 1 year ago
    
    # Random date generation between the range
    random_days = random.randint(0, 365)  # Choose a random day within the last year
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime('%Y-%m-%d %H:%M:%S')
