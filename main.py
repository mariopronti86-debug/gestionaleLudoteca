from gioco import Gioco

"""
Gestionale per la Ludoteca "Tana del chilling"
Classe Main di test
v 1.0
Authors: Pronti Mario 1 SW 2025
"""

if __name__ == "__main__":

    print("***** LUDOTECA TANA DEL CHILLING *****")
    g_dixit = Gioco("Dixit", "Asmodee", "Francia", 24.57, 3, 8, 30, 1, "tavolo")
    g_dixit_test = g_dixit

    g_monopoly = Gioco("Monolpoly", "Hasbro", "USA", 30.87, 2, 6, 90, 10, "tavolo")

    print(g_dixit)
    print(g_dixit.is_disponibile())
    print(g_dixit == g_dixit_test)
    print(g_dixit == g_monopoly)
