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
            return
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
        
        for i, k in enumerate(self.__contatos):
            if k.getName()== nome:
                return i
            
        return -1
    
    def addContact(self, nome:str, fones:list[Fone]):
        po= self.findPosByName(nome)
        if po!= -1:
            contato= self.__contatos[po]
        else:
            contato=Contato(nome)
            self.__contatos.append(contato)
        for i in fones:
            if i.isValid():
                contato.addFone(i.getId(), i.getNumber())
            else:
                print(f"fail: invalid number {i}")
        self.__contatos.sort(key=lambda c: c.getName())
    def getContact(self, nome:str):
        po=self.findPosByName(nome)
        if po==-1:
            return None
        return self.__contatos[po]
    

    def search(self, pattern:str):
        encontrado=[]
        for contato in self.__contatos:
            if pattern in str(contato):
               encontrado.append(contato)
        return encontrado
        
    def rm(self, nome:str):
        po=self.findPosByName(nome)
        if po==-1:
            return None
        self.__contatos.pop(po)

    def rmFone(self, nome:str, index:int):
        contato=self.getContact(nome)
        if contato:
            contato.rmFone(index)
        else:
            print("fail: contato nao existe")

    def getFavorited(self):
        co=[]
        for self.__contatos in self.__fav:
            co.append(self.__contatos)
            return self.__fav
    def favs(self):
        return "\n".join(str(c) for c in self.__contatos if c.isFavorited())
         
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
            nome= args[1]
            fone=[]
            for i in args[2:]:
                id, number= i.split(":")
                fone.append(Fone(id, number))
            agenda.addContact(nome,fone)
        
        elif args[0]=="show":
            print(agenda)
        
        elif args[0]=="rm":
            agenda.rm(args[1])
        elif args[0]=="rmFone":
            agenda.rmFone(args[1], int(args[2]))
        elif args[0]=="tfav":
            contato= agenda.getContact(args[1])
            if contato:
                contato.toogleFavorited()
        elif args[0]=="favs":
            print(agenda.favs())

        elif args[0]=="search":
            s=agenda.search(args[1])
            for i in s:
                print(i)
        else:
            print("comando invalido")
main()
