import time

# Código sem estrutura de dados eficiente (busca em lista desordenada - O(n))
def busca_ineficiente(lista, valor):
    for item in lista:
        if item == valor:
            return True
    return False

# Código otimizado com conjunto (Hash Set - O(1) no melhor caso)
def busca_otimizada(conjunto, valor):
    return valor in conjunto

# Criando uma grande lista e conjunto com números de 1 a 1 milhão
dados_lista = list(range(1, 1000001))
dados_conjunto = set(dados_lista)

valor_procurado = 999999

# Teste de desempenho - Lista
inicio = time.time()
busca_ineficiente(dados_lista, valor_procurado)
fim = time.time()
print(f"Tempo de busca na lista: {fim - inicio:.6f} segundos")

# Teste de desempenho - Conjunto
inicio = time.time()
busca_otimizada(dados_conjunto, valor_procurado)
fim = time.time()
print(f"Tempo de busca no conjunto: {fim - inicio:.6f} segundos")




