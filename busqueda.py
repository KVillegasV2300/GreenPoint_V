#librerias
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import webbrowser
import os

#modulos
import Centros as m

#deplegar barra de busqueda
def Barra_Busqueda(root, scroll):
    #frames
    busqueda=Frame(root) 
    cuadro=Frame(busqueda)
    barra=Frame(busqueda)

    #scrollbar :p (Mi mayor enemigo)
    scrollbar = Scrollbar(cuadro) 
    #scrollbar.pack(side = RIGHT, fill = Y)  

    #botones principales
    lista = Listbox(cuadro, selectmode="multiple", yscrollcommand=scrollbar.set) #list box de materiales
    boton_mostrar = Button(barra, text="                                    >", command=lambda: Barra_mostrar(cuadro), width=20) #boton para deplegar la lista de opciones
    buscar_btn = Button(barra, text="Buscar", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"), command=lambda: [Barra_mostrar(cuadro),busqueda_materiales(lista)]) #un boton multi funcion (varias opcines) para actualizar la lista

    #insertar todos los materiales establecidos en "Centro.py"
    for mt in range(len(m.materiales_reciclables)):
        lista.insert(END, m.materiales_reciclables[mt])

    #empaquetamos
    barra.pack()
    lista.pack()
    busqueda.place(x=450,y=120) #aca estamos usando place, a si que cualquier mkodificacion ocupamos mover sus coordenadas x e y :b
    boton_mostrar.grid(row=0, column=1)
    buscar_btn.grid(row=0, column=0)
    scrollbar.config(command = lista.yview)

    #para mostrarlo por encima
    busqueda.lift()

    #busqueda por materiales
    def busqueda_materiales(lista):
        #optenemos la lista de materiales
        Indices = lista.curselection()
        Opciones = []
        scroll.clear() #limpiamos para evitar repetciones
        
        #optenemos las opcines de la lista
        for ind in Indices:
            Opciones.append(lista.get(ind))
        
        #filtramos los centros
        resultados = [] #aqui pondremos los materiales que cumplan con las condiciones
        for centro in m.centros: #primera condicion: accederemos a todos los centros
            for material in Opciones: #segunda condicion: accederemos a las opciones
                if material in centro["materiales"]: #tercera condicion: aqui verificamos si el "material" esta en el "centro" iterado
                    if not centro in resultados: #esto es para evitar que se repitan (soy paranoico si?)
                        resultados.append(centro) #pues aqui nomas append jajaj salu2
        #mostramos los centros con la funcion de mostrar
        for centro in resultados:
                mostrar_centro(centro, scroll.scrollable_frame)
                #print(centro)
                #mostrar_centro(centro["nombre"], centro["direccion"], centro["materiales"], centro["precios"], centro["horarios"], centro["link"],scroll.scrollable_frame)

    #ocultar/mostrar elementos
    def Barra_mostrar(L):
        #mostrar u ocultar barra de busqueda
        if L.winfo_ismapped(): 
            L.pack_forget()
        else:
            L.pack()

#funcion para mostrar los centros, es la interfaz chavos
def mostrar_centro(centro_i, root):
    # Crear un Frame para contener el centro
    centro = Frame(root, padx=15, pady=15, bg="#D9D9D9")
    centro.pack()

    # Agregar el nombre del centro
    nombreCentro = Label(centro, text = centro_i["nombre"], font=("Arial", 24, "bold"), fg="black", bg="#FFFFFF")
    nombreCentro.pack()

    #agregar horarios
    t_horario = Label(centro, text="Horarios:", font=("Arial", 12, "bold"), bg="#D9D9D9", fg="black")
    m_horario = Label(centro, text= centro_i["horarios"], font=("Arial", 12, "bold"), bg="#D9D9D9", fg="black")
    t_horario.pack()
    m_horario.pack()

    # Agregar un frame de informacion
    informacion = Frame(centro, bg="#FFFFFF", width=400, height=250)
    informacion.pack_propagate(False) #evitar el resize
    informacion.pack(side=LEFT, padx=25, pady=25)

    # Agregar los materiales
    t_materiales = Label(informacion, text="Materiales aceptados", font=("Arial", 12, "bold"), bg="#E6FFE6", fg="#2E8B57")
    t_materiales.pack()
    #aqui mostraremos el material con el precio, todo en un frame (seran dependiendo de los que esten en el arreglo y se ocupara validar cuando hagamos lo de "agregar") 
    for m, p in zip(centro_i["materiales"],centro_i["precios"]):
        f_materiales = Frame(informacion) #aqui el frame donde ira UN SOLO material
    
        #mostrar materiales
        m_materiales = Label(f_materiales, text=f"{m}", font=("Arial", 8, "bold"))
        m_materiales.pack(side=LEFT, padx=10, pady=5)
        
        #mostrar precios
        m_precios = Label(f_materiales, text=f"..........{p}$", font=("Arial", 8, "bold"))
        m_precios.pack(side=RIGHT, padx=10, pady=5)
        f_materiales.pack(fill=X)

    # Agregar el frame de direccion y frame
    imagenes = Frame(centro, bg="#FFFFFF", width=400, height=250)
    imagenes.pack_propagate(False) #evitar el resize
    imagenes.pack(side=RIGHT, padx=15, pady=15)

    #mostrar informacion
    t_direccion = Label(imagenes, text="Direccion:", font=("Arial", 12, "bold"), bg="#E6FFE6", fg="#2E8B57")

    #insertar widget de texto
    m_direccion = Text(imagenes, height=10, width=30)
    m_direccion.insert(END, centro_i["direccion"])
    m_direccion.config(state=tk.DISABLED) #texto no editable

    #inserta boton de ver en mapa
    b_mapa = Button(imagenes, text="Ver mapa", command=lambda:webbrowser.open(centro_i["link"]))

    #empaquetamos
    t_direccion.pack()
    m_direccion.pack(pady=10)
    b_mapa.pack(pady=5)

def busqueda_key(key):
    #filtramos los centros
    resultados = [] #aqui pondremos los materiales que cumplan con las condiciones
    for centro in m.centros: #primera condicion: accederemos a todos los centros
        if key in centro["clave"]:
            resultados.append(centro) #pues aqui nomas append jajaj salu2
    
    return resultados
