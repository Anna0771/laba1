import pygame  # импортируем библиотеку для создания игры
   # импортируем библиотеку для выхода из программы
   
TILE = 20  # размер квадрата на экране

# Цвета в формате RGB
GREEN = (0, 255, 0)     # Игрок (зелёный)
BLACK = (0, 0, 0)       # Вход (чёрный)
BROWN = (139, 69, 19)   # Выход (коричневый)
YELLOW = (255, 255, 0)  # Предмет (жёлтый)
WHITE = (255, 255, 255) # Фон (белый)
BLUE = (0, 0, 255)      # Стены (синие)

# Простая карта где:
# S - вход
# E - выход
# C - предмет
# 1 - стена
# " " (пробел) - фон (пустое место)
map = [
    "11111111111111111111111111",
    "1  S        1            1",
    "1  S        1 C  1       1",
    "1           111111       1",
    "1    11111111            1",
    "1    1 C                 1",
    "1    11111            E  1",
    "1                     E  1",
    "11111111111111111111111111"
]

# Размер окна по карте
width = len(map[0]) * TILE
height = len(map) * TILE

screen = pygame.display.set_mode((width, height))


# позиция игрока
for y, row in enumerate(map):
    if 'S' in row:
        player_x = row.index('S')
        player_y = y
        break

running = True  # игра работает

while running:
    for eventt in pygame.event.get():  # проверяем все события (нажатия, закрытия)
        if eventt.type == pygame.QUIT:  # если закрыть окно, игра завершается
            running = False

        if eventt.type == pygame.KEYDOWN:  # если нажата клавиша
            new_x, new_y = player_x, player_y  # предполагаемые новые координаты
            if eventt.key == pygame.K_ESCAPE:  # если нажали ESC - выход
                running = False
            elif eventt.key == pygame.K_w:  # W - вверх
                new_y -= 1
            elif eventt.key == pygame.K_s:  # S - вниз
                new_y += 1
            elif eventt.key == pygame.K_a:  # A - влево
                new_x -= 1
            elif eventt.key == pygame.K_d:  # D - вправо
                new_x += 1

            # Проверяем, что новая позиция на карте в пределах и не стена
            if 0 <= new_x < len(map[0]) and 0 <= new_y < len(map):
                tile = map[new_y][new_x]

                if tile != '1':  # если не стена
                    player_x, player_y = new_x, new_y  # двигаем игрока

                if tile == 'C':  # если предмет
                    # Убираем предмет с карты
                    map[new_y] = map[new_y][:new_x] + ' ' + map[new_y][new_x+1:]

                if tile == 'E':  # если выход
                    running = False  # заканчиваем игру

    screen.fill(WHITE)

    # Рисуем карту
    for y, row in enumerate(map):
        for x, tile in enumerate(row):
            rect = pygame.Rect(x*TILE, y*TILE, TILE, TILE)
            if tile == '1':
                pygame.draw.rect(screen, BLUE, rect)    # стена - синий
            elif tile == 'S':
                pygame.draw.rect(screen, BLACK, rect)   # вход - чёрный
            elif tile == 'E':
                pygame.draw.rect(screen, BROWN, rect)   # выход - коричневый
            elif tile == 'C':
                pygame.draw.rect(screen, YELLOW, rect)  # предмет - жёлтый

    # Рисуем игрока зеленым квадратом
    player_rect = pygame.Rect(player_x*TILE, player_y*TILE, TILE, TILE)
    pygame.draw.rect(screen, GREEN, player_rect)

    pygame.display.flip()  # обновляем экран


