# Test pygame program
import pygame as pyg
import random


# Returns x, y coords of food
def gen_food(snake, size_x, size_y):
    # Generate new coords until one doesn't cause a collision
    while True:
        x, y = (
            random.randint(1, (size_x - 1) // 10),
            random.randint(1, (size_y - 1) // 10),
        )
        x, y = 10 * x, 10 * y
        sentinel = True
        for old_x, old_y in snake:
            if sentinel and (old_x == x and old_y == y):
                sentinel = False
        if sentinel:
            break
    return x, y


pyg.init()
pyg.font.init()
font = pyg.font.SysFont("Arial", 10)
screen_x = screen_y = 300
screen = pyg.display.set_mode((screen_x, screen_y))
pyg.display.update()
pyg.display.set_caption("Boa")
clock = pyg.time.Clock()

red, green, blue = (200, 0, 0), (0, 200, 0), (0, 0, 200)
size_x = size_y = 10
d_x, d_y = 0, -size_y

# List containing all segments of the snake
snake = [(250, 250), (250, 260), (250, 270)]
food_x, food_y = gen_food(snake, screen_x, screen_y)
eaten = False
score = 0

# Main loop
gameover = False
while not gameover:

    # Handle actions
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            quit()
        # Movement keys
        if event.type == pyg.KEYDOWN:
            if (event.key == pyg.K_LEFT or event.key == pyg.K_a) and d_x <= 0:
                d_x, d_y = -size_x, 0
            elif (event.key == pyg.K_RIGHT or event.key == pyg.K_d) and d_x >= 0:
                d_x, d_y = size_x, 0
            elif (event.key == pyg.K_UP or event.key == pyg.K_w) and d_y <= 0:
                d_x, d_y = 0, -size_y
            elif (event.key == pyg.K_DOWN or event.key == pyg.K_s) and d_y >= 0:
                d_x, d_y = 0, size_y

    # New segment position
    x, y = snake[len(snake) - 1]
    new_x, new_y = x + d_x, y + d_y

    # Check collisions
    if new_x == food_x and new_y == food_y:
        eaten = True

    snake.append((new_x, new_y))

    # Food is eaten
    if eaten:
        food_x, food_y = gen_food(snake, screen_x, screen_y)
        eaten = False
        score += 10
    else:
        snake.pop(0)

    # Draw
    screen.fill((0, 0, 0))
    for x, y in snake:
        pyg.draw.rect(screen, green, [x, y, size_x, size_y])
    pyg.draw.rect(screen, red, [food_x, food_y, size_x, size_y])

    textsurface = font.render("Score: {}".format(score), False, (255, 255, 255))
    screen.blit(textsurface, (0, 0))

    pyg.display.update()
    clock.tick(15)

while True:

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            quit()

    screen.fill((0, 0, 0))
    for x, y in snake:
        pyg.draw.rect(screen, green, [x, y, size_x, size_y])
    pyg.draw.rect(screen, red, [food_x, food_y, size_x, size_y])
    textsurface = font.render(
        "Game Over! Score: {}".format(score), False, (255, 255, 255)
    )
    screen.blit(textsurface, (screen_x // 2 - 40, screen_y // 2))
    pyg.display.update()
