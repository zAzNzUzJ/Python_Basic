def my_calculator(n):
    
    if n=="1":
        x=int(input(" Enter the  1dt number :"))
        y=int(input(" Enter the  2nd number :"))
        print("\n OUT PUT : \n The Addition of the numbers is ",x+y)
    elif n=="2":
        x=int(input(" Enter the number to be squared :"))
        print("\n OUT PUT : \n The Square of the number is ",x**2)
    elif n=="3":
        x=int(input(" Enter the  1dt number :"))
        y=int(input(" Enter the  2nd number :"))
        
        print("\n OUT PUT : \n \t\tThe exponenation of the numbers is ",x**y)
    else:
        print ("\n OUT PUT : \n !!! ERROR NOT A VALID OPTION !!!")

def sumofall(x):
    sum=0
    for i in range(x+1):
        sum=sum+i 
    return sum

def oddofall(x):
    for i in range(1,x+1,2):
        print ("-- ",i)
    return 0
def evenofall(x):
    for i in range(0,x+1,2):
        print ("-- ",i)
    return 0


###############################################################################
import random
def stonepaper(x,s1,s2):
    user=s1
    system=s2
    li=["stone","scissors","paper"]
    y=random.choice(li)
    if x==y:
        print(" \n ----------------------------------\n ||\tuser :   ",x,"\t ||")
        print(" ||\tSystem : ",y,"\t ||")
        print("----------------------------------")
        print(" ||\tx--- DRAW ---x\t ||")
        print("----------------------------------")
    elif x!=y:
        print(" \n ----------------------------------\n ||\tuser :   ",x,"\t ||")
        print(" ||\tSystem : ",y,"\t ||")
        if (x=="stone" and y=="scissors") or (x=="scissors" and y=="paper") or (x=="paper" and y=="stone") :
            print("----------------------------------")
            print(" ||\t$$-- ^_^ USER WINS ^_^ --$$\t ||")
            print("----------------------------------\n\n")
            user=user+1
        elif (y=="stone" and x=="scissors") or (y=="scissors" and x=="paper") or (y=="paper" and x=="stone") :
            print("----------------------------------")
            print(" ||\t$$-- *_* SYSTEM WINS *_* --$$\t ||")
            print("----------------------------------\n\n")
            system=system+1
    print("###############################\n######### FINAL SCORE #########\n###############################\n######### USER --   ",user,"########\n######### SYSTEM -- ",system,"########\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n")
    return user,system

####################################################################################    
####################################################################################


def listoverlap(a,b):
    list=[]
    for i in (b):     
        if i in a and i not in list:
            list.append(i)
    return list
        

###############################################################################
