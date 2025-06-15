# Filter # usage = to manage some parts of list
nums=[1,2,3,4,5,6,7,8,9,10]

# filter(function,list)
def even(num):
    return (num%2)==0

evenNums=list(filter(even,nums))
print(evenNums)

print('--------------')

# Comprehension
values=[1,2,3,4,5,6,7,8,9,10]
values=[value for value in values if (value%2)==0]
print(values)

print('--------------')

# For loop
lists=[1,2,3,4,5,6,7,8,9,10]
evenLists=[]
for list in lists:
    if (list%2)==0:
        print(list)
        evenLists.append(list)
print(evenLists)