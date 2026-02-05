from datetime import datetime

class Acquisto:

    def __init__(self, num_fattura, prezzo, rateizzato, data, cliente, giochi):
        self.num_fattura = num_fattura
        self.prezzo = prezzo
        self.rateizzato = rateizzato
        self.data = data
        self.cliente = cliente
        self.giochi = giochi


    def __eq__(self, other):
        if not isinstance(other, Acquisto):
            return False
        return self.num_fattura == other.num_fattura
    

    def __repr__(self):
        return f"Acquisto ({self.num_fattura}, {self.prezzo}, {self.rateizzato}, {self.data}, {self.cliente}, {self.giochi})"