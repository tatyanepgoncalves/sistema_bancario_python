# main.py
from menu import menu
from services.operacoes import (
    depositar, sacar, exibir_extrato, criar_cliente, criar_conta, listar_contas
)


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d": 
            depositar(clientes)
        elif opcao == "s": 
            sacar(clientes)
        elif opcao == "e": 
            exibir_extrato(clientes)
        elif opcao == "nu": 
            criar_cliente(clientes)
        elif opcao == "nc": 
            criar_conta(len(contas) + 1, clientes, contas)
        elif opcao == "lc": 
            listar_contas(contas)
        elif opcao == "q": 
            break
        else: 
            print("@@@ Opção inválida! @@@")

if __name__ == "__main__":
    main()
