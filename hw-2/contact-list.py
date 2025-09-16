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
        self._contact.append(last_name.lower())
        self._contact.append(first_name.lower())
        self._contact.append(self.birthday)

class ContactBook():

    contact_book = [] # list of lists to store all contacts

    def sortBook(self):
        self.contact_book.sort()
        return

    def searchContactbyIndex(self, input): 
        # Try to find a contact by index, outputs the contact if it is found, None if not 
        try:
            output = self.contact_book[input]
        except IndexError as e: return None
        return output

    def insertContact(self, input):
        try:
            self.contact_book.append(input)
        except Exception as e: print(f"!! Failed to add contact: {e}")
        return 
    
    def removeContactbyName(self, first, last):
        first, last = first.lower(), last.lower() # Clean the inputs
        index = next((i for i, r in enumerate(self.contact_book) if first in r and last in r), -1)
        try:
            del self.contact_book[index]
            return True
        except IndexError as e: print(f"!! Error deleting contact: {e}"); return False
    
    def removeContactbyIndex(self, pos:int):
        try:
            del self.contact_book[pos]
            return True
        except IndexError as e: print(f"!! Error deleting contact: {e}"); return False

def main():
    print("\nHW2 - Contact List\nSolution by Aldo Navarro\n")
    book = ContactBook() # init the book
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
            t_flag = False # temp flag, init and clear
            user_input = int(input("Enter a menu item > "))

            if user_input == 1: # New Contact
                t_flag = True
                in_fname = input(" - Enter the user's first name > ")
                in_lname = input(" - Enter the user's last name > ")
                while t_flag:
                    try:
                        in_bday = input(" - Enter the user's birthday > ")
                        selected_contact = Contact(in_fname, in_lname, in_bday) # prepare the contact
                        book.insertContact(selected_contact._contact) # try to insert just the list into the book
                        print(selected_contact, selected_contact._contact) # print the list
                        t_flag = False # break from the loop
                    except Exception as e: print(f"!! Error: {e}")

            if user_input == 2: # Import Contacts
                print("WIP")

            if user_input == 3: # Display all Contacts
                book.sortBook()
                print(book.contact_book)
            
            if user_input == 4: # Export all Contacts
                print("WIP") 
            
            if user_input == 5: # Delete a Contact
                user_input = input(" - Remove contact by [N]ame, [P]osition, or [E]xit > ")
                if user_input[0].upper() == "N": # by name
                    in_fname = input(" - - Enter the user's first name > ")
                    in_lname = input(" - - Enter the user's last name > ")
                    val = book.removeContactbyName(in_fname, in_lname)
                    if val == True:
                        print(f" - Deleted the contact {in_fname.capitalize()} {in_lname.capitalize()}.\n")
                    else:
                        print(f"!! Failed to delete the contact, please try again.\n")

                if user_input[0].upper() == "P": # by position in the list
                    in_pos = input(" - - Enter the contact's position in the list > ")
                    try:
                        in_pos = int(in_pos)
                    except ValueError as e: print(f"! This is not a number.")
                    x = book.searchContactbyIndex(in_pos)
                    if x != None:
                        user_input = input(f" - - Are you sure you want to remove the contact {x[1], x[0]}? y/N > ")
                        if user_input[0].upper() == "Y":
                            val = book.removeContactbyIndex(in_pos)
                            if val == True:
                                print(f" - Deleted the contact in position {in_pos}.\n")
                            else:
                                print(f"!! Failed to delete the contact, please try again.\n")
                        else: print(" - Did not delete the contact.")
                    else: print("!! No contact in that position, please verify and try again.")
                    
            if user_input == 6: # Exit
                print("HW2 Complete")
                break

        except Exception as e: print(f"!!! Error: {e}")

if __name__ == "__main__":
    main()
