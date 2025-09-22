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
        return f"Cor:{self .color}, Tam:{self .size}, Umidade:{self .wetness}"

"""
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
        args: list[str]=line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "new":
            color = args [1]
            size = args [2]
            toalha = Toalha(color,size)
        elif args[0] == "show":
            print(toalha)
        elif args[0] == "dry":
            amount: int = int(args[1])
            toalha.dry(amount)
        else: 
            print("falhou: comando não encontrado")
main()