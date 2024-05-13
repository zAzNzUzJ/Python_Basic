# ################ -RegEX- ####################
# import re

# data=open("text.txt","r+")
# start_num=[]
# spl_char=[]
# start_num_underscore=[]
# start_num_uorw=[]
# start_num_uorallw=[]
# numbeforeat=[]
# anybeforeat=[]
# for i in data.readlines():
    
#     #print(re.search(r"^[\d]+[\w]+[@]+[\w]+[\.][\w]+", i,re.IGNORECASE) )

    
    
#     # if (re.search(r"^[\d]+[\w]+[@]+[\.\w]", i) is not None):
#     #     start_num.append(i)
#     # if (re.search(r"[\d \w]+[#`~!]+[\w \d]+[@]+[\.\w]", i) is not None):
#     #     spl_char.append(i)
#     # if (re.search(r"^[\d]+[_][\w]+[@]+[\.\w]+", i) is not None):
#     #     start_num_underscore.append(i)
#     # if (re.search(r"^[\d]+[_a-z]+[@]+[\.\w]+", i) is not None):
#     #     start_num_uorw.append(i)
#     # if (re.search(r"^[\d]+[_a-zA-Z]+[@]+[\.\w]+", i) is not None):
#     #     start_num_uorallw.append(i)
#     # if (re.search(r"[\w]+[\d][@]+[\.\w]+", i) is not None):
#     #     numbeforeat.append(i)
#     # if (re.search(r"[\d]+[\w\d]+[@]+[\.\w]+", i) is not None):
#     #     anybeforeat.append(i)
    
    
   
#     if (re.search(r"[\d \w]+[#`~!]+[\w \d]+", i) is not None):
#         spl_char.append(i)
#     if (re.search(r"^[\d]+[\w]+", i) is not None):
#         start_num.append(i)
#     if (re.search(r"^[\d]+[_][\w]+", i) is not None):
#         start_num_underscore.append(i)
#     if (re.search(r"^[\d]+[_a-z]+", i) is not None):
#         start_num_uorw.append(i)
#     if (re.search(r"^[\d]+[_a-zA-Z]+", i) is not None):
#         start_num_uorallw.append(i)
#     if (re.search(r"[\w]+[\d][@]+", i) is not None):
#         numbeforeat.append(i)
#     if (re.search(r"[\d]+[\w\d]+[@]+", i) is not None):
#         anybeforeat.append(i)
    
    
    
    
# print("\n\t 1) provide me the list of emails that do have special characters of #~`!")
# print("\n \t",spl_char)
# print("\n\t 2) provide me the list of emails that start with numbers")
# print("\n \t",start_num)
# print("\n\t3) provide me the list of emails that start with numbers followed by an underscore")
# print("\n \t",start_num_underscore)
# print( "\n\t 4) provide me the list of emails that start with numbers followed by an underscore or small case characters")
# print("\n \t",start_num_uorw)
# print("\n\t 5) provide me the list of emails that start with numbers followed by an underscore or small case characters or large case characters")
# print("\n \t",start_num_uorallw)
# print("\n\t 6) Provide me list of emails with only numbers before the @")
# print("\n \t",numbeforeat)
# print("\n\t 7) Provide me list of emails with numbers anywhere before the @")
# print("\n \t",anybeforeat)    
     
     
     
     
# def greeting ():
#     return "hello"
    
# # print( id(greeting()  )  )
# # print(greeting)

# # var = greeting
# # print(var)

# # Higher order function
# def enhanced_greeting(greeting_function , add_greeting):
#     return greeting_function() + add_greeting

# print(greeting())
# print(enhanced_greeting(greeting," You are  wonderful!"))

# # # another example Higher order 
# def enhanced_greeting_1(salutation):
    
#     def greeting_function():
#         return "Hello " + salutation
    
#     return greeting_function
# def greeting_function()_1("Mr"))
# print(enhanced_greeting_1("Mr")())
# print(enhanced_greeting_1("Miss")())


# # imperative functions

# def my_addition(num1,num2):
#     return num1+num2

# def my_sub(num1,num2):
#     return num1-num2


# print(my_addition(1,2))
# print(my_sub(1,2))

# # lambda functions
# add_lambda = lambda num1,num2: num1+num2
# print(add_lambda(1,2))

# sub_lambda = lambda num1,num2: num1-num2
# print(sub_lambda(1,2))

# # gen_lambda = lambda num1,num2,op: num1 op num2

# # HOF 
# def my_operator_definition(op):
#     if op == '+':
#         return lambda num1,num2: num1+num2
#     else:   
#         return lambda num1,num2: num1-num2

# print(my_operator_definition('+')(1,2))
# print(my_operator_definition('-')(1,2))
           
# def fun1():
#     print("FUNTION ")

#     def fun2():
#         print("sub")
        
#     fun2()   
# def cal(op,a,b):
#     if op=="+":
#         return a+b
#     if op=="-":
#         return a-b

# print(cal("+",1,2)  )
# fun1() 
        

    
