
from .generators.name import generate_name
from .generators.address import generate_address
from .generators.date import generate_date
from .generators.email import generate_email

class dummy_data_generator:
    def __init__(self):
        self.name_generator = generate_name
        self.address_generator = generate_address
        self.date_generator = generate_date
        self.email_generator = generate_email
    
    def name(self):
        return self.name_generator()

    def address(self):
        return self.address_generator()

    def date(self):
        return self.date_generator()

    def email(self):
        return self.email_generator()
