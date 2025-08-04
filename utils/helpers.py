def filtrar_cliente(cpf, clientes):
  clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
  return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
  if not cliente.contas:
    print("\n@@@ Cliente não possui conta! @@@")
    return
  
  # FIXME: não permite cliente escolher a conta
  return cliente.contas[0]
