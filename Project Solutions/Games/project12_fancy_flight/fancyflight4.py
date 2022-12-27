#Last difficulty, extreme weather event, is hidden.
#Press down when on the last difficulty

# Import the pygame module
import pygame
import random
import copy
import store_highscores

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
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



# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(game.minspeed[game.difficulty], game.maxspeed[game.difficulty])

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

# Define the cloud object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf=None
        if(game.difficulty<3):
            self.surf = pygame.image.load("cloud.png").convert()
        elif(game.difficulty<4):
            self.surf = pygame.image.load("stormcloud.png").convert()
        else:
            self.surf = pygame.image.load("nightmarecloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(game.cloudspeed[game.difficulty], 0)
        if self.rect.right < 0:
            self.kill()

class Game:
    def __init__(self):
        self.curscreen="menu"
        self.score=0
        self.difficulty=3

        self.spawnspeed=[
            350,
            250,
            200,
            150,
            100,
        ]
        self.minspeed=[
            4,
            5,
            10,
            15,
            20,
        ]
        self.maxspeed=[
            15,
            20,
            25,
            30,
            40,
        ]

        self.cloudspawnspeed=[
            1500,
            1000,
            750,
            500,
            250
        ]
        self.cloudspeed=[
            -4,
            -5,
            -8,
            -12,
            -20
        ]

        self.difficultynames=[
            "Clear Skies",
            "Safe Flying",
            "Rough Weather",
            "Violent Storms",
            "Extreme Weather Event"
        ]

        self.bgcolors=[
        [209, 247, 255],
        [135, 206, 250],
        [255, 212, 148],
        [19, 19, 66],
        [0, 0, 0],
        ]

        self.textcolors=[
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [255,255,255],
            [255,0,0],
        ]

        self.updatetextcolors()
    def updatetextcolors(self):
        self.bgrgb=(self.bgcolors[self.difficulty][0],self.bgcolors[self.difficulty][1],self.bgcolors[self.difficulty][2])
        self.textrgb=(self.textcolors[self.difficulty][0],self.textcolors[self.difficulty][1],self.textcolors[self.difficulty][2])
        

def startgame():
    all_sprites.add(player)
    #player.rect.move(0,SCREEN_HEIGHT/2)
    player.rect = player.surf.get_rect(
            center=(
                0,
                SCREEN_HEIGHT/2
            )
    )

    pygame.time.set_timer(ADDCLOUD, game.cloudspawnspeed[game.difficulty])
    pygame.time.set_timer(ADDENEMY, game.spawnspeed[game.difficulty])
    pygame.mixer.music.play(loops=-1)
    game.curscreen="game"
    game.score=0

def gameover():
    global curscreen
    player.kill()
    for enemy in enemies:
        enemy.kill()
    for cloud in clouds:
        cloud.kill()

    # Stop any moving sounds and play the collision sound
    move_up_sound.stop()
    move_down_sound.stop()
    collision_sound.play()

    pygame.time.set_timer(ADDCLOUD, 0)
    pygame.time.set_timer(ADDENEMY, 0)

    #running = False
    store_highscores.writescore(game.score,game.difficulty)

    game.curscreen="gameover"

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Set current screen
game=Game()
game.curscreen="menu"

# Setup for sounds. Defaults are good.
pygame.mixer.init()

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
ADDCLOUD = pygame.USEREVENT + 2

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Variable to keep the main loop running
running = True

# Load and play background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load("Apoxode_-_Electric_1.mp3")

# Load all sound files
# Sound sources: Jon Fincher
move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("Collision.ogg")

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Arial', 48)
small_font=pygame.font.SysFont('Arial',24)


#startgame()
# Main loop
while running:
    # for loop through the event queue 

    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
            if event.key== K_SPACE:
                if(game.curscreen=="menu" or game.curscreen=="gameover"):
                    startgame()
            if event.key== K_m:
                if(game.curscreen=="gameover"):
                    game.curscreen="menu"
            if event.key==K_DOWN:
                if(game.curscreen=="menu"):
                    game.difficulty+=1
                    game.difficulty=min(game.difficulty,len(game.difficultynames)-1)
                    game.updatetextcolors()
            if event.key==K_UP:
                if(game.curscreen=="menu"):
                    game.difficulty-=1
                    game.difficulty=max(game.difficulty,0)
                    game.updatetextcolors()
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
        
        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        
        # Add a new cloud?
        elif event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # Fill the screen with sky blue
    screen.fill(game.bgrgb)
    if(game.curscreen=="game"):
        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()

        # Update the player sprite based on user keypresses
        player.update(pressed_keys)

        # Update enemy position
        enemies.update()
        clouds.update()
        
        # Draw the player on the screen
        screen.blit(player.surf, player.rect)

        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        score_surface = my_font.render("Score: "+str(game.score), False, (game.textrgb))
        screen.blit(score_surface, (0,0))

        # Check if any enemies have collided with the player
        if pygame.sprite.spritecollideany(player, enemies):
            # If so, then remove the player and stop the loop
            gameover()

        game.score+=1
            
    elif(game.curscreen=="menu"):
        start_text_surface = my_font.render('Fancy Flight', False, (game.textrgb))
        press_text_surface= my_font.render('Press Space to Start',False,(game.textrgb))
        screen.blit(start_text_surface, (100,0))

        screen.blit(press_text_surface, (100,100))

        difficulty_surfaces=[]
        totaldisplays=4
        for i in range(totaldisplays):
            curdifficultysurface=None
            #Extreme weather is hidden
            if(game.difficulty==4 and i==totaldisplays-1):
                curdifficultysurface=my_font.render(game.difficultynames[4], False, (128,0,0))
            elif(i==game.difficulty):
                curdifficultysurface=my_font.render(game.difficultynames[i], False, (128,128,128))
            else:
                curdifficultysurface=my_font.render(game.difficultynames[i], False, (game.textrgb))
            difficulty_surfaces.append(curdifficultysurface)
            screen.blit(difficulty_surfaces[i], (100,200+(100*i)))

    elif(game.curscreen=="gameover"):
        game_over_surface = my_font.render('Game Over', False, (game.textrgb))
        difficulty_surface=my_font.render('Difficulty: '+str(game.difficultynames[game.difficulty]), False, (game.textrgb))
        score_surface=my_font.render("Score: "+str(game.score), False, (game.textrgb))
        play_again_surface= my_font.render('Press Space to Play Again',False,(game.textrgb))
        menu_surface= my_font.render('Press M to return to the Menu',False,(game.textrgb))

        screen.blit(game_over_surface, (0,0))
        screen.blit(difficulty_surface, (0,100))
        screen.blit(score_surface, (0,200))
        screen.blit(play_again_surface, (0,300))
        screen.blit(menu_surface, (0,400))

        if(game.difficulty==3 and game.score>=1):
            secret_surface=small_font.render("Press down when on "+game.difficultynames[game.difficulty]+" for a surprise...",False,(game.textrgb))
            screen.blit(secret_surface, (0,500))
        if(game.difficulty==4 and game.score>=500):
            secret_surface=my_font.render("That was incredible flying!",False,(game.textrgb))
            screen.blit(secret_surface, (0,500))


    # Setup the clock for a decent framerate
    clock = pygame.time.Clock()

    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

# All done! Stop and quit the mixer.
pygame.mixer.music.stop()
pygame.mixer.quit()