def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".
    >>> meal("7:15")
    ontbijt
    >>> meal("22:12")
    None
    >>> meal("18:53")
    """
    hour = int(time.split(":")[0])
    if 7 <=  hour <= 8:
        return "ontbijt"
    elif 12 <= hour <= 13:
        return "lunch"
    elif 18 <= hour <= 19:
        return "avondeten"

if __name__ == '__main__':
    time = input("Hoe laat is het? ")
    
    meal_type = meal(time)
    if meal_type is not None:
        print(f"Het is tijd voor {meal_type}")