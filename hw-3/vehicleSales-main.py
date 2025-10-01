import vehiclesales

def main():
    print("HW3 - Vehicle Sales\nSolution by Aldo Navarro\n")
    while True:
        try:
            user_input = ""
            print("Menu Items:\n" \
            "1. Import Vehicle Sales Data\n2. Display annual sales for all Models for all Brands\n" \
            "3. Display monthly sales for all Models for all Brands\n" \
            "4. Display annual sales for all Models for one Brand\n" \
            "5. Display monthly sales for all Models for one Brand\n6. Exit")

            user_input = int(input("\nEnter a menu item > "))
            if user_input == 1: # import file
                vehiclesales.readFromFile("US Vehicle Model Sales by Month 2025.txt")
                ...


            if user_input == 2: # annual sales for ALL brands
                ...


            if user_input == 3: # month-by-month sales for ALL brands
                ...


            if user_input == 4: # annual sales for ONE brand
                ...


            if user_input == 5: # month-by-month sales for ONE brand
                ...

                
            if user_input == 6: 
                print("HW3 Complete"); break
        except ValueError: print("!!! Invalid menu entry")

if __name__ == "__main__":
    main()