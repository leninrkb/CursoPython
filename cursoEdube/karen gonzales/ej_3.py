class Reservacion():
    def __init__(self):
        self.nombre=''
        self.seccion=''
        
class Vuelo():
    def __init__(self):
        self.secFumar=50
        self.secNoFumar=50
        self.total=100
        self.destino=''
        self.reservaciones=[]
        
    def nuevaReservacion(self,n,f):
        if f.lower() == 'y':
            if self.secFumar > 0:
                self.secFumar-=1
                f='fumar'
            else:
                print('no hay espacio en la seccion para fumar!')
                return False
        else:
            if self.secNoFumar > 0:
                self.secNoFumar-=1
                f='no fumar'
            else:
                print('no hay espacio en la seccion no fumar!')
                return False
        r = Reservacion()
        r.nombre=n
        r.seccion=f
        self.reservaciones.append(r)
        self.total-=1
        return True
    
    def cancelarReservacion(self,n,f):
        for i in range(len(self.reservaciones)):
            if n == self.reservaciones[i].nombre:
                if f.lower() == 'y':
                    self.secFumar+=1
                else:
                    self.secNoFumar+=1
                self.reservaciones.pop(i)
                self.total+=1
                return True
        return False
    def verReservaciones(self):
        for i in range(len(self.reservaciones)):
            print(f'R{i+1} -> nombre: {self.reservaciones[i].nombre} // seccion: {self.reservaciones[i].seccion}')
        print()
    
class Agencia():
    def __init__(self):
        self.vuelos=[]
        self.destinos=['paris','madrid','londres']
        self.secciones=['fumar','no fumar']     
    
    def prepararVuelos(self):
        for i in range(len(self.destinos)):
            v=Vuelo()
            v.destino = self.destinos[i]
            self.vuelos.append(v)
            
    def verEstadoVuelo(self,n):
        v=self.vuelos[n-1]
        print(f'''
                Estado del vuelo {n} - {self.destinos[n-1]}
                Destino: {v.destino}
                Total disponible: {v.total} asientos
                Total disponible en seccion fumar: {v.secFumar}
                Total disponible en seccion no fumar: {v.secNoFumar}
                Detalle de reservaciones:
              ''')
        v.verReservaciones()
        
    def hacerReservacion(self):
        print('\n--- Realizando reservacion...')
        print(f'Destinos: {self.destinos}')
        v = int(input('Elija su destino (1-3): '))

        for i in range(len(self.vuelos)):
            vuelo = self.vuelos[i]
            if vuelo.destino == self.destinos[v-1]:
                if vuelo.total > 0:
                    n = input('Su nombre: ')
                    f = input('Desea seccion fumar? (y/n): ')
                    if vuelo.nuevaReservacion(n,f):
                        print('reservacion exitosa!...')
                        return True
                    else:
                        print('no se realizo la reservacion...')                     
                else:
                    print('no hay suficiente espacio...')
        return False
    def hacerCancelacion(self):
        print('\n--- Realizando cancelacion...')
        print(f'Destinos: {self.destinos}')
        v = int(input('Elija el destino a cancelar (1-3): '))

        for i in range(len(self.vuelos)):
            vuelo = self.vuelos[i]
            if vuelo.destino == self.destinos[v-1]:
                if vuelo.total == 100:
                    print('no existe reservacion por cancelar...')
                    break
                n = input('Su nombre: ')
                f = input('Se encontraba en seccion fumar? (y/n): ')
                if vuelo.cancelarReservacion(n,f):
                    print('cancelacion exitosa!...')
                    return True
                else:
                    print('no se realizo la cancelacion...')
        return False
    def iniciarAgencia(self):
        self.prepararVuelos()
        while(True):
            print(f'''
                  INICIO
                1-hacer reservacion
                2-hacer cancelacion
                3-ver estado de un vuelo
                4-salir
                ''')
            op = input(f'seleccione una opcion: ')
            if op == '1':
                while(self.hacerReservacion()):
                    q = input('hacer otra reservacion? y/n: ')
                    if q == 'y':
                        continue
                    else:
                        break
            if op == '2':
                while(self.hacerCancelacion()):
                    q = input('hacer otra cancelacion? y/n: ')
                    if q == 'y':
                        continue
                    else:
                        break
            if op == '3':
                print(f'Vuelos: {self.destinos}')
                v = int(input('Elija el vuelo a detallar (1-3): '))
                self.verEstadoVuelo(v) 
            if op == '4':
                break
a = Agencia()
a.iniciarAgencia()