lista1 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(lista1)

lista2=sorted(lista1)
print(lista2)

lista3=sorted(lista1, reverse=True)
print(lista3)

even_index=lista1[::2]
print(even_index)

odd_index=lista1[1::2]
print(odd_index)

multiplu=[n for n in lista1 if n % 3 == 0]
print(multiplu)

