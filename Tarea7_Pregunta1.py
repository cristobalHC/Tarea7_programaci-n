lista=[]
numero=int(input("ingrese los numeros:"))
for x in range(10):
    lista.append(numero)
    numero=int(input("ingrese los numeros:"))
lista.reverse()
print(lista)