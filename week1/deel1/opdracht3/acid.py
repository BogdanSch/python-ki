def is_acidic(ph: float) -> bool:
    """
    Bepaalt het millieu van een oplossing op basis van de pH-waarde.
    return: True/False
    
    >>> is_acidic(0)
    True
    >>> is_acidic(7)
    False
    >>> is_acidic(12)
    False
    """
    if ph < 7.0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    ph = float(input("Geef een pH-waarde: "))
    if is_acidic(ph):
        print("Het is een zuur")
    else:
        print("Het is een base")
    