FLESJES_IN_MINUTE: int = 12

def hoeveelheid_water(minuten: int) -> int:
    """
    Geeft de hoeveelheid water uit de douche, gerekend in flesjes,
    gegeven het aantal minuten douchen.
    
    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    0
    >>> weeks_elapsed(40, 61)
    3
    """
    return minuten * FLESJES_IN_MINUTE

if __name__ == "__main__":
    minuten = int(input("Hoeveel minuten douche je? "))
    hoeveelheid_water(minuten)