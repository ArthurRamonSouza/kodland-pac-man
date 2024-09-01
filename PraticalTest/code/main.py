import pygame
import sys
from pacman import start_game

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 900
HEIGHT = 950

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
FONT = pygame.font.SysFont(None, 55)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Menu")

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_s:
                   start_game();
                if event.key == pygame.K_i:
                    show_instructions()

        screen.fill(BLACK)

        draw_text('Pac-Man Game', FONT, WHITE, screen, WIDTH // 2, HEIGHT // 4)
        draw_text('Press S to Start', FONT, RED, screen, WIDTH // 2, HEIGHT // 2)
        draw_text('Press I for Instructions', FONT, RED, screen, WIDTH // 2, HEIGHT // 2 + 60)
        draw_text('Press Q to Quit', FONT, RED, screen, WIDTH // 2, HEIGHT // 2 + 120)

        pygame.display.flip()

def show_instructions():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return

        screen.fill(BLACK)

        draw_text('Instructions', FONT, WHITE, screen, WIDTH // 2, HEIGHT // 4)
        draw_text('Use arrow keys to move Pac-Man', FONT, WHITE, screen, WIDTH // 2, HEIGHT // 2)
        draw_text('Avoid ghosts and eat pellets', FONT, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 60)
        draw_text('Press Q to quit the game', FONT, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 120)
        draw_text('Press B to go back', FONT, RED, screen, WIDTH // 2, HEIGHT // 2 + 180)

        pygame.display.flip()

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        screen.fill(BLACK)
        draw_text('Game is running... Press Q to quit.', FONT, WHITE, screen, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()

if __name__ == '__main__':
    main_menu()