from tkinter import *
from tkinter.messagebox import *
from .ORM import *
from .logs import *
import re

class Administradora:
    '''
    La clase administradora tiene el objetivo de "administrar" y conectar el archivo '__main__' con la base de datos utilizabndo peewee + SQLITE3
    Este es llamado por el controlador para que se comunique con VIEW y el usuario.
    '''
    def validar(self, texto=None):
        '''
        valida los textos ingresados retornando False y un cartel de error si no se cumple el patron
        '''
        patron="^[A-Za-z]+(?:[ -][A-Za-z]+)*$"
        if not re.fullmatch(patron, texto):
            showerror("Error","El Titulo ingresado es incorrecto.")
            return False
        else: 
            return True

    def entradas(self, textotit, textodes, llenarlist):
        '''
        Funcion que valida para luego ingresar datos a la base a traves de la funcion Alta
        '''
        if not self.validar(textotit.get()):
            return
        self.alta(textotit, textodes, llenarlist)
        
    def alta(self, textotit, textodes, llenarlist):
        '''
        ingresa datos a la base
        '''
        try:
            subir = Noticia(titulo=textotit.get(), descripcion = textodes.get())
            subir.save()
            self.limpiargrid(llenarlist)
            crear_log('alta')
        except:
            showerror("Error","El Titulo ingresado ya existe.")            

    def limpiargrid(self, listalimpia):
        '''
        Funcion para limpiar los espacios que han sido ingresados a la base de datos
        '''
        for x in range(len(listalimpia)):
            listalimpia[x].delete(0, "end")

    def baja(self, id_baja):
        '''
        Elimina los datos de la base a travez de su ID
        '''
        dato_eliminar = Noticia.get(Noticia.id == id_baja)
        dato_eliminar.delete_instance()
        crear_log('baja')
    
    def modificacion(self, id_mod, textotit, textodes, llenarlist):
        '''
        Modifica los datos de la base a travez de su ID con un nuevo ingreso de datos validados 
        '''
        if not self.validar(textotit.get()):
            return
        try:
            dato_modificar = Noticia.update(titulo = textotit.get(), descripcion = textodes.get()).where(Noticia.id == id_mod)
            dato_modificar.execute()
            self.limpiargrid(llenarlist)
            crear_log('modi')
        except:
            showerror("Error","El Titulo ingresado ya existe.")

    def obternerDatos(self):
        '''
        busca en la base de datos, todos los datos que contenga, los devuelve al controllador para que sean impresos con VIEW
        '''
        tdatos = []
        for datos in Noticia.select():
            dato = [datos.id, datos.titulo, datos.descripcion, datos.fecha, datos.estado_de_publicacion, datos]
            tdatos.append(dato)
        return tdatos
