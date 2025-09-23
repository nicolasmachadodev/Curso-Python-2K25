# Cheatsheet: Funções com argumentos nomeados

- Permite passar argumentos pelo nome ao chamar a função.
- Exemplo:
  def saudacao(nome, mensagem):
      print(f"{mensagem}, {nome}!")
  saudacao(mensagem="Olá", nome="Nicolas")
- Pode misturar argumentos posicionais e nomeados.
- Útil para deixar o código mais claro e flexível.
