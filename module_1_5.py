immutable_var = (1, 2, 3, 4, "Flower", True, 1.3, [3, 4, 5, 6])
print(immutable_var)
# immutable_var [0] = 8
# Значения элементов кортежа нельзя изменить, потому что кортеж не поддерживает обращение по элементам.
# Кортежи - это объекты неизменяемого типа в Python
mutable_list = [5, 6, 7, "Sun", "Water"]
print(mutable_list)
mutable_list [2] = 8
print(mutable_list)
mutable_list [4] = "Grass"
print(mutable_list)