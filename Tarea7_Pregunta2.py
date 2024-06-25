lista=[]
LetraA="aA"
Palabras=input("ingresar palabra (Enter para finalizar):")
while Palabras!= "":
    lista.append(Palabras)
    Palabras=input("ingresar palabra (Enter para finalizar):")

for Palabras in lista:
    a=0
    print(Palabras)
    for letra in Palabras:
        if letra in LetraA:
            a=a+1
    print("el numero de letras a o A es de:",a)
    print(" ")