class Toalha:
    def __init__ (self, color: str, size: str): #construtor
        self.color: str= color #atributos
        self.size: str = size 
        self.wetness: int = 0

    def dry(self, amount: int) -> None:
        self .wetness += amount
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self. wetness = self .getMaxWetness()

    def getMaxWetness (self) -> int:
        if self .size == "P":
            return 10 
        if self .size == "M":
            return 20
        if self .size == "G":
            return 30
        return 0
    
    def __str__ (self) -> str:
        return f"Cor:{self.color}, Tam:{self.size}, Umidade:{self.wetness}"

def isdry (self) -> bool:
    return self.wetness == 0

def wringOut (self) -> None :
    self.wetness = 0


"""
VALORES INSERIDOS DIRETAMENTE DO PROGRAMADOR:

doguito = Toalha ("velha" , "G")
print (doguito)
doguito.dry(10)
print(doguito) 
doguito.dry(30)
print(doguito)

"""

def main ():
    toalha = Toalha("" , "") #objeto manipulado
    while True: #loop infinito 
        line: str = input()
        print ("$" + line)
        args: list[str]=line.split(" ")


        if args[0] == "end":
            break


        elif args[0] == "criar":
            color = args [1]
            size = args [2]
            toalha = Toalha(color,size)


        elif args[0] == "mostrar":
            print(toalha)

        elif args [0] == "seca":
            if toalha.isdry():
                print("sim")
            else:
                print("nao")

        elif args[0] == "enxugar":
            amount: int = int(args[1])
            toalha.dry(amount)

        elif args[0] == "torcer":
            toalha.wringOut()

        else: 
            print("falhou: comando não encontrado")
main()