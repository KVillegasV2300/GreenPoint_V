import tkinter as tk
from tkinter import messagebox, simpledialog
import os

# Lista de materiales reciclables
materiales_reciclables = [
    "Escombros", "Desechos vegetales", "Aceites y grasas", "Plásticos", "Papel", "Cartón",
    "Vidrio", "Metales", "Electrónicos", "Cascajo", "Aceites usados"
]

RUTA = "centros.txt"
ARCHIVO = os.path.join("GreenPoint_V", RUTA)

# Lista inicial de centros
centros = []

# Función para cargar datos de centros.txt
def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            for linea in f:
                partes = linea.strip().split(";")
                if len(partes) >= 8:
                    nombre = partes[0]
                    direccion = partes[1]
                    telefono = partes[2]
                    horarios = partes[3]
                    materiales = partes[4].split(",")
                    precios = list(map(float, partes[5].split(",")))
                    link = partes[6]
                    clave = partes[7]
                    centro = {
                        "nombre": nombre,
                        "direccion": direccion,
                        "telefono": telefono,
                        "horarios": horarios,
                        "materiales": materiales,
                        "precios": precios,
                        "link": link,
                        "clave": clave
                    }
                    centros.append(centro)

cargar_datos()

# Función para guardar los datos
def guardar_datos():
    with open(ARCHIVO, "w") as f:
        for centro in centros:
            f.write(f"{centro['nombre']};{centro['direccion']};{centro['telefono']};{centro['horarios']};{','.join(centro['materiales'])};{','.join(map(str, centro['precios']))};{centro['link']};{centro['clave']}\n")

# Función para registrar un centro
def registrar_centro():
    ventana.withdraw()
    nombre = simpledialog.askstring("Entrada", "Ingresa el nombre del centro:")
    direccion = simpledialog.askstring("Entrada", "Ingresa la dirección del centro:")
    telefono = simpledialog.askstring("Entrada", "Ingresa el teléfono del centro:")
    horarios = simpledialog.askstring("Entrada", "Ingresa el horario del centro:")

    materiales = []
    n = simpledialog.askinteger("Materiales", "Ingresa la cantidad de materiales que vas a registrar:")
    for i in range(n):
        material = simpledialog.askstring("Entrada", f"Ingrese el nombre del material {i+1}:")
        materiales.append(material)

    precios = []
    for i in range(n):
        precio = float(simpledialog.askstring("Entrada", f"Ingrese el precio del material {materiales[i]}:"))
        precios.append(precio)

    link = simpledialog.askstring("Entrada", "Ingresa el enlace relacionado al centro:")
    clave = simpledialog.askstring("Entrada", "Ingresa la clave única del centro:")

    centro = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
        "horarios": horarios,
        "materiales": materiales,
        "precios": precios,
        "link": link,
        "clave": clave
    }

    centros.append(centro)
    guardar_datos()
    ventana.deiconify()

# Función para consultar centros
def consultar_centros():
    if not centros:
        messagebox.showinfo("Sin centros", "No hay centros registrados.")
    else:
        consulta = ""
        for centro in centros:
            materiales = ", ".join(centro['materiales'])
            precios = ", ".join(map(str, centro['precios']))
            consulta += f"Nombre: {centro['nombre']}; Dirección: {centro['direccion']}; Teléfono: {centro['telefono']}; Horarios: {centro['horarios']}; Materiales: {materiales}; Precios: {precios}; Link: {centro['link']}\n"
        messagebox.showinfo("Lista de Centros", consulta)

# Función para buscar un centro por clave
def buscar_centro():
    clave_buscar = simpledialog.askstring("Entrada", "Ingresa la clave del centro que deseas buscar:")
    centro_encontrado = None

    for centro in centros:
        if centro['clave'] == clave_buscar:
            centro_encontrado = centro
            break

    if centro_encontrado:
        materiales = ", ".join(centro_encontrado['materiales'])
        precios = ", ".join(map(str, centro_encontrado['precios']))
        consulta = f"Nombre: {centro_encontrado['nombre']}, Dirección: {centro_encontrado['direccion']}, Teléfono: {centro_encontrado['telefono']}, Horarios: {centro_encontrado['horarios']}, Materiales: {materiales}, Precios: {precios}, Link: {centro_encontrado['link']}"
        messagebox.showinfo("Centro encontrado", consulta)
    else:
        messagebox.showwarning("No encontrado", "No se encontró un centro con esa clave.")

# Función para editar un centro
def editar_centro():
    ventana.withdraw()
    clave = simpledialog.askstring("Entrada", "Ingresa la clave del centro que deseas editar:")
    for centro in centros:
        if centro['clave'] == clave:
            centro['nombre'] = simpledialog.askstring("Entrada", "Ingresa el nuevo nombre o presiona ENTER para mantener el actual:") or centro['nombre']
            centro['direccion'] = simpledialog.askstring("Entrada", "Ingresa la nueva dirección o presiona ENTER para mantener la actual:") or centro['direccion']
            centro['telefono'] = simpledialog.askstring("Entrada", "Ingresa el nuevo teléfono o presiona ENTER para mantener el actual:") or centro['telefono']
            centro['horarios'] = simpledialog.askstring("Entrada", "Ingresa el nuevo horario o presiona ENTER para mantener el actual:") or centro['horarios']
            n = len(centro['materiales'])
            for i in range(n):
                nuevo_material = simpledialog.askstring("Entrada", f"Ingresa el nuevo material {i+1} o presiona ENTER para mantener el actual:") or centro['materiales'][i]
                centro['materiales'][i] = nuevo_material
            for i in range(n):
                nuevo_precio = simpledialog.askstring("Entrada", f"Ingresa el nuevo precio para {centro['materiales'][i]} o presiona ENTER para mantener el actual:") or centro['precios'][i]
                centro['precios'][i] = float(nuevo_precio)
            centro['link'] = simpledialog.askstring("Entrada", "Ingresa el nuevo enlace o presiona ENTER para mantener el actual:") or centro['link']
            guardar_datos()
            messagebox.showinfo("Éxito", "El centro se actualizó correctamente.")
            ventana.deiconify()
            return
    messagebox.showwarning("Error", "No se encontró un centro con esa clave.")
    ventana.deiconify()

# Función para eliminar un centro
def eliminar_centro():
    ventana.withdraw()
    clave = simpledialog.askstring("Entrada", "Ingresa la clave del centro que deseas eliminar:")
    for centro in centros:
        if centro['clave'] == clave:
            centros.remove(centro)
            guardar_datos()
            messagebox.showinfo("Éxito", "El centro se eliminó exitosamente.")
            ventana.deiconify()
            return
    messagebox.showwarning("Error", "No se encontró un centro con esa clave.")
    ventana.deiconify()

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("GreenPoint")
ventana.geometry("1000x500")

etiqueta_seleccionar = tk.Label(ventana, text="LISTA DE CENTROS\n\nSelecciona una opción\n", font=("Arial", 20))
etiqueta_seleccionar.pack(pady=10)

boton1 = tk.Button(ventana, text="Registrar Centro", command=registrar_centro)
boton1.pack(pady=5)

boton2 = tk.Button(ventana, text="Consultar Centros", command=consultar_centros)
boton2.pack(pady=5)

boton3 = tk.Button(ventana, text="Buscar Centro", command=buscar_centro)
boton3.pack(pady=5)

boton4 = tk.Button(ventana, text="Editar Centro", command=editar_centro)
boton4.pack(pady=5)

boton5 = tk.Button(ventana, text="Eliminar Centro", command=eliminar_centro)
boton5.pack(pady=5)

boton6 = tk.Button(ventana, text="Salir", command=ventana.quit)
boton6.pack(pady=5)

ventana.mainloop()