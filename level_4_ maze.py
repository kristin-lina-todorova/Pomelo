import pygame
import sys
import os

pygame.init()

WIDTH = 1000
HEIGHT = 512  # Adjusted height
FONT = pygame.font.SysFont("comicsans", 30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Labyrinth game")

BG_IMAGE = pygame.image.load(os.path.join('assets', '436175.png'))
BG = pygame.transform.scale(BG_IMAGE, (WIDTH, HEIGHT)) 

COMPUTER_IMAGE = pygame.image.load(os.path.join('assets', 'download (1).jpg'))
COMPUTER = pygame.transform.scale(COMPUTER_IMAGE, ())

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Define maze map
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

# Calculate cell size to fit the screen
CELL_SIZE = min(WIDTH // len(MAZE_MAP[0]), HEIGHT // len(MAZE_MAP))

# Calculate maze size
MAZE_WIDTH = len(MAZE_MAP[0]) * CELL_SIZE
MAZE_HEIGHT = len(MAZE_MAP) * CELL_SIZE

# Calculate maze position to center it on the screen
MAZE_X = (WIDTH - MAZE_WIDTH) // 2
MAZE_Y = (HEIGHT - MAZE_HEIGHT) // 2

# Find player start position




def main():
    player_pos = None
    for y, row in enumerate(MAZE_MAP):
        for x, cell in enumerate(row):
            if cell == " ":
                player_pos = (MAZE_X + x * CELL_SIZE, MAZE_Y + y * CELL_SIZE)
                break
        if player_pos:
            break

    # Main loop
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(40)
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw maze
        for y, row in enumerate(MAZE_MAP):
            for x, cell in enumerate(row):
                if cell == "+":
                    pygame.draw.rect(screen, WHITE, (MAZE_X + x * CELL_SIZE, MAZE_Y + y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Draw player
        pygame.draw.rect(screen, GREEN, (player_pos[0], player_pos[1], CELL_SIZE, CELL_SIZE))

        # Update display
        pygame.display.update()

        # Move player
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

    pygame.quit()
    sys.exit()

main()
