import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Game")

#set up sprites and other variables

ship_rect = [300,500,45,27]
ship_image = pygame.image.load('ship.png')
gameover = False
clock = pygame.time.Clock()

#game loop starts here
while not gameover:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                gameover = True
            #other key events here that happen ONCE when you press
                
    #keys that you can hold down:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        ship_rect[0] += 5
    if keys[pygame.K_LEFT]:
        ship_rect[0] -= 5
            
    #actions that happen automatically.
        
    #move stuff
                 
    #handle collisions

    #clear the screen
    screen.fill((0,0,0))
    
    #draw stuff
    screen.blit(ship_image, ship_rect)

    #show the new screen (60x per second).
    pygame.display.flip()

pygame.quit()
    

