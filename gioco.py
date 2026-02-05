class Gioco:
    """Rappresenta il gioco nel catalogo Ludoteca"""

    def __init__(self, titolo, nome_editore, nazione_editore, prezzo, min_giocatori, max_giocatori, durata_media, quantita, tipo):
        self.titolo = titolo
        self.nome_editore = nome_editore
        self.nazione_editore = nazione_editore
        self.prezzo = prezzo
        self.min_giocatori = min_giocatori
        self.max_giocatori = max_giocatori
        self.durata_media = durata_media
        self.quantita = quantita
        self.tipo = tipo    # tavolo || carte || dadi


    def __eq__(self, other):
        """Due giochi sono uguali quando hanno stesso nome ed editore"""
        if not isinstance(other, Gioco):
            return False
        return self.titolo == other.titolo and self.nome_editore == other.nome_editore
    

    def __repr__(self):
        return (f"Gioco ({self.titolo}, {self.nome_editore}, {self.nazione_editore}, {self.prezzo}, {self.min_giocatori}, {self.max_giocatori}, {self.durata_media}, {self.quantita}, {self.tipo})")
    

    def is_disponibile(self):
        return self.quantita>0
