with open('./text.txt') as file:
    paragraph=file.read()

    paraCount=int(input('Paragraph count: ')) # String to int

    for count in range(paraCount):
        with open('./generator.txt','a') as write_file:
            write_file.write(paragraph+'\n\n')

