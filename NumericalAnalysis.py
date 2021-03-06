# This code is based on 'Numercial Methods For Engineers , Steven C.Chapra, Raymond P.Canale"
# code developer : yunjin Kyung, MyoungJi univerity


import math

# Bracketing Method
class Bisect : #Bisection Method
    def __init__(self, xl, xu, tol):
        self.xl = xl
        self.xu = xu
        self.tol = tol
        self.equ = input("Please Enter your Equation(Pythonic) : ")
      
    def show(self):
        print("Equ : {}  xl : {}  xu: {} tolerance: {}".format(self.equ, self.xl, self.xu,self.tol))

    def fu(self):
        x=self.xu
        self.valu = eval(self.equ)
        return self.valu

    def fn(self):
        x=self.xl
        self.vall = eval(self.equ)
        return self.vall
    
    def fxm(self):
        x=self.xr
        self.valxm = eval(self.equ)
        return self.valxm

    def analysis(self):
        if (Bisect.fu(self)*Bisect.fn(self)) >= 0 :
            print("Please reset your range : xl,xu")

        else : 
            rep = 0
            eps = 1
            
            while eps > self.tol : 
                rep = rep + 1 
                self.xr = (self.xl + self.xu)/2
                
                if not (self.xr == 0) :
                    eps = abs((self.xl-self.xr)/self.xr)
                
                print('rep =',rep,'f(xm)=',self.fxm(),'xm=',self.xr,'eps=',format(eps,".4f"))

                if self.fn()*self.fxm() > 0 :
                 self.xl=self.xr
               
             
                elif self.fn()*self.fxm() < 0 :
                 self.xu=self.xr
                 

                else : 
                 eps = 0
        return self.xr

# Open Method
class NR :  # Newton-Rhapson Method

    def __init__(self,xi, tol):
        self.xi = xi
        self.tol = tol
        self.equ = input("Please Enter your Original Equation(Pythonic) : ")
        self.equd = input("Please Enter your defferent Equation(Pythonic) : ")
    def f(self):
        x=self.xi
        self.val = eval(self.equ)
        return self.val

    def fd(self):
        x=self.xi
        self.vald = eval(self.equd)
        return self.vald
    
    def analysis(self):
        i=0
        eps = 1
        while eps > self.tol :
            i=i+1
            x= self.xi - self.f()/self.fd()
            eps = abs((x-self.xi)/x)
            self.xi = x
            print("rep : {} xi : {}  eps: {}".format(i,self.xi,eps))
        return self.xi

class Secant : # Secant Method
    def __init__(self) -> None:
        pass
