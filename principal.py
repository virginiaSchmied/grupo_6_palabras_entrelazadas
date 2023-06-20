#! /usr/bin/env python
import os, random, sys, math,extrasNuevos

import pygame
from pygame.locals import *

from configuracion import *
from extras import *

from funcionesRESUELTO import *
from extrasNuevos import*
from pyvidplayer import Video
import pygame.mixer
from pygame import mixer



pygame.init()
pygame.display.set_caption("Palabras Entrelazadas")

#musica de fondo
pygame.mixer.init()
pygame.mixer.music.load('cancioncita.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
sonido_win = pygame.mixer.Sound('WOW.mp3')
sonido_lose = pygame.mixer.Sound('SONIDO_PERDER.wav')
sonido_lose.set_volume(0.1)
sonido_win.set_volume(0.4)
wrong_word = pygame.mixer.Sound('SONIDO_ERROR.wav')
wrong_word.set_volume(0.1)

#configuracion de la ventana.
screen = pygame.display.set_mode((ANCHO, ALTO))

#fondos que se usaran en el juego.
fondo=pygame.image.load("game_screen.png")
fondo_menu=pygame.image.load("menu_def.png")
fondo_puntajes=pygame.image.load("mejores_puntajes.png")

#listas necesarias para mostrar los aciertos y errores.
aciertos=[]
errores=[]

#cargar los mejores puntajes en una lista (los puntajes estan en un archivo), usando la funcion mayores que definimos en extrasNuevos.
f=open("puntajes.txt","r")
lineas=f.readlines()
f.close()
lista=[]
for elem in lineas:
    lista.append(int(elem))
mejores=mayores(3,lista)

#intro del juego
def intro():
    pygame.init()
    #cargamos el video de la intro. Para esto se uso la libreira pyvidplayer
    vid=Video("intro.mp4")
    vid.set_size((800,800))
    #En este While se va a reproducir el video. Si se presiona el mouse, llama a la funcion menu.
    RUN=True
    while RUN:
        limite = pygame.time.get_ticks()/1000
        vid.draw(screen,(0,0))
        pygame.display.update()
        if limite >14 and limite < 15:
            vid.close()
            menu()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                vid.close()
                RUN=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                vid.close()
                menu()

#menu del juego. Permite ir directamente al juego, ver el tutorial o ver los mejores puntajes
def menu():
    RUN = True

    #cargar las imagenes de los botones

    start_img =pygame.image.load('boton_transparente.png').convert_alpha()
    tutorial_img = pygame.image.load('boton_transparente.png').convert_alpha()
    mej_punt_img= pygame.image.load('boton_transparente.png').convert_alpha()

    #configurar los botones usando la clase Boton que se definio en extrasNuevos.
    start_button = extrasNuevos.Boton(50, 250, start_img, 1)
    tutorial_button = extrasNuevos.Boton(450, 250, tutorial_img, 1)
    mej_punt_button=extrasNuevos.Boton(270, 450, tutorial_img, 1)
    while RUN:
        #cargamos el fondo del menu
        screen.blit(fondo_menu,(0,0))
        #Si se hace click en alguno de los botones, se llamara a la funcion correspondiente.
        if start_button.dibujar(screen):
            RUN=False
            main()
        if tutorial_button.dibujar(screen):
            RUN=False
            tutorial()
        if mej_punt_button.dibujar(screen):
            RUN=False
            mejores_puntajes()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                RUN = False

        pygame.display.update()

#mejores puntajes del juego
def mejores_puntajes():
    num1=mejores[0]
    num2=mejores[1]
    num3=mejores[2]
    #carga el fondo de puntajes
    screen.blit(fondo_puntajes,(0,0))
    #ubica los puntajes en sus respectivas posiciones.
    n1=Texto(screen,str(num1),(244,106,194),350,480)
    n2=Texto(screen,str(num2),(244,106,194),170,630)
    n3=Texto(screen,str(num3),(244,106,194),580,660)
    pygame.display.update()
    #cuando se presione el mouse, se ira a el juego.
    RUN=True
    while RUN:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                RUN=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                menu()

#tutorial del juego, es un video como la intro. si se presiona click va al menu denuevo
def tutorial():
    vid=Video("tutorial.mp4")
    vid.set_size((800,800))
    tiempo=pygame.time.get_ticks()/1000
    RUN=True
    while RUN:
        vid.draw(screen,(0,0))
        pygame.display.update()
        limite=(pygame.time.get_ticks()/1000)-tiempo
        if limite >29 and limite < 30:
            vid.close()
            menu()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                vid.close()
                RUN=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                vid.close()
                menu()

#JUEGO
def main():

        RUN=True
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()

        #para que el juego cuando comience este en 60 segundos.
        arranque= pygame.time.get_ticks()/1000

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        candidata = ""
        diccionario = []

        #lee el diccionario
        lectura(diccionario)

        #elige las 7 letras al azar y una de ellas como principal
        letrasEnPantalla = dame7Letras()
        letraPrincipal = dameLetra(letrasEnPantalla)

        #se queda con 7 letras que permitan armar muchas palabras, evita que el juego sea aburrido
        while(len(dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario))< MINIMO):
            letrasEnPantalla = dame7Letras()
            letraPrincipal = dameLetra(letrasEnPantalla)

        print(dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario))

        #dibuja la pantalla la primera vez
        dibujar(screen,fondo, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos)
        lista_candidatas=[]
        while segundos > fps/1000 and RUN:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
                fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    RUN=False
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra   #va concatenando las letras que escribe
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1] #borra la ultima
                    if e.key == K_RETURN:  #presionó enter

                        puntaje=procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario,lista_candidatas)
                        puntos += puntaje
                        if puntaje>0:
                            aciertos.append(candidata)#si es un acierto se va a agregar a la lista de aciertos
                            sonido_win.play()
                        else:
                            errores.append(candidata) #si es un error a la lista de errores
                            wrong_word.play()
                        lista_candidatas.append(candidata)#la candidata se agrega a la lista de candidatas, para que no haya repetidos.
                        candidata = ""

            segundos=TIEMPO_MAX-pygame.time.get_ticks()/1000 + arranque


            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen,fondo, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos)
            ac=correctos(aciertos,screen) #se van a ir mostrando los aciertos y los errores en pantalla en la posicion que correspondan
            er=incorrectos(errores,screen)
            pygame.display.flip()
            if segundos>0 and segundos<1: #con esto se va a ir a la parte final del juego
                f=open("puntajes.txt","a")
                f.write("\n"+str(puntos))#aca se añade el puntaje al archivo de puntajes, para que la proxima vez que se juegue ese puntaje se tenga en cuenta al calcular los 3 mejores
                f.close()
                if puntos<=0: #si obtuviste menos de 0 o 0 puntos en total, se mostrara la pantalla de "perder", junto al puntaje obtenido.
                        vid=Video("PERDER.mp4")
                        vid.set_size((800,800))
                        sonido_lose.play()
                        tiempo=pygame.time.get_ticks()/1000
                        RUN=True
                        while RUN:
                            vid.draw(screen,(0,0))
                            texto=Texto(screen,str(puntos),(255,243,0),570,145)
                            pygame.display.update()
                            limite=(pygame.time.get_ticks()/1000)-tiempo
                            if limite >9 and limite < 10:
                                vid.close()
                                pygame.quit()
                                sys.exit()
                                pygame.mixer.music.stop()
                                RUN=False
                            for event in pygame.event.get():
                                if event.type==pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                    vid.close()
                                    RUN=False
                else:#si obtuviste mas de 0 puntos,se mostrara la pantalla de "victoria",junto al puntaje obtenido.
                    vid=Video("VICTORIA.mp4")
                    vid.set_size((800,800))
                    sonido_win.play()
                    RUN=True
                    tiempo=pygame.time.get_ticks()/1000
                    while RUN:
                        vid.draw(screen,(0,0))
                        texto=Texto(screen,str(puntos),(238,87,133),570,145)
                        pygame.display.update()
                        limite=(pygame.time.get_ticks()/1000)-tiempo
                        if limite >9 and limite < 10:
                                vid.close()
                                pygame.quit()
                                sys.exit()
                                pygame.mixer.music.stop()
                                RUN=False
                        for event in pygame.event.get():
                            if event.type==pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                                vid.close()
                                RUN=False


        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

#Programa Principal ejecuta Main
if __name__ == "__main__":
    intro()

