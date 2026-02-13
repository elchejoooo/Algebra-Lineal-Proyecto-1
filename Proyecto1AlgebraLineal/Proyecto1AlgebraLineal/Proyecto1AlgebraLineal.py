import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np
from logica import MotorRecta
from interfaz import Formularios

class AppPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Graficador de Rectas R2 - UMES")
        self.root.geometry("400x550")
        self.motor = MotorRecta()
        
        tk.Label(self.root, text="Menu de Seleccion de Datos", font=("Arial", 16, "bold")).pack(pady=30)
        
        opciones = [
            ("1. Ecuaciones Parametricas", "parametricas"),
            ("2. Forma Vectorial", "vectorial"),
            ("3. Forma Normal", "normal"),
            ("4. Forma Algebrrica General", "general"),
            ("5. Forma Punto Pendiente", "pendiente")
        ]

        for texto, tipo in opciones:
            if tipo == "parametricas":
                cmd = lambda: Formularios.entrada_parametricas(self.root, self.ejecutar_logica)
            elif tipo == "vectorial":
                cmd = lambda: Formularios.entrada_vectorial(self.root, self.ejecutar_logica)
            elif tipo == "normal":
                cmd = lambda: Formularios.entrada_normal(self.root, self.ejecutar_logica)
            elif tipo == "general":
                cmd = lambda: Formularios.entrada_general(self.root, self.ejecutar_logica)
            elif tipo == "pendiente":
                cmd = lambda: Formularios.entrada_pendiente(self.root, self.ejecutar_logica)
            else:
                cmd = lambda t=texto: print(f"Opcion {t} pendiente")
            
            ttk.Button(self.root, text=texto, width=35, command=cmd).pack(pady=10)

        tk.Label(self.root, text="Seleccione una forma para ingresar datos", fg="gray").pack(side="bottom", pady=20)

    def ejecutar_logica(self, tipo, **kwargs):
        if tipo == "parametricas":
            self.motor.calcular_desde_parametricas(kwargs['p1'], kwargs['p2'], kwargs['t1'], kwargs['t2'])
        elif tipo == "vectorial":
            self.motor.calcular_desde_vectorial(kwargs['p'], kwargs['d'])
        elif tipo == "normal":
            self.motor.calcular_desde_normal(kwargs['p'], kwargs['n'])
        elif tipo == "general":
            self.motor.generar_desde_general(kwargs['a'], kwargs['b'], kwargs['c'])
        elif tipo == "pendiente":
            self.motor.calcular_desde_pendiente(kwargs['m'], kwargs['b'])
        
        self.mostrar_grafica()

    def mostrar_grafica(self):
        p, d, n = self.motor.punto_p, self.motor.v_director, self.motor.v_normal
        plt.figure("Resultado Grafico - UMES")
        plt.axhline(0, color='gray', linewidth=1); plt.axvline(0, color='gray', linewidth=1)
        
        t = np.linspace(-15, 15, 100)
        plt.plot(p[0]+t*d[0], p[1]+t*d[1], color='green', label='Recta (Verde)', linewidth=2)
        
        plt.quiver(0, 0, p[0], p[1], color='yellow', angles='xy', scale_units='xy', scale=1, label='Punto P (Amarillo)')
        plt.quiver(p[0], p[1], d[0], d[1], color='blue', angles='xy', scale_units='xy', scale=1, label='Director (Azul)')
        plt.quiver(p[0], p[1], n[0], n[1], color='red', angles='xy', scale_units='xy', scale=1, label='Normal (Rojo)')
        
        plt.axis('equal'); plt.grid(True, linestyle=':', alpha=0.6); plt.legend(); plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppPrincipal(root)
    root.mainloop()