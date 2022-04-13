def MetodoOrdenamientoBurbuja(numero):
    for i in range(1,len(numero)):
        for j in range(0,len(numero)-i):
            if(numero[j+1]<numero[j]):
                aux=numero[j];
                numero[j]=numero[j+1];
                numero[j+1]=aux;

    print(numero)

def MetodoOrdenamientoBurbujaBidireccional(numero):
    for k in range(len(numero)//2):
        swapped = False
        for i in range(1+k, len(numero)-k):
            if numero[i] < numero[i-1]:
                numero[i], numero[i-1] = numero[i-1], numero[i]
                swapped = True
        if not swapped:
            break

        swapped = False
        for i in range(len(numero)-k-1, k, -1):
            if numero[i] < numero[i-1]:
                numero[i], numero[i-1] = numero[i-1], numero[i]
                swapped = True
        if not swapped:
            break

    print(numero)

numero=[10,5,2,3,7,8,6,4,9,1]
print("Numeros desordenados:",numero)
print("Numeros ordenados por metodo burbuja:")
MetodoOrdenamientoBurbuja(numero)
print("Numeros ordenados por metodo burbuja bidireccional:")
MetodoOrdenamientoBurbujaBidireccional(numero)

