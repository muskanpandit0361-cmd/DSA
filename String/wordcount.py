string="This is a sentence"
space=0
wordcount=0
if string=="":
    print("Empty String")
else:    
    for i in string:
        if (i==" "):
            space+=1
    wordcount=space+1
    print(wordcount)        

