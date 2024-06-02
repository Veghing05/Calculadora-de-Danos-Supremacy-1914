class GerenciadorDeRecursos:
    def __init__(self, recursos_iniciais):
        self.recursos = recursos_iniciais
    
    def atualizar_recursos(self, alteracoes_recursos):
        for recurso, alteracao in alteracoes_recursos.items():
            self.recursos[recurso] += alteracao
    
    def verificar_custo_producao(self, custo_producao):
        for recurso, custo in custo_producao.items():
            if self.recursos.get(recurso, 0) < custo:
                return False
        return True
    
    def executar_producao(self, custo_producao):
        if self.verificar_custo_producao(custo_producao):
            for recurso, custo in custo_producao.items():
                self.recursos[recurso] -= custo
            return True
        else:
            print("Recursos insuficientes para executar a produção.")
            return False

    def __str__(self):
        return str(self.recursos)


class PlanejadorDeEstrategia:
    def __init__(self):
        self.fila_producao = []

    def adicionar_na_fila(self, item, custo_producao):
        self.fila_producao.append((item, custo_producao))

    def executar_fila(self, gerenciador_recursos):
        for item, custo_producao in self.fila_producao:
            if gerenciador_recursos.executar_producao(custo_producao):
                print(f"Produzido: {item}")
            else:
                print(f"Falha ao produzir: {item} devido a recursos insuficientes")
        self.fila_producao = []


def obter_recursos_iniciais():
    recursos = {}
    recursos['dinheiro'] = int(input("Digite a quantidade inicial de dinheiro: "))
    recursos['graos']= int(input("Digite a quantidade inicial de grãos: "))
    recursos['peixe'] = int(input("Digite a quantidade inicial de peixe: "))
    recursos['ferro'] = int(input("Digite a quantidade inicial de ferro: "))
    recursos['madeira'] = int(input("Digite a quantidade inicial de madeira: "))
    recursos['carvao'] = int(input("Digite a quantidade inicial de carvão: "))
    recursos['combustivel'] = int(input("Digite a quantidade inicial de combustivel: "))
    recursos['gas'] = int(input("Digite a quantidade inicial de gás: "))
    return recursos


def obter_renda_diaria():
    renda = {}
    renda['dinheiro'] = int(input("Digite a renda diária de dinheiro: "))
    renda['graos'] = int(input("Digite a renda diária de grãos: "))
    renda['peixe'] = int(input("Digite a renda diária de peixe: "))
    renda['ferro'] = int(input("Digite a renda diária de ferro: "))
    renda['madeira'] = int(input("Digite a renda diária de madeira: "))
    renda['carvao'] = int(input("Digite a renda diária de carvao: "))
    renda['combustivel'] = int(input("Digite a renda diária de combustivel: "))
    renda['gas'] = int(input("Digite a renda diária de gás: "))
    return renda


def obter_custo_unidades():
    custo_blindado= {'dinheiro': 8500,  'ferro': 200, 'combustivel': 1000}
    custo_cavalaria= {'dinheiro': 6000, 'graos': 1200, 'peixe': 1200}

    custo_artilharia = {'dinheiro': 10000, 'ferro': 3000, 'combustivel': 2000}
    custo_tanque = {'dinheiro': 20000, 'ferro': 5000, 'combustivel': 3000}
    custo_tanque_pesado = {'dinheiro': 30000, 'ferro': 7000, 'combustivel': 4000}

    custo_canhao_ferroviario= {'dinheiro': 50000, 'ferro': 10000, 'madeira': 5000, 'carvao': 5000, 'combustivel': 10000}

    custo_balao= {'dinheiro': 5000, 'madeira': 1000,'gas': 1000}
    custo_caca= {'dinheiro': 20000, 'ferro': 2500, 'madeira': 5000, 'combustivel': 10000}
    custo_bombardeiro= {'dinheiro': 50000, 'ferro': 5000, 'madeira': 7500, 'combustivel': 10000}

    custo_cruzador_leve= {'dinheiro': 15000, 'ferro': 3000, 'carvao': 2000, 'combustivel': 2000}
    custo_submarino= {'dinheiro': 20000, 'ferro': 3000, 'madeira': 2000,'combustivel': 3000}
    custo_navio_de_combate= {'dinheiro': 50000, 'ferro': 15000, 'madeira': 5000, 'carvao': 10000, 'combustivel': 5000}



    def obter_custo_constucoes():
        
    custo_fabrica = {'dinheiro': 10000, 'madeira': 2000, 'ferro': 1000}
    return {'Infantaria': custo_infantaria, 'Tanque': custo_tanque, 'Fábrica': custo_fabrica}


def main():
    recursos_iniciais = obter_recursos_iniciais()
    gerenciador_recursos = GerenciadorDeRecursos(recursos_iniciais)
    
    custos_unidades = obter_custo_unidades()
    planejador_estrategia = PlanejadorDeEstrategia()
    
    while True:
        print("\n1. Adicionar produção à fila")
        print("2. Atualizar recursos com renda diária")
        print("3. Executar fila de produções")
        print("4. Mostrar recursos restantes")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            item = input("Digite o nome do item para produzir (Infantaria, Tanque, Fábrica): ")
            if item in custos_unidades:
                planejador_estrategia.adicionar_na_fila(item, custos_unidades[item])
            else:
                print("Item inválido.")
        elif escolha == '2':
            renda_diaria = obter_renda_diaria()
            gerenciador_recursos.atualizar_recursos(renda_diaria)
        elif escolha == '3':
            planejador_estrategia.executar_fila(gerenciador_recursos)
        elif escolha == '4':
            print("Recursos restantes:")
            print(gerenciador_recursos)
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
