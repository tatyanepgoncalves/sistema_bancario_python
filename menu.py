import textwrap

def menu():
  return input(textwrap.dedent("""
  ================ MENU ================
  [d]  Depositar
  [s]  Sacar
  [e]  Extrato
  [nc] Nova conta
  [lc] Listar contas
  [nu] Novo usuário
  [q]  Sair
  => """))