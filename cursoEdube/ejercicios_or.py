# objetos

class Utils():
    numero = ''
    vec = []

    def ingresarNumero(self):
        self.numero = input('ingrese el numero: ')

    def logitudNumero(self):
        return len(self.numero)


# funcionalidad - ejecucion
obj = Utils()
obj.ingresarNumero()
lon = obj.logitudNumero()

for i in range(lon):
    c = obj.numero
    if not c[i] in obj.vec:
        n = c.count(c[i])
        print(c[i], 'aparece', n, 'veces')
        obj.vec.append(c[i])


# -----------------------------------------------------------------------
# ejercicio 2

# objetos
class Vector():
    def ingresarVector(self):
        # esta funcion se encargara unicamente de ingresar un vector y me lo retorna
        sn = 's'
        vec = []
        while (sn == 's'):
            sn = 'n'
            vec.append(int(input('ingrese un numero: ')))
            sn = input('ingresar otro numero? (s/n): ')

        return vec


# ejecucion

obj = Vector()
vec1 = obj.ingresarVector()
vec2 = obj.ingresarVector()

print(vec1)
print(vec2)
print(set(vec1) & set(vec2))


# -------------------------------------------------------------------
# ejercicio 3

import random

class Vector2():

    def generarVectorRandom(self):
        lon = int(input('de que longitud desea el vector? : '))
        vec = []
        for i in range(lon):
            vec.append(random.randrange(1, 10))
        return vec

    def cifraComparar(self):
        c = int(input('cifra a comprar en el vector: '))
        return c

    def comprobarCondicion(self,vec,c,seCumple):
        if seCumple:
            print('verdadero, el vector',vec,'solo tiene cifras menores a',c)
        else:
            print('falso, la condicion no se cumple')



# ejecucion

obj = Vector2()
vec = obj.generarVectorRandom()
c = obj.cifraComparar()
seCumple = True

for i in range(len(vec)):
    if not vec[i] < c:
        seCumple = False
        break

obj.comprobarCondicion(vec,c,seCumple)

