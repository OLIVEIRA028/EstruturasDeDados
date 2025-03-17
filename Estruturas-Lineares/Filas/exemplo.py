from collections import deque

# Criando uma fila
fila = deque()

# Enfileirando elementos
fila.append("A")
fila.append("B")
fila.append("C")

# Desenfileirando elementos
primeiro = fila.popleft()

# Estado final da fila
print("Fila após remoção:", list(fila))
print("Elemento removido:", primeiro)

