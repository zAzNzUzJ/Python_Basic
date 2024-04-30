#############################
############ SETS ###########
#############################
import funtions06 as s
#union,difference,intersection,mutal difference

# a={4,2,3,1,6}
# b={4,5,2,6}

# print(set.issuperset(a,b))
# print(a.union(b))
# print(set.symmetric_difference(a,b))
# set.issubset
# set.isdisjoint

# my_copy_set = set()
# my_copy_set.add(1)
# print(my_copy_set)

# a=input("Enter the A set elements : ").split(",")
# b=input("Enter the B set elements : ").split(",")
# x=set()
# y=set()
# for i in a:
#    x.add(int(i))
# for i in b:
#    y.add(int(i))
    
# print(x,"\n",y)

# s.my_set_store(x,y)


##########################################################################
#################################### SCOPE VAR ###########################
##########################################################################                                    



# var = 10
# m= 10
# print("global variable var: ", var)

# def return_global_m():
#     return m

# def f():
#     # local variable to f() # enclosed variable to f1()
#     var1= 100
#     m=100
#     print("enclosed variable var1: ", var1)
#     print("just defined m: ", m)
    
#     def f1():
#         # local variable to f1()
#         var2= 1000
#         # nonlocal m # this line tells python that do not create a local variable 
#         global m # tells python use global variable
#         m=1000
#         print("local variable var2: ", var2)
#         print("m: ", m)
#     f1()    
#     print("after calling f1() local m: ", m)
#     print("after calling f1() Global m: ",  return_global_m() )    
# f()    

#####################################################################
######################### EXception HANDELING #######################
#####################################################################

"""-----------
Exception Handling
https://docs.python.org/3/library/exceptions.html#exception-hierarchy
----------------"""
# scratch example:

# def f1():
#         print(1+"hello")

# def f ():
#     try:
#         f1()
#     except Exception:
#         print("I am inside except block")    

# f()


# without exceptions code 
# input_var = int(input("Please enter a number "))
# print("Adding 10 to your value entered is " , input_var+ 10)

# with exceptions code to demonstrate need of exceptions
# try:
#     input_var = int(input("Please enter a number "))
# except Exception:
#     try:
#         input_var = int(input("You entered an incorrect number , Please try again ! "))
#     except :
#         input_var = int(input("You stupid please enter a number"))    
# print("Adding 10 to your value entered is " , input_var+ 10)
    

# # with exceptions code  for a function to demonstrate exception propogation 
# def my_simple_fun():
#         return f"Adding 10 to your value entered is  {int(input('Please enter a number '))+ 10}"
        
# try:
#     print(my_simple_fun())
# except Exception:
#     try:
#         print(my_simple_fun())
#     except :
#         print(my_simple_fun())


# # with exceptions code  for a function but with other exception to demonstrate exception matching
 
# # a function within a function to demonstrate exception propogation
# def inner_simple_func():
#     return f"Adding 10 to your value entered is  {int(input('Please enter a number '))+ 10}"

# def my_simple_fun():
#         print("Doing Nothing here -- just try to handle exception if possible ")
#         return inner_simple_func()
        
# try:
#     print(my_simple_fun())
# except ImportError:
#     try:
#         print(my_simple_fun())
#     except :
#         print(my_simple_fun())
# def files(a):
#     pass

# while True:
#     try:
#         i = int(input('Select: '))
#         if i in range(4):
#             files(i)
#             break
#     except:    
#         print ("except")

#     print('\nIncorrect input, try again')


##########################################################################
#Q1
###############################################################33


# k1=input("Enter the keys in number : ").split(",")
# dict1={}
# for i in k1:
#    dict1[int(i)]=input("Enter the value for - "+i+" : ")
# print(dict1)
# s.findcol(dict1)

##########################################################################
#Q2
###############################################################
# lis=[]
# for i in range(5):
#    lis.append(input("ENter the element for -"+str(i)+" :"))
# s.findind(lis)

##########################################################################
#Q3
###############################################################

# age=int(input("Enter the Age ::: "))
# #print("YOU LIved = ",365*age)
# class my_exception(Exception):
#     pass
# #s=" 0"
# try:
#    if 365*age<100001:
#       print(365*age)
#    else:
#       #s+=age
#       raise my_exception
# except :      
#    print("  YOU LIVED FOR SO LONG  WILL DIE SOON BIEEEEEEE!!!")
   
##########################################################################
#Q4
# ###############################################################
# class negative_number_error(Exception):
#    pass
# class positive_number_error(Exception):
#    pass
# class homogenous_list_error(Exception):
#    pass


# def create_positive_numbered_list(my_int_list1):
#    while True:
#       p=input("Enter the positive number :(exit to close) ")
#       if p!="exit":
#          my_int_list1.append(int(p))
#       else:
#          break      
#    for i in my_int_list1:
#       if i <0:
#          raise negative_number_error
   
#    print(my_int_list1)
      
      
# def create_negative_numbered_list(my_int_list2):
#    while True:
#       p=input("Enter the Negative number :(exit to close) ")
#       if p!="exit":
#          my_int_list2.append(int(p))
#       else:
#          break
#    for i in my_int_list2:
#       if i >0:
#          raise positive_number_error
      
#    print(my_int_list2)
      
      
# def create_heterogenous_list(my_het_list3):
#    ty=type(my_het_list3[0])
#    for i in range(1,len(my_het_list3)):
#       if ty!=type(my_het_list3[i]):
#          raise homogenous_list_error
     
#    print(my_het_list3)
      
      
    
    
    

# def my_exception_store(): 
#     my_int_list1=[]
#     my_int_list2=[]
#     my_het_list3=[1,2,3,4,"abc"]

#     while(True):
#         try:
#             print("Welcome to my_exception_store !!!!")
#             print("-------------------------------------")
#             print("Following operations are supported :")
#             print("1) Create a positive numbered list  ")
#             print("2) Create a negative numbered list  ")
#             print("3) Create a heterogenous list ")
#             print("4) Refresh the program to start with blank lists")
#             print("5) Exit  ")
            
#             choice = int(input("Please enter your choice !!!! "))
#             if choice ==1:
#                 create_positive_numbered_list(my_int_list1)
#             elif choice ==2:
#                 create_negative_numbered_list(my_int_list2)
#             elif choice ==3:
#                 create_heterogenous_list(my_het_list3)
#             elif choice ==4:
#                 my_int_list1.clear()
#                 my_int_list2.clear()
#                 my_het_list3.clear()
#                 print("Store restarted !!!! ")
#             elif choice ==5:
#                 break
#             else:
#                 print("Please choose something from the above")
#         except negative_number_error:     
#             print("We received a negative number in the list and I handled negative_number_error exception")
#             my_int_list1.clear()
#         except positive_number_error:     
#             print("We received a positive number in the list and I handled positive_number_error exception")
#             my_int_list2.clear()
#         except homogenous_list_error:    
#             print("We received a Homogenous list and I handled homogenous_list_error exception")
#             my_het_list3.clear()
            
# my_exception_store()   
   
   
   ######################################################################################################
   
   
   
class negative_number_error(Exception):
    pass

def create_positive_numbered_list(my_list):
    """
    1) Create a postive numbered list 
    Note : raise an exception if the users inserts a negative number OR user creates an empty list 
    """
    for cntr in range(0,int(input("Please enter number of elements to the positive numbered list"))):
        num = int(input("Please enter a number to be added ")) 
        if (num ) <0:
            raise  negative_number_error
        else:
            my_list.append(num)
    print(my_list)   

# my custom exception created 
class positive_number_error(Exception):
    pass

def create_negative_numbered_list(my_list):
    """
    2) Create a negative  numbered list 
    Note : raise an exception if the users inserts a positive number/Zero OR user creates an empty list
    """
    for cntr in range(0,int(input("Please enter number of elements to the negative numbered list"))):
        num = int(input("Please enter a number to be added "))
        if num >0:
            raise  positive_number_error
        else:
            my_list.append(num)
    print(my_list)   

# my custom exception created 
class homogenous_list_error(Exception):
    pass



def value_provider(element):
    datatype_choice = int(input(f"Please choose a datatype of the {element} to be added \
        \n 1) int \n 2) float \n 3) str \n 4) tuple \n 5) list \n 6) set \n 7) dictionary \n "))

    if datatype_choice == 1:
        ret_val = int(input("Please enter an integer to be added "))
    if datatype_choice == 2:
        ret_val = float(input("Please enter a float to be added "))
    if datatype_choice == 3:
        ret_val = input("Please enter a string to be added ")
    if datatype_choice == 4:
        ret_val = tuple(input("Please enter a tuple to be added like 1,2 ").split(","))
    if datatype_choice == 5:
        ret_val = input("Please enter a list to be added like 1,2,3,4 ").split(",")
    if datatype_choice == 6:
        ret_val = set(input("Please enter a set to be added like 1,2 ").split(","))
    if datatype_choice == 7:
        my_temp_dict = {}
        keys = input("Please enter the keys of the dictionary to be added like key1,key2 ").split(",")
        for key in keys : 
            my_temp_dict[key] = value_provider('key'+key)
        ret_val = my_temp_dict
    return ret_val

def create_heterogenous_list(my_list):
    """    3) Create a heterogenous list 
    Note : raise an exception if the users creates a homogenous list (all elements of same datatype)
    """
    for cntr in range(0,int(input("Please enter number of elements to the heterogenous list"))):
        my_list.append(value_provider('Index'+str(cntr)))
    print(my_list)   
    
    # check if we are have a homogenous list  
    is_homogenous = True
    for subscript in range(1,len(my_list)):
        if  type(my_list[0]) != type(my_list[subscript]):
            is_homogenous = False
            break
        
    if is_homogenous:
        raise homogenous_list_error
    else:
        print("We received a Heterogenous list ")       

def find_an_element(my_list):
    
    datatype_choice = int(input("""Please choose a datatype of the element to be searched \n 1) int \n 2) float \n 3) str \n 4) tuple \n 5) list \n 6) set \n 7) dictionary \n """))

    print(datatype_choice)
    if datatype_choice == 1:
        input_val = int(input("Please enter an integer  "))
    if datatype_choice == 2:
        input_val = float(input("Please enter a float "))
    if datatype_choice == 3:
        input_val = input("Please enter a string ")
    if datatype_choice == 4:
        input_val = tuple(input("Please enter a tuple like 1,2 ").split(","))
    if datatype_choice == 5:
        input_val = input("Please enter a list like 1,2,3,4 ").split(",")
    if datatype_choice == 6:
        input_val = set(input("Please enter a set like 1,2 ").split(","))
    if datatype_choice == 7:
        my_temp_tuple_list = []
        for str_elem in input("Please enter a dictionary like key1:value1,key2:value2 ").split(","):
            my_temp_tuple_list.append(tuple(str_elem.split(":")))
            input_val = dict(my_temp_tuple_list)
    
    print(f"{input_val} found in provided list {my_list} : {input_val in my_list}")
    
# invocation 

def my_exception_store(): 
    my_int_list1=[]
    my_int_list2=[]
    my_het_list3=[]

    while(True):
        try:
            print("Welcome to my_exception_store !!!!")
            print("-------------------------------------")
            print("Following operations are supported :")
            print("1) Create a positive numbered list  ")
            print("2) Create a negative numbered list  ")
            print("3) Create a heterogenous list ")
            print("4) Refresh the program to start with blank lists")
            print("5) Exit  ")
            
            choice = int(input("Please enter your choice !!!! "))
            if choice ==1:
                create_positive_numbered_list(my_int_list1)
            elif choice ==2:
                create_negative_numbered_list(my_int_list2)
            elif choice ==3:
                create_heterogenous_list(my_het_list3)
            elif choice ==4:
                my_int_list1.clear()
                my_int_list2.clear()
                my_het_list3.clear()
                print("Store restarted !!!! ")
            elif choice ==5:
                break
            else:
                print("Please choose something from the above")
        except negative_number_error:     
            print("We received a negative number in the list and I handled negative_number_error exception")
            my_int_list1.clear()
        except positive_number_error:     
            print("We received a positive number in the list and I handled positive_number_error exception")
            my_int_list2.clear()
        except homogenous_list_error:    
            print("We received a Homogenous list and I handled homogenous_list_error exception")
            my_het_list3.clear()
            
my_exception_store()    

