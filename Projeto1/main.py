import random
import math

class Forma:
    def __init__(self, tipo):
        self.tipo = tipo

    def descricao(self):
        raise NotImplementedError

class Ponto(Forma):
    def __init__(self, x, y):
        super().__init__('Ponto')
        self.x = x
        self.y = y

    def descricao(self):
        return f'Ponto em ({self.x}, {self.y})'

class SegmentoReta(Forma):
    def __init__(self):
        super().__init__('Segmento de Reta')
        self.ponto_inicial = Ponto(random.randint(0, 10), random.randint(0, 10))
        self.ponto_final = Ponto(random.randint(0, 10), random.randint(0, 10))

    def descricao(self):
        return (f'Segmento de reta com ponto inicial em ({self.ponto_inicial.x}, {self.ponto_inicial.y}) '
                f'e ponto final em ({self.ponto_final.x}, {self.ponto_final.y})')

class Triangulo(Forma):
    def __init__(self):
        super().__init__('Triângulo')
        self.p1 = Ponto(random.randint(0, 10), random.randint(0, 10))
        self.p2 = Ponto(random.randint(0, 10), random.randint(0, 10))
        self.p3 = Ponto(random.randint(0, 10), random.randint(0, 10))

    def descricao(self):
        lados = self.lados()
        tipo = self.tipo_triangulo(lados)
        perimetro = sum(lados)
        area = self.area()
        return (f'Triângulo {tipo} com vértices em ({self.p1.x}, {self.p1.y}), ({self.p2.x}, {self.p2.y}), '
                f'({self.p3.x}, {self.p3.y}), perímetro: {perimetro:.2f}, área: {area:.2f}')

    def lados(self):
        lado1 = math.dist((self.p1.x, self.p1.y), (self.p2.x, self.p2.y))
        lado2 = math.dist((self.p2.x, self.p2.y), (self.p3.x, self.p3.y))
        lado3 = math.dist((self.p3.x, self.p3.y), (self.p1.x, self.p1.y))
        return lado1, lado2, lado3

    def tipo_triangulo(self, lados):
        a, b, c = lados
        if a == b == c:
            return 'Equilátero'
        elif a == b or b == c or a == c:
            if self.is_retangulo():
                return 'Retângulo e Isósceles'
            return 'Isósceles'
        else:
            if self.is_retangulo():
                return 'Retângulo e Escaleno'
            return 'Escaleno'

    def is_retangulo(self):
        lados = sorted(self.lados())
        return math.isclose(lados[0]**2 + lados[1]**2, lados[2]**2)

    def area(self):
        return abs(self.p1.x*(self.p2.y - self.p3.y) + self.p2.x*(self.p3.y - self.p1.y) + self.p3.x*(self.p1.y - self.p2.y)) / 2

class Circulo(Forma):
    def __init__(self):
        super().__init__('Círculo')
        self.centro = Ponto(random.randint(0, 10), random.randint(0, 10))
        self.raio = random.randint(1, 5)

    def descricao(self):
        circunferencia = 2 * math.pi * self.raio
        area = math.pi * self.raio**2
        return (f'Círculo com centro em ({self.centro.x}, {self.centro.y}), raio: {self.raio}, '
                f'circunferência: {circunferencia:.2f}, área: {area:.2f}')

class Retangulo(Forma):
    def __init__(self):
        super().__init__('Retângulo')
        self.x1, self.y1 = random.randint(0, 5), random.randint(0, 5)
        self.x2, self.y2 = self.x1 + random.randint(1, 5), self.y1 + random.randint(1, 5)

    def descricao(self):
        largura = abs(self.x2 - self.x1)
        altura = abs(self.y2 - self.y1)
        perimetro = 2 * (largura + altura)
        area = largura * altura
        return (f'Retângulo com vértices em ({self.x1}, {self.y1}), ({self.x2}, {self.y1}), ({self.x2}, {self.y2}), ({self.x1}, {self.y2}), '
                f'largura: {largura}, altura: {altura}, perímetro: {perimetro}, área: {area}')

class Quadrado(Retangulo):
    def __init__(self):
        super().__init__()
        self.tipo = 'Quadrado'
        self.x2, self.y2 = self.x1 + (self.x2 - self.x1), self.y1 + (self.x2 - self.x1)

    def descricao(self):
        lado = abs(self.x2 - self.x1)
        perimetro = 4 * lado
        area = lado * lado
        return (f'Quadrado com vértices em ({self.x1}, {self.y1}), ({self.x2}, {self.y1}), ({self.x2}, {self.y2}), ({self.x1}, {self.y2}), '
                f'lado: {lado}, perímetro: {perimetro}, área: {area}')

class Plano:
    def __init__(self):
        self.formas = []

    def adicionar_forma(self, forma):
        self.formas.append(forma)

    def remover_forma_aleatoria(self):
        if self.formas:
            forma_removida = self.formas.pop(random.randint(0, len(self.formas) - 1))
            return forma_removida.descricao()
        return None

    def listar_formas(self):
        if not self.formas:
            return "Atualmente o plano está vazio."
        return "\n".join([f"{idx + 1}. {forma.descricao()}" for idx, forma in enumerate(self.formas)])

def main():
    plano = Plano()
    while True:
        print("\nMenu:")
        print("1. Gerar uma figura")
        print("2. Excluir uma figura aleatória do plano")
        print("3. Encerrar o programa")
        print(" ")
        opcao = input("Escolha uma opção: ")
        print(" ")
        if opcao == "1":
            tipo_figura = random.choice([SegmentoReta, Triangulo, Circulo, Retangulo, Quadrado])
            figura = tipo_figura()
            plano.adicionar_forma(figura)
            print("Figura criada:")
            print(figura.descricao())
        elif opcao == "2":
            descricao = plano.remover_forma_aleatoria()
            if descricao:
                print("Figura removida:")
                print(descricao)
            else:
                print("Atualmente o plano está vazio.")
            print("Figuras restantes no plano:")
            print(plano.listar_formas())
        elif opcao == "3":
            print("Programa encerrado.")
            break
        else:
            print("Comando inválido, tente novamente.")

if __name__ == "__main__":
    main()

