# # add=lambda first_num,second_num: first_num+ second_num
# # sqr=lambda first_num: str(first_num**2)
# # exp=  lambda first_num,second_num: first_num**second_num
# # uppercase=lambda received_string: received_string.upper()
# # raise_sal= lambda existing_salary,raise_salary_percentage: existing_salary + (existing_salary*raise_salary_percentage/100) 
# # get_height= lambda height: round((height/30.48),2)
# # convert_to_rupee=lambda no_of_dollars:no_of_dollars*82
# # get_fare_details=lambda source, destination, fare_in_INR, discount_rate_percentage: ("Fare from " + source +" to " + destination + " is " + str(fare_in_INR- (fare_in_INR*discount_rate_percentage/100) ) + " INR with has a applied discount of " + str(discount_rate_percentage)+ "%")

# def option_fun(opt):
#     if opt==1:
#         return lambda first_num,second_num: first_num+ second_num
#     if opt==2:
#         return lambda first_num: str(first_num**2)
#     if opt==3:
#         return lambda first_num,second_num: first_num**second_num
#     if opt==4:
#         return lambda received_string: received_string.upper()
#     if opt==5:
#         return  lambda existing_salary,raise_salary_percentage: existing_salary + (existing_salary*raise_salary_percentage/100) 
#     if opt==6:
#         return  lambda height: round((height/30.48),2)
#     if opt==7:
#         return lambda no_of_dollars:no_of_dollars*82
#     if opt==8:
#         return lambda source, destination, fare_in_INR, discount_rate_percentage: ("Fare from " + source +" to " + destination + " is " + str(fare_in_INR- (fare_in_INR*discount_rate_percentage/100) ) + " INR with has a applied discount of " + str(discount_rate_percentage)+ "%")



# while True:
#     print("1- ADD ")
#     print("2- SQUARE ")
#     print("3 - EXPONENT ")
#     print("4- uppercase ")
#     print("5 - raise salary ")
#     print("6 - height to Feet ")
#     print("7- USD-INR ")
#     print("8 - TAXI FARE ")
#     print(" 10 - EXIT ")
    
#     opt=int(input("ENter the opt : "))
#     if opt==1:
#         x=int(input("ENter the number 1 : "))
#         y=int(input("Enter 2nd Number   : "))
#         print(option_fun(opt)(x,y)) 
#         #print(add(x,y))
#     if opt==2:
#         x=int(input("ENter the number 1 : "))
#         print(option_fun(opt)(x))
#     if opt==3:
#         x=int(input("ENter the number 1 : "))
#         y=int(input("Enter 2nd Number   : "))
#         print(option_fun(opt)(x,y))
#     if opt==4:
#         x=input("ENter the lowercase string : ")
        
#         print(option_fun(opt)(x))
#     if opt==5:
#         x=int(input("ENter the Existing sal : "))
#         y=int(input("Enter raise %   : "))
#         print(option_fun(opt)(x,y))
#     if opt==6:
#         x=int(input("ENter the height : "))
#         print(option_fun(opt)(x))
#     if opt==7:
#         x=int(input("ENter the dollar amt : "))
#         print(option_fun(opt)(x))
#     if opt==8:
#         x=input("ENter Source  : ")
#         y=input("Enter Destination   : ")
#         z=int(input("ENter fare  : "))
#         a=int(input("Enter discount %   : "))
#         print(option_fun(opt)(x,y,z,a))
#     if opt==10:
#         print(" EXIT ")
#         break



###########################################################################################################################
############################################################################################################################
#######################  NUMPY #####################

import numpy as np

# a=[[1,2,3],[4,5,6],[7,8,9]]
# print(a[0][2]) 

# for i in range(3):
#     for j in range(3): 
#         print(a[i][j],end=" ")
#     print("\n ")
    
    # 
# b=np.arange(2048)
# b=np.array(b).reshape(2,2,2,2,2,2,2,2,2,2,2)
# print(b)


# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             for l in range(2):
#                 print(b[i][j][k][l],end=" ")
#             print(" __ ",end=" ")
#         print(" + + ",end=" ")
#     print("\n ")
      