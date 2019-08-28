myUniqueList= []
myLeftovers= []

def listParse(input):
    test= False
    for i in myUniqueList:
        if i== input:
           test= True
    if test== True:
        myLeftovers.append(input)
    elif test== False:
        myUniqueList.append(input)
    print(myUniqueList)
    print(myLeftovers)
    print()
    
myUniqueList.append(1)
print(myUniqueList)
print()

listParse(1)
listParse(2)
listParse(4)
listParse(6)
listParse(4)

