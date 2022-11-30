
class Libro():
    def __init__(self):
        self.vecesLeido=0
        self.nombre=''

class Curso():
    def __init__(self):
        self.librosLeidos=[]
        self.nombre=''
    
    def leerLibros(self,libs):
        self.nombre = input('\nnombre del curso: ')
        newlibs=[]
        for i in range(len(libs)):
            l = Libro()
            l.nombre = libs[i].nombre
            newlibs.append(l)
        for i  in range(len(newlibs)):
            l = newlibs[i]
            mn = '# veces leido el libro '+l.nombre+': '
            l.vecesLeido = int(input(mn))
            self.librosLeidos.append(l)

    def porcentajeUsoLibro(self):
        total=0
        print('\nCurso ',self.nombre)
        for i in range(len(self.librosLeidos)):
            total+=self.librosLeidos[i].vecesLeido
        for i in range(len(self.librosLeidos)):
            p=self.librosLeidos[i].vecesLeido*100/total
            print('uso del libro ',self.librosLeidos[i].nombre,': ',p,'%')

    def librosPorUsoAs(self):
        itera = 0
        for i in range(len(self.librosLeidos)):
            for j in range(len(self.librosLeidos)-1):
                itera+=1
                if self.librosLeidos[j].vecesLeido > self.librosLeidos[j+1].vecesLeido:
                    self.librosLeidos[j], self.librosLeidos[j+1] = self.librosLeidos[j+1], self.librosLeidos[j]
        for i in range(len(self.librosLeidos)):
            print('libro ',self.librosLeidos[i].nombre,' leido ',self.librosLeidos[i].vecesLeido)

    

        
class Biblioteca():
    def __init__(self):
        self.libros=[]
        self.cursosRegistrados=[]

    def ingresarLibros(self,n):
        print('\n *** ingresando libros ***')
        for i in range(n):
            l = Libro()
            l.nombre = input('nombre del nuevo libro: ')
            self.libros.append(l)

    def verLibros(self):
        print('\n libros existentes: ')
        for i in range(len(self.libros)):
            print(' - ',(i+1),self.libros[i].nombre)
    
    def verCursosRegistrados(self):
        print('\n cursos registrados: ')
        for i in range(len(self.cursosRegistrados)):
            print(' - ',(i+1),self.cursosRegistrados[i].nombre)

    def registrarLectura(self):
        nm = int(input('\n# cursos a registrar: '))
        for i in range(nm):
            c = Curso()
            c.leerLibros(self.libros)
            self.cursosRegistrados.append(c)

    def verLibroMasLeido(self):
        for i in range(len(self.cursosRegistrados)):
            c = self.cursosRegistrados[i].librosLeidos
            for j in range(len(self.libros)):
                if c[j].nombre == self.libros[j].nombre:
                    self.libros[j].vecesLeido+=c[j].vecesLeido
        mayor=self.libros[0]
        for j in range(len(self.libros)):
            if self.libros[j].vecesLeido > mayor.vecesLeido:
                mayor = self.libros[j]
        print('\nel libro mas leido es ',mayor.nombre,' con ',mayor.vecesLeido,' leidas')

    def porcentajeUso(self):
        for i in range(len(self.cursosRegistrados)):
            self.cursosRegistrados[i].porcentajeUsoLibro()

    def librosPorUso(self,nom):
        for i in range(len(self.cursosRegistrados)):
            if self.cursosRegistrados[i].nombre == nom:
                print('Curso ',nom)
                self.cursosRegistrados[i].librosPorUsoAs()
                break



b = Biblioteca()
b.ingresarLibros(int(input('# libros ingresar: ')))
b.verLibros()
b.registrarLectura()
b.verCursosRegistrados()
b.verLibroMasLeido()
b.porcentajeUso()
b.librosPorUso(input('curso a mostrar: '))