from math import gcd, pi

class Fraction:
    def __init__(self,ch1,ch2):
        assert ch1==int(ch1) 
        assert ch2==int(ch2)
        assert ch2 != 0
        self.ch1 = ch1
        self.ch2 = ch2
    
    def __str__(self):
        print(f"{self.ch1} / {self.ch2}")
        
    def add(self,fraction):
        self.ch1=self.ch1*fraction.ch2+self.ch2*fraction.ch1
        self.ch2=self.ch2*fraction.ch2
        
    def mult(self,fraction):
        self.ch1=self.ch1*fraction.ch1
        self.ch2=self.ch2*fraction.ch2
    
    def simplify(self):
        assert gcd(self.ch1,self.ch2)
        a=gcd(self.ch1,self.ch2)
        self.ch1=int(self.ch1/a)
        self.ch2=int(self.ch2/a)

"""
if __name__=='__main__':        
    f1=Fraction(3,4)
    f2=Fraction(1,2)
    f1.__str__()
    f1.add(f2)
    f1.__str__()
    f1.mult(f2)
    f1.__str__()
    f1.simplify()
    f1.__str__()
"""   
    
def H(n):
    f=Fraction(0,1)
    for i in range(1,n+1):
        h=Fraction(1,i)
        f.add(h)
        f.simplify()
    f.__str__()

def Leib(n):
    f=Fraction(0,1)
    for i in range(n+1):
        l=Fraction((-1)**i,2*i+1)
        f.add(l)
        f.simplify()
    f.__str__()
        
class Polynomial:
    def __init__(self,liste):
        assert type(liste)==list
        self.coef=liste
    
    def __str__(self):
        n=len(self.coef)
        a=str()
        for i in range(n):
            if i != n-1:
                a=a+str(self.coef[i])+'*x**'+str(n-1-i)+' + '
            else:
                a=a+str(self.coef[i])+'*x**'+str(n-1-i)
        print(a)
    
    def add(self,poly):
        n1=len(self.coef)
        n2=len(poly.coef)
        n=min(n1,n2)
        if n==n1:
            self.coef=[0 for i in range(n2-n1)]+self.coef
        else:
            poly.coef=[0 for i in range(n1-n2)]+poly.coef
        for i in range(len(self.coef)):
            self.coef[i]=self.coef[i]+poly.coef[i]
    
    def deriv(self):
        n=len(self.coef)
        for i in range(n):
            self.coef[i]=self.coef[i]*(n-1-i)
        self.coef.remove(self.coef[n-1])
            
    def integrate(self,const):
        n=len(self.coef)
        for i in range(n):
            self.coef[i]=self.coef[i]/(n-i)
        self.coef.append(const)
            
if __name__=='__main__':
    p=Polynomial([1,2,7,5])
    p.__str__()
    p1=Polynomial([5,7])
    p.add(p1)
    p.__str__()
    p.deriv()
    p.__str__()
    p.integrate(12)
    p.__str__()