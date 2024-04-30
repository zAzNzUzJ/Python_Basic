
        ################################
        ################################
        ######_____DICTIONARY_____######
        ################################
        ################################
#     2: Add an element to the capitals collection like --> Afghanistan: Kabul
#     3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella
#     4: Remove an element from the collection 	
#     5: Take a key from the user and show value if it is present in the dictionary
#     6: Take a key from the user update it if it is present in the dictionary or add the key to the dictionary 	


def dict_display_capitals(capitals): 
       print(capitals) 
     
def dict_add_element(capitals):
        Key=input("Enter the Country name comma seperated :")
        value=input("Enter the Capital name comma seperated :")
        capitals[Key]=value
                
        
def dict_add_elements(capitals):
        Key=input("Enter the Country name comma seperated :").split(",")
        value=input("Enter the Capital name comma seperated :").split(",")
        for i in range(len(Key)):
                capitals[Key[i]]=value[i]
        
def dict_remove_element(capitals):
        Key=input("Enter the Country name TO DELETE  :")
        if Key in capitals.keys():
                del capitals[Key]
        else:
                print("\n INVALID KEY")
     

def dict_show_value_for_a_key(capitals):
        Key=input("Enter the Country name TO SHOW  :")
        if Key in capitals.keys():
                print(capitals[Key]) 
        else:
                print("\n INVALID KEY")

def dict_update_or_add_a_key(capitals):
        Key=input("Enter the Country name comma seperated :")
        value=input("Enter the Capital name comma seperated :")
        capitals.update({Key:value})
    

def my_dict_store():
    print("\n Welcome to Our Dict Store !!! ")
	
    capitals= {}
    """
        # Write your code here to create the dictionary from the user and reference it with capitals
    """
    print("Unimplemented , Write your code here to create the dictionary from the user and reference it with capitals") 
    print(capitals)
    
    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("    1: Display all elements in the capitals collection")
        print('    2: Add an element to the capitals collection like --> Afghanistan: Kabul')
        print('    3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella')
        print("    4: Remove an element from the collection 	")
        print("    5: Take a key from the user and show value if it is present in the dictionary")
        print("    6: Take a key from the user update itadd the key to the dictionary")
        print("    7: Exit the Program ")
        choice = int(input("\n Please enter your choice "))
        
        if choice   ==1:
            dict_display_capitals(capitals) 
        elif choice ==2:
            dict_add_element(capitals)
        elif choice ==3:
            dict_add_elements(capitals)
        elif choice ==4:
            dict_remove_element(capitals) 
        elif choice ==5:
            dict_show_value_for_a_key(capitals)
        elif choice ==6:
            dict_update_or_add_a_key(capitals)
        elif choice ==7:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

my_dict_store()





















