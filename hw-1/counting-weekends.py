# this is a python file, be patient!
from datetime import datetime, date, timedelta

def handleDates(u_input: str):
    dateFormats = [
        "%m/%d/%y",  # 12/05/20
        "%m/%d/%Y",  # 12/5/2020
        "%m/%-d/%Y", # 12/5/2020
    ]
    # try to use strptime to derive dates
    for fmt in dateFormats:
        try:
            dtx = datetime.strptime(u_input, fmt)
            return dtx.month, dtx.day, dtx.year
        except ValueError:
            continue
    # split the numbers into actual integers
    parts = u_input.split("/")
    if len(parts) == 3:
        month, day, year = parts
        if len(year) == 2:
            year = "20" + year
        return int(month), int(day), int(year)
    raise ValueError(f"Not a valid date: {u_input}")
    
def countWeekends(m1:int, d1:int, y1:int, m2:int, d2:int, y2:int):
    # check if the years allign with the intended range
    if not 1800 < y1 < 2200:
        raise ValueError(f"{y1} is out of the intended date range of 1800 - 2200.")
    if not 1800 < y2 < 2200:
        raise ValueError(f"{y2} is out of the intended date range of 1800 - 2200.")    
    
    # test if dates are real
    try:
        start = date(y1, m1, d1)
        end = date(y2, m2, d2)
    except ValueError as e:
        print(f"Invalid date entered: {e}")

    # this is to avoid potential issues and keep the larger date first
    past_flag = False
    if start > end:
        start, end = end, start
        past_flag = True # change the output to say "was" instead of "is"

    # day count, inclusive
    total_days = (end - start).days + 1

    # divide the total day count into weeks, keeping the remainder
    weekends, remainder = divmod(total_days, 7)

    # check the remainder for a single weekend day
    start_wd = start.weekday()
    for i in range(remainder):
        wd = (start_wd + 1) % 7
        if wd in (5, 6): # Saturday or Sunday
            weekends += 1

    return weekends, past_flag

def main():
    print("HW1 - Counting Weekends\nSolution by Aldo Navarro\n\nFormat dates as such: m/d/y\n")
    while True:
        try:
            user_input = input("Enter a starting date, or Q to quit > ")
            if user_input.lower() == "q":
                break        

            user_input2 = input("Enter a second date, or Q to quit > ")
            if user_input2.lower() == "q":
                break
            m1, d1, y1 = handleDates(user_input)
            m2, d2, y2 = handleDates(user_input2)
            
            weekends, p_flag = countWeekends(m1, d1, y1, m2, d2, y2)
            
            # shouldn't happen, but if there's no output then nothing will happen
            if weekends != "":
                # change the language of the output to make sense
                if p_flag == True:
                    p_flag = "after"
                else: p_flag = "before"
                # add an s 
                if weekends > 1:
                    mltpl = "s"

                # print statement
                print(f"The day {user_input} occured {weekends} weekend{mltpl} {p_flag} {user_input2}\n")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()