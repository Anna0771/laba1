import pygame  # импортируем библиотеку для создания игры

TILE = 40  # размер квадрата на экране

# Загружаем картинки и масштабируем под размер тайла
pygame.init()
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (TILE, TILE + 10))

wall_img = pygame.image.load("wall.png")
wall_img = pygame.transform.scale(wall_img, (TILE, TILE))

start_img = pygame.image.load("start.png")
start_img = pygame.transform.scale(start_img, (TILE, TILE))

exit_img = pygame.image.load("exit.png")
exit_img = pygame.transform.scale(exit_img, (TILE, TILE))

coin_img = pygame.image.load("coin.png")
coin_img = pygame.transform.scale(coin_img, (TILE, TILE))

with open("map.txt", encoding="utf-8") as f:
    game_map = f.readlines()

# Размер окна по карте
width = len(game_map[0]) * TILE
height = len(game_map) * TILE

screen = pygame.display.set_mode((width, height))

# Позиция игрока
for y, row in enumerate(game_map):
    if "S" in row:
        player_x = row.index("S")
        player_y = y
        break

running = True  # игра работает


# Игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            new_x, new_y = player_x, player_y
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_w:
                new_y -= 1
            elif event.key == pygame.K_s:
                new_y += 1
            elif event.key == pygame.K_a:
                new_x -= 1
            elif event.key == pygame.K_d:
                new_x += 1

            if 0 <= new_x < len(game_map[0]) and 0 <= new_y < len(game_map):
                tile = game_map[new_y][new_x]
                if tile != "1":
                    player_x, player_y = new_x, new_y
                if tile == "C":
                    game_map[new_y] = (
                        game_map[new_y][:new_x]
                        + " "
                        + game_map[new_y][new_x + 1:]
                    )
                if tile == "E":
                    running = False

    # Отрисовка каждый кадр
    screen.fill((0, 0, 0))

    for y, row in enumerate(game_map):
        for x, tile in enumerate(row):
            if tile == "1":  # стена
                screen.blit(wall_img, (x * TILE, y * TILE))
            elif tile == "S":  # вход
                screen.blit(start_img, (x * TILE, y * TILE))
            elif tile == "E":  # выход
                screen.blit(exit_img, (x * TILE, y * TILE))
            elif tile == "C":  # предмет
                screen.blit(coin_img, (x * TILE, y * TILE))

    # игрок
    screen.blit(player_img, (player_x * TILE, player_y * TILE - 12))

    pygame.display.flip()  # обновляем экран
