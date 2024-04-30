class Employee:
    organisation_name=""
    def __init__(self):
        self.emp_id=""
        self.name=""
        self.base_location=""
        self.deployed_location=""
        self.designation=""
        self.salary=""
      
    def set_emp_details(self,eidn,name,base,dep,des,sal):
        self.emp_id=eidn
        self.name=name
        self.base_location=base
        self.deployed_location=dep
        self.designation=des
        self.salary=sal
        
    def get_emp_details(self):
        return self.emp_id,self.name,self.base_location,self.deployed_location,self.designation,self.salary
      
        
    def get_organisation_name(self):
        return self.organisation_name
        
    
    
    
    
    def set_organisation_name(self,on):
        self.organisation_name=on
        
        
        
class Manager(Employee):
    managed_employees=[]
    
    def appraisal_4_employee(self,emp_reference,percent_raise):
        emp_reference.salary=(emp_reference.salary*percent_raise/100)+emp_reference.salary
    
    
    def get_manager_details(self):
        return self.emp_id,self.name,self.managed_employees



def main():
    emp=[]
    while True:
        print("#############################")
        print("#  1- ADD EMPLOYEE          #")
        print("#  2- DEL EMPLOYEEE         #")
        print("#  3 - MANAGER              #")
        print("#  4 - DIPLAY EMPLOYEEE     #")
        print("#  5 - APPRAISAL            #")
        print("#  6 - EXIT                 #")
        print("#############################")
        opt=input("\n \t Enter the Option : ")
        
        if opt=='1':
            e=Employee()
            id=input(" ENTER EMP ID :")
            name=input(" ENTER EMP NAME:")
            sal=int(input(" Enter the SALARY : "))
            e.set_emp_details(id,name,"base","dep","jsvhdb",sal)
            emp.append(e)
            
        elif opt=='2':
            print("EMPLOYES PRESENT : ")
            c=0
            for i in emp:
                print(c," NAME ",i.name)
                c=c+1
        
            ch=int(input(" ENTER THE SL NO OF EMP : "))
            del emp[ch]
        elif opt=='3':
        
            M=Manager()
            M.set_emp_details("MANAGER","ANUJ","base","dep","jsvhdb",99999999)
            M.set_organisation_name(" -MCA-KERALA- ")
            print(M.get_organisation_name())
            id,name,obj=M.get_manager_details()
            #APPEND EMP TO MANAGER LIST
            for i in emp:
                M.managed_employees.append(i)
            emp=[]
            print("\n MANAGER ID ",id)
            print("\n MANAGER NAME ",name)
            print("\n MANAGED EMPLOYEES :")
            for i in obj:
                print(" \t NAME: ",i.name)
            
        elif opt=='4':
            for i in M.managed_employees:
                print(i.get_emp_details())
        elif opt=="5":
            print("EMPLOYES PRESENT : ")
            c=0
            for i in M.managed_employees:
                print(c," NAME ",i.name)
                c=c+1
        
            ch=int(input(" ENTER THE SL NO OF EMP : "))
            per=int(input("Enter Appraisal percentage : "))
            M.appraisal_4_employee(M.managed_employees[ch],per)
        elif opt=="6":
            break
        else:
            print("INVALID OPTION")
            
            
                            
            
            
    # e1=Employee()
    # e2=Employee()
    # e3=Employee()
    # e1.set_emp_details("SDHAF","ANUJ","base","dep","jsvhdb",10000)
    # e2.set_emp_details("asjgfvh","sdaf","base","dep","af",10000)
    # e3.set_emp_details("SDfasfdHAF","asfd","base","dep","jsvhdb",10000)
    # print(e1.get_emp_details())
    # print(e2.get_emp_details())
    # print(e3.get_emp_details())
    # M=Manager()
    # M.set_emp_details("MANAGER","ANUJ","base","dep","jsvhdb",99999999)
    # M.set_organisation_name("I LUV KARELA")
    # M.managed_employees.append(e1)
    # M.managed_employees.append(e2)
    # M.managed_employees.append(e3)
    # id=""
    # name=""
    # obj=[]
    # id,name,obj=M.get_manager_details()
    # print("\n MANAGER ID ",id)
    # print("\n MANAGER NAME ",name)
    # print("\n MANAGED EMPLOYEES :")
    # for i in obj:
    #     print(" \t NAME: ",i.name)
    # M.appraisal_4_employee(e1,5000)   
    # print(obj[0].get_emp_details())
    
    
    
    
    
    


main()
# M1=Manager()
# M1.set_emp_details()


        

        
        
        
        