def matchCheck(arg1,arg2,arg3):
    
    arg1= int(arg1)
    arg2= int(arg2)
    arg3= int(arg3)

    if arg1== arg2:
        ans= True
    elif arg2== arg3:
        ans= True
    elif arg1== arg3:
        ans= True
    else:
        ans= False
    return ans 

arg1= 1
arg2= 2
arg3= 3

ans1= matchCheck(arg1,arg2,arg3)
print(ans1)

arg1= 1
arg2= 1
arg3= 2

ans2= matchCheck(arg1,arg2,arg3)
print(ans2)

arg1= 1
arg2= 2
arg3= "2"

ans3= matchCheck(arg1,arg2,arg3)
print(ans3)
