import pygame
import os

pygame.init()

WIDTH = 1000
HEIGHT = 512 


screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Dialog")

DIALOG_1_IMAGE = pygame.image.load(os.path.join('assets', 'dialog_1.png'))
DIALOG_1 = pygame.transform.scale(DIALOG_1_IMAGE, (WIDTH, HEIGHT))

DIALOG_2_IMAGE = pygame.image.load(os.path.join('assets', 'dialog_2.png'))
DIALOG_2 = pygame.transform.scale(DIALOG_2_IMAGE, (WIDTH, HEIGHT))

DIALOG_3_IMAGE = pygame.image.load(os.path.join('assets', 'dialog_3.png'))
DIALOG_3 = pygame.transform.scale(DIALOG_3_IMAGE, (WIDTH, HEIGHT))

DIALOG_4_IMAGE = pygame.image.load(os.path.join('assets', 'dialog_4.png'))
DIALOG_4 = pygame.transform.scale(DIALOG_4_IMAGE, (WIDTH, HEIGHT))

DIALOG_5_IMAGE = pygame.image.load(os.path.join('assets', 'dialog_5.png'))
DIALOG_5 = pygame.transform.scale(DIALOG_5_IMAGE, (WIDTH, HEIGHT))

start_time = pygame.time.get_ticks()
while pygame.time.get_ticks() < start_time+5000:
    screen.blit(DIALOG_1, (0,0))
    pygame.display.update()

start_time = pygame.time.get_ticks()
while pygame.time.get_ticks() < start_time+5000:
    screen.blit(DIALOG_2, (0,0))
    pygame.display.update()

start_time = pygame.time.get_ticks()
while pygame.time.get_ticks() < start_time+5000:
    screen.blit(DIALOG_3, (0,0))
    pygame.display.update()

start_time = pygame.time.get_ticks()
while pygame.time.get_ticks() < start_time+5000:
    screen.blit(DIALOG_4, (0,0))
    pygame.display.update()

start_time = pygame.time.get_ticks()
while pygame.time.get_ticks() < start_time+5000:
    screen.blit(DIALOG_5, (0,0))
    pygame.display.update()