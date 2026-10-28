FLESJES_IN_MINUTE: int = 12

def hoeveelheid_water(minuten: int) -> int:
    """
    Geeft de hoeveelheid water uit de douche, gerekend in flesjes,
    gegeven het aantal minuten douchen.
    """
    return minuten * FLESJES_IN_MINUTE

if __name__ == "__main__":
    minuten = int(input("Hoeveel minuten douche je? "))
    hoeveelheid_water(minuten)