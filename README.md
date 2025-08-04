# 💰 Sistema Bancário em Python

Este projeto é uma simulação de um sistema bancário desenvolvido em Python, com o objetivo de praticar conceitos de lógica de programação, modularização e uso de funções. Agora o sistema está mais organizado, utilizando funções para cada operação, e com suporte a múltiplos usuários e contas.

---

## 🔧 Funcionalidades Implementadas

- **Depósito**  
  - Adiciona um valor positivo ao saldo da conta.
  - Registra o valor no extrato

- **Saque**  
  Realiza saques com base nas seguintes regras:
  - Limite máximo por saque: R$500,00
  - Máximo de 3 saques diários
  - Saques não podem ultrapassar o saldo disponível
  - Saques são registrados no extrato
  - Valida saldo, limite por saque e quantidade de saques

- **Extrato**  
  - Exibe todas as movimentações realizadas na conta (depósitos e saques).
  - Exibe o saldo atual.

-  **Criar usuário (`nu`)**
  - Cadastro de novo usuário com nome, cpf, data de nascimento e endereço
  - Impede duplicação de usuários com o mesmo CPF

-  **Criar conta (`nc`)**
  - Criação de uma conta bancária vinculada a um usuário existente
  - Cada conta é composta por número, agência e usuário titular

- **Listar Contas (`lc`)**
  - Lista todas as contas cadastradas com seus dados principais.

- **Sair**  
  Encerra a execução do sistema.

## 📋 Menu Interativo

Ao executar o programa, o menu abaixo será exibido:

````py
==================== MENU ==================
  [d]\tDepositar
  [s]\tSacar
  [e]\tExtrato
  [nc]\tNova conta
  [lc]\tListar conta
  [nu]\tNovo usuário
  [q]\tSair
=>
````

O usuário pode então escolher uma opção digitando a letra correspondente.

## 🚀 Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Salve o código em um arquivo chamado, por exemplo, `sistema_bancario.py`.
3. No terminal, execute o arquivo com:

````bash
  python sistema_bancario.py
````

## 🧠 Conceitos Praticados
- Parâmetros posicionais e nomeados (/, *)
- Modularização do código
- Manipulação de listas e dicionários
- Programação procedural
- Validação de entrada de dados

## 🛣️ Melhorias Futuras

- Armazenamento persistente (JSON, SQLite)
- Interface com autenticação por senha
- Identificação e login de usuários
- Registro de data/hora das operações
- Refatoração para Programação Orientada a Objetos
- Testes unitários com ``unittest`` ou ``pytest``

## ✅ Requisitos

- Python 3.8 ou superior
- Terminal para execução interativa


## 📝 Observações
Este projeto é um exercício inicial e está em constante evolução. O objetivo principal é praticar a lógica de programação e os fundamentos da linguagem Python.


Feito com 💻 por Tatyane — *Estudante de Sistemas de Informação e Desenvolvedora Full Stack*