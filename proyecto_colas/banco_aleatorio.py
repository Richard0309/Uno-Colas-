import random
from colores import selec_color#se importa la función de selec_color
def b_aleatorio():
    carta= random.randint(1,15)#se escoge un número aleatorio entre 1 y 15
    if carta>10:#si la carta es mayor a 10 se le asgina un valor de comodin
        if carta==11:
            carta="+2"
        elif carta==12:
            carta="+4"
        elif carta==13:
            carta="cd"
        elif carta==14:
            carta="ct"
        elif carta==15:
            carta="cc"
    else:
        carta=carta#si la carta es menor o igual a 10 la carta vale ese número mismo
    carta_final=selec_color(carta)#esta variable vale el valor que retorne la función que recibió como parametro la carta
    return carta_final#se retorna la variable
            