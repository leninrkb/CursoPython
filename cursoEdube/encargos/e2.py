def pedirTerminosN():
    return int(input('n) numeros de terminos a generar = ' ))

def pedirTerminosX():
    return int(input('x) valor de x (1-10) = '))


class Formula():
    a=1
    b=4
    def factorial(self,n):
        if n == 1 or n == 0:   
            return 1
        else:
            return n * self.factorial(n - 1)
    def formulaSerie(self, x, n):
        r = ((x+self.a)**n)/((self.factorial(self.b)*n)**0.5)
        return r
    def verFormula(self, x, n):
        print(f"""
            ({x}+{self.a})^{n}
            ----------
            (√({self.b}!({n})))
            """)


formula = Formula()
n = pedirTerminosN()
x = pedirTerminosX()
terminos=[]

for i in  range(n,0,-1):
    r = formula.formulaSerie(x,i)
    formula.verFormula(x,i)
    formula.a+=2
    formula.b+=4

    if i % 2 == 0:
        terminos.append(-r)
        continue
    terminos.append(r)


print('terminos generados',terminos)
print('sumatoria',sum(terminos))
print('*** by rkb.lenin@gmail.com ***')