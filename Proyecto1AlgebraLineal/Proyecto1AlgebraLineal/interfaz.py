import tkinter as tk
from tkinter import ttk, messagebox

class Formularios:
    @staticmethod
    def entrada_parametricas(parent, callback_graficar):
        ventana = tk.Toplevel(parent)
        ventana.title("Ingreso: Ecuaciones Parametricas")
        ventana.geometry("350x500")

        # Encabezado segun tu imagen
        tk.Label(ventana, text="Ingrese dos puntos y sus tiempos", font=('Arial', 11, 'bold')).pack(pady=15)

        # Punto 1
        tk.Label(ventana, text="Punto 1 (x, y):").pack()
        ex1 = ttk.Entry(ventana, justify='center'); ex1.pack(pady=2)
        ey1 = ttk.Entry(ventana, justify='center'); ey1.pack(pady=2)
        
        # Tiempo 1
        tk.Label(ventana, text="Tiempo 1 (t1):").pack(pady=(5,0))
        et1 = ttk.Entry(ventana, justify='center'); et1.pack(pady=2)

        # Punto 2
        tk.Label(ventana, text="Punto 2 (x, y):").pack(pady=(10,0))
        ex2 = ttk.Entry(ventana, justify='center'); ex2.pack(pady=2)
        ey2 = ttk.Entry(ventana, justify='center'); ey2.pack(pady=2)
        
        # Tiempo 2
        tk.Label(ventana, text="Tiempo 2 (t2):").pack(pady=(5,0))
        et2 = ttk.Entry(ventana, justify='center'); et2.pack(pady=2)

        def enviar():
            try:
                p1 = (float(ex1.get()), float(ey1.get()))
                p2 = (float(ex2.get()), float(ey2.get()))
                t1, t2 = float(et1.get()), float(et2.get())
                callback_graficar("parametricas", p1=p1, p2=p2, t1=t1, t2=t2)
                ventana.destroy()
            except ValueError:
                messagebox.showerror("Error", "Por favor ingrese solo numeros validos")

        # Boton segun tu imagen
        ttk.Button(ventana, text="Guardar y Continuar", command=enviar).pack(pady=25)