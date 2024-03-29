import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 512

BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

FONT = pygame.font.SysFont("comicsans", 32)

BG = pygame.transform.scale(pygame.image.load("level_3_debug\level_3_basement_bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

button = pygame.Rect(SCREEN_WIDTH//2 - BUTTON_WIDTH//2, SCREEN_HEIGHT - BUTTON_HEIGHT - 10, BUTTON_WIDTH, BUTTON_HEIGHT)

correct_debugged_code = """def shift_digits(number):
    shift_value = 3
    shifted_number = ""
    for digit in str(number):
        shifted_digit = (int(digit) + shift_value) % 10
        shifted_number += str(shifted_digit)
        shift_value += 2
        
    return int(shifted_number)

original_number = 4387
shifted_number = shift_digits(original_number)
print(f"Original number: {original_number}")
print(f"Shifted number: {shifted_number}") """

wrong_debugged_code = """"def shift_digits(number):
    shift_value = 3
    shifted_number = ""
    for digit in str(number):
        shifted_digit = digit + shift_value % 10
        shifted_digit += str(shifted_digit)
        shift_value += 4
        
    return int(shifted_number)

original_number = 4387
shifted_number = shift_number(original_number)
print(f"Original number: {original_number}")
print(f"Shifted number: {shifted_number}") """

rules_text = [
        "Debug the provided code to get the combination.",
        "Enter the 4-digit combination to unlock the door.",
        "Click on the boxes on the door to enter digits.",
        "Click 'Submit' after debugging code to check the combination."
    ]

original_code = "4387"
correct_code = "7856"

def draw_main_screen(screen):
    screen.fill(BG)
    pygame.draw.rect(screen, WHITE, (50, 50, 700, 200))  
    pygame.draw.rect(screen, BLACK, (50, 300, 700, 250))  

    for i, text in enumerate(rules_text):
        text_surface = FONT.render(text, True, BLACK)
        screen.blit(text_surface, (70, 70 + i * 40))

    submit_button = pygame.Rect(350, 500, 100, 50)
    pygame.draw.rect(screen, BLACK, submit_button)
    submit_text = FONT.render("Submit", True, WHITE)
    screen.blit(submit_text, (submit_button.x + 20, submit_button.y + 15))

    entered_text = FONT.render("Entered Code: " + entered_code, True, BLACK)
    screen.blit(entered_text, (50, 275))

    pygame.display.flip()

def draw_debug_window(screen):
    pygame.draw.rect(screen, GRAY, (100, 100, 600, 400))  
    pygame.draw.rect(screen, BLACK, (300, 520, 200, 50))  

    debug_text = FONT.render("Debug Code:", True, BLACK)
    screen.blit(debug_text, (110, 110))

    pygame.display.flip()

def handle_debug_events(screen):
    global entered_code

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    entered_code = entered_code[:-1]
                elif event.key == pygame.K_RETURN:
                    return
                else:
                    entered_code += event.unicode

        screen.fill(WHITE)
        draw_debug_window(screen)
        pygame.display.flip()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Debugging Game")

    global entered_code

    attempts = 0
    unlocked = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 50 <= x <= 300 and 300 <= y <= 550:  
                    digit = str((x - 50) // 50)
                    if len(entered_code) < 4:
                        entered_code += digit
                elif 350 <= x <= 450 and 500 <= y <= 550:  
                    if len(entered_code) == 4:
                        if entered_code == correct_code:
                            unlocked = True
                        else:
                            attempts += 1
                            entered_code = ""
                    else:
                        attempts += 1
                        entered_code = ""

        screen.fill(WHITE)
        draw_main_screen(screen)

        if unlocked:
            unlocked_text = FONT.render("Door Unlocked! Proceed to Next Level.", True, GREEN)
            screen.blit(unlocked_text, (200, 550))
        elif attempts >= 3:
            attempts_text = FONT.render("Max Attempts Reached! Game Over.", True, RED)
            screen.blit(attempts_text, (250, 550))
        else:
            if len(entered_code) == 4:
                attempts_text = FONT.render("Wrong Code! Attempts: " + str(attempts), True, RED)
                screen.blit(attempts_text, (300, 550))

        pygame.display.flip()

        if not unlocked and attempts < 3:
            if len(entered_code) < 4:
                handle_debug_events(screen)

    pygame.quit()
    sys.exit()

def run_level(screen):
    pygame.init()
    clock = pygame.time.Clock()
    
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Level 2")

    run_level(screen)
