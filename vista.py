#librerias
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, simpledialog
import copy

#configuracion de la aplicacion
root = Tk() #establecemos la rama "principal"
root.geometry("1100x700") #Establecemos el tamaño de la ventana
root.configure(bg="#E6FFE6")
root.resizable(False,False) #La venta no sera reescalable

usuario = {}
estado = "no sesion"

#estilos reutilizables
# Estilos reutilizables
Boton_estilo = {"bg": "#2E8B57", "fg": "white", "font": ("Arial", 12, "bold"), "relief": "flat"}
Boton_rojo = {"bg": "#C51D34", "fg": "white", "font": ("Arial", 12, "bold"), "relief": "flat"}
Boton_azul = {"bg": "#92C5FC", "fg": "white", "font": ("Arial", 12, "bold"), "relief": "flat"}

Entrada_estilo = {"font": ("Arial", 12), "bg": "#FFFFFF", "fg": "#2E8B57", "highlightthickness": 2}
Label1_estilo = { "font" : ("Arial", 14, "bold"), "bg" : "#E6FFE6"}
Label2_estilo = { "font" : ("Arial", 12), "bg" : "#E6FFE6"}
Label3_estilo = { "font" : ("Arial", 12, "bold"), "bg" : "#E6FFE6"}

def interfaz_principal(busqueda_centros, interfaz_funciones, administrar_centros, administrar_cuentas):

    # Encabezado
    titulo_label = Label(root, text="GreenPoint", font=("Arial", 28, "bold"), bg="#A3D9A5", fg="#2E8B57")
    titulo_label.pack(fill="x")

    """----------------------------------pagina principal-----------------------------"""
    def pagina_principal():
        frame_principal = Frame(root, width=1100, height=700)
        #botones de inciar sesion
        def botones_inicio():
            #agregamos los botones de iniciar sesion y registrarse
            btn_iniciar_sesion = Button(botones_frame, text="inciar sesion", **Boton_estilo, command= lambda: [interfaz_funciones["eliminar_frame"](frame_principal),iniciar_sesion()])
            btn_registrar_usuario = Button(botones_frame, text="registrar usuario", **Boton_estilo, command= lambda: [interfaz_funciones["eliminar_frame"](frame_principal),pagina_registrar()])
            
            btn_iniciar_sesion.grid(row=0, column=0)
            btn_registrar_usuario.grid(row=0, column=1)
        
        def botones_centro():
            btn_agregar_centro = Button(botones_frame, text="Tus centros", **Boton_estilo, command= lambda: [interfaz_funciones["eliminar_frame"](frame_principal),pagina_crear()])
            btn_agregar_centro.grid(row=0, column=0)
            
            btn_editar_cuenta = Button(botones_frame, text="Tu cuenta", **Boton_estilo, command= lambda: [interfaz_funciones["eliminar_frame"](frame_principal),pagina_cuenta()])
            btn_editar_cuenta.grid(row=0, column=1)
        
        def botones_usuario():
            btn_editar_cuenta = Button(botones_frame, text="Tu cuenta", **Boton_estilo, command= lambda: [interfaz_funciones["eliminar_frame"](frame_principal),pagina_cuenta()])
            btn_editar_cuenta.grid(row=0, column=0)

        def manejar_busqueda(lista):
            #limpiamos el scroll
            scroll.clear()
            #mostramos
            resultados = busqueda_centros["busqueda_materiales"](lista)
            #mostramos los resultados
            for centro in resultados:
                interfaz_funciones["mostrar_centro"](centro, scroll.scrollable_frame)

        #otro encabezado (posibles botones futuros)
        botones_frame = Frame(frame_principal, bg="#636363")
        botones_frame.pack(fill="x")

        #logica de los botones
        if estado == "no sesion":
            botones_inicio()
        elif estado == "usuario":
            botones_usuario()
        elif estado == "administrador":
            botones_centro()

        #texto
        subtitulo_label = Label(frame_principal, text="Buscar Centros de Reciclaje por Material", **Label1_estilo)
        subtitulo_label.pack(pady=10)

        #scroll
        scroll = interfaz_funciones["frame_scroll"](frame_principal, 500, 1000) #frame principal de busqueda y SCROLLBAR
        scroll.place(x=40,y=170) #place significa que NOSOTROS necesitaremos acomodar manualmente el widget, con coordenadas x e y
        
        #creamos la barra
        barra = interfaz_funciones["barra_busqueda"](frame_principal)
        barra["buscar_btn"].config(command=lambda:[manejar_busqueda(barra["lista"]), interfaz_funciones["ocultar_frame"](barra["cuadro_frame"])])
        barra["busqueda_frame"].place(x=450, y=120)

        frame_principal.pack(fill=BOTH, expand=True)
    
    """---------------------------------------------crear centros------------------------------------------"""
    def pagina_crear():
        frame_principal = Frame(root)
        clave = administrar_cuentas["obtener_clave"](usuario)
        print(clave)

        def boton_casa():
            #otro encabezado (posibles botones futuros)
            botones_frame = Frame(frame_principal, bg="#636363")
            botones_frame.pack(fill="x")
            btn_agregar_centro = Button(botones_frame, text="Pagina principal", **Boton_estilo, command= lambda: [interfaz_funciones["eliminar_frame"](frame_principal),pagina_principal()])
            btn_agregar_centro.grid(row=0, column=0)
        
        def busqueda_key(key):
            resultados = busqueda_centros["busqueda_key"](str(key))
            for centro in resultados:
                agregar_centro(centro)
        
        def agregar_centro(centro):
            acciones_frame = Frame(scroll.scrollable_frame, bg="#D9D9D9")
            interfaz_funciones["mostrar_centro"](centro,  scroll.scrollable_frame)
            btn_editar = Button(acciones_frame, text="editar", **Boton_estilo, command= lambda : [interfaz_funciones["eliminar_frame"](frame_principal), pagina_editar(centro, "editar", clave)])
            btn_eliminar = Button(acciones_frame, text="eliminar", **Boton_estilo,command=lambda: eliminar_centro(centro, frame_principal))

            acciones_frame.pack(fill=X)
            btn_editar.pack(side=RIGHT)
            btn_eliminar.pack(side=RIGHT)

        boton_casa()
        #texto
        subtitulo_label = Label(frame_principal, text="Tus centros", **Label1_estilo)
        subtitulo_label.pack(pady=10)
        
        #boton de agregar
        nuevo_centro = administrar_centros["crear_centro"]() 
        btn_agregar = Button(frame_principal, text="Agregar centro", **Boton_estilo,  command= lambda : [interfaz_funciones["eliminar_frame"](frame_principal), pagina_editar(nuevo_centro, "agregar", clave)])
        btn_agregar.pack()

        #scroll
        scroll = interfaz_funciones["frame_scroll"](frame_principal, 500, 1000) #frame principal de busqueda y SCROLLBAR
        scroll.place(x=40,y=170) #place significa que NOSOTROS necesitaremos acomodar manualmente el widget, con coordenadas x e y

        busqueda_key(clave)

        frame_principal.pack(fill=BOTH, expand=True)
    
    """------------------------------------Eliminar centro-----------------------------------"""
    def eliminar_centro(centro, frame_principal):
        global usuario
        pagina_principal = tk.Toplevel(root)
        pagina_principal.title("Eliminar centro")

        def manejar_eliminar():
            contrasena = contrasena_entrada.get()
            validacion = administrar_cuentas["validar_contrasena"](contrasena, usuario)
            
            if validacion:
                administrar_centros["eliminar_centro"](centro)
                messagebox.showinfo("Centro", "El centro fue eliminado exitosamente") 
                pagina_principal.destroy()   
                
                #refrescar pagina
                interfaz_funciones["eliminar_frame"](frame_principal)
                pagina_crear()


        Label(pagina_principal, text=f"¿Deseas eliminar el centro: {centro["nombre"]}?", **Label1_estilo).pack(pady=10)
        Label(pagina_principal, text="Para eliminar el centro, necesita confirmar su contraseña", **Label2_estilo).pack(pady=5)
        contrasena_entrada = Entry(pagina_principal, **Entrada_estilo, show="*")
        contrasena_entrada.pack(pady=10)

        btn_confirmar= Button(pagina_principal, text="enviar", **Boton_rojo, command= manejar_eliminar)
        btn_cancelar = Button(pagina_principal, text="cancelar", **Boton_azul,command= lambda: [pagina_principal.destroy()])

        btn_confirmar.pack()
        btn_cancelar.pack()
    
    """------------------------------------pagina editar/agregar-----------------------------------"""
    def pagina_editar(centro, caso ,clave = None):
        frame_principal = Frame(root)
        materiales = []
        precios = []

        #asignar clave si es nuevo centro
        if clave:
            centro["clave"] = clave

        def editar_materiales(lista):
            precios.clear()
            materiales.clear()

            Opciones = busqueda_centros["obtener_indices"](lista)
            
            materiales_actuales = centro["materiales"].copy() 
            precios_actuales = centro["precios"].copy()

            for i, material in enumerate(materiales_actuales):
                if material in Opciones:
                    nuevo_precio = simpledialog.askstring(f"{material}: precio actual {precios_actuales[i]}$", "Ingresa el nuevo precio o presiona ENTER para mantener el actual:") or precios_actuales[i]
                    materiales.append(material)
                    precios.append(float(nuevo_precio))
                else:
                    print(f"se ha eliminado {material}")
            
            for material in Opciones:
                if material not in materiales_actuales:
                    nuevo_precio = simpledialog.askstring(f"{material}: Nuevo material", f"Ingresa el precio para {material}:")

                    #comprobamos si se selecciono el precio
                    if nuevo_precio:
                        materiales.append(material)
                        precios.append(float(nuevo_precio))
            
            print(precios)
            print(materiales)
        
        def obtener_cambios():
            nuevo_nombre = editar_nombre.get()
            nuevo_direccion = editar_direccion.get()
            nuevo_horario = editar_horario.get()
            nuevo_link = editar_link.get()
            nuevo_telefono = editar_telefono.get()
            
            #validacion

            if len(nuevo_nombre) > 40:
                messagebox.showwarning("Error", "El nombre debe de tener menos de 40 caracteres")
                return
            elif len(nuevo_telefono) > 15:
                messagebox.showwarning("Error", "El numero de telefono debe de tener menos de 15 caracteres")
                return
            else:
                if caso == "agregar": administrar_centros["agregar_centro"](centro) #solo si se esta agregando un nuevo centro
                administrar_centros["editar_centro"](nuevo_nombre, nuevo_direccion, nuevo_telefono, nuevo_horario, materiales, precios, nuevo_link, centro["clave"], centro)
                interfaz_funciones["eliminar_frame"](frame_principal)
                pagina_crear()
        
        def boton_casa():
            #otro encabezado (posibles botones futuros)
            botones_frame = Frame(frame_principal, bg="#636363")
            botones_frame.pack(fill="x")
            btn_agregar_centro = Button(botones_frame, text="Tus centros", **Boton_estilo, command= lambda: [interfaz_funciones["eliminar_frame"](frame_principal),pagina_crear()])
            btn_agregar_centro.grid(row=0, column=0)

        boton_casa()

        #casos
        if caso == "editar":
            Label(frame_principal, text="Editar Centro", **Label1_estilo).pack(pady=10)
            Label(frame_principal, text=f"{centro["nombre"]}", font=("Arial", 12), bg="#E6FFE6").pack(pady=5)
        elif caso == "agregar":
            Label(frame_principal, text="Agregar Centro", **Label1_estilo).pack(pady=10)
            Label(frame_principal, text=f"{centro["nombre"]}", font=("Arial", 12), bg="#E6FFE6").pack(pady=5)

        #nombre
        Label(frame_principal, text="Nombre", **Label2_estilo).pack(pady=5)
        editar_nombre = Entry(frame_principal, **Entrada_estilo)
        editar_nombre.insert(0,centro["nombre"])
        editar_nombre.pack()

        #direccion
        Label(frame_principal, text="Direccion", **Label2_estilo).pack(pady=5)
        editar_direccion = Entry(frame_principal, **Entrada_estilo)
        editar_direccion.insert(0, centro["direccion"])
        editar_direccion.pack()

        #materiales y precios
        Label(frame_principal, text="Materiales", **Label2_estilo).pack(pady=5)
        
        #horarios
        Label(frame_principal, text="Horarios", **Label2_estilo).pack(pady=10)
        editar_horario = Entry(frame_principal, **Entrada_estilo)
        editar_horario.insert(0, centro["horarios"])
        editar_horario.pack()
        
        #link
        Label(frame_principal, text="Link", **Label2_estilo).pack(pady=5)
        editar_link = Entry(frame_principal, **Entrada_estilo)
        editar_link.insert(0, centro["link"])
        editar_link.pack()

        #telefono
        Label(frame_principal, text="Telefono", **Label2_estilo).pack(pady=5)
        editar_telefono = Entry(frame_principal, **Entrada_estilo)
        editar_telefono.insert(0, centro["telefono"])
        editar_telefono.pack()

        btn_enviar = Button(frame_principal, text="Guardar", **Boton_azul, command= obtener_cambios)
        btn_cancelar = Button(frame_principal, text="Cancelar", **Boton_rojo, command= lambda: [interfaz_funciones["eliminar_frame"](frame_principal),pagina_crear()])
        btn_enviar.pack(pady=5)
        btn_cancelar.pack(pady=5)

        #creamos la barra
        barra = interfaz_funciones["barra_busqueda"](frame_principal, centro["materiales"])
        barra["buscar_btn"].config(text=f"{caso}", command =lambda : [interfaz_funciones["ocultar_frame"](barra["cuadro_frame"]), editar_materiales(barra["lista"])])
        barra["busqueda_frame"].place(x=430, y=240)

        frame_principal.pack(fill=BOTH, expand=True)
    
    """------------------------------------iniciar_sesion-----------------------------------"""
    def iniciar_sesion():
        frame_principal = Frame(root)

        def boton_casa():
            #otro encabezado (posibles botones futuros)
            botones_frame = Frame(frame_principal, bg="#636363")
            botones_frame.pack(fill="x")
            btn_agregar_centro = Button(botones_frame, text="Pagina principal",**Boton_estilo, command= lambda: [interfaz_funciones["eliminar_frame"](frame_principal),pagina_principal()])
            btn_agregar_centro.grid(row=0, column=0)

        def iniciar_sesion():

            global estado
            global usuario

            nombre = insertar_nombre.get()
            correo = insertar_correo.get()
            contrasena = insertar_contrasena.get()

            usuario = administrar_cuentas["iniciar_sesion"](nombre, correo, contrasena)

            if usuario:
                messagebox.showinfo("Éxito", "se ha iniciado sesion correctamente")

                #aqui actualizamos datos
                tipo = administrar_cuentas["obtener_tipo"](usuario)
                print(tipo)
                if tipo == "usuario":
                    estado = "usuario"  # Modificamos la variable global
                elif tipo == "administrador":
                    estado = "administrador"  # Modificamos la variable global
                print(usuario)
                print(estado)
                interfaz_funciones["eliminar_frame"](frame_principal)
                pagina_principal()

        
        boton_casa()
        Label(frame_principal, text="Iniciar sesion", **Label1_estilo).pack(pady=10)

        #nombre
        Label(frame_principal, text="nombre", **Label2_estilo).pack(pady=10)
        insertar_nombre = Entry(frame_principal, **Entrada_estilo)
        insertar_nombre.pack(pady=5)

        #correo
        Label(frame_principal, text="correo", **Label2_estilo).pack(pady=10)
        insertar_correo = Entry(frame_principal, **Entrada_estilo)
        insertar_correo.pack(pady=5)
        
        #contraseña
        Label(frame_principal, text="contraseña", **Label2_estilo).pack(pady=10)
        insertar_contrasena = Entry(frame_principal, **Entrada_estilo, show="*")
        insertar_contrasena.pack(pady=5)
        
        #botones
        boton_enviar = Button(frame_principal, text = "Iniciar sesion", command= iniciar_sesion, **Boton_estilo)
        boton_enviar.pack(pady=10)

        frame_principal.pack(fill=BOTH, expand=True)

    """------------------------------------pagina cuenta-----------------------------------"""
    def pagina_cuenta():
        frame_principal = Frame(root)

        def boton_casa():
            #otro encabezado (posibles botones futuros)
            botones_frame = Frame(frame_principal, bg="#636363")
            botones_frame.pack(fill="x")
            btn_agregar_centro = Button(botones_frame, text="Pagina principal",**Boton_estilo, command= lambda: [interfaz_funciones["eliminar_frame"](frame_principal),pagina_principal()])
            btn_agregar_centro.grid(row=0, column=0)
        
        def cerrar_sesion():
            global estado
            global usuario

            estado = "no sesion"
            usuario = {}

            print(usuario)
            messagebox.showinfo("Éxito", "se ha cerrado sesion correctamente")

        
        boton_casa()
        
        Label(frame_principal, text="Tu cuenta", **Label1_estilo).pack(pady=10)
        #nombre
        Label(frame_principal, text="Nombre:", **Label2_estilo).pack(pady=5)
        Label(frame_principal, text=usuario["nombre"], **Label3_estilo).pack(pady=5)

        #correo
        Label(frame_principal, text="Correo:", **Label2_estilo).pack(pady=5)
        Label(frame_principal, text=usuario["correo"], **Label3_estilo).pack(pady=5)

        #contraseña
        Label(frame_principal, text="Contraseña:", **Label2_estilo).pack(pady=5)

        texto_contrasena = "*" * len(usuario["contrasena"])
        contrasena_label = Label(frame_principal, text=texto_contrasena, **Label3_estilo)        
        contrasena_label.pack(pady=5)

        btn_editar = Button(frame_principal, text="Editar", **Boton_azul, command= lambda : [interfaz_funciones["eliminar_frame"](frame_principal), pagina_editar_cuenta()])
        btn_cerrar = Button(frame_principal, text="Cerrar sesion", **Boton_rojo, command=lambda : [cerrar_sesion() ,pagina_principal(),interfaz_funciones["eliminar_frame"](frame_principal)])
        btn_editar.pack(pady=5)
        btn_cerrar.pack(pady=5)

        frame_principal.pack(fill=BOTH, expand=True)
    
    """------------------------------------editar cuenta-----------------------------------"""
    def pagina_editar_cuenta():
        frame_principal = Frame(root)

        def boton_casa():
            #otro encabezado (posibles botones futuros)
            botones_frame = Frame(frame_principal, bg="#636363")
            botones_frame.pack(fill="x")
            btn_agregar_centro = Button(botones_frame, text="Regresar",**Boton_estilo, command= lambda: [interfaz_funciones["eliminar_frame"](frame_principal),pagina_cuenta()])
            btn_agregar_centro.grid(row=0, column=0)
        
        def manejar_editar():
            global usuario

            nuevo_nombre = editar_nombre.get()
            nuevo_correo = editar_correo.get()
            nueva_contrasena = editar_contrasena.get()
            nueva_confirmar = confirmar_contrasena.get()

            cambios = administrar_cuentas["editar_cuenta"](nuevo_nombre, nuevo_correo, nueva_contrasena, nueva_confirmar, usuario)

            if cambios:
                interfaz_funciones["eliminar_frame"](frame_principal)
                pagina_cuenta()

        boton_casa()
        #editar
        Label(frame_principal, text="Editar cuenta", **Label1_estilo)
        #nombre
        Label(frame_principal, text="Nombre", **Label2_estilo).pack(pady=5)
        editar_nombre = Entry(frame_principal, **Entrada_estilo)
        editar_nombre.insert(0,usuario["nombre"])
        editar_nombre.pack()

        #correo
        Label(frame_principal, text="Correo", **Label2_estilo).pack(pady=5)
        editar_correo = Entry(frame_principal, **Entrada_estilo)
        editar_correo.insert(0,usuario["correo"])
        editar_correo.pack()

        #contraseña
        Label(frame_principal, text="Contraseña", **Label2_estilo).pack(pady=5)
        editar_contrasena = Entry(frame_principal, **Entrada_estilo, show="*")
        editar_contrasena.insert(0,usuario["contrasena"])
        editar_contrasena.pack()

        #confrimar contraseña
        Label(frame_principal, text="Confirmar contraseña", **Label2_estilo).pack(pady=5)
        confirmar_contrasena = Entry(frame_principal, **Entrada_estilo, show="*")
        confirmar_contrasena.insert(0,usuario["contrasena"])
        confirmar_contrasena.pack()

        #botones
        btn_confirmar = Button(frame_principal, text="Confirmar", **Boton_azul,command=manejar_editar)
        btn_cancelar = Button(frame_principal, text="Cancelar", **Boton_rojo, command=lambda : [interfaz_funciones["eliminar_frame"](frame_principal), pagina_cuenta()])
        btn_confirmar.pack(pady=5)
        btn_cancelar.pack(pady=5)

        frame_principal.pack(fill=BOTH, expand=True)

    """------------------------------------registrar cuenta-----------------------------------"""
    def pagina_registrar():
        frame_principal = Frame(root)

        def boton_casa():
            #otro encabezado (posibles botones futuros)
            botones_frame = Frame(frame_principal, bg="#636363")
            botones_frame.pack(fill="x")
            btn_agregar_centro = Button(botones_frame, text="Pagina principal",**Boton_estilo, command= lambda: [interfaz_funciones["eliminar_frame"](frame_principal),pagina_principal()])
            btn_agregar_centro.grid(row=0, column=0)
        
        def manejar_agregar():
            global usuario

            nuevo_nombre = agregar_nombre.get()
            nuevo_correo = agregar_correo.get()
            nueva_contrasena = agregar_contrasena.get()
            nueva_confirmar = confirmar_contrasena.get()

            cambios = administrar_cuentas["registrar_cuenta"](nuevo_nombre, nuevo_correo, nueva_contrasena, nueva_confirmar)

            if cambios:
                interfaz_funciones["eliminar_frame"](frame_principal)
                pagina_principal()

        boton_casa()
        #editar
        Label(frame_principal, text="Registrar cuenta", **Label1_estilo).pack(pady=10)
        #nombre
        Label(frame_principal, text="Nombre", **Label2_estilo).pack(pady=5)
        agregar_nombre = Entry(frame_principal, **Entrada_estilo)
        agregar_nombre.pack()

        #correo
        Label(frame_principal, text="Correo", **Label2_estilo).pack(pady=5)
        agregar_correo = Entry(frame_principal, **Entrada_estilo)
        agregar_correo.pack()

        #contraseña
        Label(frame_principal, text="Contraseña", **Label2_estilo).pack(pady=5)
        agregar_contrasena = Entry(frame_principal, **Entrada_estilo, show="*")
        agregar_contrasena.pack()

        #confrimar contraseña
        Label(frame_principal, text="Confirmar contraseña", **Label2_estilo).pack(pady=5)
        confirmar_contrasena = Entry(frame_principal, **Entrada_estilo, show="*")
        confirmar_contrasena.pack()

        #botones
        btn_confirmar = Button(frame_principal, text="Confirmar", **Boton_azul, command=manejar_agregar)
        btn_cancelar = Button(frame_principal, text="Cancelar", **Boton_rojo, command=lambda : [interfaz_funciones["eliminar_frame"](frame_principal), pagina_principal()])
        btn_confirmar.pack(pady=5)
        btn_cancelar.pack(pady=5)

        frame_principal.pack(fill=BOTH, expand=True)

    pagina_principal()
    root.mainloop()
