from models.uber2.dto import *

def showUberData():

    print("Mostrando Usuarios:")

    usuario = User(user_id=1, username="johnDoe", email="john@example.com", phone="1234567890", password="password123", address="123 Elm St", payment_info="Visa 9876")
   
    usuario.print_info()
   

    print("---")
    print("Mostrando comida:")

    comida = Comida(comida_id="Cesar", salsa="salsacesarpapas", bebida="pepsi")
    

    comida.print_info()
    

    print("---")
    print("Mostrando Conductores:")

    driver = Driver(user_id=4, username="mikeJohnson", email="mike@example.com", phone="9876543210", password="hello123", address="321 Cedar St", payment_info="Visa 4321", license_number="LIC123", vehicle=vehicle1)
    

    driver.print_info()
    
    
    print("---")
    print("Mostrando Viajes:")
    restaurante = Restaurante(trip_id=201, user_id=1, driver_id=4, start_time="2021-05-01 08:00:00", end_time="2021-05-01 08:30:00", start_location="123 Elm St", end_location="City Mall", status="Completed")
    
    restaurante .print_info()
    

    print("---")
    print("Mostrando Pagos:")

    pago = pago(payment_id=301, user_id=1, amount=25.00, payment_method="Credit Card", payment_status="Paid", trip_id=201)
   
    pago.print_info()
    
