# main.py
from menu import menu
from models.conta import ContaCorrente
from models.transacao import Deposito, Saque
from models.cliente import PessoaFisica
from utils.helpers import filtrar_cliente, recuperar_conta_cliente

clientes = []
contas = []

def depositar():
    cpf = input("Informe o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente: return print("@@@ Cliente não encontrado! @@@")

    conta = recuperar_conta_cliente(cliente)
    if not conta: return

    valor = float(input("Valor do depósito: "))
    transacao = Deposito(valor)
    cliente.realizar_transacao(conta, transacao)

def sacar():
    cpf = input("Informe o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente: return print("@@@ Cliente não encontrado! @@@")

    conta = recuperar_conta_cliente(cliente)
    if not conta: return

    valor = float(input("Valor do saque: "))
    transacao = Saque(valor)
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato():
    cpf = input("Informe o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente: return print("@@@ Cliente não encontrado! @@@")

    conta = recuperar_conta_cliente(cliente)
    if not conta: return

    print("\n========= EXTRATO =========")
    for t in conta.historico.transacoes:
        print(f"{t['tipo']}: R$ {t['valor']:.2f} em {t['data']}")
    print(f"Saldo: R$ {conta.saldo:.2f}")
    print("===========================")

def criar_cliente():
    cpf = input("CPF: ")
    if filtrar_cliente(cpf, clientes):
        return print("@@@ CPF já cadastrado! @@@")

    nome = input("Nome: ")
    nasc = input("Nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço: ")

    cliente = PessoaFisica(nome, nasc, cpf, endereco)
    clientes.append(cliente)
    print("=== Cliente criado ===")

def criar_conta():
    cpf = input("CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente: return print("@@@ Cliente não encontrado! @@@")

    numero = len(contas) + 1
    conta = ContaCorrente.nova_conta(cliente, numero)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print("=== Conta criada ===")

def listar_contas():
    for conta in contas:
        print("=" * 60)
        print(conta)

def main():
    while True:
        opcao = menu()

        if opcao == "d": depositar()
        elif opcao == "s": sacar()
        elif opcao == "e": exibir_extrato()
        elif opcao == "nu": criar_cliente()
        elif opcao == "nc": criar_conta()
        elif opcao == "lc": listar_contas()
        elif opcao == "q": break
        else: print("@@@ Opção inválida! @@@")

if __name__ == "__main__":
    main()
