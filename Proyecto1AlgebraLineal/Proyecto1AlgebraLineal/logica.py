import numpy as np

class MotorRecta:
    def __init__(self):
        self.punto_p = (0, 0)      # Color amarillo
        self.v_director = (0, 0)   # Color azul
        self.v_normal = (0, 0)     # Color rojo
        self.forma_general = ""

    def calcular_desde_parametricas(self, p1, p2, t1, t2):
        # Formula: d = (P2 - P1) / (t2 - t1)
        dx = (p2[0] - p1[0]) / (t2 - t1)
        dy = (p2[1] - p1[1]) / (t2 - t1)
        self.v_director = (dx, dy)
        self.v_normal = (-dy, dx)
        self.punto_p = p1
        
        a, b = self.v_normal
        c = a * p1[0] + b * p1[1]
        self.forma_general = f"{a:.2f}x + {b:.2f}y = {c:.2f}"
        return self.forma_general