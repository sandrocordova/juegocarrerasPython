# Juego de carreras en Python
# Descripción: Habrán dos juadores: Jugador a y jugador b, cada jugador tiene su turno
# cuando el jugador presione "Enter" el programa genera un número aleatorio, el jugador que
# llegue primero a la meta gana
# IMPORTANTE: Colocar el rango de los números aleatorios y colocar la meta
import random

def aleatorio(rangAleatorio):
    a=random.randrange(rangAleatorio) 
    print("Puntuación: "+str(a))
    return a
def generarVia(var,meta):
    via = ""
    if var >= meta: var = meta 
    for i in range(var):
        via = via+"-"
    return via
def generarMeta(puntaje, metaInt):
    resultado = metaInt-puntaje
    meta = ""
    if puntaje >= metaInt:
        meta = meta+"|WIN|";
        return meta
    for i in range(resultado):
        meta = meta+"-"
    return meta+"|WIN|"
def iniciaJuego():
    meta = 15 # La meta a la que se quiere llegar
    rangAleatorio = 10 # Colocamos el intervalo del número aleatorio que se va a generar 1->10
    puntajeA = 0 #No tocar, solo es puntuación
    puntajeB = 0 #No tocar, solo es puntuación
    flag = True #No tocar, es una variable para intercalar entre JugadorA y JugadorB
    while(puntajeA < meta and puntajeB < meta):
        if(flag):
            flag = False
            print("__________________________________________________________________________")
            a = input('Jugador A:')
            puntajeA = puntajeA + aleatorio(rangAleatorio)
            print("|_|"+str(generarVia(puntajeA, meta))+"[*a*]"+str(generarMeta(puntajeA,meta))
            + "     "+str(puntajeA)+"/"+str(meta))
        else: 
            flag = True
            print("__________________________________________________________________________")
            a = input('Jugador B:')
            puntajeB = puntajeB + aleatorio(rangAleatorio)
            print("|_|"+str(generarVia(puntajeB,meta))+"[*b*]"+str(generarMeta(puntajeB,meta))
            + "     "+str(puntajeB)+"/"+str(meta))
            
    print("__________________________________________________________________________")
    print("#####################################################")   
    if puntajeA >= meta: print("### GANA Jugador |A|, Al llegar primero a la meta ###")
    if puntajeB >= meta: print("### GANA Jugador |B|, Al llegar primero a la meta ###")
    print("#####################################################") 
print("__________________________________________________________________________")
print("################################BIENVENIDO################################")
print("%%% Presina enter cuando sea tu turno para generar un número aleatorio %%%")
iniciaJuego()
