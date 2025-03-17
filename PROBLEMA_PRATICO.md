# 📌 Problema Prático: Gerenciamento de Chamados de Suporte Técnico

## 🔹 Descrição do Problema
Em um setor de suporte técnico, os chamados dos clientes devem ser atendidos na ordem em que chegam, garantindo um atendimento justo e organizado. Para isso, é necessário um sistema que registre os chamados e processe cada um conforme a ordem de chegada.

## 🚀 Solução Utilizando Filas
A estrutura de **fila (Queue)** é a mais adequada para esse caso, pois segue o princípio **FIFO (First In, First Out)**, ou seja, o primeiro chamado inserido será o primeiro a ser processado.

### ✅ Como Funciona:
1. Novos chamados são adicionados ao final da fila.
2. O atendimento ocorre removendo o chamado do início da fila.
3. O sistema pode exibir a fila atual para acompanhamento.

A seguir nesta pasta, um código implementando essa solução em Python.
