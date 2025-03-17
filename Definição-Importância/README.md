### 📌 **Estruturas de Dados Lineares vs. Não Lineares**  

#### ✅ **Estruturas de Dados Lineares**  
- Os elementos são organizados de maneira **sequencial** ou **contínua**.  
- Cada elemento tem um único sucessor e um único antecessor (exceto os extremos).  
- **Exemplos**:  
  - **Arrays (Vetores e Matrizes)**  
  - **Listas Ligadas (Encadeadas, Duplamente Encadeadas)**  
  - **Pilhas (Stacks)**  
  - **Filas (Queues)**  

**📌 Aplicação:** Uso ideal quando os dados precisam ser percorridos sequencialmente, como em buffers de teclado ou filas de impressão.

---

#### ✅ **Estruturas de Dados Não Lineares**  
- Os elementos **não seguem uma sequência fixa** e podem estar organizados hierarquicamente ou de forma interconectada.  
- **Exemplos**:  
  - **Árvores (Tree, Binary Search Tree - BST)**  
  - **Grafos (Graph, Weighted Graphs, Directed Graphs)**  
  - **Tabelas Hash (Hash Table ou HashMap)**  

**📌 Aplicação:** Usadas quando há relações complexas entre os dados, como em sistemas de arquivos ou redes sociais.

---

### 🚀 **Impacto das Estruturas de Dados no Desempenho de um Programa**  
- **Uso correto** de estruturas melhora **eficiência** e reduz o consumo de recursos.  
- Escolher **a estrutura errada** pode tornar um programa ineficiente e lento.  
- Exemplo prático:  
  - **Sem estrutura eficiente** → Busca em uma lista não ordenada pode levar **O(n)**.  
  - **Com estrutura eficiente (árvore balanceada, hash table)** → Pode reduzir para **O(log n)** ou **O(1)**.  

---


O código dentro dessa pasta compara a busca ineficiente em uma **lista desordenada** (`O(n)`) com a busca otimizada usando um **conjunto (Hash Set, O(1) no melhor caso)**. Isso demonstra como a escolha correta da estrutura de dados pode melhorar drasticamente o desempenho de um programa. 🚀
