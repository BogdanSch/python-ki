def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
    """
    Berekent de hoeveelheid cafeine op basis van de hoeveelheid gedronken
      drankjes van het type koffie, thee, energie, en cola.
      
    >>> calculate_cafeine(5, 0, 0, 0)
    450
    >>> calculate_cafeine(1, 1, 1, 1)
    225
    """
    return 90 * coffee + 45 * tea + 80 * energy + 40 * cola

if __name__ == '__main__':
    coffee = int(input("Hoeveel koppen koffie? "))
    tea = int(input("Hoeveel koppen thee? "))
    energy_drinks = int(input("Hoeveel energiedrankjes? "))
    cola = int(input("Hoeveel glazen cola? "))
    
    cafeine_amount = calculate_cafeine(coffee, tea, energy_drinks, cola)
    print(f"Je krijgt {cafeine_amount} mg cafeïne binnen.")