class Fecha():
    def __init__(self):
        self.meses = [31,28,31,30,31,30,31,31,30,31,30,31]
        print(f'Dias = {sum(self.meses)}')
        
    def verMeses(self):
        print('DIAS EN EL MES')
        print(f'enero {"febrero":>8}{"marzo":>10}{"abril":>10}{"mayo":>10}{"junio":>10}{"julio":>10}{"agosto":>10}{"septiembre":>15}{"obtubre":>10}{"noviembre":>12}{"diciembre":>12}')
        print(f'{self.meses[0]}{self.meses[1]:>10}{self.meses[2]:>10}{self.meses[3]:>10}{self.meses[4]:>10}{self.meses[5]:>10}{self.meses[6]:>10}{self.meses[7]:>10}{self.meses[8]:>15}{self.meses[9]:>10}{self.meses[10]:>12}{self.meses[11]:>12}')
    
    def ingresoDatosUsuario(self):
        m = int(input('ingrese el mes (1=enero al 12=diciembre): '))-1
        if m in [0, 2, 4, 6, 7, 9, 11]:
            d = int(input('ingrese el dia (1 al 31): '))
            if d > 31 or d < 1:
                print(f'el mes {m+1} solo tiene entre 1 y 31 dias')
                return False
            else:
                self.calcularDiasRestantes(m,d)
        elif m in [3, 5, 8, 10]:
            d = int(input('ingrese el dia (1 al 30): '))
            if d > 30 or d < 1:
                print(f'el mes {m+1} solo tiene entre 1 y 30 dias')
                return False
            else:
                self.calcularDiasRestantes(m,d)
        elif m == 1:
            d = int(input('ingrese el dia (1 al 28): '))
            if d > 28 or d < 1:
                print(f'el mes {m+1} solo tiene entre 1 y 28 dias')
                return False
            else:
                self.calcularDiasRestantes(m,d)
        else:
            print(f'el mes {m+1} no existe...')
    
    def calcularDiasRestantes(self, m, d):
        r=0
        r=self.meses[m]-d
        for i in range((m+1), len(self.meses)):
            r+= self.meses[i]
        print(f'restan {r} dias en el anio...')

# ---------------------
fecha = Fecha()
fecha.verMeses()
fecha.ingresoDatosUsuario()
