import statistics

# 1 - Retornar a media
dados = [1, 1.2, 1.4, 1.5]
print(statistics.mean(dados))     # 24.0

# 2 - Retornar a mediana
print(statistics.median(dados))   # 40

# 3 - Retornar a moda
print(statistics.mode(dados))     # 20

# 4 - Retornar o desvio padrão
print(statistics.stdev(dados))    # 12.649...