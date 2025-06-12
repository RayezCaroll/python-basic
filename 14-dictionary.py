person={
    'name':'kyawzayaraung',
    'age':20
}

print(person['name'])
print(person['age'])

person['hair_color']="black"

print(person)

# in keyword
print("name" in person)
print("something" in person)

if "name" in person:
    print('work')

if "fdsa" in person:
    print('work')

# Key to List
person_keys=list(person.keys())
print(person_keys)

person_values=list(person.values())
print(person_values)