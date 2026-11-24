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
    for _ in range()
    if random.uniform(0,1) <= 0.25:
        gleuf_chance = random.uniform(0,1)
        if gleuf_chance <= 0.3:
            board[] += 1
        elif 0.3 < gleuf_chance <= 0.6:
            += 2
        elif 0.6 < gleuf_chance <= 0.8:
            += 3
        else: 
            += 4

if __name__ == "__main__":
    # [2, 3, 4, 1]
    board = [0, 0, 0, 0]
    discs = 
    for i in range(3):
        shuffle_round()
        
    print(f"Je bent geëindigd op deze configuratie: {board}")
    print(f"Dat zijn {calculate_points} punten!")
    