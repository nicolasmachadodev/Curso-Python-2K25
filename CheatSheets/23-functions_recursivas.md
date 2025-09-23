# Cheatsheet: Funções Recursivas

- Função recursiva chama a si mesma.
- Precisa de uma condição de parada (caso base).
- Exemplo clássico: fatorial.
- Exemplo:
  def fatorial(n):
      if n == 0:
          return 1
      else:
          return n * fatorial(n-1)
- Útil para problemas que podem ser divididos em subproblemas menores.
