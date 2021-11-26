from tkinter import *
from tkinter import ttk
from .Themes import *
from tkinter.messagebox import *

class applicacion(object):
    '''
    La clase aplicacion tiene el objetivo de crear el entorno visual de la aplicacion
    '''
    def __init__(self,root):

        # Datos estructurales basicos donde iran los demas fragmentos de la applicacion

        self.root = root
        self.root.title("Mi Primer App")
        self.tema = EleccionTema(0)
        self.root.config(bg = self.tema['fondo_gen'])

        ### Menu Para Eleccion de Temas ###
        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Classic",command=lambda:self.modificartema(0))
        self.filemenu.add_command(label="Dark", command=lambda:self.modificartema(1))
        self.filemenu.add_command(label="Custom", command=lambda:self.modificartema(2))
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Crear Custom", command=customizar_tema)
        self.menubar.add_cascade(label="Temas", menu=self.filemenu)
        self.root.config(menu=self.menubar)

        ### TITULO GENERAL ###
        self.label1 = self.crearlabels(self.root, 0, 0, 7, W+E, text="Ingrese sus datos", 
            bg=self.tema['fondo_tit'], fg=self.tema['letra'], font=("",10,"bold"))

        ###Contenedores##
        #Contenedor para Entradas
        self.framentries = Frame(self.root, bg=self.tema['fondo_gen'])
        self.framentries.grid(row=1, column=0, columnspan=2, rowspan=2)
        #Contenedor para Arbol
        self.framearbol = Frame(self.root, bg=self.tema['fondo_gen'])
        self.framearbol.grid(row=5, column=0, columnspan=7, sticky=W+E)
        #Contenedor para Botones
        self.framebotones = Frame(self.root, bg=self.tema['fondo_gen'])
        self.framebotones.grid(row=1, column=6, rowspan=2)

        ### Contenedor entradas ###

        #Declaracion de labels del cuadro utilizando funcion crearlabels
        self.label2 = self.crearlabels(self.framentries, 1, 0, 1, W, text="Titulo", anchor=W, 
            bg=self.tema['fondo_gen'], fg=self.tema['letra'], font=("",8,"bold"))
        self.label3 = self.crearlabels(self.framentries, 2, 0, 1, W, text="Descripcion", 
            bg=self.tema['fondo_gen'], anchor=W, fg=self.tema['letra'], font=("",8,"bold"))
        
        #Creo los espacios a rellenar (utilizando funcion crearentradas) y defino las variables donde se guardaran los inputs
        self.textotit, self.textodes= StringVar(), StringVar()
        self.llenar1 = self.crearentradas(self.framentries, self.textotit,45,1,2,1)
        self.llenar2 = self.crearentradas(self.framentries, self.textodes,45,2,2,1)
        self.llenarlist=[self.llenar1, self.llenar2]

        ### Contenedor Botones ###

        #botones de alta, baja y modificar
        self.boton_modi = Button(self.framebotones, text="Modificar", bg=self.tema['fondo_gen'], fg=self.tema['letra'], width=10)
        self.boton_baja = Button(self.framebotones, text="Baja", bg=self.tema['fondo_gen'], fg=self.tema['letra'], width=10)
        self.boton_alta = Button(self.framebotones, text="Alta", bg=self.tema['fondo_gen'], fg=self.tema['letra'], width=10)
        self.boton_baja.grid(row=0, column=0)
        self.boton_alta.grid(row=1, column=0)
        self.boton_modi.grid(row=2, column=0)       

        ### Contenedor Arbol ###

        #creacion base del treeview para imprimr datos de la base
        self.arbol=ttk.Treeview(self.framearbol, columns=("1","2","3","4","5","6"), show='headings', selectmode = "browse")
        self.arbol.pack(side = LEFT, fill = BOTH)
        self.dicarbol = {'1':'ID', '2':'Titulo','3':'Descripcion', '4':'Fecha', '5':'Estado Publicacion', '6':'Objeto'}
        for key in self.dicarbol:
            self.arbol.column(key, anchor='c')
            self.arbol.heading(key, text=self.dicarbol[key])
        self.barrita=ttk.Scrollbar(self.framearbol, orient="vertical", command=self.arbol.yview)
        self.barrita.pack(side = RIGHT, fill = Y)
        self.arbol.configure(yscrollcommand=self.barrita.set)

        #listados con todas las widgest que cambian el color de sus fondos con el tema
        self.listafondogen = [  self.label2, self.label3, self.boton_alta, self.boton_baja, self.boton_modi, 
                                self.llenar1, self.llenar2]
        self.listacontenedores = [self.root, self.framentries, self.framearbol, self.framebotones]

        #listados con todas las widgest que cambian el color de sus letras con el tema
        self.listaletras = [    self.label1, self.label2, self.label3, self.boton_alta, 
                                self.boton_baja, self.boton_modi,self.llenar1, self.llenar2]

    #funcion para crear labels
    def crearlabels(self, root, fila, columna, cspan=None, pega=W, **config):
        labeles = Label(root, **config)
        labeles.grid(row=fila, column=columna, columnspan=cspan, sticky=pega)
        return labeles

    #funcion para crear entradas
    def crearentradas(self, root, textoing, ancho, fila, columna, span):
        entrada = Entry(root, textvariable = textoing, width=ancho, bg=self.tema['fondo_gen'])
        entrada.grid(row=fila, column=columna, columnspan=span, sticky=W)
        return entrada
    
    #funcion para modificar colores segun el tema elegido y actualizar tkinter
    def modificartema(self, seleccion):
        self.tema = EleccionTema(seleccion)
        self.actualizarTema()
    
    def actualizarTema(self):
        self.label1['bg']=self.tema['fondo_tit']
        for x in self.listacontenedores:
            x.config(bg = self.tema['fondo_gen'])
        for x in self.listafondogen:
            x['bg'] = self.tema['fondo_gen']
        for x in self.listaletras:
            x['fg'] = self.tema['letra']

    #Funcion que muestra los datos de la tabla dentro del arbol
    def imprimirdatos(self, tdatos):
        self.arbol.delete(*self.arbol.get_children())
        for dato in tdatos:
            self.arbol.insert("", "end", values=(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5]))

if __name__ == "__main__":
    root = Tk()
    x=applicacion(root)
    mainloop()