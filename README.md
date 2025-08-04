# 🏦 Sistema Bancário com Programação Orientada a Objetos (POO) em Python

Este é um sistema bancário desenvolvido em Python utilizando os princípios da **Programação Orientada a Objetos**. Ele simula operações bancárias básicas como **depósitos**, **saques**, **emissão de extrato**, além de **cadastro de clientes** e **criação de contas**.  

A estrutura orientada a objetos permite maior organização, reutilização e escalabilidade do código.

---

````bash
sistema_bancario_python/
│   
├── main.py # Ponto de entrada da aplicação
├── models/ # Definições de classes principais
│   ├── __init__.py
│   ├── conta.py # Conta e ContaCorrente
│   ├── cliente.py # Cliente e PessoaFisica
│   ├── historico.py # Histórico de transações
│   ├── contaIterador.py # Iterador para listagem de contas
│   └── transacao.py # Transações abstratas e concretas
│
├── services/  # Operações (casos de uso)
│   ├── __init__.py
│   └── operacoes.py # Depósito, saque, extrato, criar cliente/conta
│   
├── utils/
│   ├── __init__.py
│   ├── decorators.py # Logs e utilidades
│   ├── helpers.py
│   └── menu.py # Menu interativo
│   
├── main.py
└── README.md
````


---

## ⚙️ Funcionalidades

- ✅ Cadastro de clientes (Pessoa Física)
- ✅ Abertura de conta corrente com limite de saque
- ✅ Realização de **depósitos** e **saques**
- ✅ Geração de **extrato**
- ✅ Listagem de contas existentes
- ✅ Registro de transações com data e hora
- ✅ Validações como limite de saque, número de saques e saldo



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

1. Clone o repositório:
````bash
  git clone https://github.com/tatyanepgoncalves/sistema_bancario_python.git
  cd sistema_bancario_python
````

2. (Opcional) Crie um ambiente virtual:
````bash
  python -m venv venv
  source venv/bin/activate  # Linux/macOS
  venv\Scripts\activate     # Windows

````

3. No terminal, execute:

````bash
  python sistema_bancario.py
````


## 🧭 Melhorias Futuras
- Persistência com banco de dados ou arquivos JSON
- Interface gráfica (GUI ou Web)
- Autenticação de usuários
- Tipagem estática e testes automatizados

## 🧠 Conceitos Aplicados
- Programação orientada a objetos
- Princípios de design (abstração, encapsulamento, herança)
- Iteradores personalizados
- Decoração de funções (log de operações)
- Organização modular de código

## 📝 Observações
Este projeto é um exercício inicial e está em constante evolução. O objetivo principal é praticar a lógica de programação e os fundamentos da linguagem Python.

## 📝 Licença
Este projeto está sob a licença MIT.

Feito com 💻 por Tatyane — *Estudante de Sistemas de Informação e Desenvolvedora Full Stack*