
#This is a comment !
def greeting(name: str) -> None:
    print("Hello", name, "!")

myName: str = "Samir"

greeting(myName)

myInt: int = 5

def add(numberOne: int, numberTwo: int) -> int:
    return numberOne + numberTwo

print(add(5, 7))