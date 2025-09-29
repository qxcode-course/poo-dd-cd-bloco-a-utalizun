class Animal:
    def __init__( self, especies: str, sound: str):
        self.especies: str = especies
        self.sound: str = sound
        self.age: int = 0


    
    def makesound(self) -> None:
        if self.age >= 4:
            print ("RIP")
        if self.age == 0:
            print ("---")
        if self.age > 0 and self.age < 4:
            print (self.sound)

    def ageBy(self, increment: int) -> None:
        self.age += increment
        if self.age > 4:
            self.age = 4 

    def __str__(self) -> str:
        return f"{self.especies}:{self.age}:{self.sound}"

          
    
def main():
    animal: Animal = Animal("", "")
    while True:
        line = input()
        args: list [str] = line.split(" ")
        print("$" + line)
    
        if args [0] == "end":
            break
    
        elif args [0] == "init":
            especies = args[1]
            sound = args[2]
            animal = Animal(especies, sound)

        elif args [0] == "show":
            print(animal)

        elif args[0] == "grow":
            increment: int = int (args[1])
            animal.ageBy(increment)
            if animal.age == 4:
                    print(f"warning: {animal.especies} morreu")
        elif args[0] == "noise":
            animal.makesound()
        else: 
            print("fail: comando invalido")
    
main()