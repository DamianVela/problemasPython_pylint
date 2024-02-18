'''
    Class de los clientes
'''


class Customer:
    '''
        Class de los clientes
    '''
    def __init__(self, customer_id, name, email):
        '''
            Inicialización de la clase
        '''
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        '''
            Rregresar los valores
        '''
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        '''
            Leer los datos
        '''
        return cls(data["customer_id"], data["name"],
                   data["email"])
