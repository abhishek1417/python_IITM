from abc import abstractmethod


class Abhi:
    @abstractmethod
    def Hello(self):
        pass
    @abstractmethod
    def Add(self,x,y):
        pass
    
class guvi(Abhi):
    def Hello(self):
        return "Hello from Guvi Class"
    
g =guvi()

print(g.Hello())
    