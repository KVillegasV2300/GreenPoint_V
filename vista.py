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

    #encabezado
    titulo_label = Label(root, text="GreenPoint", font=("Arial", 24, "bold"), bg="#ABEEB5", fg="#2E8B57")
    titulo_label.pack(fill="x")

    """----------------------------------pagina principal-----------------------------"""
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
    
    """---------------------------------------------crear centros------------------------------------------"""
    def pagina_crear():
        frame_principal = Frame(root)
        def boton_casa():
            #otro encabezado (posibles botones futuros)
            botones_frame = Frame(frame_principal, bg="#636363")
            botones_frame.pack(fill="x")
            btn_agregar_centro = Button(botones_frame, text="Pagina principal", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"), command= lambda: [interfaz_funciones["eliminar_frame"](frame_principal),pagina_principal()])
            btn_agregar_centro.grid(row=0, column=0)
        
        def busqueda_key(key):
            resultados = busqueda_centros["busqueda_key"](str(key))
            for centro in resultados:
                agregar_centro(centro)
        
        def agregar_centro(centro):
            acciones_frame = Frame(scroll.scrollable_frame, bg="#D9D9D9")
            busqueda_centros["mostrar_centro"](centro,  scroll.scrollable_frame)
            btn_editar = Button(acciones_frame, text="editar", command= lambda : [interfaz_funciones["eliminar_frame"](frame_principal), pagina_editar(centro)])
            btn_eliminar = Button(acciones_frame, text="eliminar")

            acciones_frame.pack(fill=X)
            btn_editar.pack(side=RIGHT)
            btn_eliminar.pack(side=RIGHT)

        boton_casa()
        #texto
        subtitulo_label = Label(frame_principal, text="Tus centros", font=("Arial", 14), bg="#E6FFE6")
        subtitulo_label.pack(pady=10)
        
        #boton de agregar
        btn_agregar = Button(frame_principal, text="Agregar centro", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"))
        btn_agregar.pack()

        #scroll
        scroll = interfaz_funciones["frame_scroll"](frame_principal) #frame principal de busqueda y SCROLLBAR
        scroll.place(x=40,y=170) #place significa que NOSOTROS necesitaremos acomodar manualmente el widget, con coordenadas x e y

        busqueda_key("1234")

        frame_principal.pack(fill=BOTH, expand=True)
    
    """------------------------------------pagina editar-----------------------------------"""
    def pagina_editar(centro):
        frame_principal = Frame(root)

        def boton_casa():
            #otro encabezado (posibles botones futuros)
            botones_frame = Frame(frame_principal, bg="#636363")
            botones_frame.pack(fill="x")
            btn_agregar_centro = Button(botones_frame, text="Tus centros", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"), command= lambda: [interfaz_funciones["eliminar_frame"](frame_principal),pagina_crear()])
            btn_agregar_centro.grid(row=0, column=0)
        
        boton_casa()
        
        Label(frame_principal, text="Editar Centro", font=("Arial", 14), bg="#E6FFE6").pack(pady=10)
        Label(frame_principal, text=f"{centro["nombre"]}", font=("Arial", 12), bg="#E6FFE6").pack(pady=5)

        #nombre
        Label(frame_principal, text="Nombre").pack(pady=5)
        editar_nombre = Entry(frame_principal)
        editar_nombre.insert(0,centro["nombre"])
        editar_nombre.pack()

        #direccion
        Label(frame_principal, text="Direccion").pack(pady=5)
        editar_direccion = Entry(frame_principal)
        editar_direccion.insert(0, centro["direccion"])
        editar_direccion.pack()

        #materiales y precios
        Label(frame_principal, text="Materiales").pack(pady=5)
        

        #horarios
        Label(frame_principal, text="Horarios").pack(pady=5)
        editar_horario = Entry(frame_principal)
        editar_horario.insert(0, centro["horarios"])
        editar_horario.pack()
        
        #link
        Label(frame_principal, text="Link").pack(pady=5)
        editar_direccion = Entry(frame_principal)
        editar_direccion.insert(0, centro["link"])
        editar_direccion.pack()

        #telefono
        Label(frame_principal, text="Telefono").pack(pady=5)
        editar_direccion = Entry(frame_principal)
        editar_direccion.insert(0, centro["telefono"])
        editar_direccion.pack()

        btn_enviar = Button(frame_principal, text="Guardar")
        btn_cancelar = Button(frame_principal, text="Cancelar")
        btn_enviar.pack(pady=5)
        btn_cancelar.pack(pady=5)

        frame_principal.pack(fill=BOTH, expand=True)



    pagina_principal()
    root.mainloop()

