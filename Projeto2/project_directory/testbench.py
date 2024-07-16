from my_libraries.useropts import Menu

def workspace():
    menu = Menu()

    print("Iniciando o testbench...\n")

    # Criar múltiplas formas geométricas
    print("Criando formas geométricas...\n")
    for _ in range(5):
        menu.criar()
    print("Formas criadas no plano:")
    menu.dashboard.showShapes()

    # Excluir uma forma geométrica
    print("\nExcluindo uma forma geométrica...\n")
    menu.excluir()
    print("Formas restantes no plano:")
    menu.dashboard.showShapes()

    # Verificar interferências entre formas geométricas
    print("\nVerificando interferências...\n")
    menu.verificar_interferencias()

    print("\nTestbench concluído.")

if __name__ == "__main__":
    workspace()

