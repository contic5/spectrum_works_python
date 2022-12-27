
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
        self.timeremaining=10
        self.score=0
        self.textrgb=(255,255,255)

class WormPart(pygame.sprite.Sprite):
    def __init__(self,w):
        super(WormPart, self).__init__()
        self.wormparent=w
        self.surf = pygame.Surface((self.wormparent.partsize, self.wormparent.partsize))
        self.surf.fill((0, 255, 0))

        if(len(w.wormparts)<=1):
            self.rect = self.surf.get_rect(
                center=(
                    50,
                    250,
                )
            )
        else:
            prevcenter=(self.wormparent.wormparts[-1].rect.centerx,self.wormparent.wormparts[-1].rect.centery)
            if(self.wormparent.direction=="U"):
                prevcenter=(self.wormparent.wormparts[-1].rect.centerx,self.wormparent.wormparts[-1].rect.centery+self.wormparent.partsize)
            if(self.wormparent.direction=="D"):
                prevcenter=(self.wormparent.wormparts[-1].rect.centerx,self.wormparent.wormparts[-1].rect.centery-self.wormparent.partsize)
            if(self.wormparent.direction=="L"):
                prevcenter=(self.wormparent.wormparts[-1].rect.centerx+self.wormparent.partsize,self.wormparent.wormparts[-1].rect.centery)
            if(self.wormparent.direction=="R"):
                prevcenter=(self.wormparent.wormparts[-1].rect.centerx-self.wormparent.partsize,self.wormparent.wormparts[-1].rect.centery)
            
            self.rect = self.surf.get_rect(
                center=(
                   prevcenter[0],prevcenter[1]
                )
            )
    def move(self,loc):
        prevcenter=(self.wormparent.wormparts[loc-1].rect.centerx,self.wormparent.wormparts[loc-1].rect.centery)

        self.rect = self.surf.get_rect(
            center=(
                prevcenter[0],prevcenter[1]
            )
        )
        
class Worm:
    def __init__(self):
        self.wormparts=[]
        self.partsize=20
        self.direction="R"
        firspart=WormPart(self)
        self.wormparts.append(firspart)
    def move(self):
        for i in range (len(self.wormparts)-1,0,-1):
            self.wormparts[i].move(i)
        
        if(self.direction=="U"):
            self.wormparts[0].rect.centery-=self.partsize
        if(self.direction=="D"):
            self.wormparts[0].rect.centery+=self.partsize
        if(self.direction=="L"):
            self.wormparts[0].rect.centerx-=self.partsize
        if(self.direction=="R"):
            self.wormparts[0].rect.centerx+=self.partsize
    def addpart(self):
        nextpart=WormPart(self)
        self.wormparts.append(nextpart)

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super(Food, self).__init__()
        self.surf = pygame.Surface((40, 40))
        self.surf.fill((200, 200, 0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH - 50),
                random.randint(200, SCREEN_HEIGHT),
            )
        ) 
    def move(self):
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH - 50),
                random.randint(200, SCREEN_HEIGHT),
            )
        ) 

def startgame():
    global w
    game.score=0
    game.timeremaining=999
    game.curscreen="game"
    w=Worm()
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

w=Worm()
food=Food()
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
            if event.key==K_UP and game.curscreen=="game":
                w.direction="U"
            if event.key==K_DOWN and game.curscreen=="game":
                w.direction="D"
            if event.key==K_LEFT and game.curscreen=="game":
                w.direction="L"
            if event.key==K_RIGHT and game.curscreen=="game":
                w.direction="R"
            if event.key== K_m:
                if(game.curscreen=="gameover"):
                    game.curscreen="menu"
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        if event.type == COUNTDOWNTIME:
           game.timeremaining-=1
           if(game.timeremaining==0):
               pygame.time.set_timer(COUNTDOWNTIME, 0)
               game.curscreen="gameover"

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    #Handle game logic
    if(game.curscreen=="game"):
        if pygame.sprite.spritecollideany(food,w.wormparts):
            food.move()
            w.addpart()
        w.move()

    # Fill the screen with white
    screen.fill((0, 0, 0))

    #Display game elements
    if(game.curscreen=="game"):
        for wp in w.wormparts:
            screen.blit(wp.surf, wp.rect)
        screen.blit(food.surf,food.rect)

    #Display text
    if(game.curscreen=="game"):
        time_surface= my_font.render('Time: '+str(game.timeremaining),False,game.textrgb)
        score_surface= my_font.render('Score: '+str(game.score),False,game.textrgb)

        screen.blit(time_surface, (0,0))
        screen.blit(score_surface, (0,50))
    elif(game.curscreen=="menu"):
        title_surface= my_font.render('Worm',False,game.textrgb)
        play_surface= my_font.render('Press Space to Play',False,game.textrgb)

        screen.blit(title_surface, (0,0))
        screen.blit(play_surface, (0,100))
    elif(game.curscreen=="gameover"):
        gameover_surface=my_font.render('Game Over',False,game.textrgb)
        score_surface= my_font.render('Score: '+str(game.score),False,game.textrgb)
        playagain_surface= my_font.render('Press Space to Play Again',False,game.textrgb)
        menu_surface= my_font.render('Press M for Menu',False,game.textrgb)

        screen.blit(gameover_surface, (0,0))
        screen.blit(score_surface, (0,100))
        screen.blit(menu_surface, (0,200))
        screen.blit(playagain_surface, (0,300))

    # Draw surf at the new coordinates
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)