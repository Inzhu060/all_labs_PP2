import pygame
import random
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions and cell size
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)       # Weight 1 food
YELLOW = (255, 255, 0)  # Weight 2 food
BLUE = (0, 0, 255)      # Weight 3 food
BLACK = (0, 0, 0)

# Create the window and set font
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
font = pygame.font.SysFont(None, 35)

# Snake initial state
snake = [(100, 100), (90, 100), (80, 100)]  # List of segments
snake_dir = (CELL_SIZE, 0)  # Moving right initially

# Game state variables
score = 0
level = 1
speed = 10

# Food dictionary: position, weight, spawn_time
food = {}

# Generate random food with weight (1, 2, or 3) and return info
def generate_food():
    while True:
        pos = (
            random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
            random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        )
        if pos not in snake:
            weight = random.choice([1, 2, 3])
            return {"pos": pos, "weight": weight, "spawn_time": time.time()}

# Draw text on the screen
def drawing_text(text, pos, color=WHITE):
    label = font.render(text, True, color)
    screen.blit(label, pos)

# Show the Game Over screen
def game_over():
    screen.fill(BLACK)
    drawing_text("Game Over!", (WIDTH // 2 - 80, HEIGHT // 2 - 60))
    drawing_text(f"Final Score: {score}", (WIDTH // 2 - 100, HEIGHT // 2 - 20))
    drawing_text(f"Level: {level}", (WIDTH // 2 - 100, HEIGHT // 2 + 20))
    drawing_text("Press R to restart or Q to quit", (WIDTH // 2 - 170, HEIGHT // 2 + 60))
    pygame.display.flip()

    # Wait for key press
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
                    main()

# Main game function
def main():
    global snake, snake_dir, score, level, speed, food

    # Reset state on restart
    snake = [(100, 100), (90, 100), (80, 100)]
    snake_dir = (CELL_SIZE, 0)
    score = 0
    level = 1
    speed = 10
    food = generate_food()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
            snake_dir = (-CELL_SIZE, 0)
        elif keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
            snake_dir = (CELL_SIZE, 0)
        elif keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
            snake_dir = (0, -CELL_SIZE)
        elif keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
            snake_dir = (0, CELL_SIZE)

        # Move the snake
        head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
        snake.insert(0, head)

        # Check for wall or self collision
        if (head in snake[1:] or head[0] < 0 or head[1] < 0 or
                head[0] >= WIDTH or head[1] >= HEIGHT):
            game_over()
            return

        # Check if snake eats food
        if head == food["pos"]:
            score += food["weight"]
            # Level up every 4 points
            if score % 4 == 0:
                level += 1
                speed = int(speed * 1.1)
            food = generate_food()  # generate new food
        else:
            snake.pop()  # remove tail if not eating

        # Check if food expired (after 5 seconds)
        if time.time() - food["spawn_time"] > 5:
            food = generate_food()

        # Draw everything
        screen.fill(BLACK)

        # Draw the snake
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

        # Draw food based on weight
        food_color = RED if food["weight"] == 1 else YELLOW if food["weight"] == 2 else BLUE
        pygame.draw.rect(screen, food_color, (*food["pos"], CELL_SIZE, CELL_SIZE))

        # Draw score and level
        drawing_text(f"Score: {score}", (10, 10))
        drawing_text(f"Level: {level}", (10, 40))

        pygame.display.flip()
        clock.tick(speed)

# Start the game
main()
pygame.quit()