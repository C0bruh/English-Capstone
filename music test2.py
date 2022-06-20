import pygame
from pygame import mixer

mixer.init()
music = pygame.mixer.music.load('help_urself.mp3')
pygame.mixer.music.play(loops=-1)