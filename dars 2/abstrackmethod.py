from abc import ABC, abstractmethod

class shakl(ABC):
    @abstractmethod
    def yuzi(self):
        pass

    @abstractmethod
    def peremetr(self):
        pass

class ucburchak(shakl):
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def yuzi(self):
        return self.a*self.b/2
    
    def peremetr(self):
        return self.a+self.b+self.c
    

class tortburchak(shakl):
    def __init__(self, a, b ,c, d) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def yuzi(self):
        return self.a*self.b
    
    def peremetr(self):
        return self.a+self.b+self.c+self.d 
    
      
