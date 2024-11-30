#librerias
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox


def interfaz_principal(busqueda_centros, interfaz_funciones):
    
    global root
    
    #configuracion de la aplicacion
    root = Tk() #establecemos la rama "principal"
    root.geometry("1100x700") #Establecemos el tamaño de la ventana
    root.configure(bg="#E6FFE6")
    root.resizable(False,False) #La venta no sera reescalable

    #encabezado
    titulo_label = Label(root, text="GreenPoint", font=("Arial", 24, "bold"), bg="#ABEEB5", fg="#2E8B57")
    titulo_label.pack(fill="x")

    """pagina principal"""
    def pagina_principal():
        frame_principal = Frame(root, width=1100, height=700)
        #botones de inciar sesion
        def botones_inicio():
            #agregamos los botones de iniciar sesion y registrarse
            btn_iniciar_sesion = Button(botones_frame, text="inciar sesion", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"))
            btn_registrar_usuario = Button(botones_frame, text="registrar usuario", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"))
            
            btn_iniciar_sesion.grid(row=0, column=0)
            btn_registrar_usuario.grid(row=0, column=1)
        
        def botones_centro():
            btn_agregar_centro = Button(botones_frame, text="Agregar centro", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"), command= lambda: [interfaz_funciones["eliminar_frame"](frame_principal),pagina_crear()])
            btn_agregar_centro.grid(row=0, column=0)

        #otro encabezado (posibles botones futuros)
        botones_frame = Frame(frame_principal, bg="#636363")
        botones_centro()
        botones_frame.pack(fill="x")

        #texto
        subtitulo_label = Label(frame_principal, text="Buscar Centros de Reciclaje por Material", font=("Arial", 14), bg="#E6FFE6")
        subtitulo_label.pack(pady=10)

        #frames
        scroll = interfaz_funciones["frame_scroll"](frame_principal) #frame principal de busqueda y SCROLLBAR
        scroll.place(x=40,y=170) #place significa que NOSOTROS necesitaremos acomodar manualmente el widget, con coordenadas x e y

        busqueda_centros["barra_busqueda"](frame_principal, scroll)

        frame_principal.pack(fill=BOTH, expand=True)
    
    """crea centros"""
    def pagina_crear():
        frame_crear = Frame(root)
        def boton_casa():
            btn_agregar_centro = Button(botones_frame, text="Pagina principal", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"), command= lambda: [interfaz_funciones["eliminar_frame"](frame_crear),pagina_principal()])
            btn_agregar_centro.grid(row=0, column=0)
        
        def busqueda_key():
            resultados = busqueda_centros["busqueda_key"]("1908")
            for centro in resultados:
                acciones_frame = Frame(scroll.scrollable_frame, bg="#D9D9D9")
                busqueda_centros["mostrar_centro"](centro,  scroll.scrollable_frame)
                btn_editar = Button(acciones_frame, text="editar")
                btn_eliminar = Button(acciones_frame, text="eliminar")

                acciones_frame.pack(fill=X)
                btn_editar.pack(side=RIGHT)
                btn_eliminar.pack(side=RIGHT)

        #otro encabezado (posibles botones futuros)
        botones_frame = Frame(frame_crear, bg="#636363")
        botones_frame.pack(fill="x")
        
        boton_casa()
        #texto
        subtitulo_label = Label(frame_crear, text="Tus centros", font=("Arial", 14), bg="#E6FFE6")
        subtitulo_label.pack(pady=10)
        
        #boton de agregar
        btn_agregar = Button(frame_crear, text="Agregar centro", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"))
        btn_agregar.pack()

        #scroll
        scroll = interfaz_funciones["frame_scroll"](frame_crear) #frame principal de busqueda y SCROLLBAR
        scroll.place(x=40,y=170) #place significa que NOSOTROS necesitaremos acomodar manualmente el widget, con coordenadas x e y

        busqueda_key()

        frame_crear.pack(fill=BOTH, expand=True)

        




       

    pagina_principal()
    root.mainloop()

