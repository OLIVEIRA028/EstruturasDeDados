from collections import deque

class SuporteTecnico:
    def __init__(self):
        self.fila = deque()

    def adicionar_chamado(self, descricao):
        self.fila.append(descricao)
        print(f"Chamado adicionado: {descricao}")

    def atender_chamado(self):
        if self.fila:
            chamado = self.fila.popleft()
            print(f"Atendendo chamado: {chamado}")
        else:
            print("Nenhum chamado na fila.")

    def visualizar_fila(self):
        print("Chamados na fila:", list(self.fila))

# Exemplo de uso
suporte = SuporteTecnico()
suporte.adicionar_chamado("Problema de conexão")
suporte.adicionar_chamado("Erro no sistema")
suporte.visualizar_fila()
suporte.atender_chamado()
suporte.visualizar_fila()
