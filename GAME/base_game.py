print ("THE ONE PIECE IS REAL")
# Example file showing a circle moving on screen
import pygame
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
player_pos = pygame.Vector2(screen.get_width() / 2, floor)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.rect(screen,"red",200,200)

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        if player_pos.x >= 0 + 20:
            player_pos.x -= 300 * dt

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

    # limits FPS to 100
    # dt is delta time in seconds since last frame, used for framerate
    # independent physics.
    dt = clock.tick(100) / 1000
    print (player_pos)
pygame.quit()