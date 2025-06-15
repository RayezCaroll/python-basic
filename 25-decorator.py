# Decorator is a function that we can use to specify jobs before and after our normal function.
def greet(fun):
    def wrapper(name):
        # Before
        print('hello')
        fun(name)
        # After
        print('Have a nice day')
    return wrapper

@greet
def sayName(name):
    print(name)

sayName("Kyaw Zayar Aung")