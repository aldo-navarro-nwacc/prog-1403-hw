# this is a python file, be patient!
import datetime

def main():
    print("HW1 - Counting Weekends\nSolution by Aldo Navarro\n")
    while True:
        try:
            user_input = input("Enter a number, or Q to quit > ")
            if user_input.lower() == "q":
                break        
            print(user_input)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()