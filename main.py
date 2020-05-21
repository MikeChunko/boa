# Test pygame program
import pygame as pyg


pyg.init()
screen = pyg.display.set_mode((500, 500))
pyg.display.update()
pyg.display.set_caption("Boa")
clock = pyg.time.Clock()

red, green, blue = (255, 0, 0), (0, 255, 0), (0, 0, 255)
size_x = size_y = 10
delta_x, delta_y = 0, -size_y

# List containing all segments of the snake
snake = [(250, 250), (250, 260), (250, 270)]

# Main loop
running = True
while running:

    # Handle actions
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_LEFT or event.key == pyg.K_a:
                delta_x, delta_y = -size_x, 0
            elif event.key == pyg.K_RIGHT or event.key == pyg.K_d:
                delta_x, delta_y = size_x, 0
            elif event.key == pyg.K_UP or event.key == pyg.K_w:
                delta_x, delta_y = 0, -size_y
            elif event.key == pyg.K_DOWN or event.key == pyg.K_s:
                delta_x, delta_y = 0, size_y

    # Add new segment, remove old
    x, y = snake[len(snake) - 1]
    snake.append((x + delta_x, y + delta_y))
    snake.pop(0)

    # Draw
    screen.fill((0, 0, 0))
    for x, y in snake:
        pyg.draw.rect(screen, green, [x, y, size_x, size_y])

    pyg.display.update()
    clock.tick(30)

pyg.quit()
quit()
