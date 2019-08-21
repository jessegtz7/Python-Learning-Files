import numpy as np
altura = [1.50, 1.65, 1.70, 1.85]
peso = [60, 55, 83, 92]

print(altura)
print(peso)

np_altura = np.array(altura)
np_peso = np.array(peso)

print(np_altura)
print(np_peso)

masa = np_peso / np_altura ** 2
print(masa)



r= np.array([1.0, "is", True])
print(r)

pythonList = [1, 2, 3]
numpyArray = np.array([4, 5, 6])

s = pythonList + pythonList
print(s)

f = numpyArray + numpyArray
print(f)

bni = np.array([10, 20, 30])
print(bni)
print(bni[1])

g = bni > 13
print(g)

j = bni[bni > 13]
print(j)


print(type(np_altura), type(np_peso))

np_2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])
print(np_2d)
print(np_2d.shape)
print(np_2d[0])
print(np_2d[0][2])
print(np_2d[0,2])
print(np_2d[:,1:3])
print(np_2d[1,:])

"""
np_7d = np.array([[4, 5],
                  [3, 9],
                  [3, 7],
                  [4, 6],
                  [5, 8],
                  [1, 0],
                  [1, 9]])
print(np.mean(np_7d[:,0]))
print(np.median(np_7d[:,0]))
print(np.corrcoef(np_7d[:,0], np_7d[:,1]))
print(np.std(np_7d[:,0]))
"""

altura2 = np.round(np.random.normal(1.5, 0.20, 8),2)
peso2 = np.round(np.random.normal(60.23, 15, 8), 2)
np_8d = np.column_stack((altura2, peso2))
print(np_8d)

print(np.mean(np_8d[:,0]))
print(np.median(np_8d[:,0]))
print(np.corrcoef(np_8d[:,0], np_8d[:,1]))
print(np.std(np_8d[:,0]))