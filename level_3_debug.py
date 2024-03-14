import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

font = pygame.font.Font(None, 36)

# debugging_code = "def debug_code(code):\n    # Add debugging logic here\n    return code"

def execute_debugging_code(user_code):
    pass

def shuffle_code():
    code = [4, 3, 8, 7]
    code = [code[-1]] + code[:-1]
    return code

def check_code(code):
    return code == [4, 3, 8, 7]


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Code Decipher")

code = [0, 0, 0, 0]  
code_rects = [pygame.Rect(200 + i * 100, 200, 80, 80) for i in range(4)]
dragging = False
selected_rect = None
mouse_offset = (0, 0)
door_open = False


running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 100 < event.pos[0] < 700 and 50 < event.pos[1] < 150:
                pass
            for rect in code_rects:
                if rect.collidepoint(event.pos):
                    dragging = True
                    selected_rect = rect
                    mouse_offset = (rect.x - event.pos[0], rect.y - event.pos[1])
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            if selected_rect:
                selected_rect = None
        elif event.type == pygame.MOUSEMOTION:
            if dragging and selected_rect:
                selected_rect.x = event.pos[0] + mouse_offset[0]
                selected_rect.y = event.pos[1] + mouse_offset[1]

    pygame.draw.rect(screen, GRAY, (100, 50, 600, 100))
    debug_code_surface = font.render(debugging_code, True, BLACK)
    screen.blit(debug_code_surface, (110, 60))

    for rect, digit in zip(code_rects, code):
        pygame.draw.rect(screen, GRAY, rect)
        text_surface = font.render(str(digit), True, BLACK)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

    if check_code(code):
        door_open = True

    door_color = GREEN if door_open else RED
    pygame.draw.rect(screen, door_color, (300, 450, 200, 100))
    door_text = font.render("Door", True, BLACK)
    door_text_rect = door_text.get_rect(center=(400, 500))
    screen.blit(door_text, door_text_rect)

    pygame.display.flip()

pygame.quit()

