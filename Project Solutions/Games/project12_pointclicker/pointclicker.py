
# Import the pygame module
import pygame
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Game:
    def __init__(self) -> None:
        self.gamescreen="game"
        self.timeremaining=30
        self.score=0

class GameCircle:
    def __init__(self):
        super(GameCircle, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH - 50),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
    def move(self):
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH - 50),
                random.randint(100, SCREEN_HEIGHT),
            )
        )

# Initialize pygame
pygame.init()

game=Game()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()


# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Variable to keep the main loop running
running = True

COUNTDOWNTIME = pygame.USEREVENT + 1
pygame.time.set_timer(COUNTDOWNTIME, 1000)

gc=GameCircle()
print(gc.rect)
bu_gc=None
# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                pos = pygame.mouse.get_pos()
                if(bu_gc.collidepoint(pos)):
                    game.score+=1
                    gc.move()
        if event.type == COUNTDOWNTIME:
           game.timeremaining-=1

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw surf at the new coordinates
    bu_gc=screen.blit(gc.surf, gc.rect)
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)