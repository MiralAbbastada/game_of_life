# Game of life by Miral Abbastada

import pygame
import sys
import random

# Переменные
CELL_SIZE = 10  # Размер клетки
GRID_WIDTH = 80  # Количество клеток по горизонтали
GRID_HEIGHT = 60  # Количество клеток по вертикали
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 10

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Инициализация pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game of Life by Miral Abbastada")
clock = pygame.time.Clock()

# Генерация сетки
def create_grid(randomize=False):
    """Создает сетку. Если randomize=True, клетки заполняются случайно."""
    return [[random.choice([0, 1]) if randomize else 0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Подсчет живых соседей клетки
def count_neighbors(grid, x, y):
    """Возвращает количество живых соседей для клетки с координатами (x, y)."""
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID_HEIGHT and 0 <= ny < GRID_WIDTH:
            count += grid[nx][ny]
    return count

# Обновление сетки
def update_grid(grid):
    """Обновляет сетку на основе правил игры."""
    new_grid = create_grid()
    for x in range(GRID_HEIGHT):
        for y in range(GRID_WIDTH):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == 1:  # Клетка жива
                new_grid[x][y] = 1 if neighbors == 2 or neighbors == 3 else 0
            else:  # Клетка мертва
                new_grid[x][y] = 1 if neighbors == 3 else 0
    return new_grid

# Переключение состояния клетки
def toggle_cell(grid, pos):
    """Переключает состояние клетки под курсором."""
    x, y = pos[1] // CELL_SIZE, pos[0] // CELL_SIZE  # Преобразуем координаты пикселей в координаты сетки
    if 0 <= x < GRID_HEIGHT and 0 <= y < GRID_WIDTH:
        grid[x][y] = 1 - grid[x][y]  # Меняем состояние клетки

# Отрисовка сетки
def draw_grid(grid):
    """Рисует сетку и клетки."""
    for x in range(GRID_HEIGHT):
        for y in range(GRID_WIDTH):
            rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = GREEN if grid[x][y] == 1 else BLACK
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, WHITE, rect, 1)  # Рамка клетки

# Основной цикл игры
def main():
    grid = create_grid(randomize=False)  # Изначально сетка пуста
    running = True
    paused = True  # Игра начинается на паузе
    drawing = False  # Отслеживает, рисует ли пользователь

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Закрытие окна
                running = False
            elif event.type == pygame.KEYDOWN:  # Обработка клавиш
                if event.key == pygame.K_SPACE:  # Пауза/запуск симуляции
                    paused = not paused
                elif event.key == pygame.K_s:  # Случайное заполнение сетки
                    grid = create_grid(randomize=True)
                elif event.key == pygame.K_r:  # Сброс сетки
                    grid = create_grid(randomize=False)
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Начало рисования
                if event.button == 1:  # ЛКМ
                    drawing = True
                    toggle_cell(grid, pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEMOTION:  # Рисование по драгу
                if drawing:  # Если ЛКМ зажата
                    toggle_cell(grid, pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:  # Завершение рисования
                if event.button == 1:  # ЛКМ
                    drawing = False

        if not paused:  # Обновляем сетку только если симуляция запущена
            grid = update_grid(grid)

        draw_grid(grid)  # Рисуем сетку
        pygame.display.flip()
        clock.tick(FPS)  # Контроль FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
