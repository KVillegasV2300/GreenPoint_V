import tkinter as tk
from tkinter import messagebox

usuarios = [['Zeus', 'zeustrrs16@gmail.com', 'Holas']]

def registro():
    ventana = tk.Tk()
    ventana.geometry("1800x1000")
    ventana.configure(bg="#636363")
    ventana.title("Registro")

    fondo = tk.Label()
    fondo.configure(bg="#ABF0A1", width=1200, height=30)
    fondo.place(x=0, y=0)

    registro = tk.Label()
    registro.configure(bg="white", width=80, height=45)
    registro.pack(padx=50, pady=70, ipadx=50, ipady=50)

    registrar_cuenta = tk.Text(ventana, height=4, width=50, borderwidth=0)
    registrar_cuenta_config = ('Arial', 30, 'bold')
    registrar_cuenta.insert(tk.END, "Registrar Cuenta")
    registrar_cuenta.config(state=tk.DISABLED)
    registrar_cuenta.configure(font=registrar_cuenta_config, fg='black', width=20)
    registrar_cuenta.place(x=630, y=130)

    texto_config = ('Arial', 20)
    usuario_config = ('Arial', 20)
    tk.Label(ventana, text="Nombre de Usuario", bg='white', fg='black', font=texto_config).place(x=630, y=240)
    usuario_entry = tk.Entry(ventana, bg='gray80', fg='black', borderwidth=0, width=32, font=usuario_config)
    usuario_entry.place(x=660, y=275)

    tk.Label(ventana, text="Correo Electrónico", bg='white', fg='black', font=texto_config).place(x=630, y=350)
    correo_entry = tk.Entry(ventana, bg='gray80', fg='black', borderwidth=0, width=32, font=usuario_config)
    correo_entry.place(x=660, y=385)

    tk.Label(ventana, text="Contraseña", bg='white', fg='black', font=texto_config).place(x=630, y=460)
    contra_entry = tk.Entry(ventana, show="*", bg='gray80', fg='black', borderwidth=0, width=32, font=usuario_config)
    contra_entry.place(x=660, y=495)

    tk.Label(ventana, text="Confirmar Contraseña", bg='white', fg='black', font=texto_config).place(x=630, y=570)
    contra_conf_entry = tk.Entry(ventana, show="*", bg='gray80', fg='black', borderwidth=0, width=32, font=usuario_config)
    contra_conf_entry.place(x=660, y=605)

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
            registro_exitoso()

    def registro_exitoso():
        exito_ventana = tk.Toplevel()
        exito_ventana.geometry("1800x1000")
        exito_ventana.configure(bg="#636363")

        fondo = tk.Label(exito_ventana)
        fondo.configure(bg="#ABF0A1", width=1200, height=30)
        fondo.place(x=0, y=0)

        inicio = tk.Label(exito_ventana)
        inicio.configure(bg="white", width=80, height=45)
        inicio.pack(padx=50, pady=70, ipadx=50, ipady=50)

        mensaje_exito = tk.Text(exito_ventana, height=4, width=10, borderwidth=0)
        mensaje_exito_config = ('Arial', 30, 'bold')
        mensaje_exito.insert(tk.END, "Registro Exitoso")
        mensaje_exito.config(state=tk.DISABLED)
        mensaje_exito.configure(font=mensaje_exito_config, fg='black', width=20)
        mensaje_exito.place(x=630, y=130)

        tk.Button(exito_ventana, text="Volver", command=ventana.destroy, bg='white', fg='DeepSkyBlue2', borderwidth=0, width=10, font=texto_config).place(x=640, y=750)

    tk.Button(ventana, text="Registrar", command=registro_cuenta, bg='white', fg='black', borderwidth=0, width=10, font=texto_config).place(x=980, y=750)
    tk.Button(ventana, text="Volver", command=ventana.destroy, bg='white', fg='DeepSkyBlue2', borderwidth=0, width=10, font=texto_config).place(x=640, y=750)

    ventana.mainloop()

registro()