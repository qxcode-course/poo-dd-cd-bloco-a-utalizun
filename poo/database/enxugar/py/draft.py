class Toalha:
    def __init__ (self, cor: str, tamanho: str): #construtor
        self.cor: str = cor #atributos
        self.tamanho: str = tamanho
        self.umidade: int = 0

    def dry(self, amount: int) -> None:
        self.umidade += amount
        if self.umidade >= self.getMaxWetness():
            print("toalha encharcada")
            self.umidade = self.getMaxWetness()

    def getMaxWetness (self) -> int:
        if self.tamanho == "P":
            return 10 
        if self.tamanho == "M":
            return 20
        if self.tamanho == "G":
            return 30
        return 0
    
    def __str__ (self) -> str:
        return f"Cor: { self.cor }, Tamanho: { self.tamanho }, Umidade: { self.umidade }"

    def isdry (self) -> bool:
     return self.umidade == 0

    def wringOut (self) -> None :
        self.umidade = 0


def main():
    toalha = Toalha( "" , "") 
    while True: #loop infinito 
        line: str = input()
        print ("$" + line)
        args: list[str]=line.split(" ")


        if args[0] == "end":
            break


        elif args[0] == "criar":
            cor = args [1]
            tamanho = args [2]
            toalha = Toalha( cor, tamanho )


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
if __name__ == "__main__":
    main()