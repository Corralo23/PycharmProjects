#Crie um programa que pegue uma música MP3 de um arquivo e rode ela
import pygame
pygame.init()
pygame.mixer.music.load('acdc.mp3')
pygame.mixer.music.play()
pygame.event.wait()