print('___'*20)
print('               \033[31m MP3 PLAYER\033[m')
print('---'*20)
import pygame
pygame.init()
pygame.mixer.music.load('creep.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

