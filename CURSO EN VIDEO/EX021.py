''' faça um programa em pythoon que abra e repodução um audio mp3'''

import pygame
pygame.init()
pygame.mixer.music.load('rock.mp3')
pygame.mixer.music.play()
input()   #vazio mesmo



