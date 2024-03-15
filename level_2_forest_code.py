import pygame
import sys
import tkinter as tk
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

WIDTH = 1000
HEIGHT = 512

FONT = pygame.font.SysFont("comicsans", 30)

num = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game with python!")

tile_size = 20
BG = pygame.transform.scale(pygame.image.load("level_2_trees_bg.png"), (WIDTH, HEIGHT))

class Player(): 
    def __init__(self, x, y):
        img = pygame.image.load('jay.png')
        self.image = pygame.transform.scale(img, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.vel_x = 1

    def update(self):
        dx = 0
        dy = 0
        num = 0
        # get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -15
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
        if key[pygame.K_RIGHT]:
            dx += 5

        # add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        question_displayed = False
        for tile_group in world.tile_groups:
            for tile in tile_group.tile_list:
                if tile[1].colliderect(self.rect.move(dx, 0)):
                    # choveka udrq platformata nastrani
                    dx = 0
                    if not tile_group.visited:
                        show_question()
                        tile_group.visited = True
                        question_displayed = True
                if tile[1].colliderect(self.rect.move(0, dy)):
                    # choveka udrq platformata nadolu
                    if not tile_group.visited:
                        show_question()
                        tile_group.visited = True
                        question_displayed = True
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                

        # update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            dy = 0

        # draw player onto screen
        screen.blit(self.image, self.rect)


class TileGroup():
    def __init__(self, data):
        self.tile_list = data
        self.visited = False

class World():
    def __init__(self, data):
        self.tile_list = []
        self.tile_groups = []

        dirt_img = pygame.image.load('dot2.png')

        row_count = 0
        for row in data:
            col_count = 0
            
            tiles_in_group = []
            for tile in row:
                if tile == 1:
                    # start group
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    tiles_in_group.append(tile)
                col_count += 1

            if (len(tiles_in_group) > 0):
                self.tile_groups.append(TileGroup(tiles_in_group))
            row_count += 1

    def draw(self):
        for tile_group in self.tile_groups:
            for tile in tile_group.tile_list:
                screen.blit(tile[0], tile[1])
                pygame.draw.rect(screen, (255, 205, 255), tile[1], 2)

world_data = [
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
]


player = Player(0, 0)
world = World(world_data)

def draw(screen):
    screen.blit(BG, (0, 0))
    world.draw()
    player.update()
    pygame.display.update()


questions = ["What is 2 + 2?", "What is the capital of France?", "Who wrote 'Romeo and Juliet'?", "What is 3 + 4?", "What is 1 + 1?"]
answers = ["4", "Paris", "WS", "7", "2"]

def show_question():
    global root, question_displayed
    root = tk.Tk()
    root.geometry("300x100")
    root.title("Answer the Question")

    label = tk.Label(root, text=questions[num])
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    message_label = tk.Label(root, text="", fg="red")  # Етикет за съобщенията
    message_label.pack()

    def check_answer():
        global num
        print(num)

        answer = entry.get()
        if answer.lower() == answers[num].lower():
            root.destroy() 
            question_displayed = False
            num += 1
        else:
            message_label.config(text="Incorrect answer")


    button = tk.Button(root, text="Submit", command=check_answer)
    button.pack()

    def on_closing():
        root.destroy(),
        question_displayed = False
        show_question(num)

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

question_displayed = False 

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(60)

    draw(screen)

    if not question_displayed:
        if pygame.mouse.get_pressed()[2]:
            x, y = pygame.mouse.get_pos()
            if player.rect.collidepoint(x, y):
                show_question(num)
    if question_displayed:
        root.update()
        if not root.winfo_exists():
            question_displayed = False


pygame.quit()
sys.exit()
