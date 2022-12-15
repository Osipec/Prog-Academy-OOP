"""
This class is used to keep info about customers
"""
class Customer:

    def __init__(self, surname: str, name: str, phone: str, email: str):
        self.surname = surname
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.surname} {self.name}; {self.phone}, {self.email}'
