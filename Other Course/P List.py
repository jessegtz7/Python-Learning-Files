familia = ["Zozimo", 1.73, "Isela", 1.50, "Jesse", 1.75]
familia2 = [["Rocio", 1.50],
            ["Irma", 1.53],
            ["Luis", 1.64]]

print(familia)
print(familia2)
print(type(familia),type(familia2))
print(familia[2], familia[3])

print(familia[1:4])
print(familia[:4])
print(familia[2:])

familia[5] = 1.77
print(familia)

familia[0:2] = ["Ganfe", 1.74]
print(familia)

familia = familia + ["Ivan", 1.74]
print(familia)

del(familia[2])
print(familia)
del(familia[2])
print(familia)

x = ["a", "b", "c"]
y = x
y[1] = "z"
print(y)
print(x)

w = list(x)
w = x[:]
w[0] = "h"
print(w)
print(x)