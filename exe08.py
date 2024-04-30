#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###################################################################################################
######################################## FILE HANDLING ############################################
###################################################################################################
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#




# file1 = open('my_first_file.txt','rt')
# print(file1.read())
# print("Before closing explicitly" , file1.closed)  
# file1.close()
# print("After closing explicitly" , file1.closed)  

# no need to close if we use with context
# print("Read call below \n -----------------------")

# file1=open('my_first_file.txt',"r")
# print("Before coming out of with block " , file1.closed)   
# print(file1.read())
# file1.close()
# print("After coming out of with block " , file1.closed)   

# print("Readline call below \n -----------------------")
# with( open('my_first_file.txt',"r") as file1):
#     print(file1.readline(),end= "---\n")

# print("Readlines call below \n -----------------------")
# with( open('my_first_file.txt',"r") as file1):
#     print(file1.readlines(),end= "---\n")


# print(r" strip off those \n at the end of the list ")
# with ( open('my_first_file.txt',"r") )as file1:
#     lines = []
#     for line in file1:
#         lines.append(line.strip())
# print(lines)        

# print(" Write to a file in w mode ")
# with ( open('my_first_file.txt',"w") as file1):
#     file1.write("hi there \nhow are you doing ")

# print(" Write to a file in a mode ")
# with ( open('my_first_file.txt',"a") as file1):
#     file1.write("\nThis a new line ")

# # read is the primary functionality write is just added as secondary
# with( open('my_first_file.txt',"r+") as file1):
#     print(file1.read())
#     file1.write("\nI am writing")
  
# # write is primary read is secondary functionality
# with( open('my_first_file.txt',"w+") as file1):
#     print(file1.read())
#     file1.write("hello")

# # append is the primary objective , read functionality is added
# with( open('my_first_file.txt',"a+") as file1):
#     file1.write("I appended this line in append+ mode")
#     file1.seek(0)
#     print(file1.read())


# # Python program to demonstrate  opening a file in binary mode
# file1 = open('my_first_file.txt',"rb")
# print(file1.read())
# file1.close()

# # Python program to demonstrate  writing a file in binary mode
# file1 = open('my_first_file.txt',"w+b")
# file1.write(b'how are you doing')
# file1.close()

# """
# # Key takeaways
# 1) Open => ( read / write / append) => close 
# 2) open modes ( r,w,a,x,r+,w+,a+)
# 3) text / binary format
# """

# #lets you know if the file handle is closed or not 
# print(file1.closed)

# # Python program to demonstrate  opening a file with some exception handling
# try:
#     file1 = open('my_first_file.txt',"r")
#     print("I am reading the existing file -->\n", file1.read())
# except FileNotFoundError:
#     print("File Not present , I am goind ahead and creating a file for you with some default text !!! ")    
#     file1 = open('my_first_file.txt',"w+")
#     file1.write("AB")
#     # file1.writelines(['first_line\n','second_line\n','third_line'])
    
#     print("I am location ", file1.tell())
#     print("I am resetting it at 0 " , file1.seek(0))
#     print("I am location after resetting ", file1.tell())
#     print("I am reading just after writing-->", file1.read())
#     file1.close()

# """ exercises"""
# ## 1: write a program to take some text lines from the user and write it to the file
# with( open("my_first_file.txt","w+") as file1):
#     while True:
#         x=input("Enter the text to write (exit to stop): ")
#         if x!="exit":
#             file1.write(x+"\n")
#         elif x=="exit":
#             break

# # ## 2: write a program to read from a file and write to another file 
# with( open('my_first_file.txt',"r+") as file1):
#     with( open('my_first_file02.txt',"w+") as file2):
#         for i in file1.read():
#             file2.write(i)

# # ## 3: Write a program to read from a file and modify its content 
# # ## by pre-pending each line with "HPCAP" 

# temp=[]
# with( open('my_first_file.txt',"r+") as file1):
#         for i in file1.readlines():
#                temp.append("HPCSA "+i)
# with( open('my_first_file.txt',"w+") as file2):
#     for i in temp:
#         file2.write(i)
 ######################################################################
 #########################################3       
# file1=open('my_first_file.txt',"r+")
# x=file1.read()
# print(x)
# file1.close()
 

# # ## 4: Write a program to read from a file, pre-pending each line with "HPCAP" 
# # ## and write to the different file 


# with( open('my_first_file.txt',"r+") as file1):
#     with( open('my_first_file02.txt',"w+") as file2):
#         for i in file1.readlines():
#                file2.write("HPCSA "+i)


#######################################################################################################

# import json

# # The json.load() function reads a JSON file and parses it into a Python dictionary.
# with open("person.json", "r") as fh:
#     data = json.load(fh)
    
# print(data)    



# # The json.dump() method directly writes a Python dictionary to a file in JSON format.
# with open("person_copy.json", "w") as outfile:
#     json.dump(data, outfile)


#############################################################
##################### _OOPS_ ################################
#############################################################

# class Student:
#     school_name    = "CDAC"
    
#     @classmethod
#     def get_my_school_name(cls):
#         return cls.school_name
    
#     def __init__(self,rcv_name) -> None:
#         print(self)
#         self.name = rcv_name
    
#     def get_my_name(self):
#         return self.name  
    
#     @staticmethod
#     def my_static_method():
#         print("some task related to the class ")  

# # object var createdJN
# gaurav= Student("GAURAV")
# gaurav_copy= Student("GAURAV_COPY")

# print(gaurav.get_my_name())
# print(gaurav_copy.name)

# print(Student.get_my_school_name())
# print(gaurav.school_name)

# Student.my_static_method()
# gaurav.my_static_method()

##################Exercise 01####################################
# class Employee:
#     department_name = "HR"
#     def __init__(self,emp_id,emp_salary,mgr_id):
#         self.Employee_id = emp_id
#         self.Employee_salary = emp_salary
#         self.Manager_id = mgr_id
#         print(f"{self} was created successfully with values {emp_id},{emp_salary},{mgr_id}")
        
#     def get_emp_salary(self):
#         return self.Employee_salary
    
#     def set_emp_salary(self,rcv_salary):
#         self.Employee_salary = rcv_salary
    
#     @classmethod
#     def get_department_name(cls):
#         return cls.department_name

#     @staticmethod
#     def field_expertise():
#         print ("We are the boss")

# def main():
#     arjun = Employee(100,1000,1)
#     print ("ID",arjun.Employee_id)
#     print ("Salary",arjun.Employee_salary)
#     print ("Manager ID",arjun.Manager_id)
    
#     arjun.set_emp_salary(10000)
#     print ("After Setting",arjun.Employee_salary)
    
#     print(arjun.get_department_name())
#     arjun.field_expertise()
#     # del Employee
#     print ("ID",arjun.Employee_id)
    
# print(__name__)
# if __name__ == "__main__":
#     main()

###############Exercise 02##########################
import random
class Airticket:
    def __init__(self,fli_no,seat_no):
        self.flight_number=fli_no
        self.seat_number=seat_no
        
    def show_details(self):
        print("Here are your booking details")
        print("Your departure is from",self.departure)
        print("Your arrival city is",self.arrival_city)
        print("Your Flight number is",self.flight_number)
        print("Your seat number is",self.seat_number)
        
    def set_location(self):
        self.departure=input("Enter your departure")
        self.arrival_city=input("Enter your arrival city")
        
        
    @staticmethod
    def message():
        print("Happy Journey")
        
def main():
    n=0
    a=[]
    while True:
        print("#############################################################")
        print("##        --- TICKET BOOKING ---                           ##")
        print("##---1-- MULTIPLE TICKET                                   ##")
        print("##---2-- DISPLAY ALL TICKETS                               ##")
        #print("##---3-- DELETE ALL TICKETS                               ##")
        print("##---5-- EXIT                                              ##")
        print("#############################################################")
        c= input("ENter the choice :")
        if c=='1':
            n=int(input("\n  Enter the Number of ticket : "))
            
            for i in range(n):
                print("\n BOOK TICKET FOR CUSTOMER_",i+1)
                i=Airticket(random.randrange(10000,99999),str(random.randrange(1,40))+random.choice(['A','B','C','D']))
                i.set_location()
                i.show_details()
                i.message()
                a.append(i)
        elif c=='2':
            for i in range(n):
                print("   -- CUSTOMER --   ",i+1)
                print("----------------------")
                a[i].show_details()
        
                  
                
            
            
                
            # passenger2 = Airticket(random.randrange(10000,99999),str(random.randrange(1,40))+random.choice(['A','B','C','D']))
            # passenger2.set_location()
            # passenger2.show_details()
            # passenger2.message()
        elif c=='5':
            
            break
        else:
            print(" \n INVALID OPTION ")
            
main()