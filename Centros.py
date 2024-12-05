import tkinter as tk
from tkinter import messagebox

# Lista de materiales reciclables
materiales_reciclables = [
    "Escombros", "Residuos vegetales", "Aceites y grasas", "Plásticos", "Papel", "Cartón",
    "Vidrio", "Metales", "Electrónicos", "Cascajo", "Aceites usados"
]

centros =[] #Arreglo de centro donde estaran 

# Datos de los centros de reciclaje (temporal)
centros_reciclaje = [
    {
        "nombre": "Planta de Reciclaje CIREC Miguel Hidalgo",
        "direccion": "Calle 5 de mayo #150, Col. San Lorenzo Tlaltenango",
        "telefono" : "5555555555555555",
        "horarios": "Lunes a viernes: 8:00 am - 6:00 pm",
        "materiales": ["Escombros", "Residuos vegetales", "Aceites y grasas"],
        "precios":[2,2,4],
        "link": "https://maps.app.goo.gl/9hYGHAfP6suBogjm7",
        "clave" : "1234"
    },
    {
        "nombre": "Centro de Acopio de Residuos Reciclables (CAMH)",
        "direccion": "Alcaldía Miguel Hidalgo, CDMX",
        "telefono" : "5555555555555555",
        "horarios": "Lunes a sábado: 9:00 am - 5:00 pm",
        "materiales": ["Plásticos", "Papel", "Cartón", "Vidrio", "Metales", "Electrónicos"],
        "precios":[5,3,4,3,9,9],
        "link": "https://maps.app.goo.gl/tiqugsXU9aGtLm2d9", 
        "clave" : "1234",
    },
    {
        "nombre": "Centro de Reciclaje Avenida Juárez",
        "direccion": "Avenida Juárez, Miguel Hidalgo",
        "telefono" : "5555555555555555",
        "horarios": "Lunes a viernes: 7:00 am - 4:00 pm",
        "materiales": ["Cascajo", "Residuos vegetales", "Aceites usados"],
        "precios":[2,3,4],
        "link": "https://maps.app.goo.gl/YAnK9pS8ohp5YUC46",
        "clave" : "1908"
    },
    {
        "nombre": "Centro de Reciclaje Avenida Juárez",
        "direccion": "Avenida Juárez, Miguel Hidalgo",
        "telefono" : "5555555555555555",
        "horarios": "Lunes a viernes: 7:00 am - 4:00 pm",
        "materiales": ["Aceites y grasas", "Plásticos", "Papel", "Cartón"],
        "precios":[3,3,9],
        "link": "https://maps.app.goo.gl/C1YjxMGiC8iMZ4GWA",
        "clave" : "3456"
    }
]

#meter todo en un array :) (temporal)
for i in centros_reciclaje:
        centros.append(i)
        print(i['nombre'])

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
        return
    messagebox.showwarning("Error", "No se encontró un centro con esa clave.")

def eliminar_centro(clave_ingresada):
    for centro in centros:
        if centro['clave'] == clave_ingresada:
            centros.remove(centro)
            messagebox.showinfo("Éxito", "El centro se eliminó exitosamente.")
            return
    messagebox.showwarning("Error", "No se encontró un centro con esa clave.")
