# pretend it works
from datetime import date, datetime
from dateCheck import handleDates
import csv

class Contact():
    
    def __init__(self, first_name:str, last_name:str, birth_date:str):

        self._contact = [] # initialize the list to store the information
        # note that this list is where the actual contact will be held in memory

        # self variables are just to call upon, like person.lastname would return "smith"
        self.firstname = first_name.lower() # first name, stored in lower
        self.lastname = last_name.lower() # last name
        m, d, y = handleDates(birth_date) # test if birthday is real
        self.birthday = date(y, m, d) # store the birthday in iso format

        # store each piece into the list
        self._contact.append(first_name.lower())
        self._contact.append(last_name.lower())
        self._contact.append(self.birthday)

    def contactBook(input):
        contact_book = [] # list to store every contact loaded into memory
        try:
            contact_book.append(input)
        except Exception as e: print(f"Error: {e}")

    def newContact(self, c_input):
        try:
            new_contact = c_input
            self.contactBook(c_input)
            return
        except Exception as e: print(f"Failed to add contact: {e}") 


def otherContactbook(input):
    other_contact_book = []
    try:
        other_contact_book.append(input)
    except Exception as e: print(f"Failed to add contact: {e}")
    return 


def main():
    print("\nHW2 - Contact List\nSolution by Aldo Navarro\n")
    while True:
        try:
            print("\nMenu Items:" \
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
                    selected_contact = Contact(in_fname, in_lname, in_bday) # prepare the contact
                    otherContactbook(selected_contact) # try to insert into the book
                    print(selected_contact, selected_contact._contact) # print the list
                except Exception as e: print(f"Error: {e}")

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

        except Exception as e: print(f"Error: {e}")

if __name__ == "__main__":
    main()
