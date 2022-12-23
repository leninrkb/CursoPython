class incidencia_numero:
    num=0
    ndig=0
    list=[]
    def ingresar(self):
        self.num=int(input("Por favor ingrese un número: "))
    def cantidad_dig(self):
        cont=self.num
        while cont>0:
            cont=cont//10
            self.ndig=self.ndig+1
    def lista(self):
        dig=0
        for i in range(0,self.ndig,1):
            dig=self.num%10
            self.num=self.num//10
            if dig>=0:
                self.list.append(dig)
        self.list.sort()
    def contar(self):
        z=0
        for j in range(len(self.list)):
            x=self.list[j]
            y=self.list.index(x)
            if j<(len(self.list)-1):
                z=self.list[j+1]
            if x!=z:
                print(self.list[y]," se repite: ",self.list.count(x))
        print(self.list[y]," se repite: ", self.list.count(x))
        
prueba=incidencia_numero()
prueba.ingresar()
prueba.cantidad_dig()
prueba.lista()
prueba.contar()
