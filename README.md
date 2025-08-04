# 🏦 Sistema Bancário com Programação Orientada a Objetos (POO) em Python

Este é um sistema bancário desenvolvido em Python utilizando os princípios da **Programação Orientada a Objetos**. Ele simula operações bancárias básicas como **depósitos**, **saques**, **emissão de extrato**, além de **cadastro de clientes** e **criação de contas**.  

A estrutura orientada a objetos permite maior organização, reutilização e escalabilidade do código.


---

## 🚀 Funcionalidades

### 🧾 Transações
- **Depósito**  
  - Valida valor positivo
  - Atualiza saldo
  - Registra no histórico


- **Saque**  
  - Limite de 3 saques por conta
  - Limite de R$500 por saque
  - Registra no histórico
  - Valida saldo e regras antes da operação

- **Extrato**  
  - Exibe todas as transações realizadas por uma conta
  - Exibe saldo atual

---
### 👤 Cliente

- Cadastro de **Pessoa Física** com:
  - Nome completo
  - CPF (único por cliente)
  - Data de nascimento
  - Endereço

- Cada cliente pode ter múltiplas contas.

---

### 🏦 Conta

- **Conta Corrente** com:
  - Agência (`0001`)
  - Número da conta
  - Cliente titular
  - Limite de saque
  - Histórico de transações

- As transações são armazenadas com:
  - Tipo (`Saque` ou `Depósito`)
  - Valor
  - Data e hora da operação

---

## 📋  Menu do Sistema

Ao executar o programa, o menu abaixo será exibido:

````py
==================== MENU ==================
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [nc] Nova conta
  [lc] Listar conta
  [nu] Novo usuário
  [q] Sair
=>
````
---

## 🧱 Arquitetura do Código

- `Cliente`: classe base com composição de contas
- `PessoaFisica`: herda de `Cliente`
- `Conta`: classe abstrata base para contas bancárias
- `ContaCorrente`: herda de `Conta`, com regras específicas
- `Transacao`: classe abstrata para operações
  - `Deposito` e `Saque` herdam de `Transacao`
- `Historico`: registra todas as transações da conta

---

## 💡 Padrões e Princípios Utilizados

- Programação Orientada a Objetos (POO)
- Abstração com classes base e métodos abstratos (`abc`)
- Encapsulamento com atributos privados
- Coesão: cada classe tem uma única responsabilidade
- Acoplamento reduzido entre cliente e conta
- Separação clara entre entrada de dados e lógica de negócio

---

## 📚 Requisitos

- Python 3.8 ou superior
- Executar em terminal (CLI)

---


## 🚀 Como Executar

1. Salve o código em um arquivo:  
   `sistema_bancario.py`

2. No terminal, execute:

````bash
  python sistema_bancario.py
````


## 🧭 Melhorias Futuras
- Persistência de dados com SQLite ou JSON
- Interface gráfica com Tkinter ou web com Flask/Django
- Autenticação de clientes com senha
- Suporte a contas empresariais ou investimentos
- Relatórios mensais de movimentações
- Escolha de múltiplas contas por cliente


## 📝 Observações
Este projeto é um exercício inicial e está em constante evolução. O objetivo principal é praticar a lógica de programação e os fundamentos da linguagem Python.

Feito com 💻 por Tatyane — *Estudante de Sistemas de Informação e Desenvolvedora Full Stack*