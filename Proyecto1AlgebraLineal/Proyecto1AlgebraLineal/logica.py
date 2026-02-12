import numpy as np

class MotorRecta:
    def __init__(self):
        self.punto_p = (0, 0)      # Amarillo
        self.v_director = (0, 0)   # Azul
        self.v_normal = (0, 0)     # Rojo
        self.forma_general = ""

    def calcular_desde_parametricas(self, p1, p2, t1, t2):
        dx = (p2[0] - p1[0]) / (t2 - t1)
        dy = (p2[1] - p1[1]) / (t2 - t1)
        self.v_director = (dx, dy)
        self.v_normal = (-dy, dx)
        self.punto_p = p1
        self.generar_ecuacion_general()
        return self.forma_general

    def calcular_desde_vectorial(self, p, d):
        self.punto_p = p
        self.v_director = d
        self.v_normal = (-d[1], d[0])
        self.generar_ecuacion_general()
        return self.forma_general

    def generar_ecuacion_general(self):
        a, b = self.v_normal
        c = a * self.punto_p[0] + b * self.punto_p[1]
        self.forma_general = f"{a:.2f}x + {b:.2f}y = {c:.2f}"