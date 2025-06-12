name="KyawZayarAung" # Global Variable

def sayMyName():
    age=12 #Local Code
    global name
    name="AungAung" # Override # Build a local variable
    print(name)
    name="KyawKyaw"
    print(name)
    print(age)

sayMyName()

print(name)
# print(age) # Cannot call Local from global # Error