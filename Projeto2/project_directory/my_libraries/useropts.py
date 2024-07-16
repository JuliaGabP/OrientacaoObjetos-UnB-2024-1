from my_libraries.coordsystems import CartesianBoard
import random

class Menu:
    def __init__(self):
        self.dashboard = CartesianBoard()
        self.actions = {
            'criar': self.criar,
            'excluir': self.excluir,
            'verificar_interferencias': self.verificar_interferencias,
            'sair': exit
        }

    def criar(self):
        formas = ['Quadrado', 'Retangulo', 'Circulo', 'Triangulo', 'SegmentoReta']
        forma_escolhida = random.choice(formas)
        self.dashboard.criar_forma(forma_escolhida)
        nova_forma = self.dashboard.formas[-1]
        print(f'{forma_escolhida} criado e adicionado ao plano.\nDetalhes: {nova_forma.descricao()}\n')

    def excluir(self):
        if self.dashboard.formas:
            forma_excluida = random.choice(self.dashboard.formas)
            self.dashboard.formas.remove(forma_excluida)
            print(f'A forma excluída foi: {forma_excluida.descricao()}\n')
            if self.dashboard.formas:
                print('Formas restantes no plano:\n')
                for forma in self.dashboard.formas:
                    print(forma.descricao())
            else:
                print('Não há formas restantes no plano.\n')
        else:
            print('Não há formas no plano para excluir.\n')

    def verificar_interferencias(self):
        if len(self.dashboard.formas) == 0:
            print('Não há formas no plano.\n')
        elif len(self.dashboard.formas) == 1:
            print('Apenas uma forma no plano:')
            self.dashboard.showShapes()
        else:
            forma1, forma2 = self.dashboard.obter_duas_formas_aleatorias()
            distancia = self.dashboard.calcular_distancia(forma1, forma2)
            print(f'Distância entre {forma1.descricao()} e {forma2.descricao()}: {distancia:.2f}\n')

    def run(self):
        while True:
            print("Escolha uma das opções:")
            print("1. Criar forma geométrica aleatória; formas possíveis: quadrado, retângulo, círculo, segmento de reta e triângulo")
            print("2. Excluir forma geométrica aleatória")
            print("3. Verificar interferências entre formas geométricas")
            print("4. Sair")

            option = input("Digite o número da opção desejada: ")
            print("")

            if option.isdigit() and int(option) in range(1, 5):
                command = list(self.actions.keys())[int(option) - 1]
                self.actions[command]()
            else:
                print("Opção inválida! Tente novamente.")

