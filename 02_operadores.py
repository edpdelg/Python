#camellos = int(input("¿Cuántos camellos tienes?")) #obliga al operador
###Operadores Aritméticos###
camellos = 25

print(3+4, 3-3, 3*3, 10/10, 9//10, 3**3)
""" // valor entero sin decimales"""


###Operadores comparativos###
print(3>4)
print(camellos < 10)
print(3>=4)
print(3<=4)
print("¿Hay", camellos == 25)
print(camellos != 26)
print("---------------------")

#ordenación alfabética
print(1,"Hola" > "Python")
print(2,"Hola" < "Python")
print(3,"aaa" >= "abaa" )
print(4,len("aaa") >= len("abaaaa")) 
print(5,"¿Hay", camellos == 25)
print(6,camellos != 26)
print("---------------------")

print(3 > 4 and "Hola" > "Python")
print(3 < 4 or "Hola" < "Python")
print("aaa" >= "abaa" or ("Hola" < "Python"))
print(len("aaa") >= len("abaaaa")) 
print(5,"¿Hay", camellos == 25)
print(not(camellos != 26))
print("---------------------")