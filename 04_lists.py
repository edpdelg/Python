### Lists ###

my_list = list() #Bob el Constructores de listas
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[3])
print(my_other_list[-3])
#print(my_other_list[-3]) #IndexError: No puede contar más allá de lo que existe
print(my_list.count(30)) #Cuenta el número de elementos dentro de la propia lista

age, height, name, surname = my_other_list
print("Hola, mi nombre es:", name)
print("Mi apellido es:", surname)
print("Altura:", height)
print("Y mi edad es:", age)

name, height, age, surname = my_other_list[2], my_other_list[0], my_other_list[1], my_other_list[3]
print(age) #Ha cambiado de sitio el orden de la lista

print(my_list + my_other_list)
print([1, 2, 3, 4]) #Ya viene predefinido la lista aun sin list

my_other_list.append("MourDev")#al final
my_other_list.insert(4, "Nombre de la empresa:")#insertado en una posición
print(my_other_list)

my_other_list.remove("MourDev") #pa borrar un solo elemento
print(my_other_list)

print(my_list)
my_list.pop()
print(my_list)
my_pop_element = my_list.pop(5)
print(my_list)
print(my_pop_element)

del my_other_list[4] #pa borral por indice y no retornar
print(my_other_list)

my_other_list.append(my_pop_element)
print(my_other_list)

my_new_list = my_list.copy()
my_list.clear()
print(my_new_list)

my_new_list.reverse()
print(my_new_list)
my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3]) #Slices igual que ayer

