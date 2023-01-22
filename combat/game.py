import math
import pygame
import sys
from config import *
from board import create_board
from tank import draw_tank


def game_start():
    pygame.init()

    # screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("TANK PONG")

    # score text
    score_font = pygame.font.Font("PressStart2P.ttf", 44)
    score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_RED)
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (600, 50)

    # Font
    font = pygame.font.Font("PressStart2P.ttf", 80)

    # game loop
    game_loop = True
    game_clock = pygame.time.Clock()

    # blocks
    put_block = pygame.image.load("block.png")
    blocks = create_board(board3)

    pygame.mouse.set_visible(False)

    while game_loop:

        # check game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False

        # Drawing the score
        score_format = font.render("{}".format(score1), False, COLOR_GREEN)
        screen.blit(score_format, (325, 10))

        score_format = font.render("{}".format(score2), False, COLOR_BLUE)
        screen.blit(score_format, (925, 10))

        # Drawing the board
        for i in range(len(blocks)):
            for block in blocks:
                screen.blit(put_block, block)

        # Spawn Players
        draw_tank(screen)

        # update screen
        pygame.display.flip()
        game_clock.tick(fps)
        screen.fill(COLOR_RED)

    pygame.quit()
