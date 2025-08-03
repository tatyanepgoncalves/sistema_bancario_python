menu = """

  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair

"""


account_balance = 0 
account_limit = 500
account_statement = ""
number_of_withdrawals = 0
WITHDRAWAL_LIMIT = 3

while True:
  option = input(menu)

  if option == "d":
    value = float(input("Informe o valor do depósito: "))

    if value > 0:
      account_balance += value
      account_statement += f"Depósito: R$ {value:.2f}\n"

    else:
      print("Operação falhou! O valor informado é inválido.")

  elif option == "s":
    value = float(print("Informe o valor do saque: "))

    exceeded_balance = value > account_balance
    exceeded_limit = value > account_limit
    exceeded_withdrawal = number_of_withdrawals >= WITHDRAWAL_LIMIT

    if exceeded_balance:
      print("Operação falhou! Você não tem saldo suficiente.")

    elif exceeded_limit:
      print("Operação falhou! Número máximo de saques excedido.")
    
    elif value > 0:
      account_balance -= value
      account_statement += f"Saque: R$ {value:.2f}"
      number_of_withdrawals += 1

    else:
      print("Operação falhou! O valor informado é inválido.")
  elif option == "e":
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not account_statement else account_statement)
    print(f"\nSaldo: R$ {value:.2f}")
    print("==========================================")

  elif option == "q":
    break

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")