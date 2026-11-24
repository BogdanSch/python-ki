# 4 x 4 grid
"""
Er bestaan schuifpuzzels van verschillende groottes; 
belangrijk om te weten is, is dat wanneer een zijde een even aantal velden heeft (en er dus een oneven aantal tegels zijn) 
de tegels 1 & 2 moeten worden omgewisseld.
Dit is nodig zodat de puzzel oplosbaar is, en dat zie je dus ook terug in het voorbeeld hierboven.
"""

Board = list[list[int]]
TOTAL_ROWS = 4
TOTAL_COLUMNS = 4

def is_won(board: Board) -> bool:
    """
    Controleert of het bord in een winnende configuratie staat. Geeft True als
    de configuratie winnend is, False als dat niet het geval is.
    """

def move_tile(board: Board, tile: int) -> bool:
    """
    Als de te verplaatsten tegel verplaatsbaar is: schuift de tegel in de
    configuratie van het bord en geeft True. Als dat niet het geval is, blijft
    het bord in de oorspronkelijke configuratie en functie geeft False.
    """

def print_board(board: Board) -> None:
    """
    Print alle rijen van het bord onder elkaar. Het format is zoals in de
    voorbeelden onderaan de opdracht.
    """

def create_board() -> Board:
    """
    Initialiseert een bord van formaat 4 x 4.
    Sorteert de nummers op aflopende volgorde van links boven naar rechts beneden.
    De volgorde van de tegels 1 en 2 is verwisseld.
    """
    current_number = 1
    for i in range(TOTAL_ROWS):
        for j in range(TOTAL_COLUMNS):
            if i == TOTAL_ROWS - 1 and j == TOTAL_COLUMNS - 1:
                Board[i][j] = 0
            elif i == TOTAL_ROWS - 1 and j == TOTAL_COLUMNS - 1
            Board[i][j] = current_number
            current_number += 1
            

if __name__ == '__main__':
    print("Welkom bij de schuifpuzzel!")
    board = create_board()
    while not is_won(board):
        print_board(board)
        tile = input("Tegel die je wil schuiven: ")
        valid = move_tile(board, int(tile))
        if not valid:
            print("Deze tegel kan je niet schuiven.")
    print("Gefeliciteerd, je hebt de schuifpuzzel opgelost!")