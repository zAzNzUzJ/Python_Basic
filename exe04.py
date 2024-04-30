import funtions04 as cal

# while True :
#     c=input("\n########### MENU ###########  \n # 1- SUM \n # 2- Suqare of number \n # 3- Get Exponentaion \n # 5- 'exit'or '5' to exit \n ########### @@@@@ ########### \n Enter the Options: ")
#     if c=="exit" or c=="5":
#         print ("# ..EXIT.. #")
#         break
#     else:
#         cal.my_calculator(c)
    
# n=int(input(" Enter the  number to find Sum of n numbers :"))
# print (" Sum of 1st n Number is : ",cal.sumofall(n))
# print (" ODD numbers in 1st n N number is : ")
# cal.oddofall(n)
# print (" EVEN numbers in 1st n N number is : ")
# cal.evenofall(n)
##################################
####---Stone-Paper-Scissors---####2

##################################
##-- 1 - Stone                --##
##-- 2 - Paper                --##
##-- 3 - Scissors             --##
##-- 5 - EXIT                 --##
##################################
user1=0
system1=0
while True :
    c=input(" ################################## \n ####---Stone-Paper-Scissors---####\n ################################## \n ##-- 1 - Stone                --## \n ##-- 2 - Paper                --## \n ##-- 3 - Scissors             --## \n ##-- 5 - EXIT                 --##\n ################################## \n \t###############\t \n Enter the Options: ")
    if c=="exit" or c=="5":
        
        print("###############################\n######### FINAL SCORE #########\n###############################\n######### USER --   ",user1,"#######\n######### SYSTEM -- ",system1,"#######\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n")
        if user1>system1:
            print(" ###############################\n ---$$$--- USER WINS ---$$$--- \n ###############################\n")
        elif user1<system1:
            print(" ###############################\n ---$$$--- SYSTEM WINS ---$$$--- \n ###############################\n")
        else:
            print(" ###############################\n ---$$$--- DRAW MATCH ---$$$--- \n ###############################\n")
            
        print ("\n # ..EXIT.. #")
        break
    else:
        if c=="1":
            user1,system1=cal.stonepaper("stone",user1,system1)
        elif c=="2":
            user1,system1=cal.stonepaper("paper",user1,system1)

        elif c=="3":
            user1,system1=cal.stonepaper("scissors",user1,system1)

        else:
            print ("\n OUT PUT : \n \t\t\t!!! ERROR NOT A VALID OPTION !!!")
            
            
#######################################################################################

# x=input("Enter 1st list the elements comma seperated : ").split(",")
# y=input("Enter 2nd list the elements comma seperated : ").split(",")
# print(cal.listoverlap(x,y))
###############################################################

