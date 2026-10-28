def is_acidic(ph: float) -> bool:
    """
    Bepaalt de zuurgraad op basis van de pH-waarde.
    return: 
    """
    return ph < 7.0
    
if __name__ == "__main__":
    ph = float(input("Geef een pH-waarde: "))
    print("Het is een zuur" if is_acidic(ph) else "Het is een base")
    