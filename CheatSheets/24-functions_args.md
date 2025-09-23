# Cheatsheet: Funções com argumentos (*args, **kwargs)

- def funcao(*args): permite receber vários argumentos posicionais como uma tupla.
- def funcao(**kwargs): permite receber vários argumentos nomeados como um dicionário.
- *args: use quando não sabe quantos argumentos serão passados.
- **kwargs: use quando não sabe quantos argumentos nomeados serão passados.
- Exemplo:
  def soma(*args):
      return sum(args)
  def mostrar(**kwargs):
      for chave, valor in kwargs.items():
          print(chave, valor)
- Pode combinar argumentos normais, *args e **kwargs na mesma função.
