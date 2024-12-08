import tkinter as tk
from tkinter import messagebox
import os
import sys

# Lista de materiales reciclables
materiales_reciclables = [
    "Escombros", "Residuos vegetales", "Aceites y grasas", "Plasticos", "Papel", "Carton",
    "Vidrio", "Metales", "Electronicos", "Cascajo", "Aceites usados"
]

# Función para obtener la ruta de los archivos incluidos
def obtener_ruta_relativa(ruta_relativa):
    # Detecta si el programa está en un ejecutable
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # Ruta temporal donde PyInstaller extrae los datos
    else:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, ruta_relativa)


RUTA = "centros.txt"
ARCHIVO = obtener_ruta_relativa("Datos/centros.txt")

centros =[] #Arreglo de centro donde estaran 

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

# Función para guardar los datos
def guardar_datos():
    with open(ARCHIVO, "w") as f:
        for centro in centros:
            f.write(f"{centro['nombre']};{centro['direccion']};{centro['telefono']};{centro['horarios']};{','.join(centro['materiales'])};{','.join(map(str, centro['precios']))};{centro['link']};{centro['clave']}\n")

#inicializamos
cargar_datos()

# Función para registrar un centro
def crear_centro():
    return {
        "nombre": "",
        "direccion": "",
        "telefono": "",
        "horarios": "",
        "materiales": [],
        "precios": [],
        "link": "",
        "clave": ""
    }

def agregar_centro(centro):
    centros.append(centro)
    guardar_datos()

# Función para editar un centro
def editar_centro(nombre_nuevo, direccion_nueva, telefono_nuevo, horarios_nuevos, materiales_nuevos, precios_nuevos, link_nuevo, clave_ingresada, centro):
    
    if centro in centros:
        centro['nombre'] = nombre_nuevo or centro['nombre']
        centro['direccion'] = direccion_nueva or centro['direccion']
        centro['telefono'] = telefono_nuevo or centro['telefono']
        centro['horarios'] = horarios_nuevos or centro['horarios']
        centro['materiales'] = materiales_nuevos or centro["materiales"]
        centro["precios"] = precios_nuevos or centro["precios"]
        centro['link'] = link_nuevo or centro['link']
        centro["clave"] = clave_ingresada or centro["clave"]
        messagebox.showinfo("Éxito", "El centro se añadio correctamente.")
        guardar_datos()
        return 
    messagebox.showwarning("Error", "No se encontró un centro con esa clave.")

def eliminar_centro(centro_ing):
    centros.remove(centro_ing)
    guardar_datos()
    return 
