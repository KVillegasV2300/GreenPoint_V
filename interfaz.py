import tkinter as tk
from tkinter import *
from tkinter import ttk
import webbrowser

#modulos
import Centros as m

class Frame_scroll(Frame):
    def __init__(self, container, h, w, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        #self.canvas = tk.Canvas(self, height=500, width=1000)
        self.canvas = tk.Canvas(self, height=h, width=w)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas, padx=50, pady=15)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side = RIGHT, fill = Y ) #self 
    
    def clear(self): #este es mio
        limpiar_frame(self.scrollable_frame)

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

    telefono = Frame(centro, bg="#D9D9D9")
    Label(telefono, text=f"Telefono: {centro_i["telefono"]}", font=("Arial", 12, "bold"), bg="#D9D9D9", fg="black").pack(side="left")
    telefono.pack(fill="x")

    # Agregar un frame de informacion
    informacion = Frame(centro, bg="#FFFFFF", width=400, height=250)
    informacion.pack_propagate(False) #evitar el resize
    informacion.pack(side=LEFT, padx=25, pady=25)
    #scroll

    # Agregar los materiales
    t_materiales = Label(informacion, text="Materiales aceptados (Por kilo)", font=("Arial", 12, "bold"), bg="#E6FFE6", fg="#2E8B57")
    t_materiales.pack()

    #scroll
    scroll = Frame_scroll(informacion, 300, 300)
    scroll.pack()

    #aqui mostraremos el material con el precio, todo en un frame (seran dependiendo de los que esten en el arreglo y se ocupara validar cuando hagamos lo de "agregar") 
    for m, p in zip(centro_i["materiales"],centro_i["precios"]):
        f_materiales = Frame(scroll.scrollable_frame) #aqui el frame donde ira UN SOLO material
    
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

    

def Barra_Busqueda(root, indices_por_defecto=None):
    # Crear los frames
    busqueda = Frame(root)
    cuadro = Frame(busqueda)
    barra = Frame(busqueda)

    # Crear el scrollbar
    scrollbar = Scrollbar(cuadro)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Crear los botones y la lista
    lista = Listbox(cuadro, selectmode="multiple", yscrollcommand=scrollbar.set)
    boton_mostrar = Button(barra, text=">", command=lambda: Barra_mostrar(cuadro), width=20)
    buscar_btn = Button(barra, text="Buscar", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"))

    # Llenar la lista con materiales reciclables
    for mt in range(len(m.materiales_reciclables)):
        lista.insert(END, m.materiales_reciclables[mt])

    # Seleccionar elementos por defecto si se proporcionan
    if indices_por_defecto:
        for material in indices_por_defecto:
             # Obtener el índice del nombre en la lista
            idx = m.materiales_reciclables.index(material)
            lista.select_set(idx)

    # Empaquetar los componentes
    barra.pack()
    lista.pack()
    boton_mostrar.grid(row=0, column=1)
    buscar_btn.grid(row=0, column=0)
    scrollbar.config(command = lista.yview)

    #para mostrarlo por encima
    busqueda.lift()
    # Colocar el frame de búsqueda
    #busqueda.place(x=450, y=120)

    # Retornar los componentes principales
    return {
        "busqueda_frame": busqueda,
        "cuadro_frame": cuadro,
        "barra_frame": barra,
        "scrollbar": scrollbar,
        "lista": lista,
        "boton_mostrar": boton_mostrar,
        "buscar_btn": buscar_btn
    }

#ocultar/mostrar elementos
def Barra_mostrar(L):
    #mostrar u ocultar barra de busqueda
    if L.winfo_ismapped(): 
        L.pack_forget()
    else:
        L.pack()

#limpiar frames (por si acaso jsjs)
def elimnar_frame(Frame):
    Frame.destroy()

def limpiar_frame(frame):
   for w in frame.winfo_children():
      w.destroy()