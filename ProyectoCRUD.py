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

#--------------- Barra de menu --------------- 



raiz.mainloop()#Este metodo se queda esperando a que el usuario le pase un dato