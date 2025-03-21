import pygame

pygame.init()

window = (800, 600)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Drawing circle")
ball = pygame.Color("red")
background = pygame.Color("white")
radius = 25
ball_pos = [400, 300]
speed = 20
 
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_pos[1] = max(ball_pos[1] - speed, radius)
    if keys[pygame.K_DOWN]:
        ball_pos[1] = min(ball_pos[1] + speed, window[1] - radius)
    if keys[pygame.K_LEFT]:
        ball_pos[0] = max(ball_pos[0] - speed, radius)
    if keys[pygame.K_RIGHT]:
        ball_pos[0] = min(ball_pos[0] + speed, window[0] - radius) 

    screen.fill(background)
    pygame.draw.circle(screen, ball, ball_pos, radius)
    pygame.display.flip()
    pygame.time.Clock().tick(60)