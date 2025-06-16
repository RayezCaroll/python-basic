# file=open('./text.txt')

# for line in file:
#     print(line)

# file.seek(0) # Move cursor to top of the file

# lineLists=file.readlines() # 
# print(lineLists)

# file.seek(50) # Move cursor to top of the file

# paragraph=file.read(100)
# print(paragraph)

# file.close() # To close opened file.

with open('./text.txt') as file: # Do not need to close the file again.
    for line in file:
        print(line)

print("Other Work") # Other Works will work properly.

