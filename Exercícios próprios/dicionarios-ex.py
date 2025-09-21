# 1. Crie um dicionário chamado 'livro' com as seguintes chaves: 'titulo', 'autor', 'ano' e 'preco'. Preencha com valores fictícios e imprima o dicionário.

livro = {
    'titulo': 'Aprendendo Python',
    'autor': 'Nicolas Eduardo',
    'ano': '2025',
    'price': 74.90
}
print(livro)

# 2. Acesse e imprima o valor da chave 'autor' do dicionário 'livro' usando tanto a notação de colchetes quanto o método .get().

print(livro['autor'])
print(livro.get('autor'))

# 3. Liste todas as chaves do dicionário 'livro'.

print(livro.keys())

# 4. Liste todos os valores do dicionário 'livro'.

print(livro.values())

# 5. Liste todos os itens (pares chave/valor) do dicionário 'livro'.

print(livro.items())

# 6. Adicione uma nova chave chamada 'editora' ao dicionário 'livro' e atribua um valor a ela.

livro['editora'] = 'OneBitCode'
print(livro)

# 7. Atualize o valor da chave 'preco' para um novo valor.

livro.update({'price': 59.90})
print(livro)

# 8. Remova a chave 'ano' do dicionário 'livro' usando o método apropriado.

livro.pop('ano')
print(livro)

# 9. Verifique se a chave 'editora' existe no dicionário.

print('editora' in livro)
