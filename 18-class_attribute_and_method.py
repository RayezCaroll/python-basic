# We can make same things with a blueprint by using Class.

class Car:
    steeringWheel=1 # Class level attribute # Save for same things
    def __init__(self,name,wheels):
        self.name=name # Instance level attribute # Save for different things
        self.wheels=wheels
    
    def drive(self):
        print(f'{self.name} is driving')

    @classmethod # Decorator
    def common(cls):
        print(f'All car has only {cls.steeringWheel} wheels.')


lambo=Car("Lamborghini",4)
lambo.drive() # Instance level method need to call with a viriable "marcedes"
lambo.steeringWheel
lambo.common()

# marcedes=Car("Marcedes",4)
# marcedes.drive() # Instance level method need to call with a viriable "marcedes"

print(Car.steeringWheel)
Car.common() # Class level method can call directly
