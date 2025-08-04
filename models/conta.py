from .historico import Historico
from .transacao import Saque

class Conta:
  def __init__(self, numero, cliente, limite=500, limite_saques=50):
    self._saldo = 0
    self._numero = numero
    self._agencia = "0001"
    self._cliente = cliente
    self._limite = limite
    self._limite_saques = limite_saques
    self._historico = Historico()
  
  @classmethod
  def nova_conta(cls, cliente, numero, limite, limite_saques):
    return cls(numero, cliente, limite, limite_saques)
  
  def sacar(self, valor):
    if valor <= 0:
      print("Valor inválido.")
      return False

    if valor > self._saldo:
      print("Saldo insuficiente.")
      return False
    self._saldo -= valor
    print("Saque realizado com sucesso")
    return True

  def depositar(self, valor):
    if valor <= 0:
      print("Valor inválido.")
      return False
    self._saldo += valor
    print("Depósito realizado com sucesso")
    return True

  @property
  def saldo(self): return self._saldo

  @property
  def numero(self): return self._numero

  @property
  def agencia(self): return self._agencia
  
  @property
  def cliente(self): return self._cliente

  @property
  def historico(self): return self._historico
  

class ContaCorrente(Conta):
  def __init__(self, numero, cliente, limite=500, limite_saques=3):
    super().__init__(numero, cliente)
    self.limite = limite
    self.limite_saques = limite_saques
  
  def sacar(self, valor):
    numero_saques = len([
      t for t in self.historico.transacoes
      if t["tipo"] == Saque.__name__
    ])
    if valor > self._limite:
      print("Limite excedido.")
      return False 

    if numero_saques >= self._limite_saques:
      print("Limite de saques excedido.")
      return False
    return super().sacar(valor)

  def __str__(self):
    return f"""
        Agência:\t{self.agencia}
        C/C:\t{self.numero}
        Titular:\t{self.cliente.nome}
    """

