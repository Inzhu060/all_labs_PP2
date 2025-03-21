import pygame
import time 
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Clock")

left_arm = pygame.image.load("images/leftarm.png")
right_arm = pygame.image.load("images/rightarm.png")
m_clock = pygame.image.load("images/clock.png")
clock_face = pygame.transform.scale(m_clock, (WIDTH, HEIGHT))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
    
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec

    minute_angle = minute * 6 + (second / 60) * 6
    second_angle = second * 6

    screen.blit(clock_face, (0, 0))

    rotated_r = pygame.transform.rotate(pygame.transform.scale(right_arm, (800, 640)), -minute_angle)
    right_arm_rect = rotated_r.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 12))
    screen.blit(rotated_r, right_arm_rect)

    rotated_l = pygame.transform.rotate(pygame.transform.scale(left_arm, (40, 640)), -second_angle)
    left_arm_rect = rotated_l.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 10))
    screen.blit(rotated_l, left_arm_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
    