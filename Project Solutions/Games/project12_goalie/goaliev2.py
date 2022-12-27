
# Import the pygame module
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
        #Modes: resetball,continueball
        self.modes=["resetball","continueball"]
        self.modeswritten=["Reset Ball","Continue Ball"]
        self.modeindex=0
        self.mode=self.modes[self.modeindex]
        self.curscreen="menu"
        self.timeremaining=10
        self.score=0
        self.textrgb=(255,255,255)
        self.paddlegap=40

class Indicator(pygame.sprite.Sprite):
    def __init__(self,x,y,vx,vy):
        super(Indicator, self).__init__()
        self.score=0
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy

        self.rgb=(255,255,255)
        self.size=20

        self.surf = pygame.Surface((self.size, self.size))
        self.surf.fill(self.rgb)
        self.rect = self.surf.get_rect(
            center=(
                self.x,self.y
            )
        )
    def setpos(self,x,y):
        self.x=x
        self.y=y
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
        self.vx=-int(self.v/(2**0.5))
        self.vy=0
        self.nextvx=self.vx
        self.nextvy=self.vy

        self.size=40
        self.lastpoint=-1

        self.surf = pygame.Surface((self.size, self.size))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                self.startx,self.starty
            )
        )
    def increasespeed(self):
        self.v=self.v+2

    def changeangle_and_speed(self):
        print("Increase speed")
        self.v=self.v+2
        self.angle=math.pi*random.randint(30,150)/180
        self.nextvx=-1*self.v*math.sin(self.angle)
        self.nextvy=self.v*math.cos(self.angle)
    
    def restartmovement(self):
        self.vx=self.nextvx
        self.vy=self.nextvy

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
            #If you miss once, you lose
            self.resetpos()
            pd1.resetpos()
            game.curscreen="gameover"
            self.lastpoint=1

        if(self.x>=SCREEN_WIDTH-self.size):
            if(game.mode=="continueball"):
                self.reversedirection()
                self.increasespeed()
                print("Score")
                pd1.score+=1
                self.lastpoint=0
            else:
                self.resetpos()
                pd1.resetpos()
                pd1.score+=1
                pygame.time.set_timer(STARTNEXTPOINT,500)
        
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
    global b
    pd1.score=0
    b=Ball(SCREEN_WIDTH-50,SCREEN_HEIGHT/2-25)
    game.curscreen="game"

# Initialize pygame
pygame.init()

game=Game()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

STARTMOVEMENT = pygame.USEREVENT + 1
STARTNEXTPOINT= pygame.USEREVENT + 2

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
pd1.rgb=(150,150,255)
pd1.surf.fill(pd1.rgb)

b=Ball(SCREEN_WIDTH-50,SCREEN_HEIGHT/2-25)
indicator=Indicator(-20,-20,0,0)

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
            if event.key==K_UP:
                if(game.curscreen=="menu"):
                    if(game.modeindex>0):
                        game.modeindex-=1
                        game.mode=game.modes[game.modeindex]
            if event.key==K_DOWN:
                if(game.curscreen=="menu"):
                    if(game.modeindex<len(game.modes)-1):
                        game.modeindex+=1
                        game.mode=game.modes[game.modeindex]
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        if event.type==STARTMOVEMENT:
            print("Restart Movement")
            indicator.vx=0
            indicator.vy=0
            indicator.x=-20
            indicator.y=-20

            b.restartmovement()
            pygame.time.set_timer(STARTMOVEMENT, 0)
        elif event.type==STARTNEXTPOINT:
            pygame.time.set_timer(STARTNEXTPOINT,0)
            pygame.time.set_timer(STARTMOVEMENT,500)
            pd1.resetpos()
            b.resetpos()

            b.changeangle_and_speed()
            indicator=Indicator(b.x,b.y,b.nextvx,b.nextvy)

            for i in range(5):
                indicator.move()

            print("Score")
            pd1.score+=1
            b.lastpoint=0

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
    
    #Handle game logic
    if(game.curscreen=="game"):
        b.move()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            pd1.move(0,-10)
        if pressed_keys[K_DOWN]:
            pd1.move(0,10)
        '''
        if pressed_keys[K_w]:
            pd1.move(0,-10)
        if pressed_keys[K_s]:
            pd1.move(0,10)
        '''
        
        if pygame.sprite.collide_rect(pd1, b):
            if(game.mode=="resetball"):
                b.reversedirection()
                pygame.time.set_timer(STARTNEXTPOINT,500)
            else:
                b.reversedirection()


        if(pd1.score>=99):
            game.curscreen="gameover"

    # Fill the screen with black
    screen.fill((0, 0, 0))

    if(game.curscreen=="game"):
        screen.blit(pd1.surf,pd1.rect)
        screen.blit(b.surf,b.rect)

        screen.blit(indicator.surf,indicator.rect)

        score1_surface= my_font.render('Score: '+str(pd1.score),False,pd1.rgb)

        mode_surface=my_font.render("Mode: "+game.modeswritten[game.modeindex],False,game.textrgb)
        screen.blit(mode_surface, (0,100))
        screen.blit(score1_surface, (0,50))

    elif(game.curscreen=="menu"):
        title_surface= my_font.render('Goalie Game',False,game.textrgb)
        play_surface= my_font.render('Press Space to Play',False,game.textrgb)
        mode_surface=my_font.render("Mode: "+game.modeswritten[game.modeindex],False,game.textrgb)

        screen.blit(title_surface, (0,0))
        screen.blit(play_surface, (0,100))
        screen.blit(mode_surface, (0,200))

    elif(game.curscreen=="gameover"):
        gameover_surface=my_font.render('Game Over',False,game.textrgb)
        mode_surface=my_font.render("Mode: "+game.modeswritten[game.modeindex],False,game.textrgb)
        score_surface= my_font.render('Score: '+str(pd1.score),False,game.textrgb)

        playagain_surface= my_font.render('Press Space to Play Again',False,game.textrgb)
        menu_surface= my_font.render('Press M for Menu',False,game.textrgb)

        screen.blit(gameover_surface, (0,0))
        screen.blit(mode_surface, (0,100))
        screen.blit(score_surface, (0,200))
        screen.blit(menu_surface, (0,300))
        screen.blit(playagain_surface, (0,400))

    # Draw surf at the new coordinates
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)