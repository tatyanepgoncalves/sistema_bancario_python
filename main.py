from src.services.bank_services import (
    criar_cliente,
    criar_conta,
    depositar,
    exibir_extrato,
    listar_contas,
    sacar,
)
from src.ui.menu import menu


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
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Saindo do sistema...")
            break

        else:
            print("\n@@@ Operação inválida. @@@")


if __name__ == "__main__":
    main()
