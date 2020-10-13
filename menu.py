#Libraries
from screens import servidor
import pygame
import sys

pygame.init()

#menu loop
def menup():
     #pantalla menu
     menu=pygame.display.set_mode((1250,720))
     #el barco del fondo
     shipImg=pygame.image.load('imagenes\ship_menu.png')
     #titulo menu
     mifuente=pygame.font.SysFont("Arial",60)
     titulo_menu=mifuente.render("BATTLESHIP",0,(255,255,255))
     running_menu=True
     while running_menu:
        for event in pygame.event.get():
          menu.fill((50,150,200))
          menu.blit(titulo_menu,(600,0))
          menu.blit(shipImg,(300,0)) #falta arreglar centrado a la mitad
          pygame.display.update()
          if event.type==pygame.QUIT:
               running_menu=False

          if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_LEFT:
                    running_menu=False
                    servidor.server()
        
     
menup()
pygame.quit()
