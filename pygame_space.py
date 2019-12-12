import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Game")

#set up sprites and other variables

enemies = []
bullets = []

ship_rect = [300,500,45,27]
ship_image = pygame.image.load('ship.png')
enemy_image = pygame.image.load('enemy.png')
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
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(ship_rect[0] + 22, ship_rect[1], 5, 5)
                bullets.append(bullet)
            
                
    #keys that you can hold down:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        ship_rect[0] += 5
    if keys[pygame.K_LEFT]:
        ship_rect[0] -= 5
            
    #actions that happen automatically.
    if randint(1, 10) == 1:
        new_enemy = pygame.Rect(randint(0, 760), -50, 40, 33)
        enemies.append(new_enemy)
        
        
    #move stuff

    for enemy in enemies:
        enemy[1] += 10
    for bullet in bullets:
        bullet[1] -= 8
                 
    #handle collisions
    for enemy in enemies.copy():
        for bullet in bullets.copy():
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)

    #clear the screen
    screen.fill((0,0,0))
    
    #draw stuff
    screen.blit(ship_image, ship_rect)

    for enemy in enemies:
        screen.blit(enemy_image, enemy)

    for bullet in bullets:
        pygame.draw.ellipse(screen, (200,200,0), bullet)

    #show the new screen (60x per second).
    pygame.display.flip()

pygame.quit()
    

