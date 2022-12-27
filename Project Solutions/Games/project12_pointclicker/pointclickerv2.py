
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
    K_SPACE,
    K_m,
    KEYDOWN,
    QUIT,
)

class Game:
    def __init__(self) -> None:
        self.curscreen="menu"
        self.timeremaining=30
        self.score=0

class GameCircle(pygame.sprite.Sprite):
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

def startgame():
    game.score=0
    game.timeremaining=30
    game.curscreen="game"
    pygame.time.set_timer(COUNTDOWNTIME, 1000)

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
my_font = pygame.font.SysFont('Arial', 48)

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
            if event.key== K_SPACE:
                if(game.curscreen=="menu" or game.curscreen=="gameover"):
                    print("Start Game")
                    startgame()
            if event.key== K_m:
                if(game.curscreen=="gameover"):
                    game.curscreen="menu"
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                if(game.curscreen=="game"):
                    pos = pygame.mouse.get_pos()
                    if(bu_gc.collidepoint(pos)):
                        game.score+=1
                        gc.move()
                    else:
                        game.timeremaining-=2
        if event.type == COUNTDOWNTIME:
           game.timeremaining-=1
           if(game.timeremaining<=0):
               pygame.time.set_timer(COUNTDOWNTIME, 0)
               game.curscreen="gameover"

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    # Fill the screen with white
    screen.fill((255, 255, 255))

    if(game.curscreen=="game"):
        time_surface= my_font.render('Time: '+str(game.timeremaining),False,(0,0,0))
        score_surface= my_font.render('Score: '+str(game.score),False,(0,0,0))

        screen.blit(time_surface, (0,0))
        screen.blit(score_surface, (0,50))

        bu_gc=screen.blit(gc.surf, gc.rect)
    elif(game.curscreen=="menu"):
        title_surface= my_font.render('Point Clicker',False,(0,0,0))
        play_surface= my_font.render('Press Space to Play',False,(0,0,0))

        screen.blit(title_surface, (0,0))
        screen.blit(play_surface, (0,100))
    elif(game.curscreen=="gameover"):
        gameover_surface=my_font.render('Game Over',False,(0,0,0))
        score_surface= my_font.render('Score: '+str(game.score),False,(0,0,0))
        playagain_surface= my_font.render('Press Space to Play Again',False,(0,0,0))
        menu_surface= my_font.render('Press M for Menu',False,(0,0,0))

        screen.blit(gameover_surface, (0,0))
        screen.blit(score_surface, (0,100))
        screen.blit(menu_surface, (0,200))
        screen.blit(playagain_surface, (0,300))

    # Draw surf at the new coordinates
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)