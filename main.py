#   REPASITO LISTAS  
# valores =[1,2,3,4,5]
# for valor in valores:
#     print(valor)
# valores.append(6)
# print(valores)

#   EN JS
# valores.forEach(function(valor){
#     valor
# })

# TUPLA
valoresTupla = (1,2,3,4,5)
print(valoresTupla)
for valorTupla in valoresTupla:
    print(valorTupla)
#   accediendo a elemento de tupla
# print(valoresTupla[0])
# # valoresTupla.append(6) # Las tuplas no permiten agregar elementos
# print(valoresTupla)

#   Trasformando una tupla en una lista
# listaValores = list(valoresTupla)
# print(listaValores)
# listaValores.append(6)
# print(listaValores)
# valoresTupla = tuple(listaValores)
# print(valoresTupla)

#   RETO 1
tuplaReto1 = (50,45,20,30,40,87)
listaReto1 = list(tuplaReto1)

#       Recorro la lista
listaMayores40 = []
for numero in listaReto1:
    if numero > 40 :
        listaMayores40.append(numero)
print(listaMayores40)

