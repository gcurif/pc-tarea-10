# Clase que representa los usuarios
# Atributos de la clase:
# -user_id: es ideal que todo objeto tenga un id para poder buscarlo en la base de datos
# -username: nombre de usuario
# -email: 


class User:
    def __init__(self, user_id, username, email, phone, password, address, payment_info):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password
        self.address = address
        self.payment_info = payment_info

    def print_info(self):
        print(f"User ID: {self.user_id}, Username: {self.username}, Email: {self.email}, Phone: {self.phone}")

class Driver(User):
    def __init__(self, user_id, username, email, phone, password, address, payment_info, license_number, vehicle):
        super().__init__(user_id, username, email, phone, password, address, payment_info)
        self.license_number = license_number
        self.vehicle = vehicle

    def print_info(self):
        super().print_info()
        print(f"License Number: {self.license_number}")
        self.vehicle.print_info()

class Vehicle:
    def __init__(self, vehicle_id, make, model, year, color, plate_number):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.plate_number = plate_number

    def print_info(self):
        print(f"Vehicle ID: {self.vehicle_id}, Make: {self.make}, Model: {self.model}, Color: {self.color}, Plate Number: {self.plate_number}")

class Trip:
    def __init__(self, trip_id, user_id, driver_id, start_time, end_time, start_location, end_location, status):
        self.trip_id = trip_id
        self.user_id = user_id
        self.driver_id = driver_id
        self.start_time = start_time
        self.end_time = end_time
        self.start_location = start_location
        self.end_location = end_location
        self.status = status

    def print_info(self):
        print(f"Trip ID: {self.trip_id}, Start Time: {self.start_time}, End Time: {self.end_time}, Start Location: {self.start_location}, End Location: {self.end_location}, Status: {self.status}")

class Payment:
    def __init__(self, payment_id, user_id, amount, payment_method, payment_status, trip_id):
        self.payment_id = payment_id
        self.user_id = user_id
        self.amount = amount
        self.payment_method = payment_method
        self.payment_status = payment_status
        self.trip_id = trip_id

    def print_info(self):
        print(f"Payment ID: {self.payment_id}, Amount: ${self.amount:.2f}, Method: {self.payment_method}, Status: {self.payment_status}")

class Rate:
    def __init__(self, rate_id, trip_id, rate_per_mile, rate_per_minute, base_fare):
        self.rate_id = rate_id
        self.trip_id = trip_id
        self.rate_per_mile = rate_per_mile
        self.rate_per_minute = rate_per_minute
        self.base_fare = base_fare

    def print_info(self):
        print(f"Rate ID: {self.rate_id}, Per Mile: ${self.rate_per_mile:.2f}, Per Minute: ${self.rate_per_minute:.2f}, Base Fare: ${self.base_fare:.2f}")

class Review:
    def __init__(self, review_id, trip_id, user_id, driver_id, rating, comment):
        self.review_id = review_id
        self.trip_id = trip_id
        self.user_id = user_id
        self.driver_id = driver_id
        self.rating = rating
        self.comment = comment

    def print_info(self):
        print(f"Review ID: {self.review_id}, Rating: {self.rating}, Comment: {self.comment}")
