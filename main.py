"""
This program creates a game where the user must dodge the viruses.
Player can pick up "power up" items to replenish their lives or to increase speed.
The goal of the game is to survive as long as you can.
"""
#All sound effects from https://mixkit.co/free-sound-effects/game/?page=2


import pygame
import random
import sys
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (124, 194, 33)
RED = (232, 62, 49)
BLUE = (62, 99, 125)
DARK_BLUE = (50, 80, 102)
MED_BLUE = (59, 93, 117)
LIGHT_BLUE = (184, 208, 224)


pygame.init()


#Starting location of player
player_pos_x = 500
player_pos_y = 350


#Starting position of instructions
instruction_change_x = 350


#Changes the speed of the player
change_x = 0
change_y = 0


#Starting speed of items
item_speed = 0


#Starting speed of timer
timer_speed = 0


#Size of screen
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])


#File name
pygame.display.set_caption("CPT Cybersecurity Game")
   
# Loop until the user clicks the close button.
done = False
   
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


#(CODE FROM TIMER EXAMPLE)
font = pygame.font.Font(None, 35)
 
frame_count = 0
frame_rate = 60
start_time = 90  


#Create and load an image for items
class Item(pygame.sprite.Sprite):


    def __init__(self, image):
        """Loads in the image and makes the background transparent


        Args:
        image(image): Loads this image
        """


        #Call the parent class (Sprite) constructor
        super().__init__()
   
        #Load the image
        self.image = pygame.image.load(image).convert()


        #Make the background transparent
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()


    def reset_pos(self):
        """Resets the position of the viruses/items


        """
        #Items will re-appear
        self.rect.x = random.randrange(-100, -50)
        #Items appear randomly on the y-axis
        self.rect.y = random.randrange(0, screen_width)
 
    def update(self):
        """Make sure the items don't all disappear and sets the speed of the items


        """
        #Speed of items
        self.rect.x = self.rect.x + item_speed
        #Reset to the right of the screen
        if self.rect.x > 1000:
            self.reset_pos()


#Create a group for viruses
virus_list = pygame.sprite.Group()
#Group for life power ups
power_list = pygame.sprite.Group()
#Group for speed power ups
speed_list = pygame.sprite.Group()
#Group for hearts displayed
life_list = pygame.sprite.Group()
#Group of all sprites
all_sprites_list = pygame.sprite.Group()


#Image from https://pixabay.com/vectors/virus-coronavirus-corona-covid-19-4986015/
for i in range(25):
    virus = Item("greenvirus.png")

    #Set a random location for the block
    virus.rect.x = random.randrange(-1500, screen_width-1500)
    virus.rect.y = random.randrange(screen_height)
 
    #Add the block to the groups
    virus_list.add(virus)
    all_sprites_list.add(virus)


#Image from https://pixabay.com/illustrations/pixel-heart-heart-pixel-symbol-red-2779422/
for i in range(10):
    power_up = Item("heart.png")

    #Set a random location for the block
    power_up.rect.x = random.randrange(-1500, screen_width-1500)
    power_up.rect.y = random.randrange(screen_height)
 
    #Add the block to the groups
    power_list.add(power_up)
    all_sprites_list.add(power_up)


#Speed Powerup
#image from https://www.jing.fm/iclipt/iThihh/
for i in range(5):
    s_power = Item("lighting_bolt.png")

    #Set a random location for the block
    s_power.rect.x = random.randrange(-1500, screen_width-1500)
    s_power.rect.y = random.randrange(screen_height)
 
    #Add the block to the groups
    speed_list.add(s_power)
    all_sprites_list.add(s_power)


#Create a player
#Image from https://www.deviantart.com/obinsun/art/16x16-Knight-Sprite-458197531
player = Item("knight_left.png")
player_left = Item("knight_left.png")
player_right = Item("Knight_right.png")
player_up = Item("Knight_up.png")
player_down = Item("Knight_down.png")
all_sprites_list.add(player)


#Starting number of lives
lives = 3


#(INPUT CODE FROM https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/)
# basic font for user typed
base_font = pygame.font.Font(None, 32)
user_text = ''


# color_active stores color which
# gets active when input box is clicked by user
color_active = pygame.Color(DARK_BLUE)
 
# color_passive stores color which is
# the color of the input box.
color_passive = pygame.Color(MED_BLUE)
color = color_passive
 
active = False

##Start button text
start_text = "START"

#Play background music      
#"Kick Shock" Kevin MacLeod (incompetech.com)
#Licensed under Creative Commons: By Attribution 4.0 License
#http://creativecommons.org/licenses/by/4.0/  
background_music = pygame.mixer.Sound("Kick Shock.mp3")
#Background music keeps looping
background_music.play(-1)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
       
        #(INPUT CODE FROM https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        #User can only input a name when they click on the box        
        if active:
            if event.type == pygame.KEYDOWN:
   
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
   
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
   
                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode
           
    #Set background color
    screen.fill(BLUE)
   
    if active:
        color = color_active
    else:
        color = color_passive
   
    ##Draws a user input text box to write their name
    # create rectangle
    input_rect = pygame.Rect(player_pos_x-15, player_pos_y-30, 100, 32)


    # draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(screen, color, input_rect)
   
    text_surface = base_font.render(user_text, True, (255, 255, 255))
     
    # render at position stated in arguments
    #screen.blit(text_surface, (input_rect.x, input_rect.y))
   
    screen.blit(text_surface, [player_pos_x-5, player_pos_y-25])


    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width()+10)


    ##Creates start button so that the game starts once clicked
    start_button = pygame.Rect(880,30, 100, 32)
    pygame.draw.rect(screen, GREEN, start_button)
    start_text = base_font.render("START", True, (255, 255, 255))
    screen.blit(start_text, [893,35])


    #If start button clicked...
    if event.type == pygame.MOUSEBUTTONDOWN:
        if start_button.collidepoint(event.pos):
            #Star button turns blue when clicked
            start_button = pygame.Rect(880,30, 100, 32)
            pygame.draw.rect(screen, BLUE, start_button)
            start_text = base_font.render("", True, (255, 255, 255))
            screen.blit(start_text, [893,35])
            #Starts level and timer when clicked
            item_speed = 10
            timer_speed = 2

  
    ##BACKGROUND
    pygame.draw.rect(screen, LIGHT_BLUE, [0,550,500,3])
    pygame.draw.line(screen, LIGHT_BLUE, [500,550], [520,600],3)
    pygame.draw.rect(screen, LIGHT_BLUE, [520,600,500,3])
    pygame.draw.rect(screen, LIGHT_BLUE, [0,570,300,3])
    pygame.draw.rect(screen, LIGHT_BLUE, [0,600,213,3])
    pygame.draw.circle(screen, LIGHT_BLUE,[220,600],10,3)
 
    pygame.draw.rect(screen, LIGHT_BLUE, [0,150,600,3])
    pygame.draw.line(screen, LIGHT_BLUE, [600,150], [620,100],3)
    pygame.draw.rect(screen, LIGHT_BLUE, [620,100,500,3])
    pygame.draw.rect(screen, LIGHT_BLUE, [700,80,300,3])
    pygame.draw.circle(screen, LIGHT_BLUE,[693,80],10,3)
   


    #Display instructions
    text_line_1 = "Dodge the green viruses and survive"
    text_line_2 = "for as long as you can! Collect power"
    text_line_3 = "ups to help you on your journey."
    text_line_4 = "Enter your name below and click Start!"


    #Display instructions on the screen
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(text_line_1,True,LIGHT_BLUE)
    screen.blit(text, [instruction_change_x, 180])
    text = font.render(text_line_2,True,LIGHT_BLUE)
    screen.blit(text, [instruction_change_x, 210])
    text = font.render(text_line_3,True,LIGHT_BLUE)
    screen.blit(text, [instruction_change_x, 240])
    text = font.render(text_line_4,True,LIGHT_BLUE)
    screen.blit(text, [instruction_change_x, 290])


    #Move instructions off screen when player clicks start
    instruction_change_x = instruction_change_x + item_speed


    #Display 3 lives
    life_1 = Item("life (1).png")
    #Location for the life
    life_1.rect.x = 30
    life_1.rect.y = 25
    #Add the life to the groups
    life_list.add(life_1)
    all_sprites_list.add(life_1)


    life_2 = Item("life (1).png")
    #Location for the life
    life_2.rect.x = 90
    life_2.rect.y = 25
    #Add the life to the groups
    life_list.add(life_2)
    all_sprites_list.add(life_2)


    life_3 = Item("life (1).png")
    #Location for the life
    life_3.rect.x = 150
    life_3.rect.y = 25
    #Add the life to the groups
    life_list.add(life_3)
    all_sprites_list.add(life_3)


    #When user looses a life
    #Adds a darker color heart on top of the lighter one
    if lives == 2:
        no_life = Item("life.png")
        #Location for the life
        no_life.rect.x = 150
        no_life.rect.y = 25
        #Add the life to the groups
        life_list.add(no_life)
        all_sprites_list.add(no_life)
   
    if lives == 1:
        no_life = Item("life.png")
        #Location for the life
        no_life.rect.x = 150
        no_life.rect.y = 25
        #Add the life to the groups
        life_list.add(no_life)
        all_sprites_list.add(no_life)

        no_life = Item("life.png")
        #Location for the life
        no_life.rect.x = 90
        no_life.rect.y = 25
        #Add the life to the groups
        life_list.add(no_life)
        all_sprites_list.add(no_life)

    if lives <= 0:
        no_life = Item("life.png")
        #Location for the life
        no_life.rect.x = 30
        no_life.rect.y = 25
        #Add the life to the groups
        life_list.add(no_life)
        all_sprites_list.add(no_life)
       
        no_life = Item("life.png")
        #Location for the life
        no_life.rect.x = 90
        no_life.rect.y = 25
        #Add the life to the groups
        life_list.add(no_life)
        all_sprites_list.add(no_life)
       
        no_life = Item("life.png")
        #Location for the life
        no_life.rect.x = 150
        no_life.rect.y = 25
        #Add the life to the groups
        life_list.add(no_life)
        all_sprites_list.add(no_life)
   

    #Make sure the player doesn't go past the border
    if player_pos_x > 945:
        player_pos_x = 945
        bump_sound = pygame.mixer.Sound("player_hit_border.wav")
        bump_sound.play()
    elif player_pos_x < 0:
        player_pos_x = 0
        bump_sound = pygame.mixer.Sound("player_hit_border.wav")
        bump_sound.play()
    if player_pos_y > 635:
        player_pos_y = 635
        bump_sound = pygame.mixer.Sound("player_hit_border.wav")
        bump_sound.play()
    elif player_pos_y < 0:
        player_pos_y = 0
        bump_sound = pygame.mixer.Sound("player_hit_border.wav")
        bump_sound.play()
   
   #Move player with keys
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_pos_x = player_pos_x + -10 - change_x
            #Change image of player to face left
            all_sprites_list.remove(player)
            player = player_left
            all_sprites_list.add(player)
           
        elif event.key == pygame.K_RIGHT:
            player_pos_x = player_pos_x + 10 + change_x
            #Change image of player to face the right
            all_sprites_list.remove(player)
            player = player_right
            all_sprites_list.add(player)
           
        elif event.key == pygame.K_UP:
            player_pos_y = player_pos_y + -10 - change_y
            #Change image of player to face up
            all_sprites_list.remove(player)
            player = player_up
            all_sprites_list.add(player)
           
        elif event.key == pygame.K_DOWN:
            player_pos_y = player_pos_y + 10 + change_y
            #Change image of player to face down
            all_sprites_list.remove(player)
            player = player_down
            all_sprites_list.add(player)


 
    ##CODE FROM TIMER EXAMPLE
    #Font of Timer text
    font = pygame.font.SysFont('Courier New', 25, True, False)
    # Calculate total seconds
    total_seconds = frame_count // frame_rate
    # Divide by 60 to get total minutes
    minutes = total_seconds // 60
    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60
    # Use python string formatting to format in leading zeros
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
    # Blit to the screen
    text = font.render(output_string, True, WHITE)
    screen.blit(text, [825, 650])
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count = frame_count + timer_speed


    # Limit frames per second
    clock.tick(frame_rate)
   

    #CHECK FOR COLLISIONS
    #Find the current location of the player
    player.rect.x = player_pos_x
    player.rect.y = player_pos_y

    # See if the player block has collided with anything.
    virus_hit_list = pygame.sprite.spritecollide(player, virus_list, True)
    power_hit_list = pygame.sprite.spritecollide(player, power_list, True)

    #If the player collided with a speed powerup, increases speed
    speed_hit_list = pygame.sprite.spritecollide(player, speed_list, True)
   
    for block in speed_hit_list:
        if lives > 0:
            change_x += 5
            change_y += 5
            speed_sound = pygame.mixer.Sound("speed_power_up.wav")
            speed_sound.play()
   
    for block in virus_hit_list:
        if lives > 0:
            #Subtract a life when player collides with a virus
            lives  = lives - 1
            bad_sound = pygame.mixer.Sound("player_hit.wav")
            bad_sound.play()

    for block in power_hit_list:
        #Player is only able to collect lives when they have 2 or less lives left
        #Player is unable to gain lives after they die
        if lives < 3 and lives > 0:
            lives = lives + 1
            life_sound = pygame.mixer.Sound("life_power_up.wav")
            life_sound.play()

  
    #Draw all animated alements onto the screen
    all_sprites_list.draw(screen)

    #Make sure viruses reappear on the screen
    virus.reset_pos()
    virus_list.update()

    #Update the Powerup
    power_up.reset_pos()
    power_list.update()
   
    s_power.reset_pos()
    speed_list.update()
   

    #Death message when user runs out of lives
    if lives <= 0:
       
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 150, True, False)
        #Render the text
        text = font.render("You died",True,RED)
        screen.blit(text, [240, 290])

        ##Stops the timer
        #Font of Timer text
        font = pygame.font.SysFont('Courier New', 35, True, False)
        ##(CODE FROM TIMER EXAMPLE)
        # Calculate total seconds
        total_seconds = frame_count // frame_rate
        # Divide by 60 to get total minutes
        minutes = total_seconds // 60
        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60
        # Use python string formatting to format in leading zeros
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
        # Blit to the screen
        text = font.render(output_string, True, WHITE)
        screen.blit(text, [385, 405])
        timer_speed = 0

        frame_count = frame_count + timer_speed
               
    if lives == 0:
        death_sound = pygame.mixer.Sound("player_die_sound.wav")
        death_sound.play()
        #Make sure that the death sound doesn't keep playing
        lives = lives - 1
        #Stop background music
        background_music.stop()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
