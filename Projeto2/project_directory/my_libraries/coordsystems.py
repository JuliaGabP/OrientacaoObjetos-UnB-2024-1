from my_libraries.shapes2d import *

class CartesianBoard:
    def __init__(self):
        self.formas = []

    def criar_forma(self, tipo):
        if tipo == 'Quadrado':
            forma = Quadrado()
        elif tipo == 'Retangulo':
            forma = Retangulo()
        elif tipo == 'Circulo':
            forma = Circulo()
        elif tipo == 'Triangulo':
            forma = Triangulo()
        elif tipo == 'SegmentoReta':
            forma = SegmentoReta()
        self.formas.append(forma)

    def remover_forma_aleatoria(self):
        if self.formas:
            self.formas.pop(random.randint(0, len(self.formas) - 1))
            return True
        return False

    def obter_duas_formas_aleatorias(self):
        return random.sample(self.formas, 2)

    def calcular_distancia(self, forma1, forma2):
        if isinstance(forma1, Circulo):
            ponto1 = forma1.centro
        elif isinstance(forma1, (Quadrado, Retangulo)):
            ponto1 = Ponto((forma1.x1 + forma1.x2) / 2, (forma1.y1 + forma1.y2) / 2)
        elif isinstance(forma1, Triangulo):
            ponto1 = Ponto((forma1.p1.x + forma1.p2.x + forma1.p3.x) / 3, (forma1.p1.y + forma1.p2.y + forma1.p3.y) / 3)
        elif isinstance(forma1, SegmentoReta):
            ponto1 = Ponto((forma1.ponto_inicial.x + forma1.ponto_final.x) / 2, (forma1.ponto_inicial.y + forma1.ponto_final.y) / 2)

        if isinstance(forma2, Circulo):
            ponto2 = forma2.centro
        elif isinstance(forma2, (Quadrado, Retangulo)):
            ponto2 = Ponto((forma2.x1 + forma2.x2) / 2, (forma2.y1 + forma2.y2) / 2)
        elif isinstance(forma2, Triangulo):
            ponto2 = Ponto((forma2.p1.x + forma2.p2.x + forma2.p3.x) / 3, (forma2.p1.y + forma2.p2.y + forma2.p3.y) / 3)
        elif isinstance(forma2, SegmentoReta):
            ponto2 = Ponto((forma2.ponto_inicial.x + forma2.ponto_final.x) / 2, (forma2.ponto_inicial.y + forma2.ponto_final.y) / 2)

        return math.dist((ponto1.x, ponto1.y), (ponto2.x, ponto2.y))

    def showShapes(self):
        print('\nEste plano cartesiano possui as seguintes formas:\n')
        for forma in self.formas:
            print(forma.descricao())

    def printDetails(self):
        for forma in self.formas:
            print(forma.descricao())

            
