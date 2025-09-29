class Animal:
    def __innit__( self, especies: str, sound: str):
        self.especies: str = especies
        self.sound: str = sound
        self.age: int = 0

    def __str__(self):
        return f"{ self.especies}:{ self.age}:{ self.sound}"
    
def main():
    animal: Animal = Animal("","")
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
    
    if args [0] == "end":
        break
    
    elif args [0] == "init":
        especies = args[1]
        sound = args[2]
        animal = animal(especies, sound)

    elif args [0] == "show":
        print(animal)

    elif args[0] == "grow":

    
     main()