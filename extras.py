import pygame
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

def dibujar(screen,fondo, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos):

    defaultFont= pygame.font.SysFont("comicsansms", 25,bold=True)
    defaultFontGrande= pygame.font.SysFont("comicsansms", 80,bold=True)
    #agregamos las fuentes letracandidata y intentosFont
    letracandidata=pygame.font.SysFont("comicsansms", 40,bold=True)
    intentosFont=pygame.font.SysFont("comicsansms",25, bold=True)

    #a screen blit le agregamos fondo, para que en el juego principal muestre el fondo cada vez que se dibuje la pantalla nuevamente.
    screen.blit(fondo,(0,0))



    ren1 = letracandidata.render(candidata, 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    if(segundos<15):
        ren3 = defaultFont.render(str(int(segundos)), 1,(241,25,75))
    else:
        ren3 = defaultFont.render(str(int(segundos)), 1, COLOR_LETRAS)
    #escribe grande la palabra (letra por letra) y la letra principal de otro color
    pos = 130
    for i in range(len(letrasEnPantalla)):
        if letrasEnPantalla[i] == letraPrincipal:
            screen.blit(defaultFontGrande.render(letrasEnPantalla[i], 1,(204,53,136)), (pos, 150))
        else:
            screen.blit(defaultFontGrande.render(letrasEnPantalla[i], 1, COLOR_LETRAS), (pos, 150))
        pos = pos + TAMANNO_LETRA_GRANDE

    screen.blit(ren1, (300, 700))
    screen.blit(ren2, (650, 52))
    screen.blit(ren3, (56, 62))


