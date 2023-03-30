from invasion_game import Game
import pygame

pygame.init()

width, height = 700, 500
window = pygame.display.set_mode((width, height))

game = Game(window, width, height)

not_shot = True

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        game.player.rotate(True)
    if keys[pygame.K_a]:
        game.player.rotate(False)
    
    if not keys[pygame.K_f]:
        not_shot = True
    if not_shot == True and keys[pygame.K_f]:
        game.player.shoot()
        not_shot = False

    game.loop()
    game.draw()
    pygame.display.update()
    pygame.time.Clock().tick(120)

pygame.quit()
    
