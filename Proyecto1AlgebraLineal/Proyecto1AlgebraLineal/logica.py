import numpy as np

class MotorRecta:
    def __init__(self):
        # Inicializamos los atributos que guardarán la información de la recta
        self.punto_p = (0, 0)      # Punto de paso (Representado en Amarillo)
        self.v_director = (0, 0)   # Dirección de la recta (Representado en Azul)
        self.v_normal = (0, 0)     # Vector perpendicular (Representado en Rojo)
        self.forma_general = ""    # Almacena el texto de la ecuación ax + by = c

    def calcular_desde_parametricas(self, p1, p2, t1, t2):
        # Calcula el vector director d basándose en el cambio de posición sobre el cambio de tiempo
        # Formula: d = (P2 - P1) / (t2 - t1)
        dx = (p2[0] - p1[0]) / (t2 - t1)
        dy = (p2[1] - p1[1]) / (t2 - t1)
        self.v_director = (dx, dy)
        # El vector normal es perpendicular al director: (-dy, dx)
        self.v_normal = (-dy, dx)
        self.punto_p = p1  # Usamos el primer punto como referencia
        self.generar_ecuacion_general()
        return self.forma_general

    def calcular_desde_vectorial(self, p, d):
        # En la forma vectorial x = p + td, el usuario ya nos da el punto y el director
        self.punto_p = p
        self.v_director = d
        # Calculamos el normal para la gráfica y la ecuación general
        self.v_normal = (-d[1], d[0])
        self.generar_ecuacion_general()
        return self.forma_general

    def calcular_desde_normal(self, p, n):
        # En la forma normal n * (x - p) = 0, el usuario da el normal y el punto
        self.punto_p = p
        self.v_normal = n
        # El director es perpendicular al normal
        self.v_director = (-n[1], n[0])
        self.generar_ecuacion_general()
        return self.forma_general

    def generar_desde_general(self, a, b, c):
        # Si tenemos ax + by = c, el vector normal es directamente (a, b)
        self.v_normal = (a, b)
        # El director es perpendicular (-b, a)
        self.v_director = (-b, a)
        # Buscamos un punto de paso P. Si b no es cero, despejamos y cuando x=0
        if b != 0:
            self.punto_p = (0, c/b)
        else:
            # Si b es cero, la recta es vertical, despejamos x
            self.punto_p = (c/a, 0)
        self.generar_ecuacion_general()
        return self.forma_general

    def calcular_desde_pendiente(self, m, b):
        # En y = mx + b, el punto de corte con Y es (0, b)
        self.punto_p = (0, b)
        # La pendiente m indica que por cada 1 en X, sube 'm' en Y
        self.v_director = (1, m)
        # Vector normal perpendicular
        self.v_normal = (-m, 1)
        self.generar_ecuacion_general()
        return self.forma_general

    def generar_ecuacion_general(self):
        # Basado en n * x = n * p -> ax + by = c
        a, b = self.v_normal
        c = a * self.punto_p[0] + b * self.punto_p[1]
        # Formateamos el string para mostrarlo al usuario
        self.forma_general = f"{a:.2f}x + {b:.2f}y = {c:.2f}"