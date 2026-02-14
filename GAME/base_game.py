import pickle
print ("THE ONE PIECE IS REAL")
# Example file showing a circle moving on screen
import pygame
from pygame import *
jumping = False
# pygame setup
pygame.init()
velocity_y = 0
floor = 620
gravity = 1
jump_strength = -20
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, 620)
save_file = "save.pkl"
player_dim = 40
button_pos = pygame.Vector2(0,0)
button_size = pygame.Vector2(100,100)
blocks = [
    Rect(screen.get_width()/2, screen.get_height()/2+100, 50, 50)
]
try:
    with open(save_file ,'rb') as file:
        player_pos = pickle.load(file)
        print (player_pos)
except (OSError,pickle.PickleError):
    print ('fout')

def button_clicked():
    print ("bob")
    mouse_pos = event.type == pygame.get_pos()
    print (mouse_pos)
    return(mouse_pos)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    pygame.draw.rect(screen,"blue",(button_pos,button_size))
    pygame.draw.circle(screen, "red", player_pos, player_dim)
    
    for block in blocks:
        pygame.draw.rect(screen,"blue",block)
        mid = Vector2(block.left + block.width/2,block.top + block.height/2)
        horz_inside = player_pos.x >= block.left and player_pos.x <= block.left + block.width

        dst_left = mid.x - player_pos.x + player_dim
        dst_right = player_pos.x - mid.x - player_dim
        dst_top = mid.y - (player_pos.y + player_dim)
        dst_bot = player_pos.y - mid.y -  player_dim
        player = Rect((player_pos.x - player_dim, player_pos.y - player_dim),(player_dim*2,player_dim*2)) 

        # left = player_pos.x >= block.left and player_pos.x < block.left + block.width/2

        # right = player_pos.x <= block.left + block.width and player_pos.x > block.left + block.width/2

        # above = player_pos.y >= block.top and player_pos.y < block.top + block.height/2

        # under = player_pos.y <= block.top + block.height and player_pos.y > block.top + block.height/2
        # if left and (above or under):
        #     player_pos.x -= 10
        # if right and (above or under):
        #     player_pos.x += 10
        # if above and (right or left):
        #     player_pos.y -= 10
        # if under and (right or left):
        #     player_pos.y += 10
        print (dst_top)
        if (dst_top > 0 and dst_top < block.height/2 and horz_inside):
            velocity_y = 0
            player_pos.y -= 0.5
        # if block.colliderect (player):
            


    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        if player_pos.x >= 0 + 20:
            player_pos.x -= 300 * dt
    
    if keys[pygame.K_1]:
        button_clicked
    
    if keys[pygame.K_0]:
        print (player_pos)

    if keys[pygame.K_d]:
        if player_pos.x <= screen.get_width() - 20:
            player_pos.x += 300 * dt

    # Trigger jump on KEYDOWN (not held down)
    if keys[pygame.K_SPACE] and not jumping:
            jumping = True
            velocity_y = jump_strength

    # Apply Gravity
    player_pos.y += velocity_y
    velocity_y += gravity

    # Ground Collision
    if player_pos.y >= floor:
        player_pos.y = floor
        jumping = False
        velocity_y = 0


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(100) / 1000
pygame.quit()
try:
    with open("save.pkl", 'wb') as file:
        pickle.dump(player_pos,file, protocol=pickle.HIGHEST_PROTOCOL)
except (OSError, pickle.PickleError) as e:
    print ('fout')