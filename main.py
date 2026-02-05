from gioco import Gioco
from cliente import Cliente
from acquisto import Acquisto
from datetime import datetime

"""
Gestionale per la Ludoteca "Tana del chilling"
Classe Main di test
v 1.0
Authors: Pronti Mario 1 SW 2025
"""

if __name__ == "__main__":

    print("***** LUDOTECA TANA DEL CHILLING *****\n")

    gioco1 = Gioco("Catan", "Kosmos", "Germania", 45.90, 3, 4, 90, 5, "tavolo")
    gioco2 = Gioco("Ticket to Ride", "Days of Wonder", "Francia", 52.00, 2, 5, 60, 3, "tavolo")
    gioco3 = Gioco("Uno", "Mattel", "USA", 12.50, 2, 10, 30, 15, "carte")
    gioco4 = Gioco("Pandemic", "Z-Man Games", "USA", 48.00, 2, 4, 45, 4, "tavolo")
    gioco5 = Gioco("Dixit", "Libellud", "Francia", 35.90, 3, 6, 30, 8, "carte")
    gioco6 = Gioco("Yahtzee", "Hasbro", "USA", 18.00, 1, 6, 30, 10, "dadi")
    gioco7 = Gioco("Azul", "Plan B Games", "Canada", 42.50, 2, 4, 40, 6, "tavolo")
    gioco8 = Gioco("Bang!", "dV Giochi", "Italia", 22.00, 4, 7, 45, 7, "carte")
    gioco9 = Gioco("Carcassonne", "Hans im Glück", "Germania", 38.00, 2, 5, 35, 5, "tavolo")
    gioco10 = Gioco("King of Tokyo", "Iello", "Francia", 44.00, 2, 6, 30, 0, "dadi")


    cliente1 = Cliente("Mario Rossi", "TS001234", 450)
    cliente2 = Cliente("Laura Bianchi", "TS002156", 1200)
    cliente3 = Cliente("Giuseppe Verdi", "TS003789", 320)
    cliente4 = Cliente("Anna Ferrari", "TS004523", 875)
    cliente5 = Cliente("Francesco Ricci", "TS005891", 150)
    cliente6 = Cliente("Giulia Romano", "TS006347", 2100)
    cliente7 = Cliente("Marco Colombo", "TS007612", 680)
    cliente8 = Cliente("Sofia Russo", "TS008934", 430)
    cliente9 = Cliente("Alessandro Gallo", "TS009245", 1550)
    cliente10 = Cliente("Chiara Conti", "TS010678", 920)


    acquisto1 = Acquisto("FAT001", 45.90, False, datetime(2025, 1, 15), cliente1, [gioco1])
    acquisto2 = Acquisto("FAT002", 104.50, True, datetime(2025, 1, 18), cliente2, [gioco2, gioco3])
    acquisto3 = Acquisto("FAT003", 48.00, False, datetime(2025, 1, 20), cliente3, [gioco4])
    acquisto4 = Acquisto("FAT004", 58.90, False, datetime(2025, 1, 22), cliente4, [gioco5, gioco8])
    acquisto5 = Acquisto("FAT005", 18.00, False, datetime(2025, 1, 25), cliente5, [gioco6])
    acquisto6 = Acquisto("FAT006", 126.90, True, datetime(2025, 1, 28), cliente6, [gioco1, gioco7, gioco9])
    acquisto7 = Acquisto("FAT007", 42.50, False, datetime(2025, 2, 1), cliente7, [gioco7])
    acquisto8 = Acquisto("FAT008", 90.00, True, datetime(2025, 2, 3), cliente8, [gioco4, gioco5])
    acquisto9 = Acquisto("FAT009", 60.00, False, datetime(2025, 2, 4), cliente9, [gioco3, gioco8, gioco6])
    acquisto10 = Acquisto("FAT010", 38.00, False, datetime(2025, 2, 5), cliente10, [gioco9])

    
    # TEST: Stampa alcuni giochi
    print("=== GIOCHI ===")
    print(gioco1)
    print(gioco3)
    
    # TEST: Verifica disponibilità
    print("\n=== DISPONIBILITÀ ===")
    print(f"{gioco1.titolo} disponibile? {gioco1.is_disponibile()}")
    print(f"{gioco10.titolo} disponibile? {gioco10.is_disponibile()}")
    
    # TEST: Stampa alcuni clienti
    print("\n=== CLIENTI ===")
    print(cliente1)
    print(cliente6)
    
    # TEST: Stampa alcuni acquisti
    print("\n=== ACQUISTI ===")
    print(acquisto1)
    print(acquisto2)
    print(acquisto6)
    
    # TEST: Acquisti rateizzati
    print("\n=== ACQUISTI RATEIZZATI ===")
    print(f"Acquisto {acquisto2.num_fattura} rateizzato? {acquisto2.rateizzato}")
    print(f"Acquisto {acquisto6.num_fattura} rateizzato? {acquisto6.rateizzato}")
    print(f"Acquisto {acquisto1.num_fattura} rateizzato? {acquisto1.rateizzato}")

