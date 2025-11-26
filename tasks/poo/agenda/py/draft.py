class Fone:
    def __init__(self, id:str, number:str):
        self.__id: str = id
        self.__number: str = number


    def isValid(self):
        v = "0123456789()."
        return all(k in v for k in self.__number)
    
    
    
    def getId(self):
        return self.__id
    def getNumber(self):
        return self.__number
    def __str__(self):
        return f"{self.__id}:{self.__number}"
    
class Contato:
    def __init__(self, nome:str):
        self.__nome: str = nome
        self.__fav: bool = False
        self.__fone: list= []

    def addFone(self, id: str, number: str):
        fone= Fone(id, number)
        if fone.isValid():
            self.__fone.append(fone)
        print("fail: numero invalido")
    def rmFone(self, index:int):
        try:
            self.__fone.pop(index)
        except:
            print("fail: indice invalido")

    def toogleFavorited(self):
        self.__fav = not self.__fav
        
    def isFavorited(self):
        return self.__fav
    
    def getFone(self):
        return self.__fone
    def getName(self):
        return self.__nome
    def setName(self, nome:str):
        self.__nome = nome

    def __str__(self):
        j="@" if self.__fav else "-"
        return f"{j} {self.__nome} ["+ ", ".join(str(k) for k in self.__fone)+"]"
    
class agenda:
    def __init__(self):
        self.__contatos = []

    def findPosByName(self, nome:str):
        for k, i in enumerate(self.__contatos):
            if k.getName()== nome:
                return i
            
        return -1
                



def main(): 