import os

RUTA = "usuarios.txt"
ARCHIVO = os.path.join("GreenPoint_V", RUTA)

# Lista inicial de usuarios
usuarios = []

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

cargar_datos()

# Función para guardar los datos
def guardar_datos():
    with open(ARCHIVO, "w") as f:
        for usuario in usuarios:
            f.write(f"{usuario['nombre']};{usuario['correo']};{usuario['contrasena']};{usuario['tipo']}\n")

RUTA2 = "administradores.txt"
ARCHIVO2 = os.path.join("GreenPoint_V", RUTA)

# Lista inicial de administradores
administradores = []

# Función para cargar datos de administradores.txt
def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
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
                    administradores.append(administrador)

cargar_datos()

# Función para guardar los datos
def guardar_datos():
    with open(ARCHIVO, "w") as f:
        for administrador in administradores:
            f.write(f"{administrador['nombre']};{administrador['correo']};{administrador['contrasena']};{administrador['tipo']};{administrador['clave']}\n")