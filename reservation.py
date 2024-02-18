'''
    Class de las reservaciones
'''


class Reservation:
    '''
        Class de las reservaciones
    '''
    def __init__(self, reservation_id, customer_id, hotel_id, room_number):
        '''
            Inicialización de la clase
        '''
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.room_number = room_number

    def to_dict(self):
        '''
            Regreso de un diccionario
        '''
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id,
            "room_number": self.room_number
        }

    @classmethod
    def from_dict(cls, data):
        '''
           Leer los datos
        '''
        return cls(data["reservation_id"], data["customer_id"],
                   data["hotel_id"], data["room_number"])
