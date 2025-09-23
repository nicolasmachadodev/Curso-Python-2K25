# Cheatsheet: Função Lambda (Aula 25)

- Função lambda é uma função anônima, definida em uma linha.
- Sintaxe: lambda argumentos: expressão
- Exemplo: soma = lambda x, y: x + y
- Pode ser usada para funções simples, geralmente como argumento de outras funções (ex: sorted, map, filter).
- Exemplo de uso:
  numeros = [1, 2, 3, 4]
  dobrados = list(map(lambda x: x * 2, numeros))
- Não substitui funções normais para lógicas complexas.
- Útil para operações rápidas e simples.
