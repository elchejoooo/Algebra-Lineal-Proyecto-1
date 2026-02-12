import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt # Importante para la grafica
import numpy as np

# --- FUNCION PARA GENERAR LA GRAFICA (PASO FINAL) ---
def generar_grafica(p1, v_director, v_normal):
    x1, y1 = p1
    dx, dy = v_director
    nx, ny = v_normal

    # Crear la figura
    plt.figure("Grafica de la Recta R2 - UMES")
    
    # 1. Ejes coordenados (Gris) 
    plt.axhline(0, color='gray', linewidth=1)
    plt.axvline(0, color='gray', linewidth=1)

    # 2. Linea Recta (Verde) 
    # Dibujamos una linea extendida usando el punto y el director
    t_vals = np.linspace(-10, 10, 100)
    linea_x = x1 + t_vals * dx
    linea_y = y1 + t_vals * dy
    plt.plot(linea_x, linea_y, color='green', label='Linea Recta', linewidth=2)

    # 3. Vector al punto P (Amarillo) - Desde el origen al punto 
    plt.quiver(0, 0, x1, y1, color='yellow', angles='xy', scale_units='xy', scale=1, label='Vector al punto P')

    # 4. Vector Director (Azul) - Saliendo desde el punto P 
    plt.quiver(x1, y1, dx, dy, color='blue', angles='xy', scale_units='xy', scale=1, label='Vector Director')

    # 5. Vector Normal (Rojo) - Saliendo desde el punto P 
    plt.quiver(x1, y1, nx, ny, color='red', angles='xy', scale_units='xy', scale=1, label='Vector Normal')

    # Configuraciones finales de la grafica
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.axis('equal') # Para que no se deformen los angulos de 90 grados
    plt.title("Visualizacion de Rectas y Vectores")
    plt.show()

# --- FUNCION PARA EL FORMULARIO DE LA OPCION 1 ---
def abrir_formulario_parametricas():
    ventana_datos = tk.Toplevel(root)
    ventana_datos.title("Ingreso: Ecuaciones Parametricas")
    ventana_datos.geometry("350x450")

    tk.Label(ventana_datos, text="Ingrese dos puntos y sus tiempos", font=('Arial', 10, 'bold')).pack(pady=10)

    # Campos de entrada (Iguales a los anteriores)
    tk.Label(ventana_datos, text="Punto 1 (x, y):").pack()
    entry_x1 = ttk.Entry(ventana_datos); entry_x1.pack()
    entry_y1 = ttk.Entry(ventana_datos); entry_y1.pack()
    tk.Label(ventana_datos, text="Tiempo 1 (t1):").pack()
    entry_t1 = ttk.Entry(ventana_datos); entry_t1.pack()

    tk.Label(ventana_datos, text="\nPunto 2 (x, y):").pack()
    entry_x2 = ttk.Entry(ventana_datos); entry_x2.pack()
    entry_y2 = ttk.Entry(ventana_datos); entry_y2.pack()
    tk.Label(ventana_datos, text="Tiempo 2 (t2):").pack()
    entry_t2 = ttk.Entry(ventana_datos); entry_t2.pack()

    def procesar_datos():
        try:
            x1, y1 = float(entry_x1.get()), float(entry_y1.get())
            x2, y2 = float(entry_x2.get()), float(entry_y2.get())
            t1, t2 = float(entry_t1.get()), float(entry_t2.get())
            
            if t1 == t2:
                messagebox.showerror("Error", "Los tiempos no pueden ser iguales.")
                return

            # Calculos Matematicos [cite: 12, 14, 20]
            dx = (x2 - x1) / (t2 - t1)
            dy = (y2 - y1) / (t2 - t1)
            v_dir = (dx, dy)
            v_nor = (-dy, dx)
            
            # Cerrar ventana de ingreso y abrir grafica
            ventana_datos.destroy()
            generar_grafica((x1, y1), v_dir, v_nor)

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese solo numeros validos")

    ttk.Button(ventana_datos, text="Graficar Ahora", command=procesar_datos).pack(pady=20)

# --- CONFIGURACION VENTANA PRINCIPAL (Igual a la anterior) ---
root = tk.Tk()
root.title("Graficador de Rectas R2 - UMES") 
root.geometry("400x500")

titulo = tk.Label(root, text="Menu de Seleccion de Datos", font=("Arial", 14, "bold"))
titulo.pack(pady=20)

def seleccionar_opcion(nombre_opcion):
    if "1." in nombre_opcion:
        abrir_formulario_parametricas()
    else:
        messagebox.showinfo("Proximamente", f"Lógica para {nombre_opcion} pendiente.")

opciones = ["1. Ecuaciones Parametricas", "2. Forma Vectorial", "3. Forma Normal", "4. Forma Algebraica General", "5. Forma Punto Pendiente"]
for opcion in opciones:
    ttk.Button(root, text=opcion, width=35, command=lambda o=opcion: seleccionar_opcion(o)).pack(pady=10)

root.mainloop()