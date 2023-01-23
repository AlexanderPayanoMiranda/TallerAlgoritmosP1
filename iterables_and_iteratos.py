from itertools import combinations

_, letters, K = input("Ingrese el numero de items de la lista: "), input("Ingrese las letras: ").split(), int(input("Ingrese el numero con el cual se realizaran las combinaciones: "))

comb = list(combinations(letters, K))

a_list = list(filter(lambda tpl: "a" in tpl, comb))

print(len(a_list)/len(comb))
