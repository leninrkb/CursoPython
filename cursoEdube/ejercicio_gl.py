# vector = [12,4,5,3,6,7,83,9,2]
# itera = 0
# for i in range(len(vector)):
#     for j in range(len(vector)-1):
#         itera+=1
#         if vector[j]>vector[j+1]:
#             vector[j], vector[j+1] = vector[j+1], vector[j]
# print(vector,itera)



# vec = [2,3,4,5,6,1,20,2,8,6,45,7,8]
# mayorDiferencia = 0
# dif = 0
# pos=[0,0]

# for i in range(len(vec)-1):
#     dif = vec[i]-vec[i+1]
#     dif = (dif**2)**0.5
#     if dif > mayorDiferencia:
#         pos[0] = i
#         pos[1] = i+1
#         mayorDiferencia = dif

# print('la amyor diferencia es:',mayorDiferencia)
# print('las posiciones son:',pos)


def tomarVector():
    vec=[]
    for i in range(7):
        vec.append(int(input('ingrese un temperatura:')))
    return vec

def queDiaOcurrio(i):
    if i == 1:
        return 'lunes'
    if i == 2:
        return 'martes'
    if i == 3:
        return 'miercoles'
    if i == 4:
        return 'jueves'
    if i == 5:
        return 'viernes'
    if i == 6:
        return 'sabado'
    if i == 7:
        return 'domingo'


vec1 = tomarVector()
promedio = sum(vec1)/len(vec1)
vecDif=[]
menorTemperatura = min(vec1)
minorIndex=0

for i in range(len(vec1)):
    if menorTemperatura == vec1[i]:
        minorIndex = i
    vecDif.append(vec1[i]-promedio)

print('\nvector ingresado',vec1)
print('la temperatura promedio es:',promedio)
print('vector diferencias:',vecDif)
print('menor temperatura:',menorTemperatura)
print('numero de dia ocurrido:',queDiaOcurrio(minorIndex+1))
