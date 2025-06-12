from Car.carmodule import Car
from Car.function import checkEngine

lambo=Car("lamboghini",4)
print(lambo.name) # From Car/carmodule.py

checkEngine() # From Car/function.py










# ----------------------------------------

# from carmodule import Car # carmodule.py

# lambo=Car("Lamborghini",4)
# lambo.drive() # Instance level method need to call with a viriable "marcedes"
# lambo.steeringWheel
# lambo.common()

# marcedes=Car("Marcedes",4)
# marcedes.drive() # Instance level method need to call with a viriable "marcedes"

# print(Car.steeringWheel)
# Car.common() # Class level method can call directly