import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 10
BLOCK_SIZE = 20
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Snake attributes
snake = [(WIDTH // 2, HEIGHT // 2)]
snake_direction = 'RIGHT'
snake_speed = BLOCK_SIZE

# Fruit attributes
fruit = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
         random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)

# Game variables
score = 0
clock = pygame.time.Clock()

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, WHITE, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

def draw_fruit():
    pygame.draw.rect(screen, RED, (fruit[0], fruit[1], BLOCK_SIZE, BLOCK_SIZE))

def game_over():
    font = pygame.font.SysFont('Arial', 36)
    text = font.render(f'Game Over! Score: {score}', True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != 'DOWN':
        snake_direction = 'UP'
    elif keys[pygame.K_DOWN] and snake_direction != 'UP':
        snake_direction = 'DOWN'
    elif keys[pygame.K_LEFT] and snake_direction != 'RIGHT':
        snake_direction = 'LEFT'
    elif keys[pygame.K_RIGHT] and snake_direction != 'LEFT':
        snake_direction = 'RIGHT'

    # Update snake position
    head = list(snake[0])
    if snake_direction == 'UP':
        head[1] -= snake_speed
    elif snake_direction == 'DOWN':
        head[1] += snake_speed
    elif snake_direction == 'LEFT':
        head[0] -= snake_speed
    elif snake_direction == 'RIGHT':
        head[0] += snake_speed
    snake.insert(0, tuple(head))

    # Check collision with fruit
    if snake[0][0] == fruit[0] and snake[0][1] == fruit[1]:
        score += 1
        fruit = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                 random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
    else:
        snake.pop()

    # Check collision with screen boundaries
    if (snake[0][0] >= WIDTH or snake[0][0] < 0 or
        snake[0][1] >= HEIGHT or snake[0][1] < 0):
        game_over()

    # Check collision with itself
    if len(snake) != len(set(snake)):
        game_over()

    draw_snake()
    draw_fruit()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
