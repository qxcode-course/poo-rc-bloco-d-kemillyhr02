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
    
class Agenda:
    def __init__(self):
        self.__contatos = []

    def findPosByName(self, nome:str):
        for k, i in enumerate(self.__contatos):
            if k.getName()== nome:
                return i
            
        return -1
    
    def addContact(self, nome:str):
        Fones= list[Fone]
        return
    def getContact(self, nome:str):
        return
    def getFavorited(self):
        co=[]
        for self.__contatos in self.__fav:
            co.append(self.__contatos)
            return self.__fav

        return
    def __str__(self):
        return "\n".join(str(c) for c in self.__contatos)
        
    
def main():
    agenda= Agenda()
    while True:
        line= input()
        args= line.split()
        print(f"${line}")
        if args[0]=="end":
            break
        elif args[0]=="add":
            agenda.addContact(args[1])
        
        elif args[0]=="show":
            print(agenda)
        
        elif args[0]=="rm":
            agenda.rmFone(int(args[1]))

        elif args[0]=="tfav":
            agenda.toogleFavorited(int(args[2]))
        else:
            print("comando invalido")
main()
