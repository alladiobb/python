conjunto = {1,2,3,4}
conjunto2 = {5,6,7,8}
conjunto3 = {1,3,5,7}

conjuntoMaior = {1,2,3,4,5,6,7,8}

print(conjunto)
conjunto.add(5)
#
conjunto=conjunto.union(conjunto2)
print(conjunto)
#
conjunto=conjunto3.intersection(conjunto2)
print(conjunto)

conjunto=conjunto3.difference(conjunto2)
print(conjunto)
conjunto=conjunto2.difference(conjunto3)
print(conjunto)
# Soma da diferença dos dois acima
conjunto=conjunto2.symmetric_difference(conjunto3)
print(conjunto)

#Se é um subConjunto do conjunto
isConjunto_subSet = conjunto.issubset(conjuntoMaior)
print(isConjunto_subSet)

#Se é um superConjunto
isConjunto_superSet = conjunto.issuperset(conjuntoMaior)
print(isConjunto_superSet)