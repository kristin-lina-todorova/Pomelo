import pygame
import sys
import tkinter as tk
pygame.init()

WIDTH = 1000
HEIGHT = 512

FONT = pygame.font.SysFont("comicsans", 30)

num = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Techscape")

tile_size = 20
bg_images = [pygame.transform.scale(pygame.image.load(f"level_2_portal_{i}.png"), (WIDTH, HEIGHT)) for i in range(1, 3)]
num_images = len(bg_images)
current_image = 0

class Player():
    def __init__(self, x, y):
        clock = pygame.time.Clock()
        self.animation_frames = [pygame.transform.scale(pygame.image.load(f'player{i}.png'), (80, 80)) for i in range(1, 9)]
        self.standing_image = pygame.transform.scale(pygame.image.load('player1.png'), (80, 80))
        self.image_index = 0
        self.image = self.animation_frames[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.vel_x = 2

    def update(self):
        dx = 0
        dy = 0
        num = 0
   
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -20
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 30
            self.direction = -1
        if key[pygame.K_RIGHT]:
            dx += 30
            self.direction = 1

        self.vel_y += 20
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y
      
        if dx != 0: 
            self.image_index = (self.image_index + 1) % len(self.animation_frames)
            self.image = self.animation_frames[self.image_index]
        else: 
            self.image = self.standing_image

        question_displayed = False
        for tile_group in world.tile_groups:
            for tile in tile_group.tile_list:
                if tile[1].colliderect(self.rect.move(dx, 0)):
                    
                    dx = 0
                    if not tile_group.visited:
                        show_question()
                        tile_group.visited = True
                        question_displayed = True
                if tile[1].colliderect(self.rect.move(0, dy)):

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

        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            dy = 0

        screen.blit(self.image, self.rect)


class TileGroup():
    def __init__(self, data):
        self.tile_list = data
        self.visited = False

class World():
    def __init__(self, data):
        self.tile_list = []
        self.tile_groups = []

        dirt_img = pygame.image.load('dot.png')

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

world_data = [
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
]


player = Player(0, 0)
world = World(world_data)

def draw(screen):
    world.draw()
    player.update()
    pygame.display.update()


questions = ["What is the function of a program \n which one or more statements \nand/or other functions?",
             "Which part of the program performs certain actions\n by accepting arguments and returning a result?",
             "Which type is used to define\n integers?",
             "What are the variables that contain a memory address\n where the value\n of another variable or object resides?", 
             "In which programming technique is a function\n called by itself during\n its execution?"]

answers = ["main", "function", "int", "pointers", "recursion"]

def show_question():
    global root, question_displayed
    root = tk.Tk()
    root.geometry("500x150")
    root.title("Answer the Question")

    label = tk.Label(root, text=questions[num])
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    message_label = tk.Label(root, text="", fg="red")
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
        if not question_displayed:
            root.destroy()
            show_question()


    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

question_displayed = False 

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    current_image = (current_image + 1) % num_images
    screen.blit(bg_images[current_image], (0, 0)) 
    pygame.display.flip() 
    draw(screen)
    clock.tick(5)
    
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
