import pygame
from pygame.locals import *
from pyvidplayer import Video
import pygame.mixer
from pygame import mixer
from configuracion import *


pygame.init()
#clase para el botón
class Boton():
    def __init__(self, x, y, imagen, escala):
        ancho = imagen.get_width()
        alto = imagen.get_height()
        self.imagen = pygame.transform.scale(imagen, (int(ancho * escala), int(alto * escala)))
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def dibujar(self, surface):
        accion = False
        #obtener la posicion del mouse
        pygame.init()
        pos = pygame.mouse.get_pos()

        #checkear si se presiona con el click izquierdo
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                accion = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #dibujar el boton en pantalla
        surface.blit(self.imagen, (self.rect.x, self.rect.y))

        return accion

#funcion para escribir texto en pantalla.
def Texto(screen,texto,color,x,y):
    text_color = (color)
    font= pygame.font.SysFont("comicsansms",80,bold=True)
    text = font.render(texto, True, text_color)
    text_rect = text.get_rect()
    text_rect.center = (ANCHO//2,ALTO//2)
    screen.blit(text,(x,y))
    pygame.display.flip()


#funcion que busca los mayores de una lista (en este caso va a buscar los 3 mayores de la lista de puntajes, que se obtiene abriendo el archivo de puntajes en formato de lectura, esto se hace en principal)
def mayores(num,lista):
    cont=0
    mayores=[]
    while cont<num:
        aux=0
        pos=0
        for i in range (len(lista)):
            if lista[i]>aux:
                aux=lista[i]
                pos=i
        mayores.append(aux)
        lista.pop(pos)
        aux=0
        pos=0
        cont=cont+1
    return(mayores)

#las funciones correctos e incorrectos va a mostrar en pantalla las palabras segun sean aciertos o errores.
def correctos(lista,screen):
    pos=355
    for elem in lista:
        text_color =(79,187,89)
        font= pygame.font.SysFont("comicsansms",25,bold=True)
        text = font.render(elem, True, text_color)
        text_rect = text.get_rect()
        text_rect.center = (ANCHO//2,ALTO//2)
        screen.blit(text,(200,pos))
        pygame.display.flip()
        pos=pos+25
def incorrectos(lista,screen):
    pos=355
    for elem in lista:
        text_color =(241,25,75)
        font= pygame.font.SysFont("comicsansms",25,bold=True)
        text = font.render(elem, True, text_color)
        text_rect = text.get_rect()
        text_rect.center = (ANCHO//2,ALTO//2)
        screen.blit(text,(550,pos))
        pygame.display.flip()
        pos=pos+25



