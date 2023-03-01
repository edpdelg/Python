"""Sets tiene de base un array, 
pero no existen los arrays sino listas"""

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {"Mango", "Aguacate", 35} #Tiene forma de Set
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Uva") #Un set no es una estructura ordenada

my_other_set.add("Arroz") #No admite repetidos
print(my_other_set)

print("Uva" in my_other_set) #Búsquedas
print("Moure" in my_other_set)

my_other_set.remove("Uva")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

#del my_other_set #Lo manda todo a la chingada
#print(my_other_set)

my_set = {"Mango", "Aguacate", 35}

my_list = [my_set]
print(type(my_list))
print(my_list)

print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set))

print(my_other_set)
my_other_set.update(my_set)
print(my_other_set.union(my_other_set).union(my_set).union({"Javascript", "C#"})) 
#SOLO PARA ESTA EJECUCIÓN, NO ESTÁ EN LA VARIABLE

print(my_new_set.difference(my_set)) #Objetos que NO TIENE








