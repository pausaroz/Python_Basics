##Egzamin na poziom 102
##
##Masz do wyboru:
##
##1. napisać grę tekstową papier, kamień, nożyce - https://pl.wikipedia.org/wiki/Papier,_kamie%C5%84,_no%C5%BCyce
##2. kółko i krzyżyk (najprostsza plansza 3x3)
##
##W obu przypadkach, to ma być aplikacja konsolowa, nie rób żadnej grafiki do tego. 
##
##W oby przypadkach musi być również możliwość gry z komputerem.
##
##W przypadku 1 jest to trywialne, bo to tylko loswanie jednego z 3 elementów
##W przypadku 2 zrób to najprościej jak się da i po prostu losuj co się pojawi na dowolnym polu, nie staraj się teraz tworzyć, algorytmu "myślenia" analizującego planszę.
##
##Gdy uda Ci się skończyć zadanie, nagraj krótki film z rozgrywką, wrzuć go (najlepiej na YT).
##
##Potem zrób wpis na ⁠p-101-egzamin.
##
##Wpis ma zawierać 4 elementy:
##
##1. Napisz co sprawiło Ci największy problem i jak udało Ci się z tym poradzić
##2. Daj link do nagrania rozgrywki
##3. Daj link do repozytorium z kodem (publicznie dostępne).
##4. Jeśli do rozwiązania były Ci potrzebne inne materiały niż książka, wrzuć linki.
##
##Na tym, etapie, to ja zatwierdzam odpowiedzi. Zdany egzamin, umożliwi Ci przejście na kolejny poziom.
##
##Jeśli masz z czymś problem, czegoś nie rozumiesz, po prostu napisz w tym poście. 

import random

def computer_choice():
    """Return computer choice whwre on board 3x3 must be 'O'"""
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    return y, x

def ask_to_user():
    """Return position from user"""
    x = int(input("Choice x: "))
    y = int(input("Choice y: "))
    return x, y
                

def beautiful_board(board):
    """Print in 3 lines board with 'O', 'X',' ' """
    print(f"{' ' * 5}x:0, x:1, x:2")
    for i in range(len(board)):
        print(f"y:{i} {board_3x3[i]}")
    print("")

def board_in_string(board):
    """Return board in string """
    board_in_string = ""
    for i in range(len(board)):
        for j in range(len(board)):
            board_in_string = board_in_string + board_3x3[i][j]

    return board_in_string

def board_in_slicing(board):
    """Return row column and athwart in string what is in board"""
    string_board = board_in_string(board)
    #row
    row1, row2, row3 = string_board[0:3], string_board[3:6], string_board[6:]
    #column
    column1 = string_board[0] + string_board[3] + string_board[6]
    column2 = string_board[1] + string_board[4] + string_board[7]
    column3 = string_board[2] + string_board[5] + string_board[8]
    #athwart
    athwart1 = string_board[0] + string_board[4] + string_board[8]
    athwart2 = string_board[2] + string_board[4] + string_board[6]

    return row1, row2, row3, column1, column2, column3, athwart1, athwart2

def winner(board):
    """Return who win"""
    row_column_athwart = board_in_slicing(board)
    if "XXX" in row_column_athwart:
        return "USER"
    elif "OOO" in row_column_athwart:
        return "computer"
    
    
    
board_3x3 = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
    ]

print("""You play in O and X board 3 x 3 Goodluck! \n
      #1 You insert: 'X'
      #2 Computer insert 'O'
      #3 You insert 'X' only in an empty pleace
      #4 You insert 'X' by choice x and y (x, y), on board 3X3\n""")

round = 0
while True:
    if  (" " not in board_3x3[0] and " " not in board_3x3[1] and " " not in board_3x3[2]) or (winner(board_3x3) in ("USER", "computer")):
        break
    else:
        if round % 2 == 0:
            try:
                beautiful_board(board_3x3)
                user_x, user_y = ask_to_user()
                while board_3x3[user_y][user_x] != ' ' :
                    print("You cant do thay")
                    user_x, user_y = ask_to_user()
            except (IndexError, ValueError):
                print("You enter too big number or none, try again")
                user_x, user_y = ask_to_user()
            board_3x3[user_y][user_x] = "X"
        else:
            comp_x, comp_y = computer_choice()
            while board_3x3[comp_x][comp_y] != " ":
                comp_x, comp_y = computer_choice()
            board_3x3[comp_x][comp_y] = "O"
    round = round + 1

print(f"Win {winner(board_3x3)}")


