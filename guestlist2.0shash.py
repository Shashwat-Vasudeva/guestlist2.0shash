# create empty list called guests 

#Function format_name(name)
#remove extra space

#function is_duplicate(name)
# if name in guests
#return ture
#else 
#return false

#formating functions

#function add_guets 
#ask user for name 
#format name 
#if empty or duplicate
#print error 
#else add name to guests

#function modify_guets
# ask for existing name 
#format name
#if name not in guests list
#print error
#else ask for new name 
#if empty print error or duplicate 
#else replace old name with new 

#function sort_guets
#sort guests alphabetically 

#function show_count 
#print number of guests

#function show_invitation 
#for each guest in guests lsit 
#print invitation msg 



guest = []
#format helping functions 

def format_name(name)
return "".(name.title().strip())

def is_duplicate(name):
return name in guests


def add_guets():
    name = input("Enter guest name:")
    name = format_name(name)

    if name== "":
        elif is_duplicate(name):
            print("Error:Guest already exists")
            else:
                guests.append(name)
                print(f"{name}added successfully")

def modify_guets():
    old_name = format_name(input("Enter new name:"))

    if old_name not in guests:
        print("error: Guest not found.")
        return

        new_name = format_name(input("Enter new name:"))

        if new_name =="":
            print("Error: Name cannot be empty.")
            elif is_duplicate(new_name):
                print("Error: Duplicate name.")
                else:
                    index = guests.index(old_name)
                    guests[index] = new_name
                    print("Guest updated successfully")

