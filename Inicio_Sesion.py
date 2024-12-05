
usuarios = []

def registro():
    usuario_entry = tk.Entry(ventana)
    correo_entry = tk.Entry(ventana)
    contra_entry = tk.Entry(ventana, show="*")

    def iniciar_sesion():
        username = usuario_entry.get()
        correo = correo_entry.get()
        contrasena = contra_entry.get()

        if username in usuarios and correo in usuarios and contrasena in usuarios:
            registro_exitoso(username, correo, contrasena)
