
#IMPORTS NECESARIOS PARA QUE LA APLICACIÓN FUNCIONE
import tkinter as tk
from tkinter import messagebox

#LOGICA DE LA APLICACIÓN
def enviar_datos():
    nombre = entrada_nombre.get()
    email = entrada_email.get()
    messagebox.showinfo("Formulario enviado", f"Nombre: {nombre}\nEmail: {email}")


#CREACIÓN DE VENTANA
ventana = tk.Tk()

#CREACIÓN DE ELEMENTOS DENTRO DE LA VENTANA
entrada_nombre = tk.Entry(ventana)
entrada_email = tk.Entry(ventana)
ventana.title("Mi Primer Formulario")
ventana.geometry("300x150")

#CONFIGURACIÓN DE POSICIONAMIENTO DE LOS ELEMENTOS DENTRO DE LA VENTANA
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_datos)
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
entrada_nombre.grid(row=0, column=1, padx=10, pady=10)
tk.Label(ventana, text="Email:").grid(row=1, column=0, padx=10, pady=10)
entrada_email.grid(row=1, column=1, padx=10, pady=10)
boton_enviar.grid(row=2, column=0, columnspan=2, pady=10)

#INICIAR APLICACIÓN
ventana.mainloop()