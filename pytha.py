def pythagore(hype, cote_b, cote_c):

    assert isinstance(hype, float), "Mauvais typage pour a"
    assert isinstance(cote_b, float), "Mauvais typage pour b"
    assert isinstance(cote_c, float), "Mauvais typage pour c"
    assert hype > cote_b and hype > cote_c, "Hypoténuse mauvais"

    somme_carre = (cote_b ** 2 + cote_c ** 2)
    return hype ** 2 == somme_carre

if __name__ == "__main__":
    HYPOTENUSE = input("Hypoténuse : ")
    COTE_B = input("Coté B : ")
    COTE_C = input("Coté C : ")

    EST_CARRE = pythagore(HYPOTENUSE, COTE_B, COTE_C)
    print(f"Triangle rectangle : {EST_CARRE}")