class Fone:
    def __init__(self, id:str, number:str):
        self.__id: str = id 
        self.__number: str = number

    def isValid(self):
        p= "0123456789()."
        return all(c in p for c in self.__number)
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
            return 
        print("fail: invalid number")
    def rmFone(self, index:str):
        try: 
            self.__fone.pop(index)
        except:
            print("fail: indice invalido")
    def toogleFavorited(self):
        self.__fav = not self.__fav

    def __str__(self):
        flag="@" if self.__fav else "-"
        return f"{flag} {self.__nome} [" + ", ".join(str(c) for c in self.__fone)+"]"

    def isFavorited(self):
        return self.__fav\
        

def main():
    contato = Contato("")
    while True :
        line = input()
        args= line.split()
        print(f"${line}")
        if args[0]=="end":
            break
        elif args[0]=="add":
            contato.addFone(args[1], args[2])
        elif args[0]=="init":
            contato=Contato(args[1])
        elif args[0]=="show":
            print(contato) 
        elif args[0]=="rm":
             contato.rmFone(int(args[1]))  
        elif args[0]=="tfav":
            contato.toogleFavorited()
        else:
            print("comando invalido")
main()  

