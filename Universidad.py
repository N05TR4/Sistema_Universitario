import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#from  sklearn import tree
import pymysql


def Menu_principal():

    # Creando ventana del inicio
    global pantalla
    pantalla = Tk()
    pantalla.geometry("350x445+450+125")
    pantalla.title("Bienvenido")
    pantalla.iconbitmap("inicio.ico")


    # Agregando una iamgen
    image = PhotoImage(file = "iniciar.gif")
    image = image.subsample(4, 4)
    label = Label(image = image)
    label.pack()

    # creando etiqueta
    Label(text = "Acceso al Sistema", bg = "#24b43c", font = ("Cambria", 15),
          fg = "white", width = "350", height = "3").pack()
    Label(text = "").pack()

    # Creando los botones
    Button(text = "Iniciar Seccion", command = inicio_seccion,font = "Cambria", width = "30", height = "2").pack()
    Label(text = "").pack()
    Button(text = "Registrarse", command = registrar,font = "Cambria", width = "30", height = "2").pack()
    Label(text = "").pack()
    Button(text = "Salir", font = "Cambria", width = "30", height = "2", command = pantalla.quit).pack()

    pantalla.mainloop()



# Funcion para la pantalla de iniciar seccion
def inicio_seccion():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x350+425+125")
    pantalla1.title("Inicio de Seccion")
    pantalla1.iconbitmap("inicio.ico")


    Label(pantalla1, text = "Por favor ingrese su usuario y contraseña\n a continuacion", bg = "#24b43c", font = ("Cambria", 15),
          fg = "white", width = "350", height = "3").pack()
    Label(pantalla1, text = "").pack()

    global nombreUsuario_verify
    global password_verify

    nombreUsuario_verify = StringVar()
    password_verify = StringVar()

    global nombre_usuario_entry
    global password_usuario_entry

    # Dandole entrada a el usuario y la contaseña
    Label(pantalla1, text = "Usuario", font = ("Cambria", 15),
          fg = "Black", width = "20", height = "2").pack()
    nombre_usuario_entry = Entry(pantalla1, textvariable = nombreUsuario_verify, width = "40")
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña", font = ("Cambria", 15),
          fg = "Black", width = "20", height = "2").pack()
    password_usuario_entry= Entry(pantalla1, textvariable = password_verify, width = "40", show = "*")
    password_usuario_entry.pack()
    Label(pantalla1).pack()

    # Creando boton de la pantalla1 para iniciar seccion
    Button(pantalla1, text = "Iniciar Seccion", font = "Cambria",command=validacion_datos, width = "30", height = "2").pack()

# Funcion que contiene la ventana para hacer el registro
def registrar():
    # Creando la ventana de registro
    global pantalla2
    pantalla2 = Toplevel(pantalla)
    pantalla2.geometry("410x350+450+125")
    pantalla2.title("Registrarse")
    pantalla2.iconbitmap("inicio.ico")

    global nombreUsuario_entry
    global password_entry

    nombreUsuario_entry = StringVar()
    password_entry = StringVar()

    # Creando etiqueta
    Label(pantalla2, text = "Por favor ingrese un usuario y una contraseña,\n para el Registrarse en el Sitema ",
          bg="#24b43c", font=("Cambria", 15), fg="white", width="350", height="3").pack()
    Label(pantalla2, text="").pack()

    # Dandole entrada para el registro
    Label(pantalla2, text="Usuario", font=("Cambria", 15),
          fg="Black", width="20", height="2").pack()
    nombreUsuario_entry = Entry(pantalla2,width="40")
    nombreUsuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Contraseña", font=("Cambria", 15),
          fg="Black", width="20", height="2").pack()
    password_entry = Entry(pantalla2, width="40", show = "*")
    password_entry.pack()
    Label(pantalla2).pack()

    # Creando boton de la pantalla2 para Registrarse
    Button(pantalla2, text="Registrarse", command = insertar_datos, font="Cambria", width="30", height="2").pack()

# Esta funcion realiza la conexion a la base de datos e inserta los datos de la ventana registro en la tabla login
def insertar_datos():

    #sql = "INSERT INTO login (Usuario ,Contraseña) VALUES ('{0}','{1}')".format(nombreUsuario_entry.get(), password_entry.get())

    miConexion = sqlite3.connect('universidad.db')
    miCursor = miConexion.cursor()

    try:
        datos = nombreUsuario_entry.get(), password_entry.get()
        miCursor.execute("INSERT INTO login VALUES(?,?)", datos)
        miConexion.commit()
        miCursor.close()
        miConexion.close()
        messagebox.showinfo("Exitoso", message="Usuario Registrado Correctamente")



    except Exception as e:
        messagebox.showwarning("ADVERTENCIA:",
                               "Ocurrio un error al crear el registro, verifique la conexion con la base de datos ")
        print(e)


def validacion_datos():
    miConexion = sqlite3.connect('universidad.db')
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT Contraseña FROM login WHERE Usuario ='" + nombreUsuario_verify.get()+"' AND Contraseña='"+password_verify.get()+"'")
    if miCursor.fetchall():
        #messagebox.showinfo(title="Inicio de Seccion Correcto", message="Bienvenido")
        pantalla1.destroy()
        miConexion.close()
        ventanaPrueba()



    else:
        messagebox.showinfo(title="Inicio de Seccion Incorrecto", message="Usuario o contraseña Incorrectos")
        miConexion.close()











# ######################## Funcion de la ventana principal o ventana de inicio despues del login ###############################
def ventanaPrueba():

    global pantalla_Inicio
    pantalla_Inicio = Toplevel(pantalla)
    pantalla_Inicio.geometry("800x800+300+100")
    pantalla_Inicio.title("Bienvenido Universidad UNPHU")
    pantalla_Inicio.iconbitmap("inicio.ico")
    pantalla_Inicio.config(background="white")
    pantalla_Inicio.state('zoomed')
    pantalla_Inicio.resizable(False, False)


    image = PhotoImage(file="logo.gif")
    image = image.subsample(1, 1)
    label = Label(pantalla_Inicio, image=image).place(x=0, y=120)

    Titulo1 = Label(pantalla_Inicio, text="", font=("Cambria", 15), bg="#24b43c", fg="white", width="500", height="3")
    Titulo1.place(x=0, y=650)
    Label(pantalla_Inicio, text="UNPHU", bg="#24b43c", font=("Cambria", 25),
          fg="white", width="350", height="3").pack()

    Label(pantalla_Inicio, text="Estudiantes Inscritos", bg="white", font=("Cambria", 20),
          fg="black", width="35", height="3").place(x=400, y=200)


    # Creando barra de menu
    menubarra = Menu(pantalla_Inicio)
    pantalla_Inicio.config(menu=menubarra)
    filemenu = Menu(menubarra)
    filemenu = Menu(menubarra, tearoff=0)
    filemenu.add_command(label="Acerca de", command= mensaje)
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=pantalla_Inicio.destroy)
    menubarra.add_cascade(label="OPCIONES", menu=filemenu)
    menubarra.add_cascade(label="ESTUDIANTES", command=V_estudiante)
    menubarra.add_cascade(label="PROFESOR", command=V_profesor)
    menubarra.add_cascade(label="MATERIAS", command=V_materia)

    # ################################ Tabla ##########################################
    global tree1
    tree1 = ttk.Treeview(pantalla_Inicio, height=10, columns=('#0', '#1', '#2', '#3', '#4', '#5'))
    tree1.place(x=0, y=300)
    #tree.column('#0', width=100)
    tree1.heading('#0', text="Nombre", anchor=CENTER)
    tree1.heading('#1', text="Apellido", anchor=CENTER)
    tree1.heading('#2', text="Direccion", anchor=CENTER)
    tree1.heading('#3', text="Telefono", anchor=CENTER)
    #tree1.heading('#4', text="Fecha Nacimiento", anchor=CENTER)
    tree1.heading('#4', text="Matricula", anchor=CENTER)
    tree1.heading('#5', text="Carrera", anchor=CENTER)
    tree1.column('#4', width=300, minwidth=300)

    mostrar_datosInicio()
    pantalla_Inicio.mainloop()

# ################# Metodo para listar los datos en la pantalla de inicio ############# #
def mostrar_datosInicio():
    miConexion = sqlite3.connect('universidad.db')
    miCursor = miConexion.cursor()
    registros = tree1.get_children()
    for elemento in registros:
        tree1.delete(elemento)

    try:
        miCursor.execute("SELECT nombre, apellido, direccion, telefono, matricula, carrera FROM estudiante")
        miConexion.commit()
        for row in miCursor:
            tree1.insert('', 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))

    except:
        pass



########################################################################################################################

def mensaje():
    acerca = '''
    Aplicacion: Sistema Universitario UNPHU.
    Version: 1.0
    Lenguaje de Programacion: Python 3.8.5
    Creador: N05TR4
    Fecha: 25/04/2021.
    '''
    messagebox.showinfo(title= "Informacion", message= acerca)







# ###################################### Ventana para registrar los estudiantes ###################################### #

def V_estudiante():
    # Variables de la Ventana estudiantes
    global nombre
    global apellido
    global direccion
    global fecha
    global telefono
    global matricula
    global carrera
    nombre = StringVar()
    apellido = StringVar()
    direccion = StringVar()
    fecha = StringVar()
    telefono = StringVar()
    matricula = StringVar()
    carrera = StringVar()


    global pantallaEstudiante

    pantallaEstudiante = Toplevel(pantalla)
    pantallaEstudiante.geometry("800x800+300+100")
    pantallaEstudiante.title("Bienvenido Universidad UNPHU")
    pantallaEstudiante.iconbitmap("inicio.ico")
    #pantallaEstudiante.config(background="black")
    pantallaEstudiante.state('zoomed')
    pantallaEstudiante.resizable(False, False)

    image = PhotoImage(file="logo.gif")
    image = image.subsample(1, 1)
    label = Label(pantallaEstudiante, image=image).place(x=0, y=120)

    Titulo1 = Label(pantallaEstudiante, text="", font=("Cambria", 15), bg="#24b43c", fg="white", width="500", height="3")
    Titulo1.place(x=0, y=650)
    Label(pantallaEstudiante, text="Registro Estudiante", bg="#24b43c", font=("Cambria", 25),
          fg="white", width="350", height="3").pack()

    # #####################Creando las etiquetas y las entrada de los datos#######################

    Label(pantallaEstudiante, text="Nombre:", font=("Cambria", 12),
          fg="Black", width="8", height="2").place(x=300, y=120)
    nombre1 = Entry(pantallaEstudiante, textvariable=nombre, width = 25)
    nombre1.place(x=400, y=135)

    Label(pantallaEstudiante, text="Apellido:", font=("Cambria", 12),
          fg="Black", width="8", height="2").place(x=550, y=120)
    apellido1 = Entry(pantallaEstudiante, textvariable=apellido, width=25)
    apellido1.place(x=650, y=135)

    Label(pantallaEstudiante, text="Direccion:", font=("Cambria", 12),
          fg="Black", width="8", height="2").place(x=810, y=120)
    direccion1 = Entry(pantallaEstudiante, textvariable=direccion, width=30)
    direccion1.place(x=910, y=135)

    Label(pantallaEstudiante, text="Fecha de Nacimiento:", font=("Cambria", 12),
          fg="Black", width="18", height="2").place(x=297, y=180)
    fecha1 = Entry(pantallaEstudiante, textvariable=fecha, width=40)
    fecha1.place(x=470, y=190)

    Label(pantallaEstudiante, text="Telefono:", font=("Cambria", 12),
          fg="Black", width="20", height="2").place(x=650, y=180)
    telefono1 = Entry(pantallaEstudiante, textvariable=telefono, width=30)
    telefono1.place(x=805, y=190)

    Label(pantallaEstudiante, text="Matricula:", font=("Cambria", 12),
          fg="Black", width="8", height="2").place(x=305, y=230)
    matricula1 = Entry(pantallaEstudiante, textvariable=matricula, width=30)
    matricula1.place(x=415, y=240)

    Label(pantallaEstudiante, text="Carrera:", font=("Cambria", 12),
         fg="Black", width="8", height="2").place(x=570, y=230)
    carrera1 = Entry(pantallaEstudiante, textvariable=carrera, width=40)
    carrera1.place(x=670, y=240)



    # ################################ Tabla ##########################################
    global tree
    tree = ttk.Treeview(pantallaEstudiante, height=10, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6'))
    tree.place(x=10, y=320)
    tree.column('#0', width=100)
    tree.heading('#0', text="Nombre", anchor=CENTER)
    tree.column('#1', width=100)
    tree.heading('#1', text="Apellido", anchor=CENTER)
    tree.heading('#2', text="Direccion", anchor=CENTER)
    tree.heading('#3', text="Fecha Nacimiento", anchor=CENTER)
    tree.column('#4', width=150, minwidth=100)
    tree.heading('#4', text="Telefono", anchor=CENTER)
    tree.column('#5', width=150, minwidth=100)
    tree.heading('#5', text="Matricula", anchor=CENTER)
    tree.column('#6', width=200, minwidth=100)
    tree.heading('#6', text="Carrera", anchor=CENTER)

    #tree.bind("<Double-1>", seleccionar)

    # ######################## Creando Los Botones ####################################
    agregar = Button(pantallaEstudiante, text="Agregar Registro",width="25", command=ingresar_datos)
    agregar.place(x=305, y=290)

    actualizar= Button(pantallaEstudiante, text="Actualizar Registro", width="25", command=actualizar_data)
    actualizar.place(x=530, y=290)

    listar= Button(pantallaEstudiante, text="Listar Registro", width="25", command=mostrar_datos)
    listar.place(x=760, y=290)

    eliminar = Button(pantallaEstudiante, text="Eliminar Registro", bg="red", width="25", command=Eliminar)
    eliminar.place(x=990, y=290)
    mostrar_datos()

    def seleccionar(event):
        item = tree.identify('item', event.x, event.y)
        nombre.set(tree.item(item, "text"))
        #nombre.set(tree.item(item, "values")[0])
        apellido.set(tree.item(item, "values")[0])
        direccion.set(tree.item(item, "values")[1])
        fecha.set(tree.item(item, "values")[2])
        telefono.set(tree.item(item, "values")[3])
        matricula.set(tree.item(item, "values")[4])
        carrera.set(tree.item(item, "values")[5])

    tree.bind("<Double-1>", seleccionar)

    pantallaEstudiante.mainloop()

# ############### Metodos para el CRUD para la ventana estudiante ###################################

def ingresar_datos():


    miConexion = sqlite3.connect('universidad.db')
    miCursor = miConexion.cursor()

    try:
        datos = nombre.get(), apellido.get(), direccion.get(), fecha.get(), telefono.get(), matricula.get(), carrera.get()
        miCursor.execute("INSERT INTO estudiante VALUES(?,?,?,?,?,?,?)", datos)
        miConexion.commit()
        LimpiarCampoEstudiante()
        mostrar_datos()
        messagebox.showinfo("Exitoso", message="Registro Exitoso")

    except:
        messagebox.showwarning("ADVERTENCIA:",
                               "Ocurrio un error al crear el registro, verifique la conexion con la base de datos")
        LimpiarCampoEstudiante()


def mostrar_datos():
    miConexion = sqlite3.connect('universidad.db')
    miCursor = miConexion.cursor()
    registros = tree.get_children()
    for elemento in registros:
        tree.delete(elemento)

    try:
        miCursor.execute("SELECT * FROM estudiante")
        miConexion.commit()
        for row in miCursor:
            tree.insert('', 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6]))

    except:
        pass


def actualizar_data():
    miConexion = sqlite3.connect('universidad.db')
    miCursor = miConexion.cursor()

    try:
        datos = nombre.get(), apellido.get(), direccion.get(), fecha.get(), telefono.get(), matricula.get(), carrera.get()
        miCursor.execute("UPDATE estudiante SET nombre=?, apellido=?, direccion=?, fecha_nacimiento=?, telefono=?, matricula=?, carrera=? WHERE matricula=" + matricula.get(), datos)
        miConexion.commit()
        LimpiarCampoEstudiante()
        mostrar_datos()

    except:
        messagebox.showwarning("ADVERTENCIA:", "Ocurrio un error al actualizar el registro")
        LimpiarCampoEstudiante()
        pass



def Eliminar():
    miConexion = sqlite3.connect('universidad.db')
    miCursor = miConexion.cursor()

    try:
        if messagebox.askyesno(message="Desea eliminar el registro?", title="ADVERTENCIA"):
            miCursor.execute("DELETE FROM estudiante WHERE matricula=" + matricula.get())
            miConexion.commit()
            LimpiarCampoEstudiante()
            mostrar_datos()
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrio un error al tratar de eliminar el registro")
        LimpiarCampoEstudiante()
        pass

def LimpiarCampoEstudiante():
    nombre.set("")
    apellido.set("")
    direccion.set("")
    fecha.set("")
    telefono.set("")
    matricula.set("")
    carrera.set("")








# ############################ Funcion para la Ventana de los profesores ##################################

def V_profesor():
    # Variables de la Ventana profesor
    global nombrep
    global apellidop
    global direccionp
    global fechap
    global telefonop
    global seccionp
    global materiap
    nombrep = StringVar()
    apellidop = StringVar()
    direccionp = StringVar()
    fechap = StringVar()
    telefonop = StringVar()
    seccionp = StringVar()
    materiap = StringVar()

    global pantallaProfesor

    pantallaProfesor = Toplevel(pantalla)
    pantallaProfesor.geometry("800x800+300+100")
    pantallaProfesor.title("Universidad UNPHU")
    pantallaProfesor.iconbitmap("inicio.ico")
    # pantallaEstudiante.config(background="black")
    pantallaProfesor.state('zoomed')
    pantallaProfesor.resizable(False, False)

    image = PhotoImage(file="logo.gif")
    image = image.subsample(1, 1)
    label = Label(pantallaProfesor, image=image)
    label.place(x=0, y=120)

    Titulo1 = Label(pantallaProfesor, text="", font=("Cambria", 15), bg="#24b43c", fg="white", width="500",
                    height="3")
    Titulo1.place(x=0, y=650)
    Label(pantallaProfesor, text="Registro Profesor", bg="#24b43c", font=("Cambria", 25),
          fg="white", width="350", height="3").pack()

    # #####################Creando las etiquetas y las entrada de los datos#######################

    Label(pantallaProfesor, text="Nombre:", font=("Cambria", 12),
          fg="Black", width="8", height="2").place(x=300, y=120)
    nombrep1 = Entry(pantallaProfesor, textvariable=nombrep, width=25)
    nombrep1.place(x=400, y=135)

    Label(pantallaProfesor, text="Apellido:", font=("Cambria", 12),
          fg="Black", width="8", height="2").place(x=550, y=120)
    apellidop1 = Entry(pantallaProfesor, textvariable=apellidop, width=25)
    apellidop1.place(x=650, y=135)

    Label(pantallaProfesor, text="Direccion:", font=("Cambria", 12),
          fg="Black", width="8", height="2").place(x=810, y=120)
    direccionp1 = Entry(pantallaProfesor, textvariable=direccionp, width=30)
    direccionp1.place(x=910, y=135)

    Label(pantallaProfesor, text="Fecha de Nacimiento:", font=("Cambria", 12),
          fg="Black", width="18", height="2").place(x=297, y=180)
    fechap1 = Entry(pantallaProfesor, textvariable=fechap, width=40)
    fechap1.place(x=470, y=190)

    Label(pantallaProfesor, text="Telefono:", font=("Cambria", 12),
          fg="Black", width="20", height="2").place(x=650, y=180)
    telefonop1 = Entry(pantallaProfesor, textvariable=telefonop, width=30)
    telefonop1.place(x=805, y=190)

    Label(pantallaProfesor, text="Seccion:", font=("Cambria", 12),
          fg="Black", width="8", height="2").place(x=305, y=230)
    seccionp1 = Entry(pantallaProfesor, textvariable=seccionp, width=30)
    seccionp1.place(x=415, y=240)

    Label(pantallaProfesor, text="Materia:", font=("Cambria", 12),
          fg="Black", width="8", height="2").place(x=570, y=230)
    materiap1 = Entry(pantallaProfesor, textvariable=materiap, width=40)
    materiap1.place(x=670, y=240)

    # ################################ Tabla ##########################################
    global tree2
    tree2 = ttk.Treeview(pantallaProfesor, height=10, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6'))
    tree2.place(x=10, y=320)
    tree2.column('#0', width=100)
    tree2.heading('#0', text="Nombre", anchor=CENTER)
    tree2.column('#1', width=100)
    tree2.heading('#1', text="Apellido", anchor=CENTER)
    tree2.heading('#2', text="Direccion", anchor=CENTER)
    tree2.heading('#3', text="Fecha Nacimiento", anchor=CENTER)
    tree2.column('#4', width=150, minwidth=100)
    tree2.heading('#4', text="Telefono", anchor=CENTER)
    tree2.column('#5', width=150, minwidth=100)
    tree2.heading('#5', text="Seccion", anchor=CENTER)
    tree2.column('#6', width=200, minwidth=100)
    tree2.heading('#6', text="Materia", anchor=CENTER)

    def seleccionar1(event):
        item = tree2.identify('item', event.x, event.y)
        nombrep.set(tree2.item(item, "text"))
        #nombrep.set(tree2.item(item, "values")[0])
        apellidop.set(tree2.item(item, "values")[0])
        direccionp.set(tree2.item(item, "values")[1])
        fechap.set(tree2.item(item, "values")[2])
        telefonop.set(tree2.item(item, "values")[3])
        seccionp.set(tree2.item(item, "values")[4])
        materiap.set(tree2.item(item, "values")[5])

    tree2.bind("<Double-1>", seleccionar1)

    # ######################## Creando Los Botones ####################################
    agregarp = Button(pantallaProfesor, text="Agregar Registro", width="25", command=ingresar_datosProfesores)
    agregarp.place(x=305, y=290)

    actualizarp = Button(pantallaProfesor, text="Actualizar Registro", width="25", command=actualizar_dataProfesor)
    actualizarp.place(x=530, y=290)

    listarp = Button(pantallaProfesor, text="Listar Registro", width="25", command=mostrar_datosProfesor)
    listarp.place(x=760, y=290)

    eliminarp = Button(pantallaProfesor, text="Eliminar Registro", bg="red", width="25", command=EliminarProfesor)
    eliminarp.place(x=990, y=290)

    mostrar_datosProfesor()
    pantallaProfesor.mainloop()



# ########################## Metodos para el CRUD de los profesores ##############################

def ingresar_datosProfesores():

    miConexion = sqlite3.connect('universidad.db')
    miCursor = miConexion.cursor()

    try:
        datos = nombrep.get(), apellidop.get(), direccionp.get(), fechap.get(), telefonop.get(), seccionp.get(), materiap.get()
        miCursor.execute("INSERT INTO profesor VALUES(?,?,?,?,?,?,?)", datos)
        miConexion.commit()
        miConexion.close()
        #messagebox.showinfo("Exitoso", message="Registro Exitoso")
        mostrar_datosProfesor()
        LimpiarCampoProfesor()

    except Exception as e:
        messagebox.showwarning("ADVERTENCIA:",
                               "Ocurrio un error al crear el registro, verifique la conexion con la base de datos")
        LimpiarCampoProfesor()
        print(e)



def mostrar_datosProfesor():
    miConexion = sqlite3.connect('universidad.db')
    miCursor = miConexion.cursor()
    registros = tree2.get_children()
    for elemento in registros:
        tree2.delete(elemento)

    try:
        miCursor.execute("SELECT * FROM profesor")
        miConexion.commit()
        for row in miCursor:
            tree2.insert('', 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6]))

    except:
        pass

def actualizar_dataProfesor():
    miConexion = sqlite3.connect('universidad.db')
    miCursor = miConexion.cursor()

    try:
        datos = nombrep.get(), apellidop.get(), direccionp.get(), fechap.get(), telefonop.get(), seccionp.get(), materiap.get()
        miCursor.execute("UPDATE profesor SET nombre=?, apellido=?, direccion=?, fecha_nacimiento=?, telefono=?, seccion=?, materia=? WHERE materia=" + materiap.get(), datos)
        miConexion.commit()
        LimpiarCampoProfesor()
        mostrar_datosProfesor()

    except Exception:
        messagebox.showwarning("ADVERTENCIA:", "Ocurrio un error al actualizar el registro")
        LimpiarCampoProfesor()
        print(EXCEPTION)


def EliminarProfesor():
    miConexion = sqlite3.connect('universidad.db')
    miCursor = miConexion.cursor()

    try:
        if messagebox.askyesno(message="Desea eliminar el registro?", title="ADVERTENCIA"):
            miCursor.execute("DELETE FROM profesor WHERE seccion=" + seccionp.get())
            miConexion.commit()
            LimpiarCampoProfesor()
            mostrar_datosProfesor()
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrio un error al tratar de eliminar el registro")
        LimpiarCampoProfesor()
        pass


def LimpiarCampoProfesor():
    nombrep.set("")
    apellidop.set("")
    direccionp.set("")
    fechap.set("")
    telefonop.set("")
    seccionp.set("")
    materiap.set("")






# ############################ Ventana de la materia ################################### #

def V_materia():
    # Variables principales de la ventana de materia
    global nombrem
    global horariom
    global profesorm
    global estudiantem
    nombrem = StringVar()
    horariom = StringVar()
    profesorm = StringVar()
    estudiantem = StringVar()

    global pantallaMateria

    pantallaMateria = Toplevel(pantalla)
    pantallaMateria.geometry("800x800+300+100")
    pantallaMateria.title("Universidad UNPHU")
    pantallaMateria.iconbitmap("inicio.ico")
    # pantallaEstudiante.config(background="black")
    pantallaMateria.state('zoomed')
    pantallaMateria.resizable(False, False)

    image = PhotoImage(file="logo.gif")
    image = image.subsample(1, 1)
    label = Label(pantallaMateria, image=image)
    label.place(x=0, y=120)

    Titulo1 = Label(pantallaMateria, text="", font=("Cambria", 15), bg="#24b43c", fg="white", width="500",
                    height="3")
    Titulo1.place(x=0, y=650)
    Label(pantallaMateria, text="Registro Materia", bg="#24b43c", font=("Cambria", 25),
          fg="white", width="350", height="3").pack()


    # ##################### Creando las etiquetas y las entrada de los datos #######################

    Label(pantallaMateria, text="Nombre:", font=("Cambria", 12),
          fg="Black", width="8", height="2").place(x=300, y=120)
    nombrem1 = Entry(pantallaMateria, textvariable=nombrem, width=25)
    nombrem1.place(x=400, y=135)

    Label(pantallaMateria, text="Horario:", font=("Cambria", 12),
          fg="Black", width="8", height="2").place(x=550, y=120)
    horariom1 = Entry(pantallaMateria, textvariable=horariom, width=25)
    horariom1.place(x=650, y=135)


    Label(pantallaMateria, text="Profesor:", font=("Cambria", 12),
          fg="Black", width="18", height="2").place(x=297, y=180)
    profesorm1 = Entry(pantallaMateria, textvariable=profesorm, width=40)
    profesorm1.place(x=470, y=190)

    Label(pantallaMateria, text="Estudiante:", font=("Cambria", 12),
          fg="Black", width="20", height="2").place(x=650, y=180)
    estudaintem1 = Entry(pantallaMateria, textvariable=estudiantem, width=30)
    estudaintem1.place(x=805, y=190)



    # ################################ Tabla ##########################################
    global tree3
    tree3 = ttk.Treeview(pantallaMateria, height=12, columns=('#0', '#1', '#2', '#3'))
    tree3.place(x=190, y=320)
    #tree3.column('#0', width=100)
    tree3.heading('#0', text="Nombre", anchor=CENTER)
    tree3.column('#1', width=400)
    tree3.heading('#1', text="Horario", anchor=CENTER)
    tree3.heading('#2', text="Profesor", anchor=CENTER)
    tree3.heading('#3', text="Estudiante", anchor=CENTER)

    def seleccionar2(event):
        item = tree3.identify('item', event.x, event.y)
        nombrem.set(tree3.item(item, "text"))
        #nombrem.set(tree3.item(item, "values")[0])
        horariom.set(tree3.item(item, "values")[0])
        profesorm.set(tree3.item(item, "values")[1])
        estudiantem.set(tree3.item(item, "values")[2])


    tree3.bind("<Double-1>", seleccionar2)

    # ######################## Creando Los Botones ####################################
    agregarp = Button(pantallaMateria, text="Agregar Registro", width="25", command = ingresar_datosMateria)
    agregarp.place(x=305, y=290)

    actualizarp = Button(pantallaMateria, text="Actualizar Registro", width="25", command=actualizar_dataMateria)
    actualizarp.place(x=530, y=290)

    listarp = Button(pantallaMateria, text="Listar Registro", width="25", command=mostrar_datosMateria)
    listarp.place(x=760, y=290)

    eliminarp = Button(pantallaMateria, text="Eliminar Registro", bg="red", width="25")
    eliminarp.place(x=990, y=290)

    mostrar_datosMateria()

    pantallaMateria.mainloop()



# ########################## Metodos para el CRUD de la ventana Materia ######################### #

def ingresar_datosMateria():

    miConexion = sqlite3.connect('universidad.db')
    miCursor = miConexion.cursor()

    try:
        datos = nombrem.get(), horariom.get(), profesorm.get(), estudiantem.get()
        miCursor.execute("INSERT INTO materia VALUES(?,?,?,?)", datos)
        miConexion.commit()
        messagebox.showinfo("Exitoso", message="Registro Exitoso")
        LimpiarCampoMateria()
        mostrar_datosMateria()

    except Exception as e:
        messagebox.showwarning("ADVERTENCIA:",
                               "Ocurrio un error al crear el registro, verifique la conexion con la base de datos")
        LimpiarCampoMateria()
        print(e)


def mostrar_datosMateria():
    miConexion = sqlite3.connect('universidad.db')
    miCursor = miConexion.cursor()
    registros = tree3.get_children()
    for elemento in registros:
        tree3.delete(elemento)

    try:
        miCursor.execute("SELECT * FROM materia")
        miConexion.commit()
        for row in miCursor:
            tree3.insert('', 0, text=row[0], values=(row[1], row[2], row[3]))

    except:
        pass


def actualizar_dataMateria():
    miConexion = sqlite3.connect('universidad.db')
    miCursor = miConexion.cursor()

    try:
        datos = nombrem.get(), horariom.get(), profesorm.get(), estudiantem.get()
        miCursor.execute("UPDATE materia SET nombre=?, horario=?, profesor=?, estudiante=? WHERE estudiante=" + estudiantem.get(), datos)
        miConexion.commit()
        LimpiarCampoMateria()
        mostrar_datosMateria()

    except:
        messagebox.showwarning("ADVERTENCIA:", "Ocurrio un error al actualizar el registro")
        LimpiarCampoMateria()


def EliminarMateria():
    miConexion = sqlite3.connect('universidad.db')
    miCursor = miConexion.cursor()

    try:
        if messagebox.askyesno(message="Desea eliminar el registro?", title="ADVERTENCIA"):
            miCursor.execute("DELETE FROM materia WHERE nombre" + nombrem.get())
            miConexion.commit()
            LimpiarCampoMateria()
            mostrar_datosMateria()
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrio un error al tratar de eliminar el registro")
        LimpiarCampoMateria()


def LimpiarCampoMateria():
    nombrem.set("")
    horariom.set("")
    profesorm.set("")
    estudiantem.set("")


Menu_principal()
