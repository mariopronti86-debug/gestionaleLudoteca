class Cliente:

    def __init__(self, nome, num_tessera, punti_fedelta):
        self.nome = nome
        self.num_tessera = num_tessera
        self.punti_fedelta = punti_fedelta

    
    def __eq__(self, other):
        if not isinstance(other, Cliente):
            return False
        return self.num_tessera == other.num_tessera
    

    def __repr__(self):
        return f"Cliente ({self.nome}, {self.num_tessera}, {self.punti_fedelta})"
    

    def acquisti_rateizzati_attivi():
        pass


    def possiede_gioco(gioco):
        pass


    def acquisti_gioco(acquisto):
        pass


    def visualizza_giochi():
        pass