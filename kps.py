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
        if siirto not in siirtovaihtoehdot:
            print("Siirto ei valittavissa\n")
        return siirto[0]
        
def vastustajan_valinta(siirto):
    vastustaja = r.choice(['k', 'p', 's'])
    if vastustaja == siirto:
        print("Tasapeli!")
    else: 
        pass



