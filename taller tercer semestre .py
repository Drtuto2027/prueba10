def llenarLista(lista):
     for i in range(6):
         numero = int(input("Ingrese el número {} de la lista".format(i+1)))
         lista.append(numero)
     return lista

def restarLista(lista1, lista2):
    lista3 = []
    for i in range(6):
        lista3.append(lista1[i]-lista2[i])
        return lista3

def calcularPromedio(lista):
    acumulado = 0
    promedio = 0
    for numero in lista:
        acumulado = acumulado + numero
    promedio = acumulado/6 
    return promedio

lista1 = [] 
lista2 = []
lista3 = []
promedio = 0
lista1 = llenarLista(lista1)
lista2 = llenarLista(lista2)
lista3 = restarLista(lista1, lista2)
promedio = calcularPromedio(lista3)
print(lista1)
print(lista2)
print(f"El resultado de la resta componente a componente de las listas 1 y 2 es {lista3}")
print(f"El promedio de la lista 3 es {promedio}")
  