import random as r

def kysy_liike():
    """
    kysyy käyttäjältä liikkeen kivi (k) sakset (s) tai paperi (p)
    tallentaa muuttujaan
    """
    print("Siirtovaihtoehdot:\nKivi (K)\nSakset (S)\nPaperi (P)\n  ")
    siirtovaihtoehdot = ['kivi', 'k', 'paperi', 'p', 'sakset', 's']
    while True:
        siirto = input("Valitse siirtosi: ").strip().lower()
        if siirto in siirtovaihtoehdot:
            return siirto[0]
        print("Siirto ei valittavissa\n")

def peli(siirto):
    vastustaja = r.choice(['k', 'p', 's'])
    if vastustaja == siirto:
        print("Tasapeli!")
    elif (vastustaja, siirto) in [('k','s'), ('s','p'), ('p','k')]:
        print("Hävisit!")
    else: 
        print("Voitit!")

if __name__ == "__main__":
    valinta = kysy_liike()
    peli(valinta)