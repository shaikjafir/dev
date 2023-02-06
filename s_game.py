import pygame
import random

# Initialize the game
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((600, 600))

# Set the title of the screen
pygame.display.set_caption("Snake Game")

# Set the clock for controlling the frame rate
clock = pygame.time.Clock()

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Define the block size and font size
block_size = 20
font_size = 20

# Define the font for displaying score
font = pygame.font.Font(None, font_size)

# Define the game over function
def game_over(score):
    game_over_text = font.render("Game Over! Your score is " + str(score), True, white)
    screen.blit(game_over_text, [150, 300])
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    quit()

# Define the Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((screen.get_width() / 2), (screen.get_height() / 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = green

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * block_size)) % screen.get_width()), (cur[1] + (y * block_size)) % screen.get_height())
        if len(self.positions) > 2 and new in self.positions[2:]:
            game_over(len(self.positions) - 1)
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (block_size, block_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, white, r, 1)

# Define the direction variables
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

# Initialize the Snake object
snake = Snake()

# Define the food object
food = pygame.Rect(random.randint(0, screen.
get_width() / block_size) * block_size, random.randint(0, screen.get_height() / block_size) * block_size), (block_size, block_size)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over(len(snake.positions) - 1)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.turn(up)
            if event.key == pygame.K_DOWN:
                snake.turn(down)
            if event.key == pygame.K_LEFT:
                snake.turn(left)
            if event.key == pygame.K_RIGHT:
                snake.turn(right)

    # Check if the snake has collided with the food
    if snake.get_head_position() == food.topleft:
        snake.length += 1
        food = pygame.Rect(random.randint(0, screen.get_width() / block_size) * block_size, random.randint(0, screen.get_height() / block_size) * block_size), (block_size, block_size)

    # Update the screen
    screen.fill((0, 0, 0))
    snake.move()
    snake.draw(screen)
    pygame.draw.rect(screen, blue, food)
    pygame.display.update()

    # Set the frame rate
    clock.tick(10)
