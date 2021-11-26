from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import shelve, os

#temas a utilizar, por default el tema incial es el tema1, los cargo a la base colores_temas
program_location = os.path.dirname(os.path.abspath(__file__))

database = shelve.open(os.path.join(program_location, 'colores_temas'))
database["tema1"] = {'letra':"black", 'fondo_gen':"snow", 'fondo_tit':"violet", 'fondo_subtit':"red"}
database["tema2"] = {'letra':"grey" ,'fondo_gen':"black",'fondo_tit':"black", 'fondo_subtit':"black"}
#database["tema3"] = {'letra':"black", 'fondo_gen':"snow", 'fondo_tit':"violet", 'fondo_subtit':"red"}
database["colores"] = ['black', 'snow', 'violet', 'blue','dark green', 'gold', 'dark salmon', 'red', 'hot pink']

#funcion que elgie el tema y lo retorna como dictionario
def EleccionTema(eleccion):
    temas_definidos = ['tema1','tema2','tema3']
    try:
        return database[temas_definidos[eleccion]]
    except:
        showerror("Error",'Debes diseñar el tema primero')
        return database[temas_definidos[0]]

#funcion que permite customizar y elegir los colores

def customizar_tema():
    ventancolor = Toplevel()
    ventancolor.title("Elige tus colores favoritos")

    seleccionar_temas(ventancolor)

    ventancolor.wait_visibility()
    ventancolor.grab_set()
    ventancolor.focus_set()
    ventancolor.wait_window()

def seleccionar_temas(root):
    principal = Frame(root, width=200, bg='snow')
    principal.pack()
    elec1, elec2, elec3, elec4 = StringVar(), StringVar(), StringVar(), StringVar()
    elecciones = [elec1, elec2, elec3, elec4]
    titus = ['Letra', 'Fondo', 'Titulo', 'Sub Titulo']
    a = 0
    for i in titus:
        opcionl = ttk.OptionMenu(principal, elecciones[a], *database["colores"])
        opcionl.grid(row=1, column=a)
        Label(principal, text=i, font=("",10,"bold"), width=15, bg='snow').grid(row=0, column=a)
        a = a + 1
    Button(root, text="Aplicar", width=10, command=lambda:aplicar(root, elecciones)).pack()

def aplicar(root, elecciones):
    database["tema3"] = {'letra':elecciones[0].get(),'fondo_gen':elecciones[1].get(),'fondo_tit':elecciones[2].get(),'fondo_subtit':elecciones[3].get()}
    root.destroy()

if __name__ == '__main__':
    root = Tk()
    tema=EleccionTema(2)
    print(tema)
    mainloop()