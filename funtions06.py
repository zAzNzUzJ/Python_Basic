
##########################################################################
def my_set_store(a,b):
    print("\n Welcome to Our SET Store !!! ")
	
    """
        # Write your code here to create the dictionary from the user and reference it with capitals
    """
    
    print(a)
    print(b)
    
    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("    1: UNION ")
        print('    2: INTERSECTION')
        print('    3: A-B')
        print("    4: B-A 	")
        print("    5: Take a element user and display member is of set A or B")
        print("    6: Display elements in A")
        print("    7: Display elements in B")
        print("    8: Add elements from user to set A")
        print("    9: Add Multiple elements to set B")
        print("    10: REmove an element taken from user Set A ")
        print("    11: EXIT --       ")
        print("##################################################\n")
        choice = int(input("\n Please enter your choice "))
        
        if choice   ==1:
             print(a.union(b))
        elif choice ==2:
            print(set.intersection(a,b))
        elif choice ==3:
            print(set.difference(a,b))
        elif choice ==4:
            print(set.difference(b,a)) 
        elif choice ==5:
            x=int(input("\nENter the element to search  : "))
            if(x in a):
                if(x in b):
                    print("\n IN BOTH A AND B ")
                    print(a)
                    print(b)
                else:
                    print("\n IN SET A ")
                    print(a)
            elif(x in b):
                print("\n IN SET B ")
                print(b)
            else:
                print("\n NOT IN SETS ")
        elif choice ==6:
            print(len(a))
            
        elif choice ==7:
            print(len(b))
        elif choice ==8:
            y=int(input("\n Enter the element to add : "))
            a.add(y)
        elif choice ==9:
            x1=set()
            x=input("\n Enter the multiple elements : ").split(",")
            for i in x:
                x1.add(int(i))
                
            
            b.update(x1)
        elif choice ==10:
            y=int(input("\n Enter the element to remove : "))
            if y in a:
                print(" \n Element present in A ")
                a.discard(y)
            elif y in b:
                print(" \n Element present in B ")
                b.discard(y)
            else:
                print("\n !!! NOT FOUND !!!!")
                
            
        elif choice ==11:
            print("\n EXIT ")
            break
            
        else:
            print("\n  Invalid Input , Please Try Again !!!!  ")


##########################################################################
##########################################################################



def findcol(dict1):
    while True:
        try:
            n=int(input("Enter the Colour Key :" ))
            print(dict1[n]) 
            break     
        except :
            print(" \n COLOUR NOT FOUND>.")

def findind(lis):
    while True:
        try:
            n=int(input("Enter the index : "))
            print(lis[n])
        except:
            print(" \n INDEX NOT FOUND ")  

        
        