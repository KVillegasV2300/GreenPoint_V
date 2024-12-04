import tkinter as tk
from tkinter import messagebox

usuarios = ['Zeus', 'zeustrrs16@gmail.com', 'Holas']

def registro():
    ventana = tk.Tk()
    ventana.geometry("1800x1000")
    ventana.configure(bg="#636363")

    fondo = tk.Label()
    fondo.configure(bg="#ABF0A1", width=1200, height=30)
    fondo.place(x=0, y=0)

    inicio = tk.Label()
    inicio.configure(bg="white", width=80, height=45)
    inicio.pack(padx=50, pady=70, ipadx=50, ipady=50)

    iniciar_sesion = tk.Text(ventana, height=4, width=50, borderwidth=0)
    iniciar_sesion_config = ('Arial', 30, 'bold')
    iniciar_sesion.insert(tk.END, "Iniciar Sesión")
    iniciar_sesion.config(state=tk.DISABLED) 
    iniciar_sesion.configure(font=iniciar_sesion_config, fg='black', width=20)
    iniciar_sesion.place(x=630, y=130)

    texto_config = ('Arial', 20)
    usuario_config = ('Arial', 20)
    tk.Label(ventana, text="Nombre de Usuario", bg='white', fg='black', font=texto_config).place(x=630, y=240)
    usuario_entry = tk.Entry(ventana)
    usuario_entry.configure(bg='gray80', fg='black', borderwidth=0, width=32, font=usuario_config)
    usuario_entry.place(x=660, y=275)

    correo_config = ('Arial', 20)
    tk.Label(ventana, text="Correo Electrónico", bg='white', fg='black', font=texto_config).place(x=630, y=350)
    correo_entry = tk.Entry(ventana)
    correo_entry.configure(bg='gray80', fg='black', borderwidth=0, width=32, font=correo_config)
    correo_entry.place(x=660, y=385)

    contra_config = ('Arial', 20)
    tk.Label(ventana, text="Contraseña", bg='white', fg='black', font=texto_config).place(x=630, y=460)
    contra_entry = tk.Entry(ventana, show="*")
    contra_entry.configure(bg='gray80', fg='black', borderwidth=0, width=32, font=contra_config)
    contra_entry.place(x=660, y=495)

    def iniciar_sesion():
        username = usuario_entry.get()
        correo = correo_entry.get()
        contrasena = contra_entry.get()

        if username in usuarios and correo in usuarios and contrasena in usuarios:
            ventana.destroy()
            registro_exitoso(username, correo, contrasena)
        else:
            messagebox.showerror("Error", "Verifique que los datos ingresados sean correctos")

    def registro_exitoso(username, correo, contrasena):
        exito_ventana = tk.Tk()
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
        mensaje_exito.insert(tk.END, "Sesión Iniciada")
        mensaje_exito.config(state=tk.DISABLED) 
        mensaje_exito.configure(font=mensaje_exito_config, fg='black', width=20)
        mensaje_exito.place(x=630, y=130)

        tk.Button(exito_ventana, text="Volver", command=exito_ventana.destroy, bg='white', fg='DeepSkyBlue2', borderwidth=0, width=10, font=texto_config).place(x=640, y=750)

    tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion, bg='white', fg='black', borderwidth=0, width=10, font=texto_config).place(x=980, y=750)
    tk.Button(ventana, text="Volver", command = ventana.destroy, bg='white', fg='DeepSkyBlue2', borderwidth=0, width=10, font=texto_config).place(x=640, y=750)

    ventana.mainloop()

registro()
