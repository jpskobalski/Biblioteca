from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from .VIEW import *
from .MODEL import *

class controlador:
    '''
    La clase controlador es la clase a quien llama el main para ejecutar la apliccacion, este se encarga de ejecutar VIEW y MODEL, 
    que a su vez ejecutan la apariencia y la logica de la aplicacion. Esta clase regula la interaccion entre estas y su relacion con el usuario.
    '''
    def __init__(self, root):
        self.root = root

        #creo el cuerpo de la app llamando a la clase applicacion, la cual contiene el diseño visual (dentro de VIEW)
        self.cuerpoapp = applicacion(self.root)

        #Creo al administrador utilizando clase administradora definida en MODEL
        #Tiene el objetivo de manejar la base de datos
        self.Administrador = Administradora()
        self.ObservadorAdministrador = Observador(self.Administrador, self.cuerpoapp)
        '''
        Les asigno a los botones de alta, mostrar, baja y modificacion de la clase aplicacion la funciones mostrarDatos, altaDatos, bajaDatos y modiDatos
        de esta manera la clase controladora regula a los modulos MODEL y VIEW, y la relacion entre si
        sin que haya relacion directa entre ellos
        '''
        self.cuerpoapp.boton_alta.config(command=self.altaDatos)
        self.cuerpoapp.boton_baja.config(command=self.bajaDatos)
        self.cuerpoapp.boton_modi.config(command=self.modiDatos)
    
    def altaDatos(self):
        self.Administrador.entradas(self.cuerpoapp.textotit, self.cuerpoapp.textodes, self.cuerpoapp.llenarlist)
        self.ObservadorAdministrador.actualizar_datos()
    
    def bajaDatos(self):
        idselected = self.cuerpoapp.arbol.item(self.cuerpoapp.arbol.focus())
        if idselected['values']=='':
            showerror("Error: Eliga Linea","No ha seleccionado ninguna linea")
            return
        idbaja = int(idselected['values'][0])
        self.Administrador.baja(idbaja)
        self.ObservadorAdministrador.actualizar_datos()
    
    def modiDatos(self):
        idselected = self.cuerpoapp.arbol.item(self.cuerpoapp.arbol.focus())
        if idselected['values']=='':
            showerror("Error: Eliga Linea","No ha seleccionado ninguna linea")
            return
        idmod = int(idselected['values'][0])
        self.Administrador.modificacion(idmod, self.cuerpoapp.textotit, self.cuerpoapp.textodes, self.cuerpoapp.llenarlist)
        self.ObservadorAdministrador.actualizar_datos()

class Observador:
    '''
    Clase que observa el objeto y sus alteraciones de la clase admniistradora, para poder actualizar a VIEW y la pueda imprimir en pantalla las actualizaciones de la base de datos
    '''    
    def __init__(self, objeto, view):
        self.observador = objeto
        self.hojaimpresion = view
        self.actualizar_datos()

    def actualizar_datos(self):
        self.datos_actualizados = self.observador.obternerDatos()
        self.hojaimpresion.imprimirdatos(self.datos_actualizados)