import pygame
import tkinter as tk
import math

pygame.font.init()

WIDTH = 1000
HEIGHT = 512

BOX_WIDTH_SIZE, BOX_HEIGHT_SIZE = 100, 30

FONT_SIZE = 16

FONT = pygame.font.SysFont("Arial", FONT_SIZE)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Techscape")

BG = pygame.transform.scale(pygame.image.load("level1_person_bg_arrows.png"), (WIDTH, HEIGHT))

boxes = []

places = []
num_places = 6 
spacing = 40
start_y = (HEIGHT - (BOX_HEIGHT_SIZE + spacing) * num_places) / 2 + 50

for i in range(num_places):
    place_x = (WIDTH - BOX_WIDTH_SIZE) / 2
    place_y = start_y + i * (BOX_HEIGHT_SIZE + spacing)
    places.append((place_x, place_y))

places.append((WIDTH/2 - BOX_WIDTH_SIZE/2 + 150, HEIGHT/2 - BOX_HEIGHT_SIZE/2 + 70))

OVAL_WIDTH = 125
OVAL_HEIGHT = 35

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

TEXT = "start"
TEXT_1 = "finish"

class Rhombus:
    def __init__(self, points, text, id):
        self.id = id
        self.points = points
        self.text = text
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.center = (sum(point[0] for point in self.points) / 4,  sum(point[1] for point in self.points) / 4)
        self.left = (points[0][0])
        self.width = (points[1][0] - self.left)
        self.top = (points[1][1])
        self.height = (points[2][1] - self.top)

    def draw(self):
        pygame.draw.polygon(WIN, (255, 255, 255), self.points)
        text_surface = FONT.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=(sum(point[0] for point in self.points) / 4,
                                                   sum(point[1] for point in self.points) / 4))
        WIN.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.collidepoint(event.pos):
                self.dragging = True
                self.offset_x = self.points[0][0] - event.pos[0]
                self.offset_y = self.points[0][1] - event.pos[1]
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                new_points = []
                for point in self.points:
                    new_x = point[0] + event.rel[0]
                    new_y = point[1] + event.rel[1]
                    new_points.append((new_x, new_y))
                self.points = new_points

    def move(self, rel):
        new_points = [(point[0] + rel[0], point[1] + rel[1]) for point in self.points]
        self.points = new_points
        
    def move_to_place(self, new_place):
        bottom_left = self.points[0]
        self.points = [(new_place[0] + point[0] - bottom_left[0],new_place[1] + point[1] - bottom_left[1]) for point in self.points]

    def collidepoint(self, pos):
        points_tuple = tuple(self.points)
        shape_polygon = pygame.draw.polygon(WIN, WHITE, points_tuple)
        return shape_polygon.collidepoint(pos)

class Parallelogram:
    def __init__(self, points, text, id):
        self.id = id
        self.points = points
        self.text = text
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.center = (sum(point[0] for point in self.points) / 4,  sum(point[1] for point in self.points) / 4)
        self.left = (points[0][0])
        self.width = (points[1][0] - self.left)
        self.top = (points[0][1])
        self.height = (points[2][1] - self.top)

    def draw(self):
        pygame.draw.polygon(WIN, (255, 255, 255), self.points)
        text_surface = FONT.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=(sum(point[0] for point in self.points) / 4,
                                                   sum(point[1] for point in self.points) / 4))
        WIN.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.collidepoint(event.pos):
                self.dragging = True
                self.offset_x = self.points[0][0] - event.pos[0]
                self.offset_y = self.points[0][1] - event.pos[1]
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                new_points = []
                for point in self.points:
                    new_x = point[0] + event.rel[0]
                    new_y = point[1] + event.rel[1]
                    new_points.append((new_x, new_y))
                self.points = new_points

    def move(self, rel):
        new_points = [(point[0] + rel[0], point[1] + rel[1]) for point in self.points]
        self.points = new_points
        
    def move_to_place(self, new_place):
        bottom_left = self.points[0]
        self.points = [(new_place[0] + point[0] - bottom_left[0],new_place[1] + point[1] - bottom_left[1]) for point in self.points]

    def collidepoint(self, pos):
        points_tuple = tuple(self.points)
        shape_polygon = pygame.draw.polygon(WIN, WHITE, points_tuple)
        return shape_polygon.collidepoint(pos)
    
rhombus_ids = [1, 2]
parallelogram_ids = [3, 4, 5, 6, 7, 8, 9, 10]

rhombus1 = Rhombus([
    (215, HEIGHT/2 - 100 - 25 + 200 + 100),
    (245, HEIGHT/2 - 100 + 200 + 100),
    (215, HEIGHT/2 - 100 + 25 + 200 + 100),
    (185, HEIGHT/2 - 100 + 200 + 100)
], "i<=n", rhombus_ids[0])

rhombus2 = Rhombus([
    (215, HEIGHT/2 - 100 - 25 - 100 + 200 + 100),
    (245, HEIGHT/2 - 100 - 100 + 200 + 100),
    (215, HEIGHT/2 - 100 + 25 - 100 + 200 + 100),
    (185, HEIGHT/2 - 100 - 100 + 200 + 100)
], "n!=0", rhombus_ids[1])

parallelogram1 = Parallelogram([
    (50 + BOX_WIDTH_SIZE + 20, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200),
    (50 + BOX_WIDTH_SIZE*2 + 20, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200),
    (50 + BOX_WIDTH_SIZE*2 - (BOX_HEIGHT_SIZE / 2) + 30, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200 + BOX_HEIGHT_SIZE),
    (50 + BOX_WIDTH_SIZE - (BOX_HEIGHT_SIZE / 2) + 30, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200 + BOX_HEIGHT_SIZE)
], "Въведи n", parallelogram_ids[0])

parallelogram2 = Parallelogram([
    (50 + BOX_WIDTH_SIZE + 20, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200 + 100),
    (50 + BOX_WIDTH_SIZE*2 + 20, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200 + 100),
    (50 + BOX_WIDTH_SIZE*2 - (BOX_HEIGHT_SIZE / 2) + 30, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200 + 100 + BOX_HEIGHT_SIZE),
    (50 + BOX_WIDTH_SIZE - (BOX_HEIGHT_SIZE / 2) + 30, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200 + 100 + BOX_HEIGHT_SIZE)
], "Изведи n", parallelogram_ids[1])

parallelogram3 = Parallelogram([
    (50 + BOX_WIDTH_SIZE + 20, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200 + 200),
    (50 + BOX_WIDTH_SIZE*2 + 20, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200 + 200),
    (50 + BOX_WIDTH_SIZE*2 - (BOX_HEIGHT_SIZE / 2) + 30, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200 + 200 + BOX_HEIGHT_SIZE),
    (50 + BOX_WIDTH_SIZE - (BOX_HEIGHT_SIZE / 2) + 30, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200 + 200 + BOX_HEIGHT_SIZE)
], "Изведи sum", parallelogram_ids[2])

parallelogram_square1 = Parallelogram([
    (50, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200),
    (50 + BOX_WIDTH_SIZE, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200 ),
    (50 + BOX_WIDTH_SIZE, HEIGHT/2 + BOX_HEIGHT_SIZE/2 - 200),
    (50, HEIGHT/2 + BOX_HEIGHT_SIZE/2 - 200)
], "i++", parallelogram_ids[3])

parallelogram_square2 = Parallelogram([
    (50, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 100),
    (50 + BOX_WIDTH_SIZE, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 100 ),
    (50 + BOX_WIDTH_SIZE, HEIGHT/2 + BOX_HEIGHT_SIZE/2 - 100),
    (50, HEIGHT/2 + BOX_HEIGHT_SIZE/2 - 100)
], "sum+=n", parallelogram_ids[4])

parallelogram_square3 = Parallelogram([
    (50, HEIGHT/2 - BOX_HEIGHT_SIZE/2),
    (50 + BOX_WIDTH_SIZE, HEIGHT/2 - BOX_HEIGHT_SIZE/2),
    (50 + BOX_WIDTH_SIZE, HEIGHT/2 + BOX_HEIGHT_SIZE/2),
    (50, HEIGHT/2 + BOX_HEIGHT_SIZE/2)
], "sum = 0", parallelogram_ids[5])

parallelogram_square4 = Parallelogram([
    (50, HEIGHT/2 - BOX_HEIGHT_SIZE/2 + 100),
    (50 + BOX_WIDTH_SIZE, HEIGHT/2 - BOX_HEIGHT_SIZE/2 + 100),
    (50 + BOX_WIDTH_SIZE, HEIGHT/2 + BOX_HEIGHT_SIZE/2 + 100),
    (50, HEIGHT/2 + BOX_HEIGHT_SIZE/2 + 100)
], "i = 1", parallelogram_ids[6])

parallelogram_square5 = Parallelogram([
    (50, HEIGHT/2 - BOX_HEIGHT_SIZE/2 + 200),
    (50 + BOX_WIDTH_SIZE, HEIGHT/2 - BOX_HEIGHT_SIZE/2 + 200),
    (50 + BOX_WIDTH_SIZE, HEIGHT/2 + BOX_HEIGHT_SIZE/2 + 200),
    (50, HEIGHT/2 + BOX_HEIGHT_SIZE/2 + 200)
], "sum+=i", parallelogram_ids[7])

shapes = [rhombus1, rhombus2, parallelogram1, parallelogram2, parallelogram3, parallelogram_square1, parallelogram_square2, parallelogram_square3, parallelogram_square4, parallelogram_square5]
placed_ids = []
correct_ids = [3, 8, 9, 1, 10, 6, 5]

BUTTON_WIDTH = 120
BUTTON_HEIGHT = 50
BUTTON_COLOR = (0, 255, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)
BUTTON_TEXT = "Check"
BUTTON_FONT = pygame.font.SysFont("Arial", 20)
BUTTON_POSITION = (WIDTH - BUTTON_WIDTH - 20, HEIGHT - BUTTON_HEIGHT - 20)

def draw_button():
    # Draw check button
    pygame.draw.ellipse(WIN, "grey", (BUTTON_POSITION[0], BUTTON_POSITION[1], BUTTON_WIDTH, BUTTON_HEIGHT))
    text_surface = BUTTON_FONT.render(BUTTON_TEXT, True, BUTTON_TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(BUTTON_POSITION[0] + BUTTON_WIDTH/2, BUTTON_POSITION[1] + BUTTON_HEIGHT/2))
    WIN.blit(text_surface, text_rect)

def restart_game():
    global placed_ids
    placed_ids = []
    main()

def create_window(message, restart = True):
    window = tk.Tk()
    window.title("Message Window")

    window_width = 400
    window_height = 200
    
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label = tk.Label(window, text=message, font=("Arial", 24))
    label.pack()
    
    if restart:
        print("Restarting game")
        restart_button = tk.Button(window, text="Restart", command=restart_game)
        restart_button.pack()
    
    window.mainloop()

def check_button_click(pos): 
    global run  # Declare run as global so it can be modified within this function
    if BUTTON_POSITION[0] <= pos[0] <= BUTTON_POSITION[0] + BUTTON_WIDTH and \
       BUTTON_POSITION[1] <= pos[1] <= BUTTON_POSITION[1] + BUTTON_HEIGHT:
          for i in range(0, len(correct_ids)):
              if placed_ids[i] != correct_ids[i]:
                  create_window("You lost!")
                  run = False  # Exiting the program when the player loses
                  return False
          create_window("First level passed!")
    elif BUTTON_POSITION[0] - BUTTON_WIDTH - 10 <= pos[0] <= BUTTON_POSITION[0] - 10 and \
         BUTTON_POSITION[1] <= pos[1] <= BUTTON_POSITION[1] + BUTTON_HEIGHT:
            restart_game()
            

def draw():
    WIN.blit(BG, (0, 0))
    for place_x, place_y in places:
        pygame.draw.circle(WIN, "white", (int(place_x + BOX_WIDTH_SIZE / 2), int(place_y + BOX_HEIGHT_SIZE / 2)), 15)  # Adjust radius as needed

    pygame.draw.ellipse(WIN, WHITE, (WIDTH/2 - OVAL_WIDTH/2, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200, OVAL_WIDTH, OVAL_HEIGHT))
    text_surface = FONT.render(TEXT, True, BLACK)
    text_rect = text_surface.get_rect(center=(WIDTH/2, HEIGHT/2 - BOX_HEIGHT_SIZE/2 - 200 + OVAL_HEIGHT//2))
    WIN.blit(text_surface, text_rect)
    
    pygame.draw.ellipse(WIN, WHITE, (WIDTH/2 - BOX_WIDTH_SIZE/2 + 300, HEIGHT/2 - BOX_HEIGHT_SIZE/2 + 65, OVAL_WIDTH, OVAL_HEIGHT))
    text_surface_1 = FONT.render(TEXT_1, True, BLACK)
    text_rect_1 = text_surface_1.get_rect(center=(WIDTH/2 - BOX_WIDTH_SIZE/2 + 360, HEIGHT/2 - BOX_HEIGHT_SIZE/2 + 55 + OVAL_HEIGHT//2 + 10))
    WIN.blit(text_surface_1, text_rect_1)
    
    rhombus1.draw()
    rhombus2.draw()
    parallelogram1.draw()
    parallelogram2.draw()
    parallelogram3.draw()
    parallelogram_square2.draw()
    parallelogram_square1.draw()
    parallelogram_square3.draw()
    parallelogram_square4.draw()
    parallelogram_square5.draw()
    
    draw_button()

    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()

    active_item = None 
    
    mouse_click_pos = None

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 

            rhombus1.handle_event(event)
            rhombus2.handle_event(event)
            parallelogram1.handle_event(event)
            parallelogram2.handle_event(event)
            parallelogram3.handle_event(event)
            parallelogram_square1.handle_event(event)
            parallelogram_square2.handle_event(event)
            parallelogram_square3.handle_event(event)
            parallelogram_square4.handle_event(event)
            parallelogram_square5.handle_event(event)
            

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and active_item:
                    for place in places:
                        if active_item.collidepoint(place):
                            active_item.move_to_place(place)
                            placed_ids.append(active_item.id)
                            break
                    active_item = None
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click_pos = event.pos
                    check_button_click(mouse_click_pos)
                    for box in shapes:
                        if box.collidepoint(event.pos):
                            active_item = box
                            break
 

        draw()

    pygame.quit()
    print("Calling main() again...")
    main()

if __name__ == "__main__":
    main()
