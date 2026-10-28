def is_acidic(ph: float) -> bool:
    """
    Bepaalt de vervoerskosten op basis van de te rijden afstand
    naar de accomodatie (tel `km` twee keer voor heen en terug).
    """
    return ph < 7.0
    
if __name__ == "__main__":
    ph = float(input("Geef een pH-waarde: "))
    print("Het is een zuur" if is_acidic(ph) else "Het is een base")
    