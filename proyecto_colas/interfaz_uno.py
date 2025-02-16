from tkinter import*
from tda_cola_lineal import Cola_Lineal
from tda_cola_circular_doble import Cola_Circular_Doble
from tda_pila import Pila
from funciones_colas import*
from colores import selec_color
from colores import escoger_color
from banco_aleatorio import b_aleatorio
import random
import time
r= str()
winner=bool(False)
jugadores = Cola_Circular_Doble()
jugadores_aux = Cola_Circular_Doble()
b_cartas = Cola_Lineal()
b_cartasaux = Cola_Lineal()
baraja1 = Cola_Circular_Doble()
baraja2= Cola_Circular_Doble()
baraja3=  Cola_Circular_Doble()
baraja4= Cola_Circular_Doble()
barajas= Cola_Circular_Doble()
poner_cartas = Pila()
poner_cartaAux = Pila()
#creando el frame
raiz = Tk()
nombre = StringVar()

miFrame = Frame(raiz, width=1300, height=800)
miFrame.pack()

etiqueta1 = Label(miFrame, text="Nombre:")
etiqueta1.grid(row=0, column=0, padx=10, pady=10)

etiqueta6 = Label(miFrame, text="Jugadores:")
etiqueta6.grid(row=3, column=1, padx=10, pady=10)

salida_jugadores = Text(miFrame, width=25, height = 4)
salida_jugadores.grid(row=3, column=2, padx=10, pady=10)
salida_jugadores.config(state=DISABLED)

entrada_nombres = Entry(miFrame)
entrada_nombres.grid(row=0,column=1,padx=10,pady=10, columnspan=3)

etiqueta2 = Label(miFrame, text="Carta:")
etiqueta2.grid(row=1, column=1, padx=10, pady=10)

entrada_cartas = Entry(miFrame)
entrada_cartas.grid(row=1,column=2,padx=10,pady=10, columnspan=3)
entrada_cartas.config(state = "disabled")

etiqueta3 = Label(miFrame, text="Ganador:")
etiqueta3.grid(row=0, column=12, padx=1, pady=1)

salida_ganador = Text(miFrame, width=25, height = 1)
salida_ganador.grid(row=1, column=12, padx=1, pady=1)
salida_ganador.config(state=DISABLED)

etiqueta4 = Label(miFrame, text="Jugador en turno")
etiqueta4.grid(row=0, column=10, padx=10, pady=10)

salida_turno = Text(miFrame, width=25, height = 1)
salida_turno.grid(row=1, column=10, padx=10, pady=10)
salida_turno.config(state=DISABLED)

etiqueta5 = Label(miFrame, text="Baraja del jugador: ")
etiqueta5.grid(row=2, column=10, padx=10, pady=10)

etiqueta7 = Label(miFrame, text="Última carta puesta")
etiqueta7.grid(row=5, column=10,padx=1,pady=1)

etiqueta_color = Label(miFrame, text="Color para cambiar: ")
etiqueta_color.grid(row=4, column=1,padx=1,pady=1)

entrada_color = Entry(miFrame)
entrada_color.grid(row=4,column=2,padx=1,pady=1, columnspan=3)
entrada_color.config(state = "disabled")

salida_baraja = Text(miFrame, width=25, height = 25)
salida_baraja.grid(row=3, column=10, padx=10, pady=10)
salida_baraja.config(state=DISABLED)

scrollVert = Scrollbar(miFrame, command=salida_baraja.yview)
scrollVert.grid(row=3, column=5, sticky="nsew")
salida_baraja.config(yscrollcommand=scrollVert.set)

salida_uc = Text(miFrame, width=15, height = 1)
salida_uc.grid(row=4, column=10, padx=10, pady=1)
salida_uc.config(state=DISABLED)






def insertar_nombre():
    nombre= entrada_nombres.get()
    cg=int(0)
    if nombre != "":
        jugadores.insertar_final(nombre)
        salida_jugadores.config(state="normal")
        salida_jugadores.delete("1.0","end")
        salida_jugadores.insert("1.0",jugadores.imprimir_normal())
        salida_jugadores.config(state=DISABLED)
        entrada_nombres.delete(0,"end")
        if not jugadores.cola_vacia():
            while not jugadores.cola_vacia():
                jugadores_aux.insertar_final(jugadores.quitar_final())
                cg=cg+1
            while not jugadores_aux.cola_vacia():
                jugadores.insertar_final(jugadores_aux.quitar_final())
    else:
        NombreNoV()
    if cg==4:
        jugar()
    return cg
        
def NombreNoV():
    raiz = Tk()
    ventana = Frame(raiz, width=1300, height=800)
    ventana.pack()
    etiqueta = Label(ventana, text="No puede dejar el nombre en blanco")
    etiqueta.grid(row=0, column=1,padx=1,pady=1)
    
def desab():
    salida_turno.configure(state='disabled')

def jugar():
    if not jugadores.cola_vacia():
         #entrada_nombres.config(state = "disabled")
         salida_jugadores.config(state=DISABLED)
         desab()
         c=int(0)
         while not jugadores.cola_vacia():
             jugadores_aux.insertar_final(jugadores.quitar_principio())
             c=c+1
         while not jugadores_aux.cola_vacia():
             jugadores.insertar_final(jugadores_aux.quitar_principio())
             
         if c>1:
             etiqueta1.destroy()
             entrada_nombres.destroy()
             entrada_cartas.config(state = "normal")
             boton_sacar.configure(state="normal")
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
                
             while not b_cartas.cola_vacia():
                 b_cartasaux.insertar(selec_color(b_cartas.quitar()))
             while not b_cartasaux.cola_vacia():
                 b_cartas.insertar(b_cartasaux.quitar())
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
                
             carta=random.randint(1,10)
             poner_cartas.insertar(selec_color(carta))
             
             salida_uc.configure(state='normal')
             salida_uc.delete("1.0","end")
             salida_uc.insert("1.0",str(poner_cartas.tope_pila()))
             salida_uc.config(state=DISABLED)
            
             salida_turno.configure(state='normal')       
             salida_turno.delete("1.0","end")
             salida_turno.insert("1.0",str(jugadores.primer_dato()))
             salida_turno.config(state=DISABLED)
             
             salida_baraja.configure(state='normal')
             salida_baraja.delete("1.0","end")
             salida_baraja.insert("1.0",impresion(barajas.primer_dato()))
             salida_baraja.config(state=DISABLED)
             boton_jugar.destroy()
             boton_guardar.destroy()
    
         else:
             Ventana_emer2()

     
    else:
        Ventana_emer()
        
def Ventana_emer2():
    raiz = Tk()
    miFrame = Frame(raiz, width=1300, height=800)
    miFrame.pack()
    etiqueta = Label(miFrame, text="No se puede jugar con una sola persona")
    etiqueta.grid(row=0, column=5, padx=10, pady=10)
        
def Ventana_emer():
    raiz = Tk()
    miFrame = Frame(raiz, width=1300, height=800)
    miFrame.pack()
    etiqueta = Label(miFrame, text="Jugadores no registrados")
    etiqueta.grid(row=0, column=5, padx=10, pady=10)
    
def Sacar():
    insertar(barajas.primer_dato(),b_aleatorio())
    salida_baraja.configure(state='normal')
    salida_baraja.delete("1.0","end")
    salida_baraja.insert("1.0",impresion(barajas.primer_dato()))
    salida_baraja.config(state=DISABLED)
    
def Poner():
    c_cartas=int(0)
    winner=bool(False)
    carta=entrada_cartas.get()
    entrada_cartas.delete(0,"end")
    if carta != "":
        if buscar(barajas.primer_dato(),carta) != False:
            #se busca la carta que se va a poner
            if (comprobar_c(primero(barajas.primer_dato()),poner_cartas.tope_pila())==True):#se compara que el color o número de la carta sea compatible con la última carta puesta
                poner_cartas.insertar(quitar(barajas.primer_dato()))
                salida_baraja.configure(state='normal')
                salida_baraja.delete("1.0","end")
                salida_baraja.insert("1.0",impresion(barajas.primer_dato()))
                salida_baraja.config(state=DISABLED)
                salida_uc.configure(state='normal')
                salida_uc.delete("1.0","end")
                salida_uc.insert("1.0",str(poner_cartas.tope_pila()))
                salida_uc.config(state=DISABLED)
                #reiniciar(barajas.primer_dato())
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
                poner_cartas.insertar(primero(barajas.primer_dato()))
                salida_uc.delete("1.0","end")
                salida_uc.insert("1.0",str(poner_cartas.tope_pila()))
                salida_baraja.delete("1.0","end")
                salida_baraja.insert("1.0",impresion(barajas.primer_dato()))
            if winner == True:
                salida_ganador.configure(state='normal')
                salida_ganador.delete("1.0","end")
                salida_ganador.insert("1.0",str(jugadores.primer_dato()))
                salida_ganador.config(state=DISABLED)
                
                salida_baraja.configure(state='normal')
                salida_baraja.delete("1.0","end")
                salida_baraja.config(state=DISABLED)
                
                salida_jugadores.configure(state='normal')
                #salida_jugadores.delete("1.0","end")
                salida_jugadores.config(state=DISABLED)
                
                salida_turno.configure(state='normal')
                salida_turno.delete("1.0","end")
                salida_turno.config(state=DISABLED)
                
                salida_uc.configure(state='normal')
                salida_uc.delete("1.0","end")
                salida_uc.config(state=DISABLED)
                boton_poner.config(state="disabled")
                boton_sacar.config(state="disabled")
                entrada_cartas.config(state="disabled")
                ventana_fin()
                
                
            else:
                
                while not poner_cartas.pila_vacia():
                    if ((poner_cartas.tope_pila()=="cd verde")or(poner_cartas.tope_pila()=="cd rojo")or(poner_cartas.tope_pila()=="cd amarillo")or(poner_cartas.tope_pila()=="cd azul")):
                        c_cartas= c_cartas+1
                    poner_cartaAux.insertar(poner_cartas.quitar())
                while not poner_cartaAux.pila_vacia():
                    poner_cartas.insertar(poner_cartaAux.quitar())
                
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
                        Cambiar_color()
                        jugadores.insertar_principio(jugadores.quitar_final())
                        barajas.insertar_principio(barajas.quitar_final())
                        for i in range (4):
                            insertar(barajas.primer_dato(),b_aleatorio())
                        jugadores.insertar_principio(jugadores.quitar_final())
                        barajas.insertar_principio(barajas.quitar_final())
                        
                            
                    if com_comodin4(poner_cartas.tope_pila())==True:#cambia color
                        Cambiar_color()
                    """salida_turno.delete("1.0","end")
                    salida_turno.insert("1.0",str(jugadores.primer_dato()))
                    salida_baraja.delete("1.0","end")
                    salida_baraja.insert("1.0",impresion(barajas.primer_dato()))"""
                        
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
                        Cambiar_color()
                        jugadores.insertar_final(jugadores.quitar_principio())
                        barajas.insertar_final(barajas.quitar_principio())
                        for i in range (4):
                            insertar(barajas.primer_dato(),b_aleatorio())
                        jugadores.insertar_final(jugadores.quitar_principio())
                        barajas.insertar_final(barajas.quitar_principio())
                    
                    if com_comodin4(poner_cartas.tope_pila())==True:
                        Cambiar_color()
                        
                salida_turno.configure(state='normal')     
                salida_turno.delete("1.0","end")
                salida_turno.insert("1.0",str(jugadores.primer_dato()))
                salida_turno.config(state=DISABLED)
                salida_baraja.configure(state='normal')
                salida_baraja.delete("1.0","end")
                salida_baraja.insert("1.0",impresion(barajas.primer_dato()))
                salida_baraja.config(state=DISABLED)
                
        else:
            NoEncontrado()
            
    else:
        Ventana_Error()

def Ventana_Error():
   raiz = Tk()
   ventana = Frame(raiz, width=1300, height=800)
   ventana.pack()
   etiqueta = Label(ventana, text="Escriba primero la carta a poner")
   etiqueta.grid(row=0, column=5,padx=1,pady=1)
   
def ventana_fin():
   raiz = Tk()
   ventana = Frame(raiz, width=1300, height=800)
   ventana.pack()
   etiqueta = Label(ventana, text="FIN DEL JUEGO")
   etiqueta.grid(row=0, column=5,padx=1,pady=1)
   
def ventana_aviso():
   raiz = Tk()
   ventana = Frame(raiz, width=1300, height=800)
   ventana.pack()
   etiqueta = Label(ventana, text="Escriba el color para cambiar en el espacio marcado")
   etiqueta.grid(row=0, column=5,padx=1,pady=1) 
    
def Cambiar_color():
    boton_sacar.configure(state="disabled")
    entrada_cartas.configure(state="disabled")
    boton_color.configure(state="normal")
    entrada_color.configure(state="normal")
    ventana_aviso()

def cambiar():
    color=entrada_color.get()
    if color != "":
        if color == "verde" or color == "rojo" or color == "azul" or color == "amarillo":
            poner_cartas.insertar(escoger_color(color))
            salida_uc.configure(state='normal')
            salida_uc.delete("1.0","end")
            salida_uc.insert("1.0",str(poner_cartas.tope_pila()))
            salida_uc.config(state=DISABLED)
            entrada_color.delete(0,"end")
            entrada_color.configure(state="disabled")
            boton_color.configure(state="disabled")
            boton_sacar.configure(state="normal")
            entrada_cartas.configure(state="normal")
        else:
            ventana_no_color()
    else:
        ventana_color()

    
def ventana_color():
   raiz = Tk()
   ventana = Frame(raiz, width=1300, height=800)
   ventana.pack()
   etiqueta = Label(ventana, text="Escriba el color que va a cambiar")
   etiqueta.grid(row=0, column=5,padx=1,pady=1)

def ventana_no_color():
   raiz = Tk()
   ventana = Frame(raiz, width=1300, height=800)
   ventana.pack()
   etiqueta = Label(ventana, text="El color escrito no es válido")
   etiqueta.grid(row=0, column=5,padx=1,pady=1)
        
    
        
boton_guardar = Button(miFrame, text= "Guardar",command=insertar_nombre)
boton_guardar.grid(row=0,column=3,padx=10,pady=10)

boton_poner = Button(miFrame, text= "Poner",command=Poner)
boton_poner.grid(row=2,column=2,padx=1,pady=1)

boton_sacar = Button(miFrame, text= "Sacar",command=Sacar)
boton_sacar.grid(row=2,column=3,padx=1,pady=1)
boton_sacar.configure(state="disabled")

boton_jugar = Button(miFrame, text= "Jugar",command=jugar)
boton_jugar.grid(row=2,column=1,padx=1,pady=1)

boton_color = Button(miFrame, text= "Cambiar color",command=cambiar)
boton_color.grid(row=4,column=3,padx=1,pady=1)
boton_color.configure(state="disabled")


raiz.mainloop()

