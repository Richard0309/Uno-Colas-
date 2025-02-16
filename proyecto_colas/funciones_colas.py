from tkinter import*
def  impresion(baraja):
    #recibe un dato de tipo cola por lo tanto se importa el objeto de cola para trabajar con el
    #se imprime el primer dato de la cola recibida, al ser una cola que esta dentro de una cola esto es efectivo
    #al haber importado la Cola se puede usar su método de .imprimir_normal() sobre la variable recibida
    from tda_cola_circular_doble import Cola_Circular_Doble
    return (baraja.imprimir_normal())
    
def insertar(cola,carta_a):
    #recibe un dato de tipo cola por lo tanto se importa el objeto de cola para trabajar con el seguido de otro dato que es la carta
    #se retorna el la cola con el dato ya insertado, y dicha cola es el primer dato de la cola general "barajas"
    from tda_cola_circular_doble import Cola_Circular_Doble
    return(cola.insertar_final(carta_a))


def insertar_inicio(cola,carta_a):
    #recibe un dato de tipo cola por lo tanto se importa el objeto de cola para trabajar con el seguido de otro dato que es la carta
    #se retorna el la cola con el dato ya insertado, y dicha cola es el primer dato de la cola general "barajas"
    from tda_cola_circular_doble import Cola_Circular_Doble
    return (cola.insertar_principio(carta_a))

def buscar(cola,busq):
    #se recibe el primer dato de la cola barajas es decir la cola dentro de la cola y la respuesta de la carta que se desea poner
    from tda_cola_circular_doble import Cola_Circular_Doble
    aux= Cola_Circular_Doble()
    c=int(0)
    c2=int(0)
    while not cola.cola_vacia():
        aux.insertar_final(cola.quitar_principio())
        c= c+1
    while not aux.cola_vacia():
        cola.insertar_final(aux.quitar_principio())
        
    while cola.primer_dato() != busq and c2 <= c:
        cola.insertar_final(cola.quitar_principio())
        c2= c2+1
    if c2 <= c and cola.primer_dato() == busq:
        return cola.primer_dato()
    else:
        return False
        
def NoEncontrado():
    #from tkinter import*
    raiz = Tk()
    ventana = Frame(raiz, width=1300, height=800)
    ventana.pack()
    etiqueta = Label(ventana, text="La carta no existe en la baraja")
    etiqueta.grid(row=0, column=1,padx=1,pady=1)



def primero(cola):
    #retorna el primer dato de la baraja jugando es decir el primer dato del primer dato de la cola
    from tda_cola_circular_doble import Cola_Circular_Doble
    return cola.primer_dato()

def quitar(cola):
    #se quita un dato del principio del primer dato de la cola que se encuentra dentro de la cola
    #es decir se quita una carta del inicio de la baraja
    from tda_cola_circular_doble import Cola_Circular_Doble
    return cola.quitar_principio()

def vacio(cola):
    #se recibe la cola que está como primer dato dentro de la cola
    #y si esta, está vacía retorna un True de no ser así un False
    from tda_cola_circular_doble import Cola_Circular_Doble
    if cola.cola_vacia():
        return True
    else:
        return False
    
def reiniciar(cola):
    #reinicia la cola que se encuentra como primer dato dentro de la cola barajas
    from tda_cola_circular_doble import Cola_Circular_Doble
    return cola.reiniciar()

def comprobar_c(carta,carta_puesta):
    #recibe la carta que se quito de la baraja y se desea poner en el mazo donde se colocan las cartas
    if (carta==carta_puesta or (carta=="+4 negro") or (carta=="cc negro")):
        #compara que si ambas cartas son iguales es decir mismo número o mismo color
        #que sea un +4 negro o un cc negro y de ser así returna un True
        return True
    #de no cumplirse está condición:
    elif(carta!=carta_puesta):
        #se asignan variables que valgan la longitud 1 de la carta pq las cartas con número tienen 01, 02, etc.
        #se asignan variables que valgan la longitud 3 de la carta pq en la longitud 3 está la 2da letra del color de la carta
        #esto porque la primera letra de los colores no es efectivo pq el azul y el amarillo si usamos su longitud 2 es decir su primera letra
        #el programa va permitir poner cartas azules con amarillas y viceversa, ahora si usamos la longitud 3 que es la 2da letra del color
        #podemos comparar que el color sea igual
        carta1=carta[1]
        cp1=carta_puesta[1]
        carta2=carta[3]
        cp2=carta_puesta[3]
        if ((cp1==carta1) or (carta2==cp2)):
            #entonces si el número de carta a poner es igual a al de la carta puesta o el color es igual al de la carta puesta
            #se retorna un True de no ser así se retorna un False
            return True
        else:
            return False
#funciones que comprueban los comodines
def com_comodin(comodin):
    #si el comodin es igual a alguna de las cadenas se retorna un True de no ser así se retorna un False
    if ((comodin=="+2 azul")or(comodin=="+2 rojo")or(comodin=="+2 verde")or(comodin=="+2 amarillo")):
        return True
    else:
        return False

def com_comodin2(comodin):
    #si el comodin es igual a alguna de las cadenas se retorna un True de no ser así se retorna un False
    if ((comodin=="ct azul")or(comodin=="ct rojo")or(comodin=="ct verde")or(comodin=="ct amarillo")):
        return True
    else:
        return False

def  com_comodin3(comodin):
    #si el comodín es igual a la cadena se retorna un True de no ser así un False
    if comodin=="+4 negro":
        return True
    else:
        return False
    
def com_comodin4(comodin):
    #Si el comodín es igual a la cadena se retorna un True de no ser así un False
    if comodin=="cc negro":
        return True
    else:
        return False
    
def encontrar_cd(contador):
    #recibe como parametro el contador que incrementa cuando se pone un cambiar dirección de cualquier color un cd
    if (contador%2!=0):#si el contador al dividirlo entre 2 es diferente de 0 se retorna un True no ser asi un False
        return True
    else:
        return False
    #Cada que se pone un cambiar dirección en el uno por ende altera el cambio de dirección pero estos tienen una peculiaridad
    #según la cantidad de veces que se pongan la dirección del juego ira normal o anormal
    #si se pone un cd 1 vez la dirección del juego es anormal si se pone 2 es normal, 3 anormal, 4 normal, 5 anormal, 6 normal
    #Es decir si la cantidad de veces que se pone un cd es una cantidad "IMPAR" la dirección será anormal
    #si la cantidad de veces que se pone un cd es una cantidad "PAR" la dirección será normal
    
        
    

        
        
        

    
        


