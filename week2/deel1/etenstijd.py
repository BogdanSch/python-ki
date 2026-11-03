def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".
    """
    if 7:00 tot en met 8:00

if __name__ == '__main__':
    time = input("Hoe laat is het? ")
    
    meal_type = meal(time)
    if meal_type is not None:
        print(f"Het is tijd voor {meal_type}")