# We can make same things with a blueprint by using Class.

name="Kyaw Zayar Aung"
print(name.upper())
print("-----------")

class Car:
    def __init__(self,name,wheels):
        self.name=name
        self.wheels=wheels
    
    def drive(self):
        print(f'{self.name} is driving')

lambo=Car("Lamborghini",4)
print(lambo.name)
print(lambo.wheels)
lambo.drive()

marcedes=Car("Marcedes",4)
marcedes.drive()