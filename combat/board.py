from config import *


def create_board(board):

    def block_pos(pos):
        x = pos[0] * BLOCK_WIDTH + (1280 - BLOCK_WIDTH * 14) / 2
        y = 250 - pos[1] * BLOCK_HEIGHT
        return x, y

    field = open(board, 'r')
    wall_list = []
    not_wall_list = []
    y = -20

    for line in field:
        x = -42.0
        for block in line:
            if block == '1':
                wall_list.append(block_pos((x, y)))
            elif block == '0':
                not_wall_list.append((x, y))
            x += 1
        y += 1
    return wall_list
