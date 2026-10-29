def is_same_rectangle(ax_length: int, ay_length: int, bx_length: int, by_length: int) -> bool:
    """
    Controleert of de lengtes van de zijdes gelijk zijn
    """
    return ax_length == bx_length and ay_length == by_length

def is_same_square(ax_length: int, ay_length: int, bx_length: int, by_length: int) -> bool:
    """
    Controleert of beide rechthoeken hetzelfde vierkant zijn
    """
    return is_same_rectangle(ax_length, ay_length, bx_length, by_length) and ax_length == ay_length

def calculate_length(c1: int, c2: int) -> int:
    """
    Berekent de lengte van een zijde op basis van twee coördinaten
    """
    return abs(c1 - c2)

if __name__ == '__main__':
    ax1 = int(input("Geef de x1 van A:"))
    ax2 = int(input("Geef de x2 van A:"))
    ax_length = calculate_length(ax1, ax2)
    
    ay1 = int(input("Geef de y1 van A:"))
    ay2 = int(input("Geef de y2 van A:"))
    ay_length = calculate_length(ay1, ay2)
        
    bx1 = int(input("Geef de x1 van B:")
    bx2 = int(input("Geef de x2 van B:")
    bx_length = calculate_length(bx1, bx2)
    
    by1 = int(input("Geef de y1 van B:")
    by2 = int(input("Geef de y2 van B:")
    by_length = calculate_length(by1, by2)
    
    print("De rechthoeken zijn gelijk!")
    print("En ze zijn ook nog vierkant!")
    else:
        Er is niks aan :(