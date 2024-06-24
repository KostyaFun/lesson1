my_dict = {"Kostya": 1997, "Oleg": 1996, "Kirill": 1995, "Masha": 1200}
print(my_dict)
print(my_dict["Oleg"])
my_dict["Ivan"] = 1346
print(my_dict)
my_dict.update({"Sonya": 1563, "Anna": 2000})
new_dict = my_dict.pop("Kostya")
print(new_dict)
print(my_dict)

my_set = {3,3,4,5,5,4,3,3,7,6,7,6,}
print(my_set)
print(my_set.add(10,))
print(my_set.add("apple"))
print(my_set)
print(my_set.remove(6))
print(my_set)
