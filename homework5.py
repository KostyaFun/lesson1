immutable_var = 1, 3, "красота", True
print(immutable_var)
print(immutable_var) # 'tuple' object does not support item assignment - причина ошибки, в кортеже нельзя изменить элемент
mutable_list = ["cat", "lion", 22, False]
print(mutable_list)
mutable_list[2] = 33
print(mutable_list)
mutable_list.extend("dog")
print(mutable_list)
mutable_list.append("Alexey")
print(mutable_list)
mutable_list.remove("lion")
print(mutable_list)