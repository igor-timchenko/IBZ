import pygame
import random
import sys

# Настройки
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 10  # Размер сетки (10x10)
CELL_SIZE = WIDTH // GRID_SIZE
NUM_MINES = 15

# Цвета
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Сапер")

# Класс для ячейки
class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.neighboring_mines = 0

# Создание игрового поля
def create_board():
    board = [[Cell() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    mines_placed = 0

    while mines_placed < NUM_MINES:
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        if not board[y][x].is_mine:
            board[y][x].is_mine = True
            mines_placed += 1

    # Подсчет соседних мин
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if board[y][x].is_mine:
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if 0 <= x + dx < GRID_SIZE and 0 <= y + dy < GRID_SIZE:
                            board[y + dy][x + dx].neighboring_mines += 1

    return board

# Рисование поля
def draw_board(board):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            cell = board[y][x]
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if cell.is_revealed:
                if cell.is_mine:
                    pygame.draw.rect(screen, RED, rect)
                else:
                    pygame.draw.rect(screen, WHITE, rect)
                    if cell.neighboring_mines > 0:
                        font = pygame.font.Font(None, 36)
                        text = font.render(str(cell.neighboring_mines), True, BLACK)
                        screen.blit(text, (x * CELL_SIZE + CELL_SIZE // 4, y * CELL_SIZE + CELL_SIZE // 4))
            else:
                pygame.draw.rect(screen, GRAY, rect)

            pygame.draw.rect(screen, BLACK, rect, 1)

# Открытие ячейки
def reveal_cell(board, x, y):
    if board[y][x].is_revealed:
        return
    board[y][x].is_revealed = True

    if board[y][x].neighboring_mines == 0 and not board[y][x].is_mine:
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if 0 <= x + dx < GRID_SIZE and 0 <= y + dy < GRID_SIZE:
                    reveal_cell(board, x + dx, y + dy)

# Основная игра
def main():
    board = create_board()
    
    while True:
        screen.fill(BLACK)
        draw_board(board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                col = mouse_x // CELL_SIZE
                row = mouse_y // CELL_SIZE

                if not board[row][col].is_revealed:
                    reveal_cell(board, col, row)

                    # Если открыта мина — игра окончена
                    if board[row][col].is_mine:
                        print("Game Over!")
                        pygame.quit()
                        sys.exit()

        pygame.display.flip()

if __name__ == "__main__":
    main()
