def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
    """
    Berekent de hoeveelheid cafeine op basis van de hoeveelheid gedronken
      drankjes van het type koffie, thee, energie, en cola.
    """
    return 90 * coffee + 

if __name__ == '__main__':
    coffee = int(input("Hoeveel koppen koffie? "))
    tea = int(input("Hoeveel koppen thee? "))
    energy_drinks = int(input("Hoeveel energiedrankjes? "))
    coke = int(input("Hoeveel glazen cola? "))
    
    cafeine_amount = calculate_cafeine(coffee, tea, energy_drinks, coke)
    print(f"Je krijgt {cafeine_amount} mg cafeïne binnen.")