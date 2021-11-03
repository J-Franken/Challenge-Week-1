def antwoord_invoer_en_controle():
    antwoord = input("Wat is je antwoord?: ").upper()
    print("\n")
    while antwoord not in ["A", "B", "C", "D"] or len(antwoord) != 1:
        antwoord = input("Voer een geldig antwoord in: ").upper()
    return antwoord
