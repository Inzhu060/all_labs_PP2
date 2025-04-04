import pygame
import sys

pygame.init()

# Set up FPS and clock
clock = pygame.time.Clock()
FPS = 100

# Window size and color definitions
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paint')
screen.fill(WHITE)

# Default color and shape mode
current_color = BLACK
brush = 5
shape_mode = 'brush'

# Draw the color palette at the top
def color_palette():
    colors = [BLACK, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)]
    for i, color in enumerate(colors):
        pygame.draw.rect(screen, color, (10 + i * 40, 10, 30, 30))

running = True
start_pos = None  # Will store the starting mouse position

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle mouse button down
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # If clicking on the palette
            if y <= 40:
                color_index = (x - 10) // 40
                if 0 <= color_index < 7:
                    current_color = [BLACK, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)][color_index]
            else:
                start_pos = event.pos  # Store the start position for shape drawing

        # Handle mouse button release — draw the selected shape
        elif event.type == pygame.MOUSEBUTTONUP and start_pos:
            end_pos = event.pos
            x1, y1 = start_pos
            x2, y2 = end_pos

            if shape_mode == 'rectangle':
                # Draw a rectangle between two points
                pygame.draw.rect(screen, current_color, (min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), 2)

            elif shape_mode == 'circle':
                # Draw a circle with radius based on distance between points
                radius = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5 / 2)
                center = ((x1 + x2) // 2, (y1 + y2) // 2)
                pygame.draw.circle(screen, current_color, center, radius, 2)

            elif shape_mode == 'square':
                # Draw a square with side equal to the smallest distance
                side = min(abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(screen, current_color, (x1, y1, side, side), 2)

            elif shape_mode == 'right_triangle':
                # Draw a right triangle using start and end positions
                points = [start_pos, (x1, y2), end_pos]
                pygame.draw.polygon(screen, current_color, points, 2)

            elif shape_mode == 'equilateral_triangle':
                # Draw an equilateral triangle with horizontal base
                side = abs(x2 - x1)
                height = (3**0.5 / 2) * side
                direction = -1 if y2 < y1 else 1
                points = [
                    ((x1 + x2) // 2, y1),
                    (x1, y1 + int(direction * height)),
                    (x2, y1 + int(direction * height))
                ]
                pygame.draw.polygon(screen, current_color, points, 2)

            elif shape_mode == 'rhombus':
                # Draw a rhombus centered between start and end positions
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                dx = abs(x2 - x1) // 2
                dy = abs(y2 - y1) // 2
                points = [
                    (center_x, y1),        # top
                    (x2, center_y),        # right
                    (center_x, y2),        # bottom
                    (x1, center_y)         # left
                ]
                pygame.draw.polygon(screen, current_color, points, 2)

            start_pos = None  # Reset the start position

        # Handle key presses for mode switching
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                shape_mode = 'rectangle'
            elif event.key == pygame.K_c:
                shape_mode = 'circle'
            elif event.key == pygame.K_b:
                shape_mode = 'brush'
            elif event.key == pygame.K_e:
                shape_mode = 'eraser'
            elif event.key == pygame.K_s:
                shape_mode = 'square'
            elif event.key == pygame.K_t:
                shape_mode = 'right_triangle'
            elif event.key == pygame.K_q:
                shape_mode = 'equilateral_triangle'
            elif event.key == pygame.K_h:
                shape_mode = 'rhombus'

    # Brush or eraser drawing while holding mouse button
    if pygame.mouse.get_pressed()[0] and start_pos and shape_mode in ['brush', 'eraser']:
        pos = pygame.mouse.get_pos()
        color = WHITE if shape_mode == 'eraser' else current_color
        pygame.draw.circle(screen, color, pos, brush)

    # Draw color palette and update screen
    color_palette()
    pygame.display.flip()
    clock.tick(FPS)
