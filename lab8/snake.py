import pygame
import random
import sys

#Initialize Pygame
pygame.init()

#Screen dimensions and cell size
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20

#Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#Create the game window and set the font
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
font = pygame.font.SysFont(None, 35)

#Snake initial state: position and direction
snake = [(100, 100), (90, 100), (80, 100)] #list of segments
snake_dir = (CELL_SIZE,0) #moving right initially

#score, level, and speed
score = 0
level = 1
speed = 10

#Generate food in a random position, not on the snake
def generate_food():
    while True:
        pos = (
            random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
            random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        )
        if pos not in snake:
            return pos
        
#draw text onthe screen
def drawing_text(text, pos, color = WHITE):
    label = font.render(text, True, color)
    screen.blit(label, pos)

# Show the Game Over screen with score and options
def game_over():
    screen.fill(BLACK)
    drawing_text("Game Over!", (WIDTH // 2 - 80, HEIGHT // 2 - 60))
    drawing_text(f"final Score: {score}", (WIDTH // 2 - 100, HEIGHT // 2 - 20))
    drawing_text(f"Level: {level}", (WIDTH // 2 - 100, HEIGHT // 2 + 20))
    drawing_text("Press R to restart or Q to quit", (WIDTH // 2 - 170, HEIGHT // 2 + 60))
    pygame.display.flip()


    # Wait for user to press R or Q
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
                    main() # restart the game

# Main game function
def main():
    # Global variables that will be reset on restart
    global snake, snake_dir, score, level, speed

    # Initialize game state
    snake = [(100, 100), (90, 100), (80, 100)]
    snake_dir = (CELL_SIZE,0)
    score = 0
    level = 1
    speed = 10
    food_pos = generate_food()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle keyboard input and prevent reversing direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
            snake_dir = (-CELL_SIZE, 0)
        elif keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
            snake_dir = (CELL_SIZE, 0)
        elif keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
            snake_dir = (0, -CELL_SIZE)
        elif keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
            snake_dir = (0, CELL_SIZE)

        # Update snake position
        head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
        snake.insert(0, head)
        
        # Check for collisions (walls or self)
        if (head in snake[1:] or head[0] < 0 or head[1] < 0 or head[0] >= WIDTH or head[1] >= HEIGHT):
            game_over()
            return
        
        # Check if snake eats the food
        if head == food_pos:
            score += 1
            food_pos = generate_food()

            # Level up every 4 points
            if score % 4 == 0:
                level += 1
                speed = int(speed * 1.1) # increase game speed

        else:
            snake.pop() # remove the tail if no food eaten

        # Drawing
        screen.fill(BLACK)
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, (*food_pos, CELL_SIZE, CELL_SIZE))

        # Draw score and level
        drawing_text(f"Score: {score}", (10, 10))
        drawing_text(f"Level: {level}", (10, 40))
        
        # Refresh screen and control frame rate
        pygame.display.flip()
        clock.tick(speed)

# Start the game
main()
pygame.quit()