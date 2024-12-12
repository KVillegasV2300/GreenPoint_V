import tkinter as tk
from tkinter import messagebox
import os
import sys
import shutil

usuarios = []
admistradores = []

# Función para obtener la ruta accesible en el sistema del usuario
def obtener_ruta_datos(nombre_archivo):
    carpeta_datos = os.path.join(os.path.expanduser("~"), "GreenPoint")  # Carpeta en el directorio del usuario
    os.makedirs(carpeta_datos, exist_ok=True)  # Crear carpeta si no existe
    return os.path.join(carpeta_datos, nombre_archivo)

# Función para obtener la ruta relativa de los archivos empaquetados
def obtener_ruta_relativa(ruta_relativa):
    if getattr(sys, 'frozen', False):  # Si está empaquetado con PyInstaller
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, ruta_relativa)

# Función para copiar el archivo inicial a una carpeta accesible
def inicializar_archivo_datos_usuario():
    ruta_destino = obtener_ruta_datos("usuarios.txt")  # Carpeta accesible
    if not os.path.exists(ruta_destino):  # Solo copiar si el archivo no existe
        ruta_origen = obtener_ruta_relativa("Datos/usuarios.txt")  # Ruta del archivo empaquetado
        shutil.copy(ruta_origen, ruta_destino)
        print(f"Archivo inicial copiado a: {ruta_destino}")

# Función para copiar el archivo inicial a una carpeta accesible
def inicializar_archivo_datos_admin():
    ruta_destino = obtener_ruta_datos("administradores.txt")  # Carpeta accesible
    if not os.path.exists(ruta_destino):  # Solo copiar si el archivo no existe
        ruta_origen = obtener_ruta_relativa("Datos/administradores.txt")  # Ruta del archivo empaquetado
        shutil.copy(ruta_origen, ruta_destino)
        print(f"Archivo inicial copiado a: {ruta_destino}")

# Llama a esta función antes de cargar los datos
inicializar_archivo_datos_usuario()
inicializar_archivo_datos_admin()

#aqui guardamos todo
ARCHIVO = obtener_ruta_datos("usuarios.txt")
ARCHIVO2 = obtener_ruta_datos("administradores.txt")

# Función para cargar datos de usuarios.txt
def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            for linea in f:
                partes = linea.strip().split(";")
                if len(partes) >= 4:
                    nombre = partes[0]
                    correo = partes[1]
                    contrasena = partes[2]
                    tipo = partes[3]
                    usuario = {
                        "nombre": nombre,
                        "correo": correo,
                        "contrasena": contrasena,
                        "tipo": tipo,
                    }
                    usuarios.append(usuario)
    
    if os.path.exists(ARCHIVO2):
        with open(ARCHIVO2, "r") as f:
            for linea in f:
                partes = linea.strip().split(";")
                if len(partes) >= 5:
                    nombre = partes[0]
                    correo = partes[1]
                    contrasena = partes[2]
                    tipo = partes[3]
                    clave = partes[4]
                    administrador = {
                        "nombre": nombre,
                        "correo": correo,
                        "contrasena": contrasena,
                        "tipo": tipo,
                        "clave": clave
                    }
                    admistradores.append(administrador)

# Función para guardar los datos
def guardar_datos():
    with open(ARCHIVO, "w") as f:
        for usuario in usuarios:
            f.write(f"{usuario['nombre']};{usuario['correo']};{usuario['contrasena']};{usuario['tipo']}\n")
    
    with open(ARCHIVO2, "w") as f:
        for administrador in admistradores:
            f.write(f"{administrador['nombre']};{administrador['correo']};{administrador['contrasena']};{administrador['tipo']};{administrador['clave']}\n")

cargar_datos()
    

#logica de las cuentas
def registrar_cuenta(username, correo, contrasena, confirmar_contrasena):
    if not username or not correo or not contrasena or not confirmar_contrasena:
        messagebox.showerror("Error", "Verifica que todas las casillas estén llenas")
        return False
    elif any(correo == usuario["correo"] for usuario in usuarios):
        messagebox.showerror("Error", "Ya existe un usuario con ese correo")
        return False
    elif contrasena != confirmar_contrasena:
        messagebox.showerror("Error", "Las contraseñas no coinciden")
        return False
    elif len(username) > 30:
        messagebox.showinfo("Oye", "El nombre de usuario solo puede contener máximo 30 caractéres")
        return False
    else:
        messagebox.showinfo("usuario registrado", "usuario registrado exitosamente")
        usuarios.append({"nombre": username, "correo": correo, "contrasena": contrasena, "tipo": "usuario"})
        guardar_datos()
        return True

def editar_cuenta(username, correo, contrasena, confirmar_contrasena, cuenta):
    
    if not username or not correo or not contrasena or not confirmar_contrasena:
        messagebox.showerror("Error", "Verifica que todas las casillas estén llenas")
        return False
    elif any(correo == usuario["correo"] and usuario is not cuenta for usuario in usuarios) or any(correo == usuario["correo"] and usuario is not cuenta for usuario in admistradores):
        messagebox.showerror("Error", "Ya existe un usuario con ese correo")
        return False
    elif contrasena != confirmar_contrasena:
        messagebox.showerror("Error", "Las contraseñas no coinciden")
        return False
    elif len(username) > 30:
        messagebox.showinfo("Oye", "El nombre de usuario solo puede contener máximo 30 caractéres")
        return False
    else:
        cuenta["nombre"] = username or cuenta["nombre"]
        cuenta["correo"] = correo or cuenta["correo"]
        cuenta["contrasena"] = contrasena or cuenta["contrasena"]
        messagebox.showinfo("Exito", "Se ha editado exitosamente")
        
        guardar_datos()
        return True


def iniciar_sesion(username, correo, contrasena):
    # se recorre la lista para buscar similares
    for usuario in usuarios:
        if usuario["nombre"] == username and usuario["correo"] == correo and usuario["contrasena"] == contrasena:
            return usuario
    
    for usuario in admistradores:
        if usuario["nombre"] == username and usuario["correo"] == correo and usuario["contrasena"] == contrasena:
            return usuario

    messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

def obtener_tipo(usuario):
    return usuario["tipo"]

def obtener_clave(usuario):
    return usuario["clave"]

def validar_contrasena(contrasena, usuario):
    if contrasena == usuario["contrasena"]:
        return True
    else:
        messagebox.showerror("Error", "Contraseña incorrecta.")
        return False
     