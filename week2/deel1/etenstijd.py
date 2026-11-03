def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".
    >>> meal("7:15 AM")
    'ontbijt'
    >>> meal("22:12")
    
    >>> meal("18:53")
    'avondeten'
    """
    hour,  = time.split(":")
    hour,  = int(time_components[0])
    
    rest = time_components[1].split(" ")
    minutes = int(rest[0])
    if rest[-1] == "PM":
        hour += 12   
    
    if 7 <= hour <= 8:
        if hour == 8 and 0 < minutes <= 59:
            return None
        return "ontbijt"
    elif 12 <= hour <= 13:
        if hour == 13 and 0 < minutes <= 59:
            return None
        return "lunch"
    elif 18 <= hour <= 19:
        if hour == 19 and 0 < minutes <= 59:
            return None
        return "avondeten"
    return None

if __name__ == '__main__':
    time = input("Hoe laat is het? ")
    
    meal_type = meal(time)
    if meal_type is not None:
        print(f"Het is tijd voor {meal_type}")