# map Functrion # To override list

nums=[2,5,6,7,8,9,10]
# map(function,list)
def mapFunction(num):
    return num*2

nums=list(map(mapFunction,nums))
print(nums)

# Comprehension way
values=[2,5,6,7,8,9,10]
values=[value*2 for value in values]
print(values)