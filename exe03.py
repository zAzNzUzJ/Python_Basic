
#DAY3
#---------------IF __ELSE------------------



def fun(x):
    if x%3==0 and x%5==0:
        print ("****FIZZ BUZ***")
    elif x%5==0:
        print("***BUZZ***")
    elif x%3==0 :
        print("***FUZZ***")
    else:
        print("xxxxINVALID INPUTxxxx")



#--------------------LOOPS----- WHILE---&&&----FOR-------------


while True :
    x=input("Enter the number to play -- 'exit' to exit: ")
    if x!="exit":
        fun(int(x))
    else:
        break