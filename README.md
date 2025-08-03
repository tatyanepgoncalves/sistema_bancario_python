# 💰 Sistema Bancário em Python

Este é um projeto básico de um sistema bancário desenvolvido em Python, com funcionalidades essenciais como **depósito**, **saque**, **extrato** e **encerramento da aplicação**. Ele é totalmente interativo via terminal e utiliza estruturas de controle simples.

## 🔧 Funcionalidades Implementadas

- **Depósito**  
  Permite ao usuário adicionar fundos à conta, desde que o valor seja positivo.

- **Saque**  
  Realiza saques com base nas seguintes regras:
  - Limite máximo por saque: R$500,00
  - Máximo de 3 saques diários
  - Saques não podem ultrapassar o saldo disponível

- **Extrato**  
  Mostra o histórico de transações e o saldo atual da conta.

- **Sair**  
  Encerra a execução do sistema.

## 🧪 Exemplo de Uso

Ao iniciar o sistema, o seguinte menu é exibido:

````py
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

````

O usuário pode então escolher uma opção digitando a letra correspondente.

## ⚠️ Possíveis Melhorias Futuras

- Separação do código em funções ou classes (paradigma procedural → OO)
- Armazenamento persistente de dados (ex: SQLite ou arquivos JSON)
- Controle por CPF ou número da conta
- Interface gráfica com Tkinter ou web com Flask
- Autenticação de usuário
- Registro de data/hora nas transações
- Validação e tratamento de exceções mais robusto
- Testes automatizados

## ✅ Requisitos

- Python 3.x instalado
- Terminal para execução interativa

## 🚀 Como Executar

1. Clone o repositório e abra o arquivo:
```bash
   git clone https://github.com/tatyanepgoncalves/sistema_bancario_python.git
   cd sistema_bancario_python
```

2. Execute o script:
````bash
  python sistema_bancario.py
````


## 📝 Observações
Este projeto é um exercício inicial e está em constante evolução. O objetivo principal é praticar a lógica de programação e os fundamentos da linguagem Python.


Feito com 💻 por Tatyane — *Estudante de Sistemas de Informação e Desenvolvedora Full Stack*