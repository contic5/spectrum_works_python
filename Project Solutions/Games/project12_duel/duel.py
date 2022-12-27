
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
    K_s,
    K_k,
    KEYDOWN,
    QUIT,
)

class Game:
    def __init__(self) -> None:
        self.curscreen="menu"
        self.p1score=0
        self.p2score=0
        self.textrgb=(0,0,0)
        self.ready=False

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
        pass

def startgame():
    game.p1score=0
    game.p2score
    game.curscreen="game"
    game.ready=False
    pygame.time.set_timer(COUNTDOWNTIME, random.randint(0,4000)+1000)

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
my_font = pygame.font.SysFont('Arial', 48)

gameovertext=""
go_sound = pygame.mixer.Sound("Idea_Bell_sound_effect.wav")

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
            if event.key==K_s:
                if(game.curscreen=="game"):
                    if(game.ready):
                        game.p1score+=1
                    else:
                        game.p2score+=1
                    game.ready=False
                    pygame.time.set_timer(COUNTDOWNTIME, random.randint(0,4000)+1000)

            if event.key==K_k:
                if(game.curscreen=="game"):
                    if(game.ready):
                        game.p2score+=1
                    else:
                        game.p1score+=1
                    game.ready=False
                    pygame.time.set_timer(COUNTDOWNTIME, random.randint(0,4000)+1000)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        if event.type == COUNTDOWNTIME:
            pygame.time.set_timer(COUNTDOWNTIME, 0)
            game.ready=True
            pygame.mixer.Sound.play(go_sound)

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    # Fill the screen with white
    screen.fill((255, 255, 255))

    if(game.p1score>=5):
        game.curscreen="gameover"
        gameovertext="P1 Wins"
    elif(game.p2score>=5):
        game.curscreen="gameover"
        gameovertext="P2 Wins"

    if(game.curscreen=="game"):
        p1score_surface= my_font.render('Score: '+str(game.p1score),False,game.textrgb)
        screen.blit(p1score_surface, (0,50))

        p2score_surface= my_font.render('Score: '+str(game.p2score),False,game.textrgb)
        screen.blit(p2score_surface, (550,50))

        if(game.ready==True):
            p1alert_surface=my_font.render("S",False,game.textrgb)
            screen.blit(p1alert_surface,(0,150))

            p12lert_surface=my_font.render("K",False,game.textrgb)
            screen.blit(p12lert_surface,(550,150))
        
    elif(game.curscreen=="menu"):
        title_surface= my_font.render('Duel',False,game.textrgb)
        play_surface= my_font.render('Press Space to Play',False,game.textrgb)

        screen.blit(title_surface, (0,0))
        screen.blit(play_surface, (0,100))
    elif(game.curscreen=="gameover"):
        gameover_surface=my_font.render('Game Over',False,game.textrgb)
        resultssurface= my_font.render(gameovertext,False,game.textrgb)
        playagain_surface= my_font.render('Press Space to Play Again',False,game.textrgb)
        menu_surface= my_font.render('Press M for Menu',False,game.textrgb)

        screen.blit(gameover_surface, (0,0))
        screen.blit(resultssurface, (0,100))
        screen.blit(menu_surface, (0,200))
        screen.blit(playagain_surface, (0,300))

    # Draw surf at the new coordinates
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)