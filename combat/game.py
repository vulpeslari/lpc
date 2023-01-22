import math
import pygame
import sys
from config import *
from board import create_board


def game_start():
    pygame.init()

    # screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("TANK PONG")

    # score text
    score_font = pygame.font.Font("PressStart2P.ttf", 44)
    score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_RED)
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (380, 50)

    # victory text
    victory_font = pygame.font.Font("PressStart2P.ttf", 100)
    victory_text = victory_font.render('YOU LOSE', True, COLOR_WHITE, COLOR_RED)
    victory_text_rect = score_text.get_rect()
    victory_text_rect.center = (450, 300)

    # sound effects
    bounce_sound_effect = pygame.mixer.Sound('bounce.wav')
    scoring_sound_effect = pygame.mixer.Sound('scoring.wav')

    pygame.mouse.set_visible(False)

    # game loop
    game_loop = True
    game_clock = pygame.time.Clock()

    # blocks
    put_block = pygame.image.load("block.png")
    blocks = create_board('boards/board' + sys.argv[1] + ".txt")

    while game_loop:

        # check game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False

        # drawing objects
        screen.blit(score_text, score_text_rect)

        for i in range(len(blocks)):
            for block in blocks[i]:
                screen.blit(put_block, block)

        # update screen
        pygame.display.flip()
        game_clock.tick(fps)

    pygame.quit()
