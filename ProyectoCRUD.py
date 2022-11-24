#Versión 0.0
from tkinter import * #Importamos de la libreriaa tkinter todos los modulos

#--------------- Configuraciones iniciales --------------- 
raiz = Tk() #TK() viene siendo como la ventana en si
raiz.title("CRUD en python")
raiz.resizable(False,False)#Para que no se pueda alterar el ancho y largo de la interface
raiz.iconbitmap("C:/Users/anton/OneDrive/Escritorio/Curso de Python/Video 59 - Practica guiada I/icono.ico")

#--------------- Frame --------------- 
miFrame = Frame(raiz, width=400, height=500)#Frame() viene siendo una hoja interna sobre la cual ahora si ponemos los elementos que conforman nuestra interface
miFrame.config(bg="#34495E")
miFrame.pack() #.pack() sirve para... empaquetar el Frame en la raiz CREO xD

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

#-------------------- Textos o Labels -------------------- 
labelTitulo = Label(miFrame, text="CRUD Python", fg="White", bg="#34495E", font=("Rockwell", 16))
labelTitulo.place(x=130, y=30)
labelId = Label(miFrame, text="ID: ", fg="White", bg="#34495E", font=("Arial", 12))
labelId.place(x=50, y=70)
labelNombre = Label(miFrame, text="Nombre: ", fg="White", bg="#34495E", font=("Arial", 12))
labelNombre.place(x=50, y=110)
labelApellido = Label(miFrame, text="Apellido(s): ", fg="White", bg="#34495E", font=("Arial", 12))
labelApellido.place(x=50, y=150)
labelDireccion = Label(miFrame, text="Dirección: ", fg="White", bg="#34495E", font=("Arial", 12))
labelDireccion.place(x=50, y=190)
labelPassword = Label(miFrame, text="Contraseña: ", fg="White", bg="#34495E", font=("Arial", 12))
labelPassword.place(x=50, y=230)
labelComentarios = Label(miFrame, text="Comentarios: ", fg="White", bg="#34495E", font=("Arial", 12))
labelComentarios.place(x=50, y=270)

#-------------------- Cuadros de texto -------------------- 
cuadroId = Entry(miFrame)
cuadroId.place(x=200, y=70)
cuadroNombre = Entry(miFrame)
cuadroNombre.place(x=200, y=110)
cuadroApellido = Entry(miFrame)
cuadroApellido.place(x=200, y=150)
cuadroDireccion = Entry(miFrame)
cuadroDireccion.place(x=200, y=190)
cuadroPassword = Entry(miFrame)
cuadroPassword.place(x=200, y=230)
#Cuadro de comentarios
cuadroComentarios = Text(miFrame, width=18, height=6)
cuadroComentarios.place(x=200, y=270)
#Con el command= y .yview le decimos que el scroll debe estar posicionado de manera vertical 
# y dentro del objeto cuadroComentarios
scrollComentarios = Scrollbar(miFrame, command=cuadroComentarios.yview) 
scrollComentarios.place(x=350, y=270)
cuadroComentarios.config(yscrollcommand=scrollComentarios.set)

#-------------------- Botones -------------------- 
botonCrear = Button(miFrame, text="   Crear  ", borderwidth=1) #el borderwidth=1 es para redondear mas el borde
botonCrear.place(x=50, y=400)
botonLeer = Button(miFrame, text="   Leer   ", borderwidth=1)
botonLeer.place(x=130, y=400)
botonBorrar = Button(miFrame, text="  Borrar  ", borderwidth=1)
botonBorrar.place(x=210, y=400)
botonActualizar = Button(miFrame, text="Actualizar", borderwidth=1)
botonActualizar.place(x=290, y=400)

raiz.mainloop()#Este metodo se queda esperando a que el usuario le pase un dato