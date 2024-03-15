import pygame
import requests

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Maze Game")

# Computer object
computer_rect = pygame.Rect(300, 200, 200, 200)
computer_color = (0, 255, 0)
is_computer_active = False
user_code = ''

# URL for Flask server
URL = 'http://localhost:5000/compile'

# Function to compile user code
def compile_code(code):
    response = requests.post(URL, json={'code': code})
    if response.status_code == 200:
        output = response.json().get('output', '')
        return output
    else:
        return 'Error: Failed to compile code.'

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if computer_rect.collidepoint(event.pos):
                is_computer_active = True
                user_code = ''

        elif event.type == pygame.KEYDOWN:
            if is_computer_active:
                if event.key == pygame.K_RETURN:
                    # Compile the user's code
                    output = compile_code(user_code)
                    print(output)  # Display the output in the console
                    # Provide feedback to the user within the game interface
                    # You can display the output on the screen or trigger other game events based on the output
                    is_computer_active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_code = user_code[:-1]
                else:
                    user_code += event.unicode

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, computer_color, computer_rect)

    # If the computer is active, display the user's code input
    if is_computer_active:
        font = pygame.font.Font(None, 32)
        input_text = font.render(user_code, True, (0, 0, 0))
        screen.blit(input_text, (computer_rect.x + 10, computer_rect.y + 10))

    pygame.display.flip()

pygame.quit()
