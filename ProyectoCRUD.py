#Versión 0.0
from tkinter import * #Importamos de la libreriaa tkinter todos los modulos

#--------------- Configuraciones iniciales --------------- 
raiz = Tk() #TK() viene siendo como la ventana en si
raiz.title("CRUD en python")
raiz.resizable(False,False)#Para que no se pueda alterar el ancho y largo de la interface
raiz.iconbitmap("C:/Users/anton/OneDrive/Escritorio/Curso de Python/Video 59 - Practica guiada I/icono.ico")

#--------------- Frame --------------- 
miFrame = Frame(raiz, width=400, height=550)#Frame() viene siendo una hoja interna sobre la cual ahora si ponemos los elementos que conforman nuestra interface
miFrame.config(bg="#34495E")
miFrame.pack() #.pack() sirve para... 

#-------------------- Barra de menu -------------------- 
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)
#Elementos del menu
ddbbMenu = Menu(barraMenu, tearoff=0)#El tearoff es lagrima y al igualarla a 0 le quitamos ese separador que se ve mal
borrarMenu = Menu(barraMenu, tearoff=0)
crudMenu = Menu(barraMenu, tearoff=0)
ayudaMenu = Menu(barraMenu, tearoff=0)
#Opciones
barraMenu.add_cascade(label="DDBB", menu=ddbbMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)
#Sub opciones
ddbbMenu.add_command(label="Conectar")
ddbbMenu.add_separator()#Esto es un separador
ddbbMenu.add_command(label="Salir")
borrarMenu.add_command(label="Borrar campos")
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")




raiz.mainloop()#Este metodo se queda esperando a que el usuario le pase un dato