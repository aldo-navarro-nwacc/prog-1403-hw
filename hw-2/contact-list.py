# pretend it works
from datetime import date, datetime, timedelta
from dateCheck import handleDates
import csv, os

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
        # Sorts the book by last name.
        self.contact_book.sort()
        return
    
    def showBook(self):
        self.contact_book.sort() # Sort prior to listing
        print(f"{'#':<3}{'Last Name':<20}{'First Name':<20}{'Birthday':<10}{'Age':<10}")
        counter = 0
        for row in self.contact_book:
            fixed_row = []
            counter += 1
            for item in row:
                if isinstance(item, str):
                    fixed_row.append(item.title())
                elif isinstance(item, date):
                    fixed_row.append(item.strftime("%Y-%m-%d"))
                else:
                    fixed_row.append(str(item))
            first, last, bday = row
            print(f"{counter:<3}{first.title():<20}{last.title():<20}{bday:%Y-%m-%d}")

        return

    def searchContactbyIndex(self, input): 
        # Try to find a contact by index, outputs the contact if it is found, None if not 
        try:
            output = self.contact_book[input]
        except IndexError as e: return None
        return output
    
    def searchContactbyName(self, fname, lname):
        # Try to find a contact by name. Returns the index if found, None if not.
        fname, lname = fname.lower(), lname.lower() # Clean the inputs
        try:
            index = next((i for i, r in enumerate(self.contact_book) if fname in r and lname in r), -1)
        except IndexError: return None
        except TypeError: return None
        if index == -1: # fix having nobody with that name and defaulting to end of list
            return None
        else: return index

    def insertContact(self, input):
        # Appends a contact to the end of the book.
        try:
            self.contact_book.append(input)
        except Exception as e: print(f"!! Failed to add contact: {e}")
        return 
    
    def removeContactbyIndex(self, index:int):
        # Try to delete a contact by index, returns True if it passes and False if not
        # Note that there is no double checking here, this will delete a contact if it exists
        try:
            del self.contact_book[index]
            return True
        except IndexError as e: print(f"!! Error deleting contact: {e}"); return False

    def readFromCSV(self):
        dir = os.path.dirname(__file__)
        contacts_csv = os.path.join(dir, "file.csv")
        with open(contacts_csv, 'r', newline='') as csvfile:
            filereader = csv.reader(csvfile, delimiter=',')
            for row in filereader:
                self.insertContact(row)

            

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
            user_input, t_flag, val, = 0, False, False # clear the input and flags
            in_fname, in_lname, in_bday, in_pos, x = "", "", "", "", "" # clear variable names just in case
            
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
                        print(f" - - The contact {in_fname} {in_lname} has been added successfully.") # print the list
                        t_flag = False # break from the loop
                    except Exception as e: print(f"!! Error adding the contact: {e}")

            if user_input == 2: # Import Contacts
                book.readFromCSV()
                print(book.contact_book)

            if user_input == 3: # Display all Contacts
                book.sortBook()
                book.showBook()
            
            if user_input == 4: # Export all Contacts
                print("WIP") 
            
            if user_input == 5: # Delete a Contact
                user_input = input(" - Remove contact by [N]ame, [P]osition, or [E]xit > ")

                if user_input[0].upper() == "N": # by name
                    in_fname = input(" - - Enter the user's first name > ")
                    in_lname = input(" - - Enter the user's last name > ")
                    in_pos = book.searchContactbyName(in_fname, in_lname)
                    x = book.searchContactbyIndex(in_pos)
                    if x != None: # if user is found
                        user_input = input(f" - - Are you sure you want to remove the contact {x[1].title()} {x[0].title()}? [y/N] > ")
                        if user_input[0].upper() == "Y": # if user confirms
                            val = book.removeContactbyIndex(in_pos)
                            if val == True:
                                print(f" - Deleted the contact {x[1].title()} {x[0].title()} in position {in_pos + 1}.")
                            else: 
                                print(f"!! Failed to delete the contact, please try again.\n") # if deletion fails for some reason
                        else: print(" - Operation canceled, no contact was deleted.") # if user declines
                    else: print("!! No contact by that name, please verify and try again.") # no contact found

                if user_input[0].upper() == "P": # by position in the list
                    in_pos = input(" - - Enter the contact's position in the list > ")
                    try:
                        in_pos = int(in_pos)
                        in_pos -= 1 # account for the 0 start in a list, so users can just count.
                    except ValueError as e: print(f"! This is not a number.")
                    x = book.searchContactbyIndex(in_pos)
                    if x != None: # if user is found
                        user_input = input(f" - - Are you sure you want to remove the contact {x[1].title()} {x[0].title()}? [y/N] > ")
                        if user_input[0].upper() == "Y": # if user confirms
                            val = book.removeContactbyIndex(in_pos)
                            if val == True:
                                print(f" - Deleted the contact {x[1].title()} {x[0].title()} in position {in_pos + 1}.")
                            else: 
                                print(f"!! Failed to delete the contact, please try again.\n") # if deletion fails for some reason
                        else: print(" - Operation canceled, no contact was deleted.") # if user declines
                    else: print("!! No contact in that position, please verify and try again.") # no position found
                    
            if user_input == 6: # Exit
                print("HW2 Complete")
                break
        except ValueError: print() # should just omit errors when pressing enter and passing '', hopefully
        except TypeError: print("!! No contact by that name, please verify and try again.") # message for the contact search
        except Exception as e: print(f"!!! Error: {e}")

if __name__ == "__main__":
    main()
