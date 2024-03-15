import pygame
import sys
import os
from io import StringIO

pygame.init()

WIDTH = 1000
HEIGHT = 512 

COMP_WIDTH = 40
COMP_HEIGHT = 30
FONT = pygame.font.SysFont("comicsans", 30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Labyrinth game")

BG_IMAGE = pygame.image.load(os.path.join('assets', '436175.png'))
BG = pygame.transform.scale(BG_IMAGE, (WIDTH, HEIGHT)) 

FLOOR_IMAGE = pygame.image.load(os.path.join('assets', 'maze.png'))

COMPUTER_IMAGE = pygame.image.load(os.path.join('assets', 'download (1).jpg'))
COMPUTER = pygame.transform.scale(COMPUTER_IMAGE, (COMP_WIDTH,COMP_HEIGHT))

PLAYER_IMAGE = pygame.image.load(os.path.join('assets', 'Untitled.png'))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

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

CELL_SIZE = min(WIDTH // len(MAZE_MAP[0]), HEIGHT // len(MAZE_MAP))

PLAYER = pygame.transform.scale(PLAYER_IMAGE, (CELL_SIZE, CELL_SIZE))

MAZE_WIDTH = len(MAZE_MAP[0]) * CELL_SIZE
MAZE_HEIGHT = len(MAZE_MAP) * CELL_SIZE

FLOOR = pygame.transform.scale(FLOOR_IMAGE, (MAZE_WIDTH, MAZE_HEIGHT))

MAZE_X = (WIDTH - MAZE_WIDTH) // 2
MAZE_Y = (HEIGHT - MAZE_HEIGHT) // 2

code_output = ""

def compile_and_execute(code):
    global code_output
    stdout_orig = sys.stdout
    sys.stdout = StringIO()
    try:
        exec(code)
        code_output = sys.stdout.getvalue()
    except Exception as e:
        code_output = f"Error: {e}"
    finally:
        sys.stdout = stdout_orig
    print(code_output)


def open_task_window():
    task_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Task Code")
    task_screen.fill(WHITE)

    task_code = "Napishi programa"

    input_text = "" 

    font = pygame.font.SysFont("comicsansms", 24)
    input_font = pygame.font.SysFont("comicsansms", 24)

    running = True
    while running:
        task_screen.fill(WHITE)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("User Input:", input_text)
                    f = open("code_from_task.py", "a")
                    f.write(input_text)
                    f.close()
                    compile_and_execute(input_text)
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        lines = task_code.split("\n")
        y_offset = 50
        for line in lines:
            text_surface = font.render(line, True, BLACK)
            task_screen.blit(text_surface, (50, y_offset))
            y_offset += 30

        input_surface = input_font.render("Input: " + input_text, True, BLACK)
        task_screen.blit(input_surface, (50, HEIGHT - 50))

        pygame.display.flip()  # Update the display

    pygame.quit()



def main():

    comp = pygame.Rect( WIDTH//2 - COMP_WIDTH//2, HEIGHT//2 - COMP_HEIGHT//2, COMP_WIDTH, COMP_HEIGHT)

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
