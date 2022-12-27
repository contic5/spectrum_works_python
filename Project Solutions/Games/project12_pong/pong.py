
# Import the pygame module
from asyncio import start_unix_server
import pygame
import random
import math

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_w,
    K_s,
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
        self.paddlegap=40


class Paddle(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Paddle, self).__init__()
        self.score=0
        self.x=x
        self.y=y
        self.startx=x
        self.starty=y
        self.height=150
        self.width=20
        self.rgb=(255,255,255)

        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill(self.rgb)
        self.rect = self.surf.get_rect(
            center=(
                self.startx,self.starty
            )
        )
    def resetpos(self):
        self.x=self.startx
        self.y=self.starty
        self.rect = self.surf.get_rect(
            center=(
                self.startx,self.starty
            )
        )
    def move(self,x,y):
        if(self.y-self.height//2+y>=0 and self.y+y+self.height//2<=SCREEN_HEIGHT):
            self.y+=y
            self.rect.move_ip(x, y)

class Ball(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Ball, self).__init__()

        self.x=x
        self.y=y
        self.startx=x
        self.starty=y
        self.v=15
        self.vx=int(self.v/(2**0.5))
        self.vy=0
        self.size=40
        self.lastpoint=-1

        self.surf = pygame.Surface((self.size, self.size))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                self.startx,self.starty
            )
        )
    def resetpos(self):
        self.x=self.startx
        self.y=self.starty
        self.vx=0
        self.vy=0
        self.rect = self.surf.get_rect(
            center=(
                self.startx,self.starty
            )
        )
    def move(self):
        self.x+=self.vx
        self.y+=self.vy
        self.rect = self.surf.get_rect(
            center=(
                self.x,self.y
            )
        )

        if(self.y<=0):
            self.y=0
            self.vy=abs(self.vy)
        if(self.y>=SCREEN_HEIGHT-self.size):
            self.y=SCREEN_HEIGHT-self.size
            self.vy=-abs(self.vy)
        
        if(self.x<=0):
            self.resetpos()
            pd1.resetpos()
            pd2.resetpos()
            pygame.time.set_timer(STARTMOVEMENT,1000)
            pd2.score+=1
            self.lastpoint=1
        if(self.x>=SCREEN_WIDTH-self.size):
            self.resetpos()
            pd1.resetpos()
            pd2.resetpos()
            pygame.time.set_timer(STARTMOVEMENT,1000)
            pd1.score+=1
            self.lastpoint=0
        
    def reversedirection(self):
        #CHANGE ANGLE OF BALL. USE SIN AND COS
        self.angle=math.pi*random.randint(30,150)/180
        if(self.vx<=0):
            self.vx=self.v*math.sin(self.angle)
        else:
            self.vx=-1*self.v*math.sin(self.angle)
        self.vy=self.v*math.cos(self.angle)
        #self.vy=self.vy*self.angle

def startgame():
    pd1.score=0
    pd2.score=0
    game.curscreen="game"

# Initialize pygame
pygame.init()

game=Game()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

STARTMOVEMENT = pygame.USEREVENT + 1

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Variable to keep the main loop running
running = True

my_font = pygame.font.SysFont('Arial', 48)

pd1=Paddle(game.paddlegap,SCREEN_HEIGHT//2)
pd1.rgb=(255,0,0)
pd1.surf.fill(pd1.rgb)
pd2=Paddle(SCREEN_WIDTH-game.paddlegap,SCREEN_HEIGHT//2)
pd2.rgb=(0,0,255)
pd2.surf.fill(pd2.rgb)

b=Ball(SCREEN_WIDTH/2-25,SCREEN_HEIGHT/2-25)

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
            pass
        if event.type==STARTMOVEMENT:
            print("Restart Movement")
            if(b.lastpoint==0):
                b.vx=-b.v/(2**0.5)
            else:
                b.vx=b.v/(2**0.5)
            pygame.time.set_timer(STARTMOVEMENT, 0)

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
    
    #Move game
    if(game.curscreen=="game"):
        b.move()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            pd2.move(0,-10)
        if pressed_keys[K_DOWN]:
            pd2.move(0,10)
        if pressed_keys[K_w]:
            pd1.move(0,-10)
        if pressed_keys[K_s]:
            pd1.move(0,10)
        
        if pygame.sprite.collide_rect(pd1, b):
            b.reversedirection()
        if pygame.sprite.collide_rect(pd2, b):
            b.reversedirection()

        if(pd1.score>=5):
            game.curscreen="gameover"
        elif(pd2.score>=5):
            game.curscreen="gameover"

    # Fill the screen with black
    screen.fill((0, 0, 0))

    if(game.curscreen=="game"):
        screen.blit(pd1.surf,pd1.rect)
        screen.blit(pd2.surf,pd2.rect)
        screen.blit(b.surf,b.rect)

        score1_surface= my_font.render('Score: '+str(pd1.score),False,pd1.rgb)
        score2_surface= my_font.render('Score: '+str(pd2.score),False,pd2.rgb)

        screen.blit(score1_surface, (0,50))
        screen.blit(score2_surface, (400,50))

    elif(game.curscreen=="menu"):
        title_surface= my_font.render('Pong',False,game.textrgb)
        play_surface= my_font.render('Press Space to Play',False,game.textrgb)

        screen.blit(title_surface, (0,0))
        screen.blit(play_surface, (0,100))

    elif(game.curscreen=="gameover"):
        gameover_surface=my_font.render('Game Over',False,game.textrgb)
        score_surface= my_font.render('Score: '+str(pd1.score)+" "+str(pd2.score),False,game.textrgb)
        results_surface=None
        if(pd1.score>=5):
            results_surface= my_font.render("Player 1 wins!",False,pd1.rgb)
        elif(pd2.score>=5):
            results_surface= my_font.render("Player 2 wins!",False,pd2.rgb)
        else:
            results_surface= my_font.render("The game is unfinished",False,game.textrgb)

        playagain_surface= my_font.render('Press Space to Play Again',False,game.textrgb)
        menu_surface= my_font.render('Press M for Menu',False,game.textrgb)

        screen.blit(gameover_surface, (0,0))
        screen.blit(score_surface, (0,100))
        screen.blit(results_surface, (0,200))
        screen.blit(menu_surface, (0,300))
        screen.blit(playagain_surface, (0,400))

    # Draw surf at the new coordinates
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)