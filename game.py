import pygame  # импортируем библиотеку для создания игры
   # импортируем библиотеку для выхода из программы
   
TILE = 40  # размер квадрата на экране

# Загружаем картинки и масштабируем под размер тайла
pygame.init()
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (TILE, TILE+10))

wall_img = pygame.image.load("wall.png")
wall_img = pygame.transform.scale(wall_img, (TILE, TILE))

start_img = pygame.image.load("start.png")
start_img = pygame.transform.scale(start_img, (TILE, TILE))

exit_img = pygame.image.load("exit.png")
exit_img = pygame.transform.scale(exit_img, (TILE, TILE))

coin_img = pygame.image.load("coin.png")
coin_img = pygame.transform.scale(coin_img, (TILE, TILE))

with open ('map.txt') as f:
    map = f.readlines()

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
        if eventt.type == pygame.QUIT:
            running = False

        if eventt.type == pygame.KEYDOWN:
            new_x, new_y = player_x, player_y
            if eventt.key == pygame.K_ESCAPE:
                running = False
            elif eventt.key == pygame.K_w:
                new_y -= 1
            elif eventt.key == pygame.K_s:
                new_y += 1
            elif eventt.key == pygame.K_a:
                new_x -= 1
            elif eventt.key == pygame.K_d:
                new_x += 1

            if 0 <= new_x < len(map[0]) and 0 <= new_y < len(map):
                tile = map[new_y][new_x]
                if tile != '1':
                    player_x, player_y = new_x, new_y
                if tile == 'C':
                    map[new_y] = map[new_y][:new_x] + ' ' + map[new_y][new_x+1:]
                if tile == 'E':
                    running = False

    # ==== ОТРИСОВКА КАЖДЫЙ КАДР ====
    screen.fill((0, 0, 0))

    for y, row in enumerate(map):
        for x, tile in enumerate(row):
            if tile == '1':      # стена
                screen.blit(wall_img, (x * TILE, y * TILE))
            elif tile == 'S':    # вход
                screen.blit(start_img, (x * TILE, y * TILE))
            elif tile == 'E':    # выходd
                screen.blit(exit_img, (x * TILE, y * TILE))
            elif tile == 'C':    # предмет
                screen.blit(coin_img, (x * TILE, y * TILE))

    # игрок
    screen.blit(player_img, (player_x * TILE, -12 + player_y * TILE))

    pygame.display.flip()   # обновляем экран


