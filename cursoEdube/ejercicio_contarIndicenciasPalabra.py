class Palabra():
    def __init__(self):
        self.palabra=''
    
    def ingresarPalabra(self):
        self.palabra = input('ingrese la palabra: ')
        
    def contarIncidencias(self):
        contado=[]
        for i in self.palabra:
            if not i in contado: 
                contado.append(i)
                print(f'la letra " {i} " se repite {self.palabra.count(i)} veces')
            

p = Palabra()
p.ingresarPalabra()
p.contarIncidencias()