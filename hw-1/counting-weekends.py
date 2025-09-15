# this is a python file, be patient!
from datetime import datetime

def handleDates(u_input: str):
    dateFormats = [
        "%m/%d/%y",  # 12/05/20
        "%m/%d/%Y",  # 12/5/2020
        "%m/%-d/%Y", # 12/5/2020
    ]
    
    for fmt in dateFormats:
        try:
            dtx = datetime.strptime(u_input, fmt)
            return dtx.month, dtx.day, dtx.year
        except ValueError:
            continue

    try:
        parts = u_input.split("/")
        if len(parts) == 3:
            month, day, year = parts
            if len(year) == 2:
                year = "20" + year
            return int(month), int(day), int(year)
    except Exception:
        raise ValueError(f"Not a valid date: {u_input}")
    
def countWeekends(date1, date2):
    
    
    
    return

def main():
    print("HW1 - Counting Weekends\nSolution by Aldo Navarro\n")
    while True:
        try:
            user_input = input("Enter a starting date, or Q to quit > ")
            if user_input.lower() == "q":
                break        

            user_input2 = input("Enter a second date, or Q to quit > ")
            if user_input2.lower() == "q":
                break
            d1, m1, y1 = handleDates(user_input)
            d2, m2, y2 = handleDates(user_input2)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()