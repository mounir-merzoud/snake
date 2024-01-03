import pygame
import sys
import random
import os

# Initialize Pygame
pygame.init()

# Define some constants
WIDTH, HEIGHT = 800, 600
SNAKE_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (1, 0)  # Start with movement to the right
        self.color = BLUE

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        current = self.get_head_position()
        x, y = self.direction
        new = ((current[0] + (x * SNAKE_SIZE)) % WIDTH, (current[1] + (y * SNAKE_SIZE)) % HEIGHT)

        # If the snake touches the apple
        if new == apple.position:
            self.length += 1
            apple.randomize_position()

        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], SNAKE_SIZE, SNAKE_SIZE))

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

# Define the Apple class
class Apple:
    def __init__(self):
        self.position = (0, 0)
        self.image = pygame.image.load("image/apple.png")  # Replace "apple.png" with the path to your image
        self.image = pygame.transform.scale(self.image, (SNAKE_SIZE, SNAKE_SIZE))
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
                         random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)

    def render(self, surface):
        surface.blit(self.image, (self.position[0], self.position[1]))

# Define the AI class
class AI:
    def __init__(self, snake, apple):
        self.snake = snake
        self.apple = apple

    def update(self):
        # Simple AI logic to move towards the apple
        head_position = self.snake.get_head_position()
        apple_position = self.apple.position

        if head_position[0] < apple_position[0]:
            self.snake.set_direction((1, 0))  # Move right
        elif head_position[0] > apple_position[0]:
            self.snake.set_direction((-1, 0))  # Move left
        elif head_position[1] < apple_position[1]:
            self.snake.set_direction((0, 1))  # Move down
        elif head_position[1] > apple_position[1]:
            self.snake.set_direction((0, -1))  # Move up

def main():
    clock = pygame.time.Clock()
    pygame.display.set_caption("Snake Game")  # Window title

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = Snake()
    global apple
    apple = Apple()
    ai = AI(snake, apple)

    best_score = 0  # Variable to store the best score

    # File to store the best score
    score_file_path = "best_score.txt"

    # Check if the file exists
    if os.path.exists(score_file_path):
        with open(score_file_path, 'r') as file:
            best_score = int(file.read())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Save the best score before quitting
                with open(score_file_path, 'w') as file:
                    file.write(str(best_score))
                pygame.quit()
                sys.exit()

        # Use AI to update the direction of the snake
        ai.update()

        snake.update()

        # Check collision with the snake's body
        if snake.get_head_position() in snake.positions[1:]:
            print("Game Over! Your Score:", snake.length - 1)
            if snake.length - 1 > best_score:
                best_score = snake.length - 1
                print("New Best Score:", best_score)

                # Save the new best score to the file
                with open(score_file_path, 'w') as file:
                    file.write(str(best_score))

            pygame.quit()
            sys.exit()

        # Clear the surface at each iteration
        surface.fill(WHITE)

        snake.render(surface)
        apple.render(surface)
        screen.blit(surface, (0, 0))

        # Display the score and best score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {snake.length - 1}", True, RED)
        best_score_text = font.render(f"Best Score: {best_score}", True, RED)

        screen.blit(score_text, (20, 20))
        screen.blit(best_score_text, (20, 70))

        # Adjust the speed based on the length of the snake
        clock.tick(snake.length + 3)

        pygame.display.update()

if __name__ == "__main__":
    main()
