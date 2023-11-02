print('___'*20)
print('               \033[31mFeito pra quem não merecia\033[m')
print('---'*20)
import pygame
pygame.init()
pygame.mixer.music.load('creep.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

