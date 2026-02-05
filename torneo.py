from datetime import datetime

class Torneo:

    def __init__(self, nome, data, num_max_partecipanti, quota_iscrizione, premio, gioco, partecipanti):
        self.nome = nome
        self.data = data
        self.num_max_partecipanti = num_max_partecipanti
        self.quota_iscrizione = quota_iscrizione
        self.premio = premio
        self.gioco = gioco
        self.partecipanti = partecipanti


    def __eq__(self, other):
        if not isinstance(other, Torneo):
            return False
        return self.nome == other.nome and self.data == other.data
    

    def __repr__(self):
        return f"Torneo ({self.nome}, {self.data}, {self.num_max_partecipanti}, {self.quota_iscrizione}, {self.premio}, {self.gioco}, {self.partecipanti})"
    

    def posti_disponibili():
        pass


    def is_pieno():
        pass


    def iscrivi_cliente(Cliente):
        pass


    def visualizza_partecipanti():
        pass