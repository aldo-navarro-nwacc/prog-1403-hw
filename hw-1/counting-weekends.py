# this is a python file, be patient!
from datetime import datetime, date, timedelta

def handleDates(u_input: str):
    dateFormats = [
        "%m/%d/%y",  # 12/05/20
        "%m/%d/%Y",  # 12/5/2020
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

def countWeekday(s: date, e: date, target_wd: int):
    total = (e - s).days + 1
    if total <= 0:
        return 0
    offset = (target_wd - s.weekday()) % 7
    first = s + timedelta(days=offset)
    if first > e:
        return 0
    return 1 + ((e - first).days // 7)
    
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
    if start > end:
        start, end = end, start

    sat_count = countWeekday(start, end, 5)
    sun_count = countWeekday(start, end, 6)

    full_weekends = 0
    sat = start + timedelta((5 - start.weekday()) % 7)
    while sat <= end:
        if sat + timedelta(days=1) <= end:
            full_weekends += 1
        sat += timedelta(days=7)

    saturdays = sat_count - full_weekends
    sundays = sun_count - full_weekends

    return full_weekends, saturdays, sundays

def main():
    print("HW1 - Counting Weekends\nSolution by Aldo Navarro\n\nFormat dates as such: m/d/y\n")
    while True:
        try:
            user_input = input("Enter a starting date, or Q to quit > ")
            if user_input.lower() == "q":
                print("HW1 Complete")
                break        
            m1, d1, y1 = handleDates(user_input)

            user_input2 = input("Enter a second date, or Q to quit > ")
            if user_input2.lower() == "q":
                print("HW1 Complete")
                break
            m2, d2, y2 = handleDates(user_input2)
            
            weekends, sat, sun = countWeekends(m1, d1, y1, m2, d2, y2)
            
            # print statement
            print("")
            print(f"Full Weekends: {weekends}")
            print(f"Saturday-only weekends: {sat}")
            print(f"Sunday-only weekends: {sun}")
            print(f"Total Weekends: {weekends + sat + sun}")
            print("")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()