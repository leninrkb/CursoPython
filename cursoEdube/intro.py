print(1_567_132)
print(0o123)
print(0x123)
print(1)
print(1.)
print(1e5)
print("Me gusta \"Monty Python\"")
print("I'm Monty Python.")
print(True > False)
print(True < False)
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
#El resultado producido por el operador 
# de división siempre es flotante
print(14 % 4)
print(2 ** 2 ** 3)
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

l = 0;
print(l)

juan = 3;
maria = 5;
adan = 6;

print(juan,",",maria,",",adan);
total = juan + maria + adan
print(total)
round((123/234),2)

x =  0
x = float(x)
y = (3*x**3) - (2*x**2) + (3*x) -1
print("y =", y)

anything = input("Dime algo...")
print("Mmm...", anything, "...¿En serio?")

# Probando mensajes de error.

anything = input("Inserta un número: ")
something = anything ** 2.0
print(anything, "al cuadrado es", something)

#casting
anything = float(input("Inserta un número: "))
something = anything ** 2.0
print(anything, "al cuadrado es", something)

leg_a = float(input("Inserta la longitud del primer cateto: "))
leg_b = float(input("Inserta la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)

# ingresa un valor flotante para la variable a aquí
a = int(input("val 1"))
# ingresa un valor flotante para la variable b aquí
b = int(input("val 2"))

# muestra el resultado de la suma aquí 
sum = a+b
# muestra el resultado de la resta aquí
res = a - b
# muestra el resultado de la multiplicación aquí
mul = a*b
# muestra el resultado de la división aquí
div = a/b

print(sum,res,mul,div)
print("\n¡Eso es todo, amigos!")


x = float(input("Ingresa el valor para x: "))

# Escribe tu código aquí.
y = 1/(x+(1/x+(1/x+(1/x))))
print("y =", y)




x = float(input("Ingresa el valor para x: "))

# Escribe tu código aquí.
y = 1/(x+(1/(x+(1/(x+(1/x))))))
print("y =", y)





hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.
mins += hour*60
dura += mins


print("dura " , dura)

