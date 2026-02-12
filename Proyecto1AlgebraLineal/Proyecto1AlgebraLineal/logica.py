import numpy as np

class MotorRecta:
    def __init__(self):
        # Atributos para los colores de la rubrica
        self.punto_p = (0, 0)      # Amarillo
        self.v_director = (0, 0)   # Azul
        self.v_normal = (0, 0)     # Rojo
        self.forma_general = ""

    def calcular_desde_parametricas(self, p1, p2, t1, t2):
        # Opcion 1: d = (P2 - P1) / (t2 - t1)
        dx = (p2[0] - p1[0]) / (t2 - t1)
        dy = (p2[1] - p1[1]) / (t2 - t1)
        self.v_director = (dx, dy)
        self.v_normal = (-dy, dx)
        self.punto_p = p1
        self.generar_ecuacion_general()
        return self.forma_general

    def calcular_desde_vectorial(self, p, d):
        # Opcion 2: P y d directos
        self.punto_p = p
        self.v_director = d
        self.v_normal = (-d[1], d[0])
        self.generar_ecuacion_general()
        return self.forma_general

    def calcular_desde_normal(self, p, n):
        # Opcion 3: P y n directos
        self.punto_p = p
        self.v_normal = n
        self.v_director = (-n[1], n[0])
        self.generar_ecuacion_general()
        return self.forma_general

    def generar_ecuacion_general(self):
        # Forma normal n * x = n * p -> ax + by = c
        a, b = self.v_normal
        c = a * self.punto_p[0] + b * self.punto_p[1]
        self.forma_general = f"{a:.2f}x + {b:.2f}y = {c:.2f}"