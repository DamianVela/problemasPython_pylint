'''
    Testeo
'''

import unittest
from hotel import Hotel
from reservation import Reservation
from customer import Customer
from data_manager import DataManager, read_data, write_data


class TestHotelReservationSystem(unittest.TestCase):
    '''
        Testeo
    '''
    def setUp(self):
        '''
            setup de los archivos json (base de datos).
        '''
        self.data_manager = DataManager("hotels.json",
                                        "customers.json",
                                        "reservations.json")
        self.read_data = read_data
        self.write_data = write_data

    def test_create_hotel(self):
        '''
            Test crear hotel
        '''
        hotel = Hotel(1, "Hotel Damian Vela", "Einstein 2421", 4)
        self.data_manager.create_hotel(hotel)
        hotels = self.read_data("hotels.json")
        self.assertIn(hotel.to_dict(), hotels)

    def test_delete_hotel(self):
        '''
            Test borrar hotel
        '''
        self.data_manager.delete_hotel(1)
        hotels = self.read_data("hotels.json")
        self.assertNotIn({"hotel_id": 1}, hotels)

    def test_create_customer(self):
        '''
            Test crear cliente
        '''
        customer = Customer(1, "Ana Vela", "anavela@gmail.com")
        self.data_manager.create_customer(customer)
        customers = self.read_data("customers.json")
        self.assertIn(customer.to_dict(), customers)

    def test_display_customer_info(self):
        '''
            Test mostrar cliente
        '''
        customer_id = 1
        new_customer = Customer(customer_id, "Nancy Noyola", "nancy@gmail.com")
        self.data_manager.create_customer(new_customer)
        displayed_customer = self.data_manager.display_customer_info(
            customer_id)
        self.assertEqual(displayed_customer["customer_id"],
                         new_customer.customer_id)
        self.assertEqual(displayed_customer["name"], new_customer.name)
        self.assertEqual(displayed_customer["email"], new_customer.email)

    def test_delete_customer(self):
        '''
            Test borrar cliente
        '''
        self.data_manager.delete_customer(1)
        customers = self.read_data("customers.json")
        self.assertNotIn({"customer_id": 1}, customers)

    def test_create_reservation(self):
        '''
            Test crear reservación
        '''
        reservation = Reservation(1, 1, 1, 3)
        self.data_manager.create_reservation(reservation)
        reservations = self.read_data("reservations.json")
        self.assertIn(reservation.to_dict(), reservations)

    def test_cancel_reservation(self):
        '''
            Test borrar reservación
        '''
        reservation_id = 1
        self.data_manager.cancel_reservation(reservation_id)
        reservations = self.read_data("reservations.json")
        self.assertNotIn({"reservation_id": reservation_id}, reservations)


if __name__ == "__main__":
    unittest.main()
