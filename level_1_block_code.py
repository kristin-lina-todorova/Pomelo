import pygame
import random

pygame.font.init()

WIDTH = 1000
HEIGHT = 512

BOX_WIDTH_SIZE, BOX_HEIGHT_SIZE = 50, 50

FONT = pygame.font.SysFont("comicsans", 30)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tech Traveller")

BG = pygame.transform.scale(pygame.image.load("bg.png"), (WIDTH, HEIGHT))

box1 = pygame.Rect(50, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200, BOX_WIDTH_SIZE, BOX_HEIGHT_SIZE)
box2 = pygame.Rect(50, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 100, BOX_WIDTH_SIZE, BOX_HEIGHT_SIZE)
box3 = pygame.Rect(50, HEIGHT/2 - BOX_HEIGHT_SIZE/2, BOX_WIDTH_SIZE, BOX_HEIGHT_SIZE)
box4 = pygame.Rect(50, HEIGHT/2 - BOX_HEIGHT_SIZE/2 + 100, BOX_WIDTH_SIZE, BOX_HEIGHT_SIZE)
box5 = pygame.Rect(50, HEIGHT/2 - BOX_HEIGHT_SIZE/2 + 200, BOX_WIDTH_SIZE, BOX_HEIGHT_SIZE)

places = [
    pygame.Rect(WIDTH/2 - BOX_WIDTH_SIZE/2, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200, BOX_WIDTH_SIZE, BOX_HEIGHT_SIZE),
    pygame.Rect(WIDTH/2 - BOX_WIDTH_SIZE/2, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 100, BOX_WIDTH_SIZE, BOX_HEIGHT_SIZE),
    pygame.Rect(WIDTH/2 - BOX_WIDTH_SIZE/2, HEIGHT/2 - BOX_HEIGHT_SIZE/2, BOX_WIDTH_SIZE, BOX_HEIGHT_SIZE),
    pygame.Rect(WIDTH/2 - BOX_WIDTH_SIZE/2, HEIGHT/2 - BOX_HEIGHT_SIZE/2 + 100, BOX_WIDTH_SIZE, BOX_HEIGHT_SIZE),
    pygame.Rect(WIDTH/2 - BOX_WIDTH_SIZE/2, HEIGHT/2 - BOX_HEIGHT_SIZE/2 + 200, BOX_WIDTH_SIZE, BOX_HEIGHT_SIZE)
]

boxes = [box1, box2, box3, box4, box5]

def draw(places, boxes):
    WIN.blit(BG, (0, 0))
    for place in places:
        pygame.draw.rect(WIN, "blue", place, 2) 
    for box in boxes:
        pygame.draw.rect(WIN, "purple", box)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    active_box = None  

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for num, box in enumerate(boxes):
                        if box.collidepoint(event.pos):
                            active_box = num
            if event.type == pygame.MOUSEMOTION:
                if active_box is not None:
                    boxes[active_box].move_ip(event.rel)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if active_box is not None:
                        for place in places:
                            if place.colliderect(boxes[active_box]):
                                boxes[active_box].center = place.center
                        active_box = None
            if event.type == pygame.QUIT:
                run = False
                break

        draw(places, boxes)

    pygame.quit()

if __name__ == "__main__":
    main()
