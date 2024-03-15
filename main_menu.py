import pygame
import sys
import os
import level_1_block_code
import level_2_forest
import level_3_debug
import level_4_maze

pygame.init()

WIDTH = 1000
HEIGHT = 512 
FONT = pygame.font.SysFont("comicsans", 30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labyrinth game")

BG_IMAGES = [
    pygame.image.load(os.path.join('level_1_block_code','level_1_city_ruins_bg.png')),
    pygame.image.load(os.path.join('level_2_forest', 'level_2_trees_bg.png')),
    #basementa -> ina da si krusti file-a
    pygame.image.load(os.path.join('level_3_debug', 'level_3_basement.png')),
    pygame.image.load(os.path.join('level_4_maze', 'level_4_maze_bg.png')),
]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


def run_level_1(screen):
    # Your logic for level 1 here
    pass

def run_level_2(screen):
    # Your logic for level 2 here
    pass

def run_level_3(screen):
    # Your logic for level 3 here
    pass

def run_level_4(screen):
    pass

def draw_main_menu(screen):
    screen.fill(BLACK)
    
    # Draw background images for level buttons
    #INA AKO IMA VREME I ISKA DA RISUVA BUTONI
    button_width = 200
    button_height = 100
    num_levels = len(BG_IMAGES)
    for i in range(num_levels):
        button_x = i * (button_width + 20) + 20
        button_y = HEIGHT // 2 - button_height // 2
        pygame.draw.rect(screen, WHITE, (button_x, button_y, button_width, button_height))
        screen.blit(pygame.transform.scale(BG_IMAGES[i], (button_width, button_height)), (button_x, button_y))
        text_surface = FONT.render(f"Level {i+1}", True, BLACK)
        text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(text_surface, text_rect)

def main_menu():
    while True:
        draw_main_menu(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                button_width = 200
                button_height = 100
                num_levels = len(BG_IMAGES)
                for i in range(num_levels):
                    button_x = i * (button_width + 20) + 20
                    button_y = HEIGHT // 2 - button_height // 2
                    if button_x <= x <= button_x + button_width and button_y <= y <= button_y + button_height:
                        #TUKA EDIN BOG ZNAE KVO SE SLUCHVA
                        # Execute the corresponding level function
                        if i == 0:
                            run_level_1(screen)
                        elif i == 1:
                            run_level_2(screen)
                        elif i == 2:
                            run_level_3(screen)
                        elif i == 3:
                            run_level_4(screen)

if __name__ == "__main__":
    main_menu()
