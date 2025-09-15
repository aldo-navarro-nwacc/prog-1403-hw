# pretend it works

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
            user_input = int(input("Enter a menu item > "))
            if user_input == 1: # New Contact
                print("WIP") 
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