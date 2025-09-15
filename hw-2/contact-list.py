# pretend it works
from datetime import date, datetime
from dateCheck import handleDates


class Contact():
    
    contact_list = [] # establish a contact list to read/write to

    def __init__(self, first_name:str, last_name:str, birth_date:str):
        
        self.firstname = first_name.lower() # first name, stored in lower
        self.lastname = last_name.lower() # last name

        m, d, y = handleDates(birth_date) # test if birthday is real
        self.birthday = date(y, m, d)

    def newContact(self, c_input):
        try:
            new_contact = c_input
            self.contact_list.append(new_contact)
            return
        except Exception as e: print(f"Failed to add contact: {e}") 


def main():
    print("\nHW2 - Contact List\nSolution by Aldo Navarro\n")
    while True:
        try:
            print("Menu Items:" \
            "\n1. Enter a new Contact" \
            "\n2. Import Contacts from File" \
            "\n3. Display all loaded Contacts" \
            "\n4. Export all Contacts to a file" \
            "\n5. Delete a loaded Contact" \
            "\n6. Exit")
            user_input = 0 # clear the input
            user_input = int(input("Enter a menu item > "))

            if user_input == 1: # New Contact
                in_fname = input("Enter the user's first name > ")
                in_lname = input("Enter the user's last name > ")
                try:
                    in_bday = input("Enter the user's birthday > ")
                    x = Contact(in_fname, in_lname, in_bday)
                    Contact.newContact(Contact, x)
                    print(Contact.contact_list)
                except Exception as e:
                    print(f"Error: {e}")

            if user_input == 2: # Import Contacts
                print("WIP")

            if user_input == 3: # Display all Contacts
                print("WIP") 
            
            if user_input == 4: # Export all Contacts
                print("WIP") 
            
            if user_input == 5: # Delete a Contact
                print("WIP") 

            if user_input == 6: # Exit
                print("HW2 Complete")
                break

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
