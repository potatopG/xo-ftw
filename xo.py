class xo:
    def __init__(self, pos,signe):
        self.pos=pos
        self.signe=signe

def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def game0():
    print("bonjour ija al3ab ya mezyen")
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    for i in range(1, 10):
        display_board(board)
        pos = int(input("selectionnez la position (1-9): "))
        while pos >= 10 or pos < 1 or board[(pos-1)//3][(pos-1)%3] != " ":
            pos = int(input("selectionnez la position (entre 1 et 9 ya bhim): "))
        
        signe = "X" if i % 2 == 1 else 'O'
        tour = xo(pos, signe)
        board[(tour.pos-1)//3][(tour.pos-1)%3] = tour.signe
    
    display_board(board)
    
game0()
