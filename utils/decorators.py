from datetime import datetime

def log_transacao(func):
  def envelope(*args, **kwargs):
    resultado = func(*args, **kwargs)
    print(f"{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}: {func.__name__} executado.")
    return resultado

  return envelope