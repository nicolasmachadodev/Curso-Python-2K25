"""
🛒 MEGA DESAFIO PYTHON – Sistema de Loja Virtual no Terminal

🎯 OBJETIVO:
Criar um sistema completo de loja virtual com clientes, estoque, carrinho de compras, vendas, backup e logs de ações.

--------------------------------------------------------------

✅ FUNCIONALIDADES OBRIGATÓRIAS:

1️⃣ Login e Cadastro de Usuário
   - Usuário escolhe: 1) Login  2) Criar conta
   - Campos do cadastro: nome, email, senha e tipo ("cliente" ou "admin")
   - Dados salvos em 'usuarios.pkl'
   - Apenas administradores podem acessar o menu de estoque e vendas

2️⃣ Gerenciar Produtos (apenas ADMIN)
   - Cadastrar produto: nome, categoria, preço e quantidade em estoque
   - Editar produto: alterar preço ou quantidade
   - Excluir produto
   - Salvar todos os produtos em 'produtos.pkl'
   - Estrutura exemplo:
     produto = {
       "nome": "Whey Protein",
       "categoria": "Suplemento",
       "preco": 119.90,
       "estoque": 10
     }

3️⃣ Carrinho de Compras (CLIENTE)
   - Visualizar produtos disponíveis
   - Adicionar produto ao carrinho (apenas se houver estoque)
   - Remover produto do carrinho
   - Mostrar total do carrinho em tempo real
   - Finalizar compra:
     • Desconta do estoque
     • Gera venda com data, total e forma de pagamento (Pix, Cartão ou Dinheiro)
     • Salva em 'vendas.pkl'

4️⃣ Histórico de Vendas (ADMIN)
   - Mostrar todas as vendas registradas
   - Estrutura exemplo:
     venda = {
       "cliente": "João Silva",
       "itens": [{"nome": "Whey", "qtd": 2, "preco": 119.90}],
       "total": 239.80,
       "pagamento": "Pix",
       "data": "24/10/2025 14:32"
     }

5️⃣ Relatórios (ADMIN)
   - Mostrar produtos com estoque baixo (menor que 5 unidades)
   - Mostrar total de vendas (por dia, mês ou geral)
   - Produto mais vendido
   - Cliente que mais gastou

6️⃣ Logs de Ações
   - Criar arquivo 'logs.txt'
   - Registrar todas as ações importantes com data e hora:
     • Login, logout
     • Cadastro de usuário
     • Cadastro, edição e exclusão de produto
     • Compra realizada
   - Opção no menu: 1) Mostrar logs   2) Apagar logs

7️⃣ Backup Automático
   - Ao sair do programa, salvar todos os dados (usuarios, produtos, vendas) em 'backup.pkl'
   - No menu: opção para restaurar backup anterior

--------------------------------------------------------------

💾 ARQUIVOS UTILIZADOS (com pickle):

- usuarios.pkl  → lista/dicionário de usuários
- produtos.pkl  → todos os produtos cadastrados
- vendas.pkl    → histórico de compras finalizadas
- backup.pkl    → cópia de segurança de TUDO
- logs.txt      → registro de ações com data e hora

--------------------------------------------------------------

📦 ESTRUTURA SUGERIDA DE FUNÇÕES:

- carregar_usuarios()
- salvar_usuarios()
- carregar_produtos()
- salvar_produtos()
- carregar_vendas()
- salvar_vendas()
- registrar_log(acao)
- backup()
- restaurar_backup()
- menu_login()
- menu_cliente()
- menu_admin()
- cadastrar_usuario()
- login()
- cadastrar_produto()
- editar_produto()
- excluir_produto()
- mostrar_produtos()
- adicionar_ao_carrinho()
- remover_do_carrinho()
- finalizar_compra()
- mostrar_relatorios()
- mostrar_logs()
- apagar_logs()

--------------------------------------------------------------

💡 DICAS:
- Use try/except para evitar erros ao abrir arquivos
- Use datetime para registrar logs e vendas: datetime.now().strftime("%d/%m/%Y %H:%M")
- Carrinho pode ser uma lista de dicionários dentro do usuário logado
- Use while True para manter os menus funcionando

--------------------------------------------------------------

🎯 DESAFIO EXTRA (OPCIONAL):
- Aplicar cores no terminal com códigos ANSI
- Usar classes e POO para organizar melhor (Produto, Usuario, Loja)
- Criar senha oculta com getpass
- Calcular lucro total e exibir gráficos (com matplotlib)

--------------------------------------------------------------
🔥 Boa sorte! Esse projeto é grande, mas se você fizer, já está pensando como programador profissional.
"""
