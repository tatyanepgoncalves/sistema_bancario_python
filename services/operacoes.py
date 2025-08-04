from models.transacao import Deposito, Saque
from models.conta import ContaCorrente
from models.cliente import PessoaFisica
from utils.decorators import log_transacao

def filtrar_cliente(cpf, clientes):
  return next((c for c in clientes if c.cpf == cpf), None)

def recuperar_conta_cliente(cliente):
  if not cliente.contas:
    print("Cliente não possui conta.")
    return
  return cliente.contas[0] # FIXME: permite escolha de conta

@log_transacao
def depositar(clientes):
  cpf = input("CPF: ")
  cliente = filtrar_cliente(cpf, clientes)
  if not cliente:
    print("Cliente não encontrado.")
    return
  valor = float(input("Valor: "))
  conta = recuperar_conta_cliente(cliente)
  if conta:
    cliente.realizar_transacao(conta, Deposito(valor))

@log_transacao
def sacar(clientes):
    cpf = input("CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado.")
        return
    valor = float(input("Valor: "))
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, Saque(valor))
@log_transacao
def exibir_extrato(clientes):
    cpf = input("CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    conta = recuperar_conta_cliente(cliente)
    if conta:
        print("\n=========== EXTRATO ===========")
        for t in conta.historico.gerar_relatorio():
            print(f"{t['tipo']}: R$ {t['valor']:.2f} ({t['data']})")
        print(f"\nSaldo: R$ {conta.saldo:.2f}")
        print("=" * 30)


@log_transacao
def criar_cliente(clientes):
    cpf = input("CPF: ")
    if filtrar_cliente(cpf, clientes):
        print("Cliente já existe.")
        return
    nome = input("Nome do cliente: ")
    nasc = input("Nascimento do cliente (dd-mm-aaaa): ")
    endereco = input("Endereço do cliente: ")
    clientes.append(PessoaFisica(nome, nasc, cpf, endereco))
    print("Cliente criado com sucesso.")


@log_transacao
def criar_conta(numero, clientes, contas):
    cpf = input("CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
    
    # NOTE: O valor padrão de limite de saques foi alterado para 50 saques
    conta = ContaCorrente.nova_conta(
       cliente=cliente, 
       numero=numero,
       limite=500,
       limite_saques=50
    )
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print("Conta criada com sucesso.")



def listar_contas(contas):
    for conta in contas:
        print("=" * 50)
        print(conta)