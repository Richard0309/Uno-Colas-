from tda_cola_circular_doble import Cola_Circular_Doble
import random

def selec_color(carta):#recibe como parametro una carta ya sea con comodín o con número
    n_color=random.randint(1,4)#se generán números aleatorios entre 1 y 4
    #según el número generado se asigna un color
    if (n_color==1):
        color="rojo"
    elif(n_color==2):
        color="azul"
    elif(n_color==3):
        color="amarillo"
    else:
        color="verde"
    #si la carta es un comodín de +4 o cc(cambia color) se retorna la carta más un espacio más la palabra negro
    #si la carta es cualquiera de los otros comodines se retorna la carta más un espacio más el color aleatorio arrojado
    if(carta=="+4"):
        return carta+" "+"negro"
    elif(carta=="+2"):
        return carta+" "+color
    elif(carta=="cc"):
        return carta+" "+"negro"
    elif(carta=="ct"):
        return carta+" "+color
    elif(carta=="cd"):
        return carta+" "+color
    #si la carta es igual a 10 se retorna el valor del 10 como cadena más un espacio más el color elatorio arrojado
    elif(carta==10):
        return str(carta)+" "+color
    else:
        #si la carta es menor que 10 se devuelve concatenado con un 0 seguido del valor de la carta hecho cadena más un espacio
        #más el color aletorio arrojado
        return "0"+str(carta)+" "+color

#esta función recibe como parametro la respuesta de la pregunta escoger color si se puso un +4 o un cc    
def escoger_color(r):
    #se evalua que color se escribió
    if r=="rojo":
        color = "rojo"
    elif r=="azul":
        color = "azul"
    elif r=="verde":
        color = "verde"
    elif r=="amarillo":
        color = "amarillo"
        #se retorna un 00 seguido de un espacio seguido del color que se escogió
    return "00"+" "+color       
        