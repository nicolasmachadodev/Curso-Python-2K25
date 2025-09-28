x = {1, 3, 6, 5, 8}
y = {2, 4, 3, 7, 9}

# 1 - Unir dois sets
print(x.union(y))

# 2 - Mostra quais valores temos em set1, que nao estao em set2 
print(x.difference(y))

# 3 - Unir dois sets, excluindo os valores em comum
print(x.symmetric_difference(y))
