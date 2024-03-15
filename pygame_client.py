import pygame
import requests
import os
import sys

# Initialize Pygame
pygame.init()

WIDTH = 1000
HEIGHT = 512 
FONT = pygame.font.SysFont("comicsans", 30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Labyrinth game")

BG_IMAGE = pygame.image.load(os.path.join('level_4_maze', 'level_4_maze_bg.png'))
BG = pygame.transform.scale(BG_IMAGE, (WIDTH, HEIGHT)) 

COMPUTER_IMAGE = pygame.image.load(os.path.join('level_4_maze', 'level_4_maze_broken_pc.jpg'))
COMPUTER = pygame.transform.scale(COMPUTER_IMAGE, (50, 50))

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
    "+ +++ + +  + + +++++++ +++  + + +++ + +++ +",
    "+   +   +  + + +     + + +    + +   + +",
    "+ +++ + +  + + + +++ + +  ++  + + +++ +   + +",
    "+   +   +  + + +   +   +        +     + +   +",
    "+ +++++ ++++ + + +++ + ++++++++++++++ + +++++",
    "+ +     +    +   +     +             + +    +",
    "++++ +++++  +++ ++++++++ ++++++++++++ +++++ +",
    "+          +   +          +            +   +",
    "+ ++++++++++ +++ +++++++++  +++++++++++ + +",
    "+            +              +            + +",
    "+ ++++++++++ +++++++++++++++ ++++++++++ + +",
    "+ +        + +              + +        + + +",
    "+ +++++++ +++++ ++++++++++ +++++ +++++ + + +",
    "+       +     + +         + +    +     + + +",
    "+ +++++ +++++++ ++++++++++ + +++++ ++++ + +",
    "+     + +      + +         +       +     + +",
    "+ ++++ + +++++++ +++++++++++ +++++ +++++ + +",
    "+ +   + + +           +     + +     +     + +",
    "+ + + + + +++++++++++ +++++ + +++++ +++++ + +",
    "+ + + + +          +      + +     + +     + +",
    "+ + + + ++++++++++ ++++++++ +++++ + +++++ + +",
    "+ + + +         + +         +     +     + + +",
    "+ + + +++++++++ + +++++++++ +++++ +++++ + + +",
    "+ + + +     +   + +         +     +     + + +",
    "+ + ++++++ +++++ + +++++++++ +++++ +++++ + +",
    "+ +         +   + +         + +   + +   + + +",
    "+ +++++++++++ + + +++++++++ + + + + + + + + +",
    "+             +   +         + + + + + + + + +",
    "+ +++++++++++ +++++++++++++ + + + + +",
    "+ +           +               + + + + + + + +",
    "+ ++++++++++++++++++++++++++++ + + + + + + +",
    "+                              + + + + + + +",
    "++++++++++++++++++++++++++++++++++++++++++++++++"
]

CELL_SIZE = min(WIDTH // len(MAZE_MAP[0]), HEIGHT // len(MAZE_MAP))

MAZE_WIDTH = len(MAZE_MAP[0]) * CELL_SIZE
MAZE_HEIGHT = len(MAZE_MAP) * CELL_SIZE
MAZE_X = (WIDTH - MAZE_WIDTH) // 2
MAZE_Y = (HEIGHT - MAZE_HEIGHT) // 2

# Define the URL for the Flask server
FLASK_URL = 'http://localhost:5000/compile'

# Function to compile code using Flask server
def compile_code(code):
    response = requests.post(FLASK_URL, json={'code': code})
    result = response.json().get('output', 'Error: No output received.')
    return result

# Function to display text on the screen
def display_text(text, x, y, color=WHITE):
    text_surface = FONT.render(text, True, color)
    screen.blit(text_surface, (x, y))

def run_level(screen):
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
        clock.tick(40)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for y, row in enumerate(MAZE_MAP):
            for x, cell in enumerate(row):
                if cell == "+":
                    pygame.draw.rect(screen, WHITE, (MAZE_X + x * CELL_SIZE, MAZE_Y + y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(screen, GREEN, (player_pos[0], player_pos[1], CELL_SIZE, CELL_SIZE))

        # Display computer icon
        screen.blit(COMPUTER, (WIDTH // 2 - 25, HEIGHT // 2 - 25))

        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if MAZE_MAP[int((player_pos[1] - MAZE_Y) // CELL_SIZE)][int((player_pos[0] - MAZE_X - CELL_SIZE) // CELL_SIZE)] == " ":
                player_pos = (player_pos[0] - CELL_SIZE, player_pos[1])
        if keys[pygame.K_RIGHT]:
            if MAZE_MAP[int((player_pos[1] - MAZE_Y) // CELL_SIZE)][int((player_pos[0] - MAZE_X + CELL_SIZE) // CELL_SIZE)] == " ":
                player_pos = (player_pos[0] + CELL_SIZE, player_pos[1])
        if keys[pygame.K_UP]:
            if MAZE_MAP[int((player_pos[1] - MAZE_Y - CELL_SIZE) // CELL_SIZE)][int((player_pos[0] - MAZE_X) // CELL_SIZE)] == " ":
                player_pos = (player_pos[0], player_pos[1] - CELL_SIZE)
        if keys[pygame.K_DOWN]:
            if MAZE_MAP[int((player_pos[1] - MAZE_Y + CELL_SIZE) // CELL_SIZE)][int((player_pos[0] - MAZE_X) // CELL_SIZE)] == " ":
                player_pos = (player_pos[0], player_pos[1] + CELL_SIZE)

        # Check if player interacts with the computer
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if WIDTH // 2 - 25 <= mouse_pos[0] <= WIDTH // 2 + 25 and HEIGHT // 2 - 25 <= mouse_pos[1] <= HEIGHT // 2 + 25:
                # Display prompt for user to enter code
                display_text("Enter your Python code:", 50, 50)
                pygame.display.update()
                code_input = ''
                # Get user's input for code
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                # Compile the code
                                result = compile_code(code_input)
                                # Display the result
                                display_text(result, 50, 100)
                                pygame.display.update()
                                break
                            elif event.key == pygame.K_BACKSPACE:
                                code_input = code_input[:-1]
                            else:
                                code_input += event.unicode

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Labyrinth game")

    run_level(screen)

if __name__ == "__main__":
    main()


