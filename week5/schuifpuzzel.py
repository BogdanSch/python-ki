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
    >>> is_won([[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 1, 2, 0]])
    False
    >>> is_won([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
    True
    """
    for i in range(TOTAL_ROWS):
        for j in range(TOTAL_COLUMNS - 1):
            if i == TOTAL_ROWS - 1 and TOTAL_COLUMNS - 1: 
                continue
            if board[i][j] > board[i][j + 1]:
                return False
    return True
    
def is_valid_point(point: tuple[int, int]) -> bool:
    """
    >>> check_boundaries((0, 0))
    True
    """
    return 0 <= tuple[0] < TOTAL_ROWS and 0 <= tuple[1] < TOTAL_COLUMNS

def move_tile(board: Board, tile: int) -> bool:
    """
    Als de te verplaatsten tegel verplaatsbaar is: schuift de tegel in de
    configuratie van het bord en geeft True. Als dat niet het geval is, blijft
    het bord in de oorspronkelijke configuratie en functie geeft False.
    >>> move_tile([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]], 15)
    True
    """
    move_directions = [-1, 1]
    
    for i in range(TOTAL_ROWS):
        for j in range(TOTAL_COLUMNS):
            if board[i][j] == move_tile:
                tile_position = (i, j)
    
    if len(tile_position) == 0:
        return False
    
    row, col = tile_position
    possible_moves = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    for point in possible_moves:
        if check_boundaries(point) and board[point[0]][point[1]] == 0:
            board[row][col], board[point[0]][point[1]] = board[point[0]][point[1]], board[row][col]
            return True
    
    return False

def print_board(board: Board) -> None:
    """
    Print alle rijen van het bord onder elkaar. Het format is zoals in de
    voorbeelden onderaan de opdracht.
    >>> print_board([[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 1, 2, 0]])
    15 14 13 12
    11 10  9  8
     7  6  5  4
     3  1  2  0
    """
    for i in range(TOTAL_ROWS):
        for j in range(TOTAL_COLUMNS):
            print(f"{board[i][j]:>2} ", end="")
        print()

def create_board() -> Board:
    """
    Initialiseert een bord van formaat 4 x 4.
    Sorteert de nummers op aflopende volgorde van links boven naar rechts beneden.
    De volgorde van de tegels 1 en 2 is verwisseld.
    >>> create_board()
    [[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 1, 2, 0]]
    """
    board: list[list[int]] = []
    for i in range(TOTAL_ROWS):
        board.append([])
        for j in range(TOTAL_COLUMNS):
            board[i].append(0)
    
    current_number = TOTAL_ROWS * TOTAL_COLUMNS - 1
    for i in range(TOTAL_ROWS):
        for j in range(TOTAL_COLUMNS):
            if i == TOTAL_ROWS - 1 and j == TOTAL_COLUMNS - 1:
                board[i][j] = 0
            elif i == TOTAL_ROWS - 1 and j == TOTAL_COLUMNS - 3:
                board[i][j] = current_number - 1
            elif i == TOTAL_ROWS - 1 and j == TOTAL_COLUMNS - 2:
                board[i][j] = current_number
            else:
                board[i][j] = current_number
                current_number -= 1
    return board

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