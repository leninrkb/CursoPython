# print('2' != 2)

# ans = int(input()) >= 100
# print(ans)

# if ans:
#     print("es igual o mayor")
# else:
#     print("es menor")



# number1 = 456
# number2 = 23
# number3 = 123

# print("max:",max(number1,number2,number3))
# print("min:",min(number1,number2,number3))




# x, y, z = 5, 10, 8

# print(x > z)
# print((y - 5) == x)



# x = 1
# y = 1.0
# z = "1"

# if x == y:
#     print("uno")
# if y == int(z):
#     print("dos")
# elif x == y:
#     print("tres")
# else:
#     print("cuatro")


# i=0
# while i<100:
#     print("hola n:",i)
#     i+=1




# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

# odd_numbers = 0
# even_numbers = 0

# # Lee el primer número.
# number = int(input("Introduce un número o escribe 0 para detener: "))

# # 0 termina la ejecución.
# while number != 0:
#     # Verificar si el número es impar.
#     if number % 2 == 1:
#         # Incrementar el contador de números impares odd_numbers.
#         odd_numbers += 1
#     else:
#         # Incrementar el contador de números pares even_numbers.
#         even_numbers += 1
#     # Leer el siguiente número.
#     number = int(input("Introduce un número o escribe 0 para detener: "))

# # Imprimir resultados.
# print("Cuenta de números impares:", odd_numbers)
# print("Cuenta de números pares:", even_numbers)



# secret_number = 777

# print(
# """
# +==================================+
# | ¡Bienvenido a mi juego, muggle!  |
# | Introduce un número entero       |
# | y adivina qué número he          |
# | elegido para ti.                 |
# | Entonces,                        |
# | ¿Cuál es el número secreto?      |
# +==================================+
# """)
# n = int(input("n: "))
# while n!= secret_number:
#     print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
#     n = int(input("n: ")) 
# print("¡Bien hecho, muggle! Eres libre ahora")



# for i in range(10):
#     print("n:",i)

# import time

# for i in range(5):
#     print(i,"Mississippi")
#     time.sleep(1)




# print("La instrucción break:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")


# # continue - ejemplo

# print("\nLa instrucción continue:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")


# l = input("palabra").upper()

# for i in l:
#     if i=="A":
#         continue
#     else:
#         print(i)


# i = 1
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else:", i)


# blocks = int(input("Ingresa el número de bloques: "))
# base = 0
# altura=0
# while base < blocks:
#     altura+=1
#     base+=1;
#     blocks-=base
# print("altura:",altura)


# &  (ampersand) - conjunción a nivel de bits.
# |  (barra vertical) - disyunción a nivel de bits.
#  ~  (tilde) - negación a nivel de bits.
#  ^  (signo de intercalación) - o exclusivo a nivel de bits (xor).


#listas y arreglos

# numbers = [10, 5, 7, 2, 1]
# print("Contenido de la lista original:", numbers)

# numbers[0] = 111
# print("Nuevo contenido de la lista: ", numbers)
# print("\nLongitud de la lista:", len(numbers))

# del numbers[0]
# print("Nuevo contenido de la lista: ", numbers)
# print("\nLongitud de la lista:", len(numbers))

# numbers = [111, 7, 2, 1]
# print(numbers[-1])
# print(numbers[-2]) 
# numbers.append(23)
# numbers.append(245)
# numbers.append(2)
# numbers.append(94)
# numbers.insert(5,34444)
# print(numbers)

# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in range(len(my_list)):
#     total += my_list[i]

# print(total)



# # cambio de variable 
# variable_1 = 1
# variable_2 = 2

# variable_1, variable_2 = variable_2, variable_1


# # invertir lista 
# my_list = [10, 1, 8, 3, 5, 2]
# length = len(my_list)

# for i in range(length // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

# print(my_list)
# my_list.reverse()
# print(my_list)

# alg burbuja, solucion mia(la mejor obviamente)
ls = [12,4,5,3,6,7,83,9,2]
s=0
for i in range(len(ls)):
    for j in range(len(ls)-1):
        s+=1
        if ls[j]>ls[j+1]:
            ls[j], ls[j+1] = ls[j+1], ls[j]

print(ls,s)


# #solucion del curso
# my_list = [12,4,5,3,6,7,83,9,2] # lista a ordenar
# swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
# s=0
# while swapped:
#     swapped = False  # no hay intercambios hasta ahora
#     for i in range(len(my_list) - 1):
#         s+=1
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # ¡ocurrió el intercambio!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print(my_list,s)


# # XD  python estas demasiado
# ls = [12,4,5,3,6,7,83,9,2]
# ls.sort()
# print(ls)
        
    
# l1 = [1,2,3,4,5,4,4,6,5,1,2,8,6,9,7,0]
# l2 = l1

# l1[0]=22
# print(l2)

# l3 = [1,2,3,4,5,4,4,6,5,1,2,8,6,9,7,0]
# l4 = l3[1:5] #[inicio:fin] inicio-incluido en el corte / fin-no incluio

# l3[0]=22
# print(l3)
# print(l4)




# # veo cuantos nums de bets estan en drawn
# drawn = [5, 11, 9, 42, 3, 49]
# bets = [3, 7, 11, 42, 34, 49]
# hits = 0

# for number in bets:
#     if number in drawn:
#         hits += 1

# print(hits)



# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2

# # del list_1[0]
# del list_2

# print(list_3)



# squares = [x ** 2 for x in range(20)]
# print(squares)


# pares = [x for x in squares if x % 2 == 0 ]
# print(pares)


# creo un tablero de ajedrez2 xd
board = []

for i in range(8):
    row = [0 for i in range(8)]
    board.append(row)
print(board)