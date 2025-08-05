# Sistema Bancário em Python

Este é um projeto simples de um sistema bancário desenvolvido em Python. Ele foi criado com o objetivo de demonstrar a aplicação de conceitos de **Programação Orientada a Objetos (POO)**, como herança, abstração, polimorfismo e encapsulamento, além de boas práticas de desenvolvimento como a criação de funções de menu, classes e manipulação de arquivos (simulada em memória).

O sistema permite a gestão de clientes e contas correntes, com funcionalidades básicas de depósito, saque e visualização de extrato.

## Funcionalidades Principais

* **Criação de Clientes**: Cadastro de novos clientes (Pessoa Física).
* **Criação de Contas**: Associação de contas correntes a um cliente existente.
* **Depósito**: Realiza depósitos em uma conta, com a verificação de valores válidos.
* **Saque**: Efetua saques de uma conta, respeitando um limite de valor por saque e um número máximo de saques diários.
* **Extrato**: Exibe o histórico de todas as transações (depósitos e saques) realizadas na conta, incluindo o saldo atual.
* **Listar Contas**: Mostra todas as contas cadastradas com os detalhes do cliente.

## Estrutura do Código 

O projeto é organizado em classes para representar as entidades do sistema:

* `Cliente`: Classe base para clientes.
* `PessoaFisica`: Subclasse de `Cliente` para representar clientes pessoa física.
* `Conta`: Classe base para contas bancárias.
* `ContaCorrente`: Subclasse de `Conta` com regras específicas de limite de saque e número de saques.
* `Historico`: Gerencia o histórico de transações de uma conta.
* `Transacao`, `Saque`, `Deposito`: Classes abstratas e concretas para definir o comportamento das transações.
* `ContasIterador`: Classe que implementa o protocolo de iteração para exibir as contas.
* **Funções de Apoio**: Funções como `menu`, `filtrar_cliente`, `recuperar_conta_cliente`, etc., que organizam a lógica de interação com o usuário.
* **Decoradores**: O decorador `@log_transacao` foi implementado para demonstrar o registro de operações, adicionando um carimbo de data e hora a cada transação.

## Como Executar o Projeto
1.  **Pré-requisitos**: Certifique-se de ter o Python instalado (versão 3.6 ou superior).

2. **Clone o repositório**:
````bash
  git clone https://github.com/tatyanepgoncalves/sistema_bancario_python.git
````

3. **Executar o Script**:
    Navegue até o diretório do projeto e execute o arquivo principal:
````bash
  cd sistema_bancario_python
````

## Tecnologias Utilizadas

* **Python**: Linguagem de programação principal.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* para relatar bugs ou sugerir novas funcionalidades, ou enviar um *pull request* com suas melhorias.

## Licença

Este projeto está licenciado sob a licença [MIT](https://opensource.org/licenses/MIT)
