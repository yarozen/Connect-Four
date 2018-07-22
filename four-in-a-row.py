import os
import sys
import time
import platform
from itertools import cycle


def draw_board(g):
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    print("""
    ║ {} {} {} {} {} {} {} ║
    ║ {} {} {} {} {} {} {} ║
    ║ {} {} {} {} {} {} {} ║
    ║ {} {} {} {} {} {} {} ║
    ║ {} {} {} {} {} {} {} ║
    ║ {} {} {} {} {} {} {} ║
    ╚═══════════════╝
      1 2 3 4 5 6 7 """.format(
        g[1][1], g[2][1], g[3][1], g[4][1], g[5][1], g[6][1], g[7][1],
        g[1][2], g[2][2], g[3][2], g[4][2], g[5][2], g[6][2], g[7][2],
        g[1][3], g[2][3], g[3][3], g[4][3], g[5][3], g[6][3], g[7][3],
        g[1][4], g[2][4], g[3][4], g[4][4], g[5][4], g[6][4], g[7][4],
        g[1][5], g[2][5], g[3][5], g[4][5], g[5][5], g[6][5], g[7][5],
        g[1][6], g[2][6], g[3][6], g[4][6], g[5][6], g[6][6], g[7][6]
    ))


def init_grid():
    grid = {}
    for column in range(1, 8):
        grid[column] = {}
        for cell in range(1, 7):
            grid[column][cell] = empty
    return grid


def get_column(grid, player):
    while True:
        draw_board(grid)
        try:
            user_key = int(input("{}'s turn [1-7]: ".format(player)))
            if user_key in range(1, 8) and grid[user_key][1] == empty:
                return user_key
        except ValueError:
            pass
        except KeyboardInterrupt:
            sys.exit(0)


def player_move(grid, col, player):
    row = None
    for row in range(1, 7):
        try:
            time.sleep(0.1)
            if grid[col][row] == empty:
                grid[col][row] = player
                if row != 1:
                    grid[col][row-1] = empty
                draw_board(grid)
                if row != 6 and grid[col][row + 1] != empty:
                     break
        except KeyboardInterrupt:
            sys.exit(0)
    return col, row


def grid_full(grid):
    for column in range(1, 8):
        if grid[column][1] == empty:
            return False
    return True


def check_4_in_a_row(g, p, x, y):
    # check for horizontal win: -
    s = 1
    # move left
    t = x
    while t != 1 and g[t - 1][y] == p:
            s += 1
            t -= 1
    # move right
    t = x
    while t != 7 and g[t + 1][y] == p:
            s += 1
            t += 1
    # check win
    if s >= 4:
        return p

    # check for vertical win: |
    s = 1
    # move up
    t = y
    while t != 1 and g[x][t - 1] == p:
        s += 1
        t -= 1
    # move down
    t = y
    while t != 6 and g[x][t + 1] == p:
        s += 1
        t += 1
    # check win
    if s >= 4:
        return p

    # check for diagonal win: \
    s = 1
    tx = x
    ty = y
    # move left & up
    while (tx != 1 and ty != 1) and g[tx - 1][ty - 1] == p:
        s += 1
        tx -= 1
        ty -= 1
    # move right & down
    tx = x
    ty = y
    while (tx != 7 and ty != 6) and g[tx + 1][ty + 1] == p:
        s += 1
        tx += 1
        ty += 1
    # check win
    if s >= 4:
        return p

    # check for diagonal win: /
    s = 1
    tx = x
    ty = y
    # move left & down
    while (tx != 1 and ty != 6) and g[tx - 1][ty + 1] == p:
        s += 1
        tx -= 1
        ty += 1
    # move right & up
    tx = x
    ty = y
    while (tx != 7 and ty != 1) and g[tx + 1][ty - 1] == p:
        s += 1
        tx += 1
        ty -= 1
    # check win
    if s >= 4:
        return p


players = ['○', '●']
empty = '.'
grid = init_grid()
turn = cycle(range(2))
winner = None
while not grid_full(grid) and not winner:
    player = players[next(turn)]
    col = get_column(grid, player)
    x, y = player_move(grid, col, player)
    winner = check_4_in_a_row(grid, player, x, y)
if not winner:
    print("Grid full with no winner")
else:
    print("{} is the Winner!".format(winner))
