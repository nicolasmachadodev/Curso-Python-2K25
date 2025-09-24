# Cheatsheet: Módulos em Python

- Módulo é um arquivo .py que pode ser importado em outros arquivos.
- Para importar um módulo: import nome_modulo
- Para importar funções específicas: from nome_modulo import funcao
- Exemplo:
  import calc
  from calc import div
- Para usar funções do módulo: nome_modulo.funcao()
- Módulos ajudam a organizar o código e reutilizar funções.
- Exemplo de funções em módulo:
  def sum(a, b): return a + b
  def div(a, b): return a / b
- Se quiser evitar erro de divisão por zero, use if/else dentro da função.
