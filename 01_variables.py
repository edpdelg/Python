my_string_variable = "Hola Mundo"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el való de tu poto:" , my_bool_variable)

#Funciones del sistema
print(len(my_int_to_str_variable)) #Length/Longitud 

#Inputos
caballos = input("¿Cuántos caballos tienes?:")
#Forzar tipo
precio = int(input("¿Cuánto te costó?:"))
print("Tengo", caballos, "Caballos", "y me costaron", precio,"$")