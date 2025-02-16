class nodoCola(object):
    dato=None
    siguiente=None
    anterior=None

class Cola_Circular_Doble(object):
    
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def cola_vacia(self):
        return self.primero == None
    
    def reiniciar (self):
        self.primero = None
        self.ultimo = None
         
    def insertar_final(self, dato):
        nodo = nodoCola()
        nodo.dato = dato
        nodo.anterior = nodo
        nodo.siguiente = nodo
        if self.cola_vacia():
            self.primero = nodo
            self.ultimo = nodo
        else:
            self.ultimo.siguiente = self.primero
            nodo.anterior = self.ultimo
            self.ultimo.siguiente = nodo
            self.primero.anterior = nodo
            self.ultimo = nodo
            
    def insertar_principio(self, dato):
        nodo = nodoCola()
        nodo.dato = dato
        nodo.anterior = nodo
        nodo.siguiente = nodo
        if self.cola_vacia():
            self.primero = nodo
            self.ultimo = nodo
        else:
            nodo.siguiente = self.primero
            nodo.anterior = self.ultimo
            self.primero.anterior = nodo
            self.primero = nodo
            self.ultimo.siguiente = self.primero
    
    def quitar_principio(self):
        dato = self.primero.dato
        nodo_eliminar = self.primero
        if self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
            nodo_eliminar.siguiente = None
            nodo_eliminar.anterior = None
        return dato
    
    def quitar_final(self):
        dato = self.ultimo.dato
        nodo_eliminar = self.ultimo
        if self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = self.primero
            self.primero.anterior = self.ultimo
            nodo_eliminar.siguiente = None
            nodo_eliminar.anterior = None
        return dato
    
    def primer_dato(self):
        return self.primero.dato
    
    def ultimo_dato(self):
        return self.ultimo.dato
    
    def imprimir_normal(self):
        caux = Cola_Circular_Doble()
        cadena = ""
        while not self.cola_vacia():
            dato = self.quitar_principio()
            cadena += str(dato) +"\n"
            caux.insertar_final(dato)
            
        while not caux.cola_vacia():
            dato = caux.quitar_principio()
            self.insertar_final(dato)
        return cadena
    
    def imprimir_inverso(self):
        caux = Cola_Circular_Doble()
        cadena = ""
        while not self.cola_vacia():
            dato = self.quitar_final()
            cadena += str(dato) +"\n"
            caux.insertar_principio(dato)
            
        while not caux.cola_vacia():
            dato = caux.quitar_final()
            self.insertar_principio(dato)
        return cadena