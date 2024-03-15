import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 5120

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


font = pygame.font.Font(None, 32)

correct_code = "1234"
entered_code = ""

def draw_main_screen(screen):
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, (50, 50, 700, 200))  
    pygame.draw.rect(screen, BLACK, (50, 300, 700, 250))  


    rules_text = [
        "Debug the provided code to get the combination.",
        "Enter the 4-digit combination to unlock the door.",
        "Click on the boxes on the door to enter digits.",
        "Click 'Submit' after debugging code to check the combination."
    ]
    for i, text in enumerate(rules_text):
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (70, 70 + i * 40))

    submit_button = pygame.Rect(350, 500, 100, 50)
    pygame.draw.rect(screen, BLACK, submit_button)
    submit_text = font.render("Submit", True, WHITE)
    screen.blit(submit_text, (submit_button.x + 20, submit_button.y + 15))

    entered_text = font.render("Entered Code: " + entered_code, True, BLACK)
    screen.blit(entered_text, (50, 275))

    pygame.display.flip()

def draw_debug_window(screen):
    pygame.draw.rect(screen, GRAY, (100, 100, 600, 400))  
    pygame.draw.rect(screen, BLACK, (300, 520, 200, 50))  

    debug_text = font.render("Debug Code:", True, BLACK)
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
            unlocked_text = font.render("Door Unlocked! Proceed to Next Level.", True, GREEN)
            screen.blit(unlocked_text, (200, 550))
        elif attempts >= 3:
            attempts_text = font.render("Max Attempts Reached! Game Over.", True, RED)
            screen.blit(attempts_text, (250, 550))
        else:
            if len(entered_code) == 4:
                attempts_text = font.render("Wrong Code! Attempts: " + str(attempts), True, RED)
                screen.blit(attempts_text, (300, 550))

        pygame.display.flip()

        if not unlocked and attempts < 3:
            if len(entered_code) < 4:
                handle_debug_events(screen)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
