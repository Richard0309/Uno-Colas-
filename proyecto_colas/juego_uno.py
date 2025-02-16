from tda_cola_circular_doble import Cola_Circular_Doble
from tda_cola_lineal import Cola_Lineal
from colores import selec_color
from colores import escoger_color
from banco_aleatorio import b_aleatorio
from tda_pila import Pila
from funciones_colas import comprobar_c
from funciones_colas import impresion
from funciones_colas import insertar
from funciones_colas import buscar
from funciones_colas import primero
from funciones_colas import insertar_inicio
from funciones_colas import quitar
from funciones_colas import vacio
from funciones_colas import com_comodin
from funciones_colas import com_comodin2
from funciones_colas import com_comodin3
from funciones_colas import com_comodin4
from funciones_colas import encontrar_cd
from funciones_colas import reiniciar
import random
r= str()
winner=bool(False)
c_cartas =int(0)
c=int(0)
dec=str()
selec=str()
color=str()
jugadores = Cola_Circular_Doble()
b_cartas = Cola_Lineal()
b_cartasaux = Cola_Lineal()
baraja1 = Cola_Circular_Doble()
baraja2= Cola_Circular_Doble()
baraja3=  Cola_Circular_Doble()
baraja4= Cola_Circular_Doble()
barajas= Cola_Circular_Doble()
poner_cartas = Pila()
#registro de jugadores
while ( (r != "no") and (c<=4)):
    jugador=input("Nombre: ")
    jugadores.insertar_final(jugador)
    c=c+1
    if(c==4):
        r="no"
    else: 
        r= str(input("Desea agregar otro jugador?"))
    if((c==1) and (r=="no")):
        print("No se puede jugar con un solo jugador")
        r="si"
print("Jugadores")
print(jugadores.imprimir_normal())
#llenado del banco
total= int(5*c)
for i in range (total):#se empieza jugando con 5 cartas por lo tanto se multiplica el contador por 5 para que al repartir cada uno tenga 5 cartas
    carta = random.randint(1,15)#se generán cartas aleatorias entre 1 y 15
    #si el rango de la carta es mayor a 10 se vuelve comodín
    if (carta>10):
    #asignando comodines a los valores númericos correspondientes
        if(carta==11):
            carta="+2"
            b_cartas.insertar(carta)
        elif(carta==12):
            carta="+4"
            b_cartas.insertar(carta)
        elif(carta==13):
            carta="cd"
            b_cartas.insertar(carta)
        elif(carta==14):
            carta="ct"
            b_cartas.insertar(carta)
        elif(carta==15):
            carta="cc"
            b_cartas.insertar(carta)
    #si el rango de la carta es menor o igual a 10 es carta con número
    elif(carta<=10):
        b_cartas.insertar(carta)
#asignación de colores a las cartas
while not b_cartas.cola_vacia():
    b_cartasaux.insertar(selec_color(b_cartas.quitar()))
while not b_cartasaux.cola_vacia():
    b_cartas.insertar(b_cartasaux.quitar())
#muestreo de las cartas antes de asignar
print("Cartas a repartir")
print(b_cartas.imprimir())
#reparto de cartas
while not b_cartas.cola_vacia():
    if (c==2):#en caso que sean solo dos jugadores
         baraja1.insertar_final(b_cartas.quitar())
         baraja2.insertar_final(b_cartas.quitar())
         barajas.insertar_final(baraja1)
         barajas.insertar_final(baraja2)
    elif (c==3):#en caso que sean solo tres jugadores
        baraja1.insertar_final(b_cartas.quitar())
        baraja2.insertar_final(b_cartas.quitar())
        baraja3.insertar_final(b_cartas.quitar())
        barajas.insertar_final(baraja1)
        barajas.insertar_final(baraja2)
        barajas.insertar_final(baraja3)
    elif (c==4):#en caso que sean los 4 jugadores
        baraja1.insertar_final(b_cartas.quitar())
        baraja2.insertar_final(b_cartas.quitar())
        baraja3.insertar_final(b_cartas.quitar())
        baraja4.insertar_final(b_cartas.quitar())
        barajas.insertar_final(baraja1)
        barajas.insertar_final(baraja2)
        barajas.insertar_final(baraja3)
        barajas.insertar_final(baraja4)
#impresión de los jugadores con sus barajas        
if c==2:# en caso que sean solo dos jugadores
    print(str(jugadores.primer_dato()))
    impresion(barajas.primer_dato())
    jugadores.insertar_final(jugadores.quitar_principio())
    print(str(jugadores.primer_dato()))
    barajas.insertar_final(barajas.quitar_principio())
    impresion(barajas.primer_dato())
elif c==3:#en caso que sean solo tres jugadores
    print(str(jugadores.primer_dato()))
    print(baraja1.imprimir_normal())
    jugadores.insertar_final(jugadores.quitar_principio())
    print(str(jugadores.primer_dato()))
    barajas.insertar_final(barajas.quitar_principio())
    impresion(barajas.primer_dato())
    jugadores.insertar_final(jugadores.quitar_principio())
    print(str(jugadores.primer_dato()))
    barajas.insertar_final(barajas.quitar_principio())
    impresion(barajas.primer_dato())
else:# en caso que sean 4 jugadores
    print(str(jugadores.primer_dato()))
    impresion(barajas.primer_dato())
    jugadores.insertar_final(jugadores.quitar_principio())
    print(str(jugadores.primer_dato()))
    barajas.insertar_final(barajas.quitar_principio())
    impresion(barajas.primer_dato())
    jugadores.insertar_final(jugadores.quitar_principio())
    print(str(jugadores.primer_dato()))
    barajas.insertar_final(barajas.quitar_principio())
    impresion(barajas.primer_dato())
    jugadores.insertar_final(jugadores.quitar_principio())
    print(str(jugadores.primer_dato()))
    barajas.insertar_final(barajas.quitar_principio())
    impresion(barajas.primer_dato())
#jugando por turnos
carta=random.randint(1,10)
poner_cartas.insertar(selec_color(carta))
print("Carta para poner")
print(poner_cartas.imprime())
while  winner != True:#mientras no haya un ganador el cico se repetira
    if ((poner_cartas.tope_pila()=="cd verde")or(poner_cartas.tope_pila()=="cd rojo")or(poner_cartas.tope_pila()=="cd amarillo")or(poner_cartas.tope_pila()=="cd azul")):
        c_cartas=c_cartas+1# si se pone un cd [cambio de dirección] se aumenta el contador
#jugando en sentido contrario        
    if ((encontrar_cd(c_cartas))==True):#si retorna un true se ejecuta el if
        jugadores.insertar_principio(jugadores.quitar_final())
        barajas.insertar_principio(barajas.quitar_final())
    
        if (com_comodin(poner_cartas.tope_pila())==True):
            for i in range (2):
                insertar_inicio(barajas.primer_dato(),b_aleatorio())#llenado de cartas automatico en caso de +2
            jugadores.insertar_principio(jugadores.quitar_final())
            barajas.insertar_principio(barajas.quitar_final())
            
        if com_comodin2(poner_cartas.tope_pila())==True:
            jugadores.insertar_principio(jugadores.quitar_final())
            barajas.insertar_principio(barajas.quitar_final())#cancela el turno con cc
    
        if com_comodin3(poner_cartas.tope_pila())==True:#añade 4 cartas al jugador siguiente y cambia el color 
            jugadores.insertar_final(jugadores.quitar_principio())
            barajas.insertar_final(barajas.quitar_principio())
            color=str(input("Escriba el color que desea cambiar: "))
            poner_cartas.insertar(escoger_color(color))
            jugadores.insertar_principio(jugadores.quitar_final())
            barajas.insertar_principio(barajas.quitar_final())
            for i in range (4):
                insertar(barajas.primer_dato(),b_aleatorio())
            jugadores.insertar_principio(jugadores.quitar_final())
            barajas.insertar_principio(barajas.quitar_final())
          
        if com_comodin4(poner_cartas.tope_pila())==True:#cambia color
            color=str(input("Escriba el color que desea cambiar: "))
            poner_cartas.insertar(escoger_color(color))
 #jugando en sentido normal       
    else:
        jugadores.insertar_final(jugadores.quitar_principio())
        barajas.insertar_final(barajas.quitar_principio())
    
        if (com_comodin(poner_cartas.tope_pila())==True):
            for i in range (2):
                insertar_inicio(barajas.primer_dato(),b_aleatorio())#llenado de cartas automatico en caso de +2
            jugadores.insertar_final(jugadores.quitar_principio())
            barajas.insertar_final(barajas.quitar_principio())
            
        if com_comodin2(poner_cartas.tope_pila())==True:
            jugadores.insertar_final(jugadores.quitar_principio())
            barajas.insertar_final(barajas.quitar_principio())#cancela el turno con ct
    
        if com_comodin3(poner_cartas.tope_pila())==True:#añade 4 cartas al jugador siguiente y cambia el color 
            jugadores.insertar_principio(jugadores.quitar_final())
            barajas.insertar_principio(barajas.quitar_final())
            color=str(input("Escriba el color que desea cambiar: "))
            poner_cartas.insertar(escoger_color(color))
            jugadores.insertar_final(jugadores.quitar_principio())
            barajas.insertar_final(barajas.quitar_principio())
            for i in range (4):
                insertar(barajas.primer_dato(),b_aleatorio())
            jugadores.insertar_final(jugadores.quitar_principio())
            barajas.insertar_final(barajas.quitar_principio())
            
        if com_comodin4(poner_cartas.tope_pila())==True:
            color=str(input("Escriba el color que desea cambiar: "))#cambia color
            poner_cartas.insertar(escoger_color(color))
    
            
    print("turno de: ",str(jugadores.primer_dato()))#el jugador que está en turno
    impresion(barajas.primer_dato())#su baraja
    print("\n última carta puesta")
    print(str(poner_cartas.tope_pila()))#la última carta puesta que sirve para saber que carta poner
    print("\n")
    dec= str(input("[p] para poner [s] para sacar del banco "))
    #evalua la decisión que se toma 
    if dec == "s":
        while dec == "s":#mientras se le de a la s se sacarán cartas
            print("\n última carta puesta")
            print(str(poner_cartas.tope_pila()))#se imprime la última carta puesta para no olvidar que carta poner cuando se termine de sacar
            print("\n")
            insertar(barajas.primer_dato(),b_aleatorio())#las cartas sacadas del banco aleatorio se insertan en la baraja del jugador
            
            impresion(barajas.primer_dato())#se imprime su maso
            dec=str(input("[s] para seguir sacando [p] para poner "))#se vuelve a preguntar la decisión
    if dec == "p":#en caso de darle a la p
        print("\n última carta puesta")
        print(str(poner_cartas.tope_pila()))
        print("\n")
        selec=str(input("Escriba la carta que va poner "))
        buscar(barajas.primer_dato(),selec)#se busca la carta que se va a poner
        if (comprobar_c(primero(barajas.primer_dato()),poner_cartas.tope_pila())==True):#se compara que el color o número de la carta sea compatible con la última carta puesta
            #en caso que sea True se procede a alo siguiente:
            poner_cartas.insertar(primero(barajas.primer_dato()))#se pone la carta aceptada en el monto de poner cartas
            quitar(barajas.primer_dato())#se quita la carta que se puso del mazo del jugador
            impresion(barajas.primer_dato())
            print("\n última carta puesta")
            print(str(poner_cartas.tope_pila()))
            print("\n")
            reiniciar(barajas.primer_dato())#sirve para probar que el ciclo de rompa adecuadamente
            if(vacio(barajas.primer_dato())==True):#se evalua si el mazo del jugador está vacío, si es True winner ahora vale True, de ser falso vale False
                winner=True
            else:
                winner=False
        else:#si se pone una carta que no es compatible porque no se tiene una se hace el siguiente ciclo:
            while(comprobar_c(primero(barajas.primer_dato()),poner_cartas.tope_pila())==False):
                #mientras la primera carta de la baraja sea diferente de la última carta puesta en el monto de cartas
                #se pone una carta sacada del banco aleatorio y se imprime como va tu mazo y así hasta que la primera
                #carta de tu mazo tenga el mismo número o color de la última carta puesta o en su defecto sea un cambia color o un +4
               insertar_inicio(barajas.primer_dato(),b_aleatorio())
               impresion(barajas.primer_dato())
            poner_cartas.insertar(primero(barajas.primer_dato()))
            impresion(barajas.primer_dato())
            print("\n última carta puesta")
            print(str(poner_cartas.tope_pila()))
            print("\n")
#cuando se rompe el ciclo imprime el jugador que ganó       
print("\n==========Fin del juego==============")
print("\nGanador: ",str(jugadores.primer_dato()))

            
                
                   
                
            
           
        
    
    
    

    



    
    
    
    
    
    
    
    
    
    

    


    





