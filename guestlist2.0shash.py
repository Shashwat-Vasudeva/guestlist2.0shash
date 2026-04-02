# create empty list called guests

#Function format_name(name)
#remove extra space

#function is_duplicate(name)
# if name in guests
#return true
#else
#return false

#formatting functions

#function add_guests
#ask user for name
#format name
#if empty or duplicate
#print error
#else add name to guests

#function modify_guests
# ask for existing name
#format name
#if name not in guests list
#print error
#else ask for new name
#if empty print error or duplicate
#else replace old name with new

#function sort_guests
#sort guests alphabetically

#function show_count
#print number of guests

#function show_invitation
#for each guest in guests list
#print invitation msg

guests = []
#format helping functions

def format_name(name):
    return name.title().strip()

def is_duplicate(name):
    return name in guests

def add_guests():
    name = input("Enter guest name: ")
    name = format_name(name)

    if name == "":
        print("Error: Name cannot be empty.")
    elif is_duplicate(name):
        print("Error: Guest already exists.")
    else:
        guests.append(name)
        print(f"{name} added successfully.")

def modify_guests():
    old_name = format_name(input("Enter existing name: "))

    if old_name not in guests:
        print("Error: Guest not found.")
        return

    new_name = format_name(input("Enter new name: "))

    if new_name == "":
        print("Error: Name cannot be empty.")
    elif is_duplicate(new_name):
        print("Error: Duplicate name.")
    else:
        index = guests.index(old_name)
        guests[index] = new_name
        print("Guest updated successfully.")

def remove_guests():
    name = format_name(input("Enter name to remove: "))

    if name in guests:
        guests.remove(name)
        print(f"{name} removed successfully.")
    else:
        print("Error: Guest not found.")

def sort_guests():
    guests.sort()
    print("Guests sorted alphabetically.")

def show_count():
    print(f"Total number of guests: {len(guests)}")

def show_invitation():
    if not guests:
        print("No guests to invite.")
    else:
        print("\n--Invitations--")
        for guest in guests:
            print(f"Dear {guest}, you are invited to the party!")
            print("--------")

def menu():
    while True:
        print("\n===== Guest Management System =====")
        print("1. Add guest")
        print("2. Modify guest")
        print("3. Remove guest")
        print("4. Sort guests")
        print("5. Show number of guests")
        print("6. Show invitations")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_guests()
        elif choice == "2":
            modify_guests()
        elif choice == "3":
            remove_guests()
        elif choice == "4":
            sort_guests()
        elif choice == "5":
            show_count()
        elif choice == "6":
            show_invitation()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
