words=['apple','orange','lemon','lime','banana']

from random import randint #### 3rd

def randomSentenceGenerator(word): #### 2nd
    rnadomIndex=randint(0,len(words)-1) #### 45h
    return f'{words[rnadomIndex]} {word}' # Will go to list(map(randomSentenceGenerator,wordLists)) as List.

with open('./text.txt') as file: #### 1st
    paragraph=file.read()
    wordLists=paragraph.split()
    sentenceList=list(map(randomSentenceGenerator,wordLists))

    paraCount=int(input('Paragraph count: ')) # String to int #### 5th
    for count in range(paraCount):
        with open('./generator.txt','a') as write_file:
            write_file.write(''.join(sentenceList)+'\n\n')

