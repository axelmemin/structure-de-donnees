from __future__ import annotations

class Tree:
    def __init__(self, label, *children):
        assert type(label)==str
        self.__label=label
        self.__children=tuple(children)
    
    def alabel(self):
        return self.__label
    
    def achildren(self):
        return self.__children
    
    def child(self,i:int):
        return self.__children[i]
    
    def nb_children(self):
        return len(self.__children)
    
    def is_leaf(self):
        if len(self.__children)==0:
            return True
        else: 
            return False

    def depth(self):
        if self.is_leaf():
            return 0
        return 1+max([s.depth() for s in self.achildren()])  

    def __str__(self):
        if self.is_leaf():
            return self.alabel()
        a=''
        for s in range(len(self.achildren())):
            if s==len(self.achildren())-1:
                a=a+self.achildren()[s].__str__()
            else:
                a=a+self.achildren()[s].__str__()+','
        return f'{self.alabel()}({a})'      

    def __eq__(self,tree):
        if self.alabel()==tree.alabel():
            for i in range(len(self.achildren())):
                return self.achildren()[i].__eq__(tree.achildren()[i])
        else:
            return False
        
t1=Tree('f',Tree('a',Tree('c')),Tree('b'))
t2=Tree('f',Tree('a',Tree('c')),Tree('b'))
print(t1.achildren())
print(t1.depth())
print(t1.__str__())
print(t1.__eq__(t2))
