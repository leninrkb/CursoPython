# def saludar(n):
#     print('hola lenin',n)

# saludar('ewee')


# # dar un valor por defecto
# def introduction(first_name, last_name="González"):

#     print("Hola, mi nombre es", first_name, last_name)


# value = None
# if value is None:
#     print("Lo siento, no contienes ningún valor")



# def strange_function(n):
#     if (n % 2 == 0):
#         return True

# def list_sum(lst):
#     s = 0
    
#     for elem in lst:
#         s += elem
    
#     return s

# print(list_sum([5, 4, 3]))

# def strange_list_fun(n):
#     strange_list = []
    
#     for i in range(0, n):
#         strange_list.insert(0, i)
    
#     return strange_list

# print(strange_list_fun(5))



global name


def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Ingresa la longitud del primer lado: '))
b = float(input('Ingresa la longitud del segundo lado: '))
c = float(input('Ingresa la longitud del tercer lado: '))

if is_a_triangle(a, b, c):
    print('Si, si puede ser un triángulo.')
else:
    print('No, no puede ser un triángulo.')