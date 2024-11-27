#librerias
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox


#configuracion de la aplicacion
root = Tk() #establecemos la rama "principal"
root.geometry("1100x700") #Establecemos el tamaño de la ventana
root.configure(bg="#E6FFE6")
root.resizable(False,False) #La venta no sera reescalable

def interfaz_principal(busqueda_centros, interfaz_funciones):
    #botones de inciar sesion
    def Agregar_botones_inicio():
        #agregamos los botones de iniciar sesion y registrarse
        btn_iniciar_sesion = Button(botones_frame, text="inciar sesion", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"))
        btn_registrar_usuario = Button(botones_frame, text="registrar usuario", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"))
        
        btn_iniciar_sesion.grid(row=0, column=0)
        btn_registrar_usuario.grid(row=0, column=1)


    #encabezado
    titulo_label = Label(root, text="GreenPoint", font=("Arial", 24, "bold"), bg="#ABEEB5", fg="#2E8B57")
    titulo_label.pack(fill="x")

    #otro encabezado (posibles botones futuros)
    botones_frame = Frame(root, bg="#636363")

    Agregar_botones_inicio()
    botones_frame.pack(fill="x")

    #texto
    subtitulo_label = Label(root, text="Buscar Centros de Reciclaje por Material", font=("Arial", 14), bg="#E6FFE6")
    subtitulo_label.pack(pady=10)

    #frames
    scroll = interfaz_funciones["frame_scroll"](root) #frame principal de busqueda y SCROLLBAR
    scroll.place(x=40,y=170) #place significa que NOSOTROS necesitaremos acomodar manualmente el widget, con coordenadas x e y

    busqueda_centros["barra_busqueda"](root, scroll)

    root.mainloop()