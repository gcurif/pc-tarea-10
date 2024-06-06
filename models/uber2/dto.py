class User:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}")


class Driver:
    def __init__(self, start_location, end_location, price):
        self.start_location = start_location
        self.end_location = end_location
        self.price = price

    def display_info(self):
        print(f"Start Location: {self.start_location}, End Location: {self.end_location}, Price: {self.price}")


class Comida:
    def __init__(self, name, description, price, category):
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def display_info(self):
        print(f"Name: {self.name}, Description: {self.description}, Price: {self.price}, Category: {self.category}")


class Restaurante:
    def __init__(self, name, location, cuisine_type, rating):
        self.name = name
        self.location = location
        self.cuisine_type = cuisine_type
        self.rating = rating

    def display_info(self):
        print(f"Name: {self.name}, Location: {self.location}, Cuisine Type: {self.cuisine_type}, Rating: {self.rating}")


class MedioPago:
    def __init__(self, method, card_number, expiration_date, security_code):
        self.method = method
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.security_code = security_code

    def display_info(self):
        print(f"Method: {self.method}, Card Number: {self.card_number}, Expiration Date: {self.expiration_date}, Security Code: {self.security_code}")