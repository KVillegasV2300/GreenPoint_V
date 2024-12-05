import tkinter as tk
from tkinter import messagebox

usuarios = []
admistradores = []

usuarios_prueba = [
    {
        "nombre": "Zeus",
        "correo" : "zeustrr216@gmail.com",
        "contrasena" : "holas",
        "tipo" : "usuario"
    },
    {
        "nombre": "2",
        "correo" : "2",
        "contrasena" : "2",
        "tipo" : "usuario"
    }
]

adminitradosres_prueba = [
    {
        "nombre" : "Residuos pato",
        "correo" : "pato@gmail.com",
        "contrasena" : "pato",
        "tipo": "administrador",
        "clave" : "1908"
    },
    {
        "nombre" : "1",
        "correo" : "1",
        "contrasena" : "1",
        "tipo": "administrador",
        "clave" : "1234"
    }
]

#meter todo en un array :) (temporal)
for i in usuarios_prueba:
        usuarios.append(i)
        print(i['nombre'])

for i in adminitradosres_prueba:
        admistradores.append(i)
        print(i['nombre'])


def registrar_cuenta(username, correo, contrasena, confirmar_contrasena):
    if not username or not correo or not contrasena or not confirmar_contrasena:
        messagebox.showerror("Error", "Verifica que todas las casillas estén llenas")
    elif any(correo == usuario[1] for usuario in usuarios):
        messagebox.showerror("Error", "Ya existe un usuario con ese correo")
    elif contrasena != confirmar_contrasena:
        messagebox.showerror("Error", "Las contraseñas no coinciden")
    elif len(username) > 30:
        messagebox.showinfo("Oye", "El nombre de usuario solo puede contener máximo 30 caractéres")
    else:
        messagebox.showinfo("usuario registrado", "usuario registrado exitosamente")
        usuarios.append([username, correo, contrasena])

def iniciar_sesion(username, correo, contrasena):
    # se recorre la lista para buscar similares
    for usuario in usuarios:
        if usuario["nombre"] == username and usuario["correo"] == correo and usuario["contrasena"] == contrasena:
            return usuario
    
    for usuario in admistradores:
        if usuario["nombre"] == username and usuario["correo"] == correo and usuario["contrasena"] == contrasena:
            return usuario

    messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
    return  

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
     