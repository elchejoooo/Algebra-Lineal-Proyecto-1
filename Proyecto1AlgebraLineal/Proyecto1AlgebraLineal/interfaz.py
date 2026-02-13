import tkinter as tk
from tkinter import ttk, messagebox

class Formularios:
    @staticmethod
    def extraer_coordenadas(texto):
        try:
            valores = [float(x.strip()) for x in texto.split(',')]
            if len(valores) != 2: raise ValueError
            return tuple(valores)
        except:
            raise ValueError("Formato incorrecto")

    @staticmethod
    def entrada_parametricas(parent, callback_graficar):
        ventana = tk.Toplevel(parent)
        ventana.title("Ingreso: Ecuaciones Parametricas")
        ventana.geometry("350x500")
        tk.Label(ventana, text="Ingrese dos puntos y sus tiempos", font=('Arial', 11, 'bold')).pack(pady=15)
        
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
            try:
                callback_graficar("parametricas", p1=(float(ex1.get()), float(ey1.get())), 
                                  p2=(float(ex2.get()), float(ey2.get())), t1=float(et1.get()), t2=float(et2.get()))
                ventana.destroy()
            except: messagebox.showerror("Error", "Datos invalidos")
        ttk.Button(ventana, text="Guardar y Continuar", command=enviar).pack(pady=20)

    @staticmethod
    def entrada_vectorial(parent, callback_graficar):
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
                p = Formularios.extraer_coordenadas(ent_p.get())
                d = Formularios.extraer_coordenadas(ent_d.get())
                callback_graficar("vectorial", p=p, d=d)
                ventana.destroy()
            except: messagebox.showerror("Error", "Use el formato: numero, numero")
        ttk.Button(ventana, text="Guardar y Continuar", command=enviar).pack(pady=25)

    @staticmethod
    def entrada_normal(parent, callback_graficar):
        ventana = tk.Toplevel(parent)
        ventana.title("Ingreso: Forma Normal")
        ventana.geometry("380x400")
        tk.Label(ventana, text="Formato: n * x = n * p", font=('Arial', 12, 'bold')).pack(pady=10)
        tk.Label(ventana, text="Por favor ingrese los datos con el formato: x, y", fg="blue").pack()

        tk.Label(ventana, text="\nVector normal n (n1, n2):").pack()
        ent_n = ttk.Entry(ventana, justify='center'); ent_n.pack()
        tk.Label(ventana, text="\nPunto p (p1, p2):").pack()
        ent_p = ttk.Entry(ventana, justify='center'); ent_p.pack()

        def enviar():
            try:
                n = Formularios.extraer_coordenadas(ent_n.get())
                p = Formularios.extraer_coordenadas(ent_p.get())
                callback_graficar("normal", p=p, n=n)
                ventana.destroy()
            except: messagebox.showerror("Error", "Use el formato: numero, numero")
        ttk.Button(ventana, text="Guardar y Continuar", command=enviar).pack(pady=25)

    @staticmethod
    def entrada_general(parent, callback_graficar):
        # Opcion 4 de tu compañera
        ventana = tk.Toplevel(parent)
        ventana.title("Ingreso: Forma Algebraica General")
        ventana.geometry("350x400")
        tk.Label(ventana, text="Ingrese coeficientes a, b y c", font=('Arial', 11, 'bold')).pack(pady=15)
        tk.Label(ventana, text="Coeficiente a:").pack()
        ea = ttk.Entry(ventana, justify='center'); ea.pack()
        tk.Label(ventana, text="Coeficiente b:").pack(pady=(10,0))
        eb = ttk.Entry(ventana, justify='center'); eb.pack()
        tk.Label(ventana, text="Coeficiente c:").pack(pady=(10,0))
        ec = ttk.Entry(ventana, justify='center'); ec.pack()

        def enviar():
            try:
                callback_graficar("general", a=float(ea.get()), b=float(eb.get()), c=float(ec.get()))
                ventana.destroy()
            except: messagebox.showerror("Error", "Datos invalidos")
        ttk.Button(ventana, text="Guardar y Continuar", command=enviar).pack(pady=25)

    @staticmethod
    def entrada_pendiente(parent, callback_graficar):
        # Opcion 5 de tu compañera
        ventana = tk.Toplevel(parent)
        ventana.title("Ingreso: Forma Punto Pendiente")
        ventana.geometry("350x400")
        tk.Label(ventana, text="Ingrese la pendiente y el intercepto", font=('Arial', 11, 'bold')).pack(pady=15)
        tk.Label(ventana, text="Pendiente (m):").pack()
        em = ttk.Entry(ventana, justify='center'); em.pack()
        tk.Label(ventana, text="Intercepto vertical (b):").pack(pady=(10,0))
        eb = ttk.Entry(ventana, justify='center'); eb.pack()

        def enviar():
            try:
                callback_graficar("pendiente", m=float(em.get()), b=float(eb.get()))
                ventana.destroy()
            except: messagebox.showerror("Error", "Datos invalidos")
        ttk.Button(ventana, text="Guardar y Continuar", command=enviar).pack(pady=25)