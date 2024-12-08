import tkinter as tk
from tkinter import messagebox

usuarios = [['Zeus', 'zeustrrs16@gmail.com', 'Holas']]

def registro():
    usuario_entry = tk.Entry(ventana, bg='gray80', fg='black', borderwidth=0, width=32)
    correo_entry = tk.Entry(ventana, bg='gray80', fg='black', borderwidth=0, width=32)
    contra_entry = tk.Entry(ventana, show="*", bg='gray80', fg='black', borderwidth=0, width=32)
    contra_conf_entry = tk.Entry(ventana, show="*", bg='gray80', fg='black', borderwidth=0, width=32)
    registro_cuenta()

    def registro_cuenta():
        username = usuario_entry.get().strip()
        correo = correo_entry.get().strip()
        contrasena = contra_entry.get()
        confirmar_contrasena = contra_conf_entry.get()

        if not username or not correo or not contrasena or not confirmar_contrasena:
            messagebox.showerror("Error", "Verifica que todas las casillas estén llenas")
        elif any(correo == usuario[1] for usuario in usuarios):
            messagebox.showerror("Error", "Ya existe un usuario con ese correo")
        elif contrasena != confirmar_contrasena:
            messagebox.showerror("Error", "Las contraseñas no coinciden")
        elif len(username) > 30:
            messagebox.showinfo("Oye", "El nombre de usuario solo puede contener máximo 30 caractéres")
        else:
            usuarios.append([username, correo, contrasena])

registro()