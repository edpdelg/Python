###tuples####

my_tuple = tuple()
my_other_tuple = ()  #SI ESCRIBIMOS CON [LIST] (TUPLE)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
#my_list = [35, 1.77, "Brais", "Moure"] si lleva [es lista]
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Brais")) #Cuántos valores hay?
print(my_tuple.index("Brais")) #Posición del valor

#my_tuple[1] = 1.80 #does not support item assignment
#La tuple es un valor inmutable, no pueden asignar más

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6]) #Slices

my_tuple = list(my_tuple)
print(type(my_tuple))

#Reasignar tuple a mutable y viceversa
my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#del my_tuple[4] #doesn't support item deletion

del my_tuple #incoherente?
#print(my_tuple) #'my_tuple' is not defined

my_tuple = ("Rependejo")
print(my_tuple)





