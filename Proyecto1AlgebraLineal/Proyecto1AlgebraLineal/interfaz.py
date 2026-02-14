import tkinter as tk
from tkinter import ttk, messagebox

class Formularios:
    @staticmethod
    def extraer_coordenadas(texto):
        # Función auxiliar para convertir el texto "x, y" en una tupla de números
        try:
            valores = [float(x.strip()) for x in texto.split(',')]
            if len(valores) != 2: raise ValueError
            return tuple(valores)
        except:
            raise ValueError("Formato incorrecto")

    @staticmethod
    def entrada_parametricas(parent, callback_graficar):
        # Ventana para ingresar puntos y tiempos uno por uno
        ventana = tk.Toplevel(parent)
        ventana.title("Ingreso: Ecuaciones Parametricas")
        ventana.geometry("350x500")
        tk.Label(ventana, text="Ingrese dos puntos y sus tiempos", font=('Arial', 11, 'bold')).pack(pady=15)
        
        # Entradas para Punto 1, Tiempo 1, Punto 2 y Tiempo 2
        tk.Label(ventana, text="Punto 1 (x, y):").pack()
        ex1 = ttk.Entry(ventana, justify='center'); ex1.pack()
        ey1 = ttk.Entry(ventana, justify='center'); ey1.pack()
        tk.Label(ventana, text="Tiempo 1 (t1):").pack()
        et1 = ttk.Entry(ventana, justify='center'); et1.pack()
        
        tk.Label(ventana, text="Punto 2 (x, y):").pack(pady=(10,0))
        ex2 = ttk.Entry(ventana, justify='center'); ex2.pack()
        ey2 = ttk.Entry(ventana, justify='center'); ey2.pack()
        tk.Label(ventana, text="Tiempo 2 (t2):").pack()
        et2 = ttk.Entry(ventana, justify='center'); et2.pack()

        def enviar():
            # Al hacer clic, enviamos los datos a la lógica principal
            try:
                callback_graficar("parametricas", p1=(float(ex1.get()), float(ey1.get())), 
                                  p2=(float(ex2.get()), float(ey2.get())), t1=float(et1.get()), t2=float(et2.get()))
                ventana.destroy()
            except: messagebox.showerror("Error", "Datos invalidos")
        ttk.Button(ventana, text="Guardar y Continuar", command=enviar).pack(pady=20)

    @staticmethod
    def entrada_vectorial(parent, callback_graficar):
        # Ventana con formato simplificado "x, y"
        ventana = tk.Toplevel(parent)
        ventana.title("Ingreso: Forma Vectorial")
        ventana.geometry("380x400")
        tk.Label(ventana, text="Formato: x = p + td", font=('Arial', 12, 'bold')).pack(pady=10)
        tk.Label(ventana, text="Por favor ingrese los datos con el formato: x, y", fg="blue").pack()

        tk.Label(ventana, text="\nPunto p (p1, p2):").pack()
        ent_p = ttk.Entry(ventana, justify='center'); ent_p.pack()
        tk.Label(ventana, text="\nVector director d (d1, d2):").pack()
        ent_d = ttk.Entry(ventana, justify='center'); ent_d.pack()

        def enviar():
            try:
                # Usamos la función auxiliar para limpiar el texto
                p = Formularios.extraer_coordenadas(ent_p.get())
                d = Formularios.extraer_coordenadas(ent_d.get())
                callback_graficar("vectorial", p=p, d=d)
                ventana.destroy()
            except: messagebox.showerror("Error", "Use el formato: numero, numero")
        ttk.Button(ventana, text="Guardar y Continuar", command=enviar).pack(pady=25)

    # ... (Los demás métodos entrada_normal, entrada_general y entrada_pendiente 
    # siguen la misma lógica: recolectar datos y enviarlos al callback)