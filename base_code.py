import pygame
import time 
pygame.font.init()

WIDTH = 900
HEIGHT = 700

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5


FONT = pygame.font.SysFont("comicsans", 30)

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Game with python!")  

BG = pygame.transform.scale(pygame.image.load("bg.png"), (WIDTH, HEIGHT)) 

def draw(player):
    
    WIN.blit(BG, (0, 0))
    
    pygame.draw.rect(WIN, "red", player)  
    
    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(400, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    clock = pygame.time.Clock()

    while run:
        
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL

        draw(player)
    pygame.quit()

if __name__ == "__main__":
    main()