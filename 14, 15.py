# a = int(input("Введите площадь:"))
# b = int(input("Введите количество жителей:"))
# c = a/b
# print("Плотность населения равна", int(c), "человек(а) на 1 квадратный метр ")

a = int(input("Введите длину первого ребра:"))
b = int(input("Введите длину второго ребра:"))
c = int(input('Введите длину третьего ребра:'))
d = a*b*c
e = 2*(a*b + b*c + a*c)
print("Объем равен:", d, "\n", "Площадь равна:", e)