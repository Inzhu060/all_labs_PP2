import pygame
import sys

pygame.init()

clock = pygame.time.Clock()
FPS = 100

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paint')
screen.fill(WHITE)

current_color = BLACK
brush = 5
shape_mode = 'brush'

def color_palette():
    colors = [BLACK, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)]
    for i, color in enumerate(colors):
        pygame.draw.rect(screen, color, (10 + i * 40, 10, 30, 30))

running = True
start_pos = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if y <= 40:
                color_index = (x - 10) // 40
                if 0 <= color_index < 7:
                    current_color = [BLACK,  (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)][color_index]
            else:
                start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP and start_pos:
            end_pos = event.pos
            if shape_mode == 'rectangle':
                rect_width = abs(end_pos[0] - start_pos[0])
                rect_height = abs(end_pos[1] - start_pos[1])
                pygame.draw.rect(screen, current_color, (min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]), rect_width, rect_height), 2)
            elif shape_mode == 'circle':
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5 / 2)
                center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                pygame.draw.circle(screen, current_color, center, radius, 2)
            start_pos = None
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                shape_mode = 'rectangle'
            elif event.key == pygame.K_c:
                shape_mode = 'circle'
            elif event.key == pygame.K_b:
                shape_mode = 'brush'
            elif event.key == pygame.K_e:
                shape_mode = 'eraser'

    if pygame.mouse.get_pressed()[0] and start_pos and shape_mode in ['brush', 'eraser']:
        pos = pygame.mouse.get_pos()
        color = WHITE if shape_mode == 'eraser' else current_color
        pygame.draw.circle(screen, color, pos, brush)

    color_palette()
    pygame.display.flip()
    clock.tick(FPS)