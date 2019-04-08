def bSort(listado):
    for a in range(len(listado)-1, 0, -1):
        for b in range(a):
            if listado[b] > listado[b+1]:
                tmp = listado[b]
                listado[b] = listado[b+1]
                listado[b+1] = tmp


listado = [11, 4, 53, 8, 21, 9, 54, 89, 74, 2, 1]

bSort(listado)
print(listado)