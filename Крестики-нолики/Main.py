import pygame
import sys
import random

# Константы
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_SIZE = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")
screen.fill(WHITE)

# Игровая доска
board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

def draw_lines():
    # Вертикальные линии
    pygame.draw.line(screen, BLACK, (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (WIDTH * 2 / 3, 0), (WIDTH * 2 / 3, HEIGHT), LINE_WIDTH)
    # Горизонтальные линии
    pygame.draw.line(screen, BLACK, (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, HEIGHT * 2 / 3), (WIDTH, HEIGHT * 2 / 3), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(screen, RED, (col * WIDTH // BOARD_SIZE + SPACE, row * HEIGHT // BOARD_SIZE + HEIGHT // BOARD_SIZE - SPACE),
                                 (col * WIDTH // BOARD_SIZE + WIDTH // BOARD_SIZE - SPACE, row * HEIGHT // BOARD_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, RED, (col * WIDTH // BOARD_SIZE + SPACE, row * HEIGHT // BOARD_SIZE + SPACE),
                                 (col * WIDTH // BOARD_SIZE + WIDTH // BOARD_SIZE - SPACE, row * HEIGHT // BOARD_SIZE + HEIGHT // BOARD_SIZE - SPACE), CROSS_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLACK, (col * WIDTH // BOARD_SIZE + WIDTH // (2 * BOARD_SIZE), row * HEIGHT // BOARD_SIZE + HEIGHT // (2 * BOARD_SIZE)), CIRCLE_RADIUS, CIRCLE_WIDTH)

def check_winner(player):
    # Проверка горизонталей и вертикалей
    for i in range(BOARD_SIZE):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(BOARD_SIZE)]):
            return True
    # Проверка диагоналей
    if all([board[i][i] == player for i in range(BOARD_SIZE)]) or all([board[i][BOARD_SIZE - i - 1] == player for i in range(BOARD_SIZE)]):
        return True
    return False

def computer_move():
    empty_cells = [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if board[r][c] is None]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 'O'
        if check_winner('O'):
            print("Компьютер выиграл!")
            pygame.quit()
            sys.exit()

def main():
    draw_lines()
    player_turn = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = mouseY // (HEIGHT // BOARD_SIZE)
                clicked_col = mouseX // (WIDTH // BOARD_SIZE)

                if board[clicked_row][clicked_col] is None:
                    board[clicked_row][clicked_col] = 'X'
                    if check_winner('X'):
                        print("Вы выиграли!")
                        pygame.quit()
                        sys.exit()
                    player_turn = False

                    computer_move()
                    player_turn = True

        draw_figures()
        pygame.display.update()

if __name__ == "__main__":
    main()
