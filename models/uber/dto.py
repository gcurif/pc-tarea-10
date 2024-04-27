# Clase que representa los usuarios
# Atributos de la clase:
# -user_id: es ideal que todo objeto tenga un id para poder buscarlo en la base de datos
# -username: nombre de usuario
# -email: correo del usuario
# -password: contraseña del usuario
# -adresss: dirección del usuario
# -payment_info: información de pago
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

# Clase que representa a los Conductores
# Se usa composición ya que almacena a su vez un objeto vehiculo
# Se usa hrencia ya que hereda todas las caracteristicas de User pero agrega dos nuevos atributos
# Atributos de la clase:
# -license_number: numero de licencia del conductor
# -vehicle: objeto Vehiculo del conductor
class Driver(User):
    def __init__(self, user_id, username, email, phone, password, address, payment_info, license_number, vehicle):
        super().__init__(user_id, username, email, phone, password, address, payment_info)
        self.license_number = license_number
        self.vehicle = vehicle

    def print_info(self):
        super().print_info()
        print(f"License Number: {self.license_number}")
        self.vehicle.print_info()


# Clase que representa el vehículo del conductor
# Atributos de la clase:
# -vehicle_id: id para identificar el vehiculo en base de datos
# -make: marca dek vehículo
# -model: modelo del vehículo
# -year: año del vehículo
# -color:  color del vehículo
# -plate_number: patente del vehículo
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

"""
(En este punto ya me dio paja escribir comentarios con Gato #, era para que se acuerde de como comentar un código nomas
ahora voy con las comillas)

Clase que representa un viaje

Atributos de la clase:
-trip_id: id para identificar en base de datos
-user_id: id del usuario que toma el viaje identificarlo (aqui se pudo ocupar composición)
-driver_id: id del conductor del viaje
-start_time: fecha de inicio del viaje
-end_time: fecha de finalización del viaje
-start_location = lugar de inicio del viaje
-end_location = lugar de finalización del viaje
"""
class Trip:
    def __init__(self, trip_id, user_id, driver_id, start_time, end_time, start_location, end_location, status):
        self.trip_id = trip_id
        self.user_id = user_id
        self.driver_id = driver_id
        self.start_time = start_time
        self.end_time = end_time
        self.start_location = start_location
        self.end_location = end_location

    def print_info(self):
        print(f"Trip ID: {self.trip_id}, Start Time: {self.start_time}, End Time: {self.end_time}, Start Location: {self.start_location}, End Location: {self.end_location}")


"""
Clase que representa un pago realizado
Atributos de la clase:
-payment_id = id para identificar en la base de datos
-user_id: usuario que realiza el pago
-amount: monto de pago en pesos o dolares
-payment_method: método de pago, tarjeta de crédito, efectivo, etc ...
-payment_status: estado del pago: completado, con error, rechazado, pendiente, etc ...
"""
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
