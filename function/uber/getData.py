from models.uber.dto import *

def showUberData():

    print("Mostrando Usuarios:")

    user1 = User(user_id=1, username="johnDoe", email="john@example.com", phone="1234567890", password="password123", address="123 Elm St", payment_info="Visa 9876")
    user2 = User(user_id=2, username="janeSmith", email="jane@example.com", phone="0987654321", password="securePass456", address="456 Oak St", payment_info="Mastercard 5432")
    user3 = User(user_id=3, username="samBrown", email="sam@example.com", phone="1122334455", password="myPassword789", address="789 Pine St", payment_info="Amex 1010")

    user1.print_info()
    user2.print_info()
    user3.print_info()

    print("---")
    print("Mostrando vehículos:")

    vehicle1 = Vehicle(vehicle_id=101, make="Toyota", model="Corolla", year=2020, color="Red", plate_number="XYZ123")
    vehicle2 = Vehicle(vehicle_id=102, make="Honda", model="Civic", year=2019, color="Blue", plate_number="ABC456")
    vehicle3 = Vehicle(vehicle_id=103, make="Ford", model="Focus", year=2021, color="Black", plate_number="DEF789")

    vehicle1.print_info()
    vehicle2.print_info()
    vehicle3.print_info()

    print("---")
    print("Mostrando Conductores:")

    driver1 = Driver(user_id=4, username="mikeJohnson", email="mike@example.com", phone="9876543210", password="hello123", address="321 Cedar St", payment_info="Visa 4321", license_number="LIC123", vehicle=vehicle1)
    driver2 = Driver(user_id=5, username="lisaWhite", email="lisa@example.com", phone="1231231234", password="password321", address="654 Spruce St", payment_info="Mastercard 8765", license_number="LIC456", vehicle=vehicle2)
    driver3 = Driver(user_id=6, username="tomGreen", email="tom@example.com", phone="3213214321", password="secure789", address="987 Willow St", payment_info="Amex 2020", license_number="LIC789", vehicle=vehicle3)

    driver1.print_info()
    driver2.print_info()
    driver3.print_info()
    
    print("---")
    print("Mostrando Viajes:")
    trip1 = Trip(trip_id=201, user_id=1, driver_id=4, start_time="2021-05-01 08:00:00", end_time="2021-05-01 08:30:00", start_location="123 Elm St", end_location="City Mall", status="Completed")
    trip2 = Trip(trip_id=202, user_id=2, driver_id=5, start_time="2021-05-02 09:00:00", end_time="2021-05-02 09:45:00", start_location="456 Oak St", end_location="Airport", status="Completed")
    trip3 = Trip(trip_id=203, user_id=3, driver_id=6, start_time="2021-05-03 10:00:00", end_time="2021-05-03 11:00:00", start_location="789 Pine St", end_location="Downtown", status="Cancelled")
    
    trip1.print_info()
    trip2.print_info()
    trip3.print_info()

    print("---")
    print("Mostrando Pagos:")

    payment1 = Payment(payment_id=301, user_id=1, amount=25.00, payment_method="Credit Card", payment_status="Paid", trip_id=201)
    payment2 = Payment(payment_id=302, user_id=2, amount=45.00, payment_method="Credit Card", payment_status="Paid", trip_id=202)
    payment3 = Payment(payment_id=303, user_id=3, amount=0.00, payment_method="Credit Card", payment_status="Refunded", trip_id=203)

    payment1.print_info()
    payment2.print_info()
    payment3.print_info()
