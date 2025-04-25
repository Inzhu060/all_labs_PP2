import pygame
import random
import sys
import psycopg2
from datetime import datetime

# Initialize Pygame
pygame.init()

# Screen and game constants
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Database setup functions
def get_or_create_user(name):
    conn = psycopg2.connect(dbname='lab10', user='postgres', password='Sql1234', host='localhost', port='5432')
    cur = conn.cursor()
    cur.execute("SELECT id FROM game_user WHERE username = %s", (name,))
    user = cur.fetchone()
    if not user:
        cur.execute("INSERT INTO game_user (username) VALUES (%s) RETURNING id", (name,))
        user_id = cur.fetchone()[0]
        conn.commit()
    else:
        user_id = user[0]
    cur.close()
    conn.close()
    return user_id

def save_game(user_id, score, level):
    conn = psycopg2.connect(dbname='lab10', user='postgres', password='Sql1234', host='localhost', port='5432')
    cur = conn.cursor()
    cur.execute("INSERT INTO user_score (user_id, score, level, save_time) VALUES (%s, %s, %s, %s)",
                (user_id, score, level, datetime.now()))
    conn.commit()
    cur.close()
    conn.close()

# Draw text
def drawing_text(text, pos, color=WHITE):
    label = font.render(text, True, color)
    screen.blit(label, pos)

def generate_food():
    while True:
        pos = (
            random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
            random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        )
        if pos not in snake:
            return pos

def game_over(user_id):
    save_game(user_id, score, level)
    screen.fill(BLACK)
    drawing_text("Game Over!", (WIDTH // 2 - 80, HEIGHT // 2 - 60))
    drawing_text(f"Final Score: {score}", (WIDTH // 2 - 100, HEIGHT // 2 - 20))
    drawing_text(f"Level: {level}", (WIDTH // 2 - 100, HEIGHT // 2 + 20))
    drawing_text("Press R to restart or Q to quit", (WIDTH // 2 - 170, HEIGHT // 2 + 60))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    main(user_id)

def main(user_id):
    global snake, snake_dir, score, level, speed, screen, font

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')
    font = pygame.font.SysFont(None, 35)

    snake = [(100, 100), (90, 100), (80, 100)]
    snake_dir = (CELL_SIZE, 0)
    score = 0
    level = 1
    speed = 10
    food_pos = generate_food()
    clock = pygame.time.Clock()
    paused = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game(user_id, score, level)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        save_game(user_id, score, level)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
            snake_dir = (-CELL_SIZE, 0)
        elif keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
            snake_dir = (CELL_SIZE, 0)
        elif keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
            snake_dir = (0, -CELL_SIZE)
        elif keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
            snake_dir = (0, CELL_SIZE)

        if not paused:
            head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
            snake.insert(0, head)
            if head in snake[1:] or head[0] < 0 or head[1] < 0 or head[0] >= WIDTH or head[1] >= HEIGHT:
                game_over(user_id)
                return

            if head == food_pos:
                score += 1
                food_pos = generate_food()
                if score % 4 == 0:
                    level += 1
                    speed = int(speed * 1.1)
            else:
                snake.pop()

            screen.fill(BLACK)
            for segment in snake:
                pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, RED, (*food_pos, CELL_SIZE, CELL_SIZE))

            drawing_text(f"Score: {score}", (10, 10))
            drawing_text(f"Level: {level}", (10, 40))

            pygame.display.flip()
            clock.tick(speed)

# Entry point
player_name = input("Enter your name: ")
user_id = get_or_create_user(player_name)
main(user_id)
pygame.quit()