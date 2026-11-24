import random

def calculate_points(board: list[int]) -> int:
    """
    Berekent het aantal punten dat is behaald met sjoelen. De
    volgorde van de punten is [2, 3, 4, 1]. Wanneer er een
    kwartet tussen zit, telt dit voor 20 punten.
    """
    

def shuffle_round(board: list[int], discs: int) -> int:
    """
    Simuleert een enkele ronde sjoelen. De variable `board` wordt
    aangepast als er een schijf in een gleuf terecht komt. Returnt
    het aantal schijven dat nog over is om nog eens mee te schuiven.
    """
    if random.uniform(0,1) <= 0.25:
        gleuf = random.
        if 
        
    else:

if __name__ == "__main__":
    board = [0, 0, 0, 0]
    for i in range(3):
        shuffle_round()
        
    print(f"Je bent geëindigd op deze configuratie: {board}")
    print(f"Dat zijn {calculate_points} punten!")
    