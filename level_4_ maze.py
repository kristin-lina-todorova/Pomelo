import pygame
import sys
import os
from io import StringIO
from level_4_compile import execute_python_code
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 512 

COMP_WIDTH = 40
COMP_HEIGHT = 30

BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50

FONT = pygame.font.SysFont("comicsans", 30)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Labyrinth game")

BG_IMAGE = pygame.image.load(os.path.join('assets', '436175.png'))
BG = pygame.transform.scale(BG_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT)) 

FLOOR_IMAGE = pygame.image.load(os.path.join('assets', 'maze.png'))

COMPUTER_IMAGE = pygame.image.load(os.path.join('assets', 'download (1).jpg'))
COMPUTER = pygame.transform.scale(COMPUTER_IMAGE, (COMP_WIDTH,COMP_HEIGHT))

PLAYER_IMAGE = pygame.image.load(os.path.join('assets', 'Untitled.png'))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (39, 42, 46)

MAZE_MAP = [

"+++++++++++++++++++++++++++++++++++++++++++++",
"+         +    +                +           +",
"+ +++  ++++  + + +++++++++  +++ + +++++++++ +",
"+   +        +   +            + +         + +",
"+++ +++++  +++ +   +++++++++  + + +++++++++ +",
"+ + +   +    + +   +   +      + + +   +     +",
"+ + +   ++++++ +++ +   +  ++  + + +   +  ++ +",
"+ + +   +        + +   +  +   +   +   +   + +",
"+ + +++ +  +++ + + +++ +  +++ + + +++ +++ + +",
"+   + + +  +   + + + + +    + + +     +   + +",
"+ +++ + +  +++ + + + + +++  + + + +++++  ++ +",
"+ +   + +    + +     +      +   +   +     + +",
"+ +++ + +++  + + +++++ ++++++   +++ +++++ + +",
"+     +      + +              +   +       + +",
"+ +++++++  +++++ ++++++++++++ +++++++ +++++ +",
"+ +   +                  +            +   + +",
"+ +   +                  +            +   + +",
"+ + +   +  + + + +++++ +   +  + + +++   + + +",
"+ + +   +  + + + +     +   +  + +   +   + + +",
"+   +++++  +++ +++ +++++++++  + + + +++++ + +",
"+   +   +    + +   +     +    + + + +   + + +",
"+++++   +  + + + +++     +  +++ +++ +   + + +",
"+   +   +  +   +   +     +  + +     +   +   +",
"+ + +++ +  + + +++ +     +  + + + +++++ +++ +",
"+ +   + +  + + +   +     +  + + +   +   + + +",
"+ +++ + +  + + +++++++ +++  + + +++ + +++ + +",
"+   +   +  + + +     + + +    + +   + +   + +",
"+++ ++++++++ + + +++ + +  ++  + + +++ +   + +",
"+            +     +   +        +     + +   +",
"+ ++++++++++ +++ +++++++++++  +++++++ + +++++",
"+ +            +              +             +",
"+ + ++++++++++ +++++++ ++++++++ +++++++++ + +",
"+ +     +    +   +              +         + +",
"+ + +++++  + + + + +++ ++++++++++ +++++++++ +",
"+   +   +  +   + +   +        +   +   +   + +",
"+   +   +  +   + +   +        +   +   +   + +",
"+ +++   +  +++ + + +++++++++  + +++   + + + +",
"+   +   +    + + + +   +          +   + +   +",
"+ +++++ ++++ + + + +   +  ++  +++ +++ +++  ++",
"+ +     +    + +   +   +   +  +     +       +",
"+++ +++++  +++ +++++++ +++ +  + +++++++++++ +",
"+   +        +         +   +  +           + +",
"+ +++++++  + + + +++++++  ++  + +++++++++ + +",
"+          +   +          +   +         +   +",
"+++++++++++++++++++++++++++++++++++++++++++++"
]

CELL_SIZE = min(SCREEN_WIDTH // len(MAZE_MAP[0]), SCREEN_HEIGHT // len(MAZE_MAP))

PLAYER = pygame.transform.scale(PLAYER_IMAGE, (CELL_SIZE, CELL_SIZE))

MAZE_WIDTH = len(MAZE_MAP[0]) * CELL_SIZE
MAZE_HEIGHT = len(MAZE_MAP) * CELL_SIZE

FLOOR = pygame.transform.scale(FLOOR_IMAGE, (MAZE_WIDTH, MAZE_HEIGHT))

MAZE_X = (SCREEN_WIDTH - MAZE_WIDTH) // 2
MAZE_Y = (SCREEN_HEIGHT - MAZE_HEIGHT) // 2

code_output = ""


def open_task_window():
    button = pygame.Rect(SCREEN_WIDTH//2 - BUTTON_WIDTH//2, SCREEN_HEIGHT - BUTTON_HEIGHT - 10, BUTTON_WIDTH, BUTTON_HEIGHT)

    font = pygame.font.SysFont("comicsansms", 24)
    surf = font.render('Submit', True, 'white')

    task_screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("Task Code")
    task_screen.fill(GRAY)

    task_code = "Napishi programa"

    input_text = "" 

    
    input_font = pygame.font.SysFont("comicsansms", 20)

    running = True
    
    task_screen.fill(GRAY) 

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                a,b = pygame.mouse.get_pos()
                if button.x <= a <= button.x + BUTTON_WIDTH and button.y <= b <= button.y + BUTTON_HEIGHT:
                    result = execute_python_code(input_text)
                    print(result)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_text += '\n'

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                    
                    task_screen.fill(GRAY) 
                else:
                    input_text += event.unicode

        a,b = pygame.mouse.get_pos()
        if button.x <= a <= button.x + BUTTON_WIDTH and button.y <= b <= button.y + BUTTON_HEIGHT:
            pygame.draw.rect(screen,(180,180,180),button )
        else:
            pygame.draw.rect(screen, (110,110,110),button)
        screen.blit(surf,(button.x +5, button.y+5))
        pygame.display.update()


        lines = task_code.split("\n")
        y_offset = 50
        for line in lines:
            text_surface = font.render(line, True, WHITE)
            task_screen.blit(text_surface, (50, y_offset))
            y_offset += 30

        show_code(input_text, task_screen)

        pygame.display.flip()  

    pygame.quit()

def show_code(input_text, task_screen):
    input_font = pygame.font.SysFont("arial", 20)
    input_lines = input_text.split("\n")
    y_offset = SCREEN_HEIGHT // 2 - 50
    for line in input_lines:
        input_surface = input_font.render(line, True, WHITE)
        task_screen.blit(input_surface, (50, y_offset))
        y_offset += input_font.get_height() + 5  


def main():

    comp = pygame.Rect( SCREEN_WIDTH//2 - COMP_WIDTH//2, SCREEN_HEIGHT//2 - COMP_HEIGHT//2, COMP_WIDTH, COMP_HEIGHT)

    player_pos = None
    for y, row in enumerate(MAZE_MAP):
        for x, cell in enumerate(row):
            if cell == " ":
                player_pos = (MAZE_X + x * CELL_SIZE, MAZE_Y + y * CELL_SIZE)
                break
        if player_pos:
            break

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(20)
        screen.blit(BG, (0, 0))
        #screen.blit(FLOOR, (MAZE_X, MAZE_Y))
        screen.blit(COMPUTER, (comp.x, comp.y))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        for y, row in enumerate(MAZE_MAP):
            for x, cell in enumerate(row):
                if cell == "+":
                    pygame.draw.rect(screen, WHITE, (MAZE_X + x * CELL_SIZE, MAZE_Y + y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        
        ddz = pygame.Rect(player_pos[0], player_pos[1], CELL_SIZE, CELL_SIZE)
        screen.blit(PLAYER, (ddz.x,ddz.y))

        player_rect = pygame.Rect(player_pos[0], player_pos[1], CELL_SIZE, CELL_SIZE)
        comp_rect = pygame.Rect(comp.x, comp.y, COMP_WIDTH, COMP_HEIGHT)
        
        screen.blit(PLAYER, (player_rect.x, player_rect.y))

        if player_rect.colliderect(comp_rect):
            open_task_window()


        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_k]:
            open_task_window()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if MAZE_MAP[int((player_pos[1] - MAZE_Y) // CELL_SIZE)][int((player_pos[0] - MAZE_X - CELL_SIZE) // CELL_SIZE)] == " ":
                player_pos = (player_pos[0] - CELL_SIZE, player_pos[1])
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if MAZE_MAP[int((player_pos[1] - MAZE_Y) // CELL_SIZE)][int((player_pos[0] - MAZE_X + CELL_SIZE) // CELL_SIZE)] == " ":
                player_pos = (player_pos[0] + CELL_SIZE, player_pos[1])
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if MAZE_MAP[int((player_pos[1] - MAZE_Y - CELL_SIZE) // CELL_SIZE)][int((player_pos[0] - MAZE_X) // CELL_SIZE)] == " ":
                player_pos = (player_pos[0], player_pos[1] - CELL_SIZE)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if MAZE_MAP[int((player_pos[1] - MAZE_Y + CELL_SIZE) // CELL_SIZE)][int((player_pos[0] - MAZE_X) // CELL_SIZE)] == " ":
                player_pos = (player_pos[0], player_pos[1] + CELL_SIZE)


    pygame.quit()
    sys.exit()

main()
