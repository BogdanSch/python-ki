def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".
    >>> meal("7:15")
    'ontbijt'
    >>> meal("22:12")
    
    >>> meal("18:53")
    'avondeten'
    """
    time_components = time.split(":")
    hour = int(time_components[0])
    minutes = int(time_components[1].split(" ")[0])
    
    if 7 <= hour <= 8 or (hour == 7 and 0 <= minutes <= 59):
        return "ontbijt"
    elif 12 <= hour <= 13 or (hour == 12 and 0 <= minutes <= 59):
        return "lunch"
    elif 18 <= hour <= 19 or ():
        return "avondeten"
    return None

if __name__ == '__main__':
    time = input("Hoe laat is het? ")
    
    meal_type = meal(time)
    if meal_type is not None:
        print(f"Het is tijd voor {meal_type}")