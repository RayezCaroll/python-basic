# with open('./about.txt','w') as file: # Override existing file contents
#     # file.write("I am student")
#     file.write()


# print('other work')

# with open('./about.txt','a') as file: # Append contents to file
#     # file.write("\nI am 28 years old")
#     file.write("\nI am 28 years old")

lists=["I am student","\nI am 28 years old"]

with open('./about.txt','w') as file:
    file.writelines(lists)

