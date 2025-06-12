person={}

while True:
    name=input("name: ")
    age=input("age: ")

    person[name]=age

    another=input("another y/n")
    if another == 'y':
        continue
    else:
        break

print(person)

print(person.items())

for (key,value) in person.items():
    print(f'{key} is {value} years old.')
