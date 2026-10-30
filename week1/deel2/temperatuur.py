def convert_temperature(old_type: str, old_temp: int) -> int:
    """
    Zet de temperatuur (old_temp) van het type old_type om naar
    de temperatuur van het nieuwe type.
    """
    if old_type == "c":
        return int((18 * old_temp + 320) / 10.0)
    else:
        return (10 * old_temp - 320) / 18

def print_table(old_type: str, begin_temp: int, end_temp: int, step_size: int) -> None:
    """
    Print de conversie-tabel.
    """
    
    new_type = "F" if old_type == "c" else "C"
    print(f"{old_type:>2} | {new_type:2}")
    
    if end_temp < begin_temp:
        return
    
    for i in range(begin_temp, end_temp + 1, step_size):
        print(f"{i:>2} | {int(convert_temperature(old_type, i)):2}")

if __name__ == "__main__":
    unit = input("Welke eenheid van temperatuur (C of F)? ").lower()
    begin_temp = int(input("Wat is de begintemperatuur? "))
    end_temp = int(input("Wat is de eindtemperatuur? "))
    
    step_size = int(input("Wat is de stapgrootte? "))
    while step_size <= 0:
        step_size = int(input("Wat is de stapgrootte? "))
        
    
    print_table(unit, begin_temp, end_temp, step_size)