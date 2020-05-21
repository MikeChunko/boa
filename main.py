# Test pygame program
import pygame as pyg


pyg.init()
screen = pyg.display.set_mode((500, 500))
pyg.display.update()
pyg.display.set_caption("Boa")

# Aliases
red, green, blue = (255, 0, 0), (0, 255, 0), (0, 0, 255)
delta_x = delta_y = 10

# List containing all segments of the snake
snake = [(250, 250)]

# Main loop
running = True
while running:

    # Close button clicked
    for event in pyg.event.get():
        print(event)
        if event.type == pyg.QUIT:
            running = False

    # Draw
    for x, y in snake:
        pyg.draw.rect(screen, green, [x, y, delta_x, delta_y])

    pyg.display.update()

pyg.quit()
quit()
