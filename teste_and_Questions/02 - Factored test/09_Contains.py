#Set
teste0 = {1,2,3,4,5,"a","b","c","c"}
#Lista
teste1 = [1,2,3,4,5,"a","b","c"]
#Dicionário
teste2 = {
    "a" : 1,
    "b" : 2,
}
#Tupla
teste3 = (1,2,3,4,5,5)
elemento = 1

print(teste0)

"""
print(teste0.__contains__(10))

try:
    print(teste1.index(10))
except ValueError:
    print("Não tem o elemento")

print(teste2.get('a'))
"""

"""
if elemento in teste0:
    print(f'teste0 tem o : {elemento}')
    
if elemento in teste1:
    print(f'teste1 tem o : {elemento}')
    
if elemento in teste2:
    print(f'teste2 tem o : {elemento}')
"""

#Set
"""
print(teste0.__contains__(1))
teste0.add(6)
teste0.remove(1)
teste0.update({10,20})
teste0.pop()
teste0.pop()
print(teste0)
"""

#Lista
"""
print(teste1.__add__([10,10,20]))
print(teste1)
teste1.append(10)
teste1.insert(0,0)
teste1.reverse()
teste1.reverse()
teste1.extend([20,30])
teste1.extend((40,50))
teste1.extend({60,70})
print(teste1.__contains__('c'))
"""

#Dicionário
"""
print(teste2)
teste2.pop('a')
print(teste2)
teste2.update(['a',1],2)
print(teste2)
"""