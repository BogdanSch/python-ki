def travel_costs(km: int) -> float:
    """
    Bepaalt de vervoerskosten op basis van de te rijden afstand
    naar de accomodatie (tel `km` twee keer voor heen en terug).
    >>> travel_costs(0)
    0.0
    >>> travel_costs(100)
    26.0
    """
    return .13 * km * 2

def overnight_costs(nights: int) -> float:
    """
    Bepaalt de overnachtingskosten op basis van het aantal nachten
    dat je op vakantie gaat.
    
    >>> overnight_costs(5)
    300
    >>> overnight_costs(10)
    600
    >>> overnight_costs(12)
    720
    """
    return 60 * nights

def total_costs(km: int, nights: int) -> int:
    """
    Bepaalt de totale kosten op basis van de afstand en het aantal
    nachten en rondt af naar hele euro's.
    Deze functie delegeert zoveel mogelijk werk naar de andere
    twee functies (roep die dus hier aan).
    
    >>> total_costs(1250, 5)
    625
    >>> total_costs(800, 10)
    808
    >>> total_costs(2159, 12)
    1281
    """
    return int(travel_costs(km) + overnight_costs(nights) + 0.5)

if __name__ == '__main__':
    km = int(input("Hoe ver ga je weg in kilometers? "))
    nights = int(input("Hoe veel nachten is je verblijf? "))
    print(f"Jouw vakantie kost: {total_costs(km, nights)}")