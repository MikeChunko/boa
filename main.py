# Test pygame program
import pygame as pyg
import random


# Returns x, y coords of food
def gen_food(snake, size_x, size_y, screen_x, screen_y):
    # Generate new coords until one doesn't cause a collision
    while True:
        x, y = (
            random.randrange(size_x, screen_x - size_x, 10),
            random.randrange(size_y, screen_y - size_y, 10),
        )
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
snake = [(screen_x // 2, screen_y // 2), 
         (screen_x // 2, screen_y // 2 - size_y),
         (screen_x // 2, screen_y // 2 - (2 * size_y))]

food_x, food_y = gen_food(snake, size_x, size_y, screen_x, screen_y)
eaten = False
score = 0
gameover = False

# Main loop
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
    if new_x == food_x and new_y == food_y:  # Food
        eaten = True
    elif new_x == 0 or new_x == screen_x - size_x or new_y == 0 or new_y == screen_y - size_y:  # Border
        gameover = True
    if d_x != 0 or d_y != 0:
        for x, y in snake:  # Snake
            if new_x == x and new_y == y:
                gameover = True

    snake.append((new_x, new_y))

    # Food is eaten
    if eaten:
        food_x, food_y = gen_food(snake, size_x, size_y, screen_x, screen_y)
        eaten = False
        score += 10
    else:
        snake.pop(0)

    # Draw
    screen.fill((0, 0, 0))
    for x, y in snake:
        pyg.draw.rect(screen, green, [x, y, size_x, size_y])
    pyg.draw.rect(screen, red, [food_x, food_y, size_x, size_y])

    for i in range(0, screen_x, 10):  # Border
        pyg.draw.rect(screen, blue, [i, 0, size_x, size_y])
        pyg.draw.rect(screen, blue, [i, screen_y - size_y, size_x, size_y])
        pyg.draw.rect(screen, blue, [0, i, size_x, size_x])
        pyg.draw.rect(screen, blue, [screen_x - size_x, i, size_x, size_y])

    textsurface = font.render("Score: {}".format(score), False, (255, 255, 255))
    screen.blit(textsurface, (0, 0))

    pyg.display.update()
    clock.tick(15)

# Game over state
while True:

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            quit()

    screen.fill((0, 0, 0))
    for x, y in snake:
        pyg.draw.rect(screen, green, [x, y, size_x, size_y])
    pyg.draw.rect(screen, red, [food_x, food_y, size_x, size_y])

    for i in range(0, screen_x, 10):  # Border
        pyg.draw.rect(screen, blue, [i, 0, size_x, size_y])
        pyg.draw.rect(screen, blue, [i, screen_y - size_y, size_x, size_y])
        pyg.draw.rect(screen, blue, [0, i, size_x, size_x])
        pyg.draw.rect(screen, blue, [screen_x - size_x, i, size_x, size_y])

    textsurface = font.render(
        "Game Over! Score: {}".format(score), False, (255, 255, 255)
    )
    screen.blit(textsurface, (screen_x // 2 - 40, screen_y // 2))

    pyg.display.update()
    clock.tick(15)
