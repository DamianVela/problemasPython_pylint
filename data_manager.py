'''
    Clase para hacer operaciones
'''


import json


def read_data(filename):
    '''
        Leer los datos de los archivos
    '''
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


def write_data(data, filename):
    '''
        Escribir los datos en el archivo json.
    '''
    with open(filename, 'w') as file:
        json.dump(data, file)


class DataManager:
    '''
        Clase para hacer operaciones
    '''
    def __init__(self, hotels_file, customers_file, reservations_file):
        '''
            Inicializar y dar los archivos
        '''
        self.hotels_file = hotels_file
        self.customers_file = customers_file
        self.reservations_file = reservations_file

    def create_hotel(self, hotel):
        '''
            Crear hotel
        '''
        hotels = read_data(self.hotels_file)
        hotels.append(hotel.to_dict())
        write_data(hotels, self.hotels_file)

    def display_hotel_info(self, hotel_id):
        '''
            Mostrar hotel
        '''
        hotels = read_data(self.hotels_file)
        for hotel in hotels:
            if hotel["hotel_id"] == hotel_id:
                return hotel
        return None

    def delete_hotel(self, hotel_id):
        '''
            Eliminar hotel
        '''
        hotels = read_data(self.hotels_file)
        hotels = [h for h in hotels if h["hotel_id"] != hotel_id]
        write_data(hotels, self.hotels_file)

    def modify_hotel_info(self, hotel_id, new_info):
        '''
            Editar la información del hotel.
        '''
        hotels = read_data(self.hotels_file)
        for hotel in hotels:
            if hotel["hotel_id"] == hotel_id:
                hotel.update(new_info)
        write_data(hotels, self.hotels_file)

    def create_customer(self, customer):
        '''
            Crear clientes
        '''
        customers = read_data(self.customers_file)
        customers.append(customer.to_dict())
        write_data(customers, self.customers_file)

    def delete_customer(self, customer_id):
        '''
            Eliminar clientes
        '''
        customers = read_data(self.customers_file)
        customers = [c for c in customers if c["customer_id"] != customer_id]
        write_data(customers, self.customers_file)

    def display_customer_info(self, customer_id):
        '''
            Mostrar clientes
        '''
        customers = read_data(self.customers_file)
        for customer in customers:
            if customer["customer_id"] == customer_id:
                return customer
        return None

    def modify_customer_info(self, customer_id, new_info):
        '''
            Editar clientes
        '''
        customers = read_data(self.customers_file)
        for customer in customers:
            if customer["customer_id"] == customer_id:
                customer.update(new_info)
        write_data(customers, self.customers_file)

    def create_reservation(self, reservation):
        '''
            Crear reservación
        '''
        reservations = read_data(self.reservations_file)
        reservations.append(reservation.to_dict())
        write_data(reservations, self.reservations_file)

    def cancel_reservation(self, reservation_id):
        '''
            Eliminar reservación
        '''
        res = read_data(self.reservations_file)
        res = [r for r in res if r["reservation_id"] != reservation_id]
        write_data(res, self.reservations_file)
