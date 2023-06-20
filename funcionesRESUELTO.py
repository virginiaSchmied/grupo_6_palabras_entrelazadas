from principal import *
from configuracion import *
import random
import math

#lee el archivo y carga en la lista diccionario todas las palabras
def lectura(diccionario):
    f=open("lemario.txt","r", encoding="ISO-8859-1") #lee el archivo
    lineas=f.readlines() #guarda en una lista todas las palabras del archivo
    f.close() #cierra el archivo
    pal=""
    for linea in lineas: #recorre cada elemento de la lista lineas
        for char in linea:
            if char!= "\n": #usa todos los caracteres del elemento menos el caracter '\n'
                pal=pal+char
        diccionario.append(pal) #agrega esa cadena a la lista diccionario
        pal=""
    return diccionario #devuelve la lista diccionario

#Devuelve una cadena de 7 caracteres sin repetir con 2 o 3 vocales y a lo sumo
# con una consonante dificil (kxyz)
def dame7Letras():
    consonantes=["B","C","D","F","G","H","J","L","M","N","P","Q","R","S","T","V","W"] #creamos una lista con consonantes (sin las consonantes dificiles)
    consonantes_dif=["K","X","Y","Z"] #creamos una lista con las consonantes dificiles
    vocales=["A","E","I","O","U"] #creamos una lista con las vocales
    letras=[] #en esta lista guardaremos las letras aleatorias

    num=random.randint(0,1) #con este numero se decidira si habrá una consonante dificil o no
    if num==1: #si el numero es 1, se elegira aleatoreamente de la lista consonantes_dif una y se la añadira a letras
        num=random.randint(0,3)
        letra=consonantes_dif[num]
        letras.append(letra)

    num=random.randint(2,3) #con este numero se decidira si habrá 2 o 3 vocales
    cont=0
    while cont<num: #con este ciclo while se elegirán aleatoriamente la cantidad 'num' de vocales y se añadira a letras
        pos=random.randint(0,4)
        letra=vocales[pos]
        if letra not in letras: #esta linea se implementa para que solo se añadan las letras que no están en la lista letras (para que no haya repetidas)
            letras.append(letra)
            cont=cont+1

    while len(letras)<7: #con este ciclo se completara la lista letra con consonantes aleatorias, se agregaran letras hasta que se cumpla que el largo de la lista letras es 7
        pos=random.randint(0,16)
        letra=consonantes[pos]
        if letra not in letras:
            letras.append(letra)

    cad="" #en esta cadena vacia se pondran las letras de forma aleatoria, es lo que retornará la función más adelante
    nums=[] #esta lista la hicimos con el proposito de que no se repitan las letras en la cadena
    cont=0
    while cont<7:
        pos=random.randint(0,6) #se toman posiciones random del 0 al 6 para acceder de forma aleatoria a los elementos de la lista letras
        if pos not in nums: #este condicional para que no se repita
            letra=letras[pos] #se elige la letra que esta en lista letras en esa poscicion (que ya nos aseguramos de que no se haya usado antes)
            cad=cad+letra #se agrega la letra a la cadena
            cont=cont+1
            nums.append(pos)

    return(cad) #la función devuelve la cadena

def dameLetra(letrasEnPantalla): #elige una letra de las letras en pantalla
    num=random.randint(0,6) #devuelve un numero aleatorio
    cont=0
    letra=""
    for char in letrasEnPantalla: #recorre la cadena dada
        if cont==num: #cuando el contador sea igual al numero, significa que ese char sera el elegido
            letra=char #lo guarda en la variable letra
        cont=cont+1
    return(letra) #devuelve esa variable letra

#si es valida la palabra devuelve puntos sino resta.
def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario,lista):
    correctas=dameAlgunasCorrectas(letraPrincipal,letrasEnPantalla,diccionario)
    puntos=Puntos(lista,candidata)
    if esValida(letraPrincipal,letrasEnPantalla,candidata,correctas):
        return(puntos)
    else:
        puntos=-1
        return(puntos)

#chequea que se use la letra principal, solo use letras de la pantalla y
#exista en el diccionario
def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    cont=0
    letras_cand=[]
    candidata=candidata.upper()
    if candidata in diccionario:
        for letra in candidata:
            if letra not in letras_cand:
                letras_cand.append(letra)
            else:
                return False
            if letra not in letrasEnPantalla:
                return False
            else:
                if letra==letraPrincipal:
                    cont=cont+1
        if cont==1:
            return True
        else:
            return False
    else:
        return False

#devuelve los puntos
def Puntos(lista,candidata):
    puntos=0
    if candidata not in lista:
        longitud=len(candidata)
        if longitud==3:
            puntos=1
        if longitud==4:
            puntos=2
        if longitud>=5 and longitud<7:
            puntos=longitud
        if longitud==7:
            puntos=10
        if longitud<3 or longitud>7:
            puntos=-1
    return(puntos)


#busca en el diccionario paralabras correctas y devuelve una lista de estas
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    cont_principal=0
    cont_letras=0
    correctas=[]
    for elem in diccionario:
        elem=elem.upper()
        long=len(elem)
        for letra in elem:
            if letra in letrasEnPantalla:
                cont_letras=cont_letras+1
            if letra==letraPrincipal:
                cont_principal=1
        if cont_letras==long and cont_principal==1:
            correctas.append(elem)
        cont_principal=0
        cont_letras=0
    return(correctas)