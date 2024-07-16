import math
import random

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def descricao(self):
        return f"Ponto({self.x}, {self.y})"

class Forma:
    def descricao(self):
        pass

class Circulo(Forma):
    def __init__(self):
        self.centro = Ponto(random.randint(0, 10), random.randint(0, 10))
        self.raio = random.randint(1, 5)

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio

    def descricao(self):
        return f"Circulo com centro em {self.centro.descricao()}, raio {self.raio}, area {self.area():.2f}, perimetro {self.perimetro():.2f}"

class Quadrado(Forma):
    def __init__(self):
        self.lado = random.randint(1, 5)
        self.x1, self.y1 = random.randint(0, 10 - self.lado), random.randint(0, 10 - self.lado)
        self.x2, self.y2 = self.x1 + self.lado, self.y1 + self.lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def descricao(self):
        return f"Quadrado com vértices em ({self.x1}, {self.y1}), ({self.x2}, {self.y1}), ({self.x2}, {self.y2}), ({self.x1}, {self.y2}), area {self.area()}, perimetro {self.perimetro()}"

class Retangulo(Forma):
    def __init__(self):
        self.lado1 = random.randint(1, 5)
        self.lado2 = random.randint(1, 5)
        self.x1, self.y1 = random.randint(0, 10 - self.lado1), random.randint(0, 10 - self.lado2)
        self.x2, self.y2 = self.x1 + self.lado1, self.y1 + self.lado2

    def area(self):
        return self.lado1 * self.lado2

    def perimetro(self):
        return 2 * (self.lado1 + self.lado2)

    def descricao(self):
        return f"Retangulo com vértices em ({self.x1}, {self.y1}), ({self.x2}, {self.y1}), ({self.x2}, {self.y2}), ({self.x1}, {self.y2}), area {self.area()}, perimetro {self.perimetro()}"

class Triangulo(Forma):
    def __init__(self):
        self.p1 = Ponto(random.randint(0, 10), random.randint(0, 10))
        self.p2 = Ponto(random.randint(0, 10), random.randint(0, 10))
        self.p3 = Ponto(random.randint(0, 10), random.randint(0, 10))

    def lados(self):
        l1 = math.dist((self.p1.x, self.p1.y), (self.p2.x, self.p2.y))
        l2 = math.dist((self.p2.x, self.p2.y), (self.p3.x, self.p3.y))
        l3 = math.dist((self.p3.x, self.p3.y), (self.p1.x, self.p1.y))
        return l1, l2, l3

    def tipo(self):
        l1, l2, l3 = self.lados()
        if l1 == l2 == l3:
            return "Equilatero"
        elif l1 == l2 or l2 == l3 or l1 == l3:
            return "Isosceles"
        else:
            return "Escaleno"

    def area(self):
        l1, l2, l3 = self.lados()
        s = (l1 + l2 + l3) / 2
        return (s * (s - l1) * (s - l2) * (s - l3)) ** 0.5

    def perimetro(self):
        return sum(self.lados())

    def descricao(self):
        return f"Triangulo {self.tipo()} com vértices em {self.p1.descricao()}, {self.p2.descricao()}, {self.p3.descricao()}, area {self.area():.2f}, perimetro {self.perimetro():.2f}"

class SegmentoReta(Forma):
    def __init__(self):
        self.ponto_inicial = Ponto(random.randint(0, 10), random.randint(0, 10))
        self.ponto_final = Ponto(random.randint(0, 10), random.randint(0, 10))

    def comprimento(self):
        return math.dist((self.ponto_inicial.x, self.ponto_inicial.y), (self.ponto_final.x, self.ponto_final.y))

    def descricao(self):
        return f"Segmento de reta de {self.ponto_inicial.descricao()} a {self.ponto_final.descricao()}, comprimento {self.comprimento():.2f}"

