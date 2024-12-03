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
#Materiales y Precios 
def registrar_centro(nombre, direccion, telefono, horarios, materiales, precios, link, clave):

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

# Función para consultar centros
#¿def consultar_centros():
    #¿if not centros:
        #¿messagebox.showinfo("Sin centros", "No hay centros registrados.")
    #¿else:
        #¿consulta = ""
        #¿for centro in centros:
            #¿materiales = ", ".join(centro['materiales'])
            #¿precios = ", ".join(map(str, centro['precios']))
            #¿consulta += f"Nombre: {centro['nombre']}; Dirección: {centro['direccion']}; Teléfono: {centro['telefono']}; Horarios: {centro['horarios']}; Materiales: {materiales}; Precios: {precios}; Link: {centro['link']}\n"
        #¿messagebox.showinfo("Lista de Centros", consulta)

# Función para buscar un centro por clave
#¿def buscar_centro():
    #¿clave_buscar = simpledialog.askstring("Entrada", "Ingresa la clave del centro que deseas buscar:")
    #¿centro_encontrado = None

    #¿for centro in centros:
        #¿if centro['clave'] == clave_buscar:
            #¿centro_encontrado = centro
            #¿break

    #¿if centro_encontrado:
        #¿materiales = ", ".join(centro_encontrado['materiales'])
        #¿precios = ", ".join(map(str, centro_encontrado['precios']))
        #¿consulta = f"Nombre: {centro_encontrado['nombre']}, Dirección: {centro_encontrado['direccion']}, Teléfono: {centro_encontrado['telefono']}, Horarios: {centro_encontrado['horarios']}, Materiales: {materiales}, Precios: {precios}, Link: {centro_encontrado['link']}"
        #¿messagebox.showinfo("Centro encontrado", consulta)
    #¿else:
        #¿messagebox.showwarning("No encontrado", "No se encontró un centro con esa clave.")

# Función para editar un centro
def editar_centro(nombre_nuevo, direccion_nueva, telefono_nuevo, horarios_nuevos, materiales_nuevos, precios_nuevos, link_nuevo, clave_ingresada):
    for centro in centros:
        if centro['clave'] == clave_ingresada:
            centro['nombre'] = nombre_nuevo or centro['nombre']
            centro['direccion'] = direccion_nueva or centro['direccion']
            centro['telefono'] = telefono_nuevo or centro['telefono']
            centro['horarios'] = horarios_nuevos or centro['horarios']
            for material in materiales_nuevos:
                centro['materiales'][material] = material
            for precio in precios_nuevos:
                centro['precios'][precio] = float(precio)
            centro['link'] = link_nuevo or centro['link']
            guardar_datos()
            messagebox.showinfo("Éxito", "El centro se actualizó correctamente.")
            return
    messagebox.showwarning("Error", "No se encontró un centro con esa clave.")

def eliminar_centro(clave_ingresada):
    for centro in centros:
        if centro['clave'] == clave_ingresada:
            centros.remove(centro)
            guardar_datos()
            messagebox.showinfo("Éxito", "El centro se eliminó exitosamente.")
            return
    messagebox.showwarning("Error", "No se encontró un centro con esa clave.")
