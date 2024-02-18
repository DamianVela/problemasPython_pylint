'''
    Class del hotel
'''


class Hotel:
    '''
        Class del hotel
    '''
    def __init__(self, hotel_id, name, address, rooms):
        '''
            Inicialización de la clase
        '''
        self.hotel_id = hotel_id
        self.name = name
        self.address = address
        self.rooms = rooms

    def to_dict(self):
        '''
            Regresar un diccionario
        '''
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "address": self.address,
            "rooms": self.rooms
        }

    @classmethod
    def from_dict(cls, data):
        '''
            Obtener los datos
        '''
        return cls(data["hotel_id"], data["name"],
                   data["address"], data["rooms"])
