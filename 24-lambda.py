# Lambda function # use case for small functions
# def add(n1,n2):
#     return n1+n2

add=lambda n1,n2:n1+n2 # can add to variable

print(add(4,5))

# With filter function
nums=[1,2,3,4,5,6,7,8,9,10]
evenNums=list(filter(lambda num: (num%2)==0,nums))
print(evenNums)

# With map
lists=[1,2,3,4,5,6,7,8,9,10]
doubleList=list(map(lambda list:list*2,lists))
print(doubleList)