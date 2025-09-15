# HW1 - Aldo Navarro - PROG 1403 Fall 2025
from datetime import datetime, date, timedelta

def handleDates(u_input: str):
    s = u_input.strip()
    # yyyy-m-d
    try:
        dt = datetime.strptime(s, "%Y-%m-%d")
        return dt.month, dt.day, dt.year
    except ValueError:
        pass
    # yy-m-d
    if "-" in s:
        parts = [p.strip() for p in s.split("-")]
        if len(parts) == 3 and all(p.isdigit() for p in parts):
            y_str, m_str, d_str = parts
            if len(y_str) == 2:
                y = 2000 + int(y_str)
                m, d  = int(m_str), int(d_str)
                try:
                    date(y, m, d)
                except ValueError as e:
                    raise ValueError(f"{u_input} is not a valid date: {e}")
                return m, d, y

    # m/d/yyyy
    try:
        dt = datetime.strptime(s, "%m/%d/%Y")
        return dt.month, dt.day, dt.year
    except ValueError:
        pass

    parts = [p.strip() for p in s.split("/")]
    # m/d/yy
    if len(parts) == 3 and all(p.isdigit() for p in parts):
        m_str, d_str, y_str = parts
        if len(y_str) == 2:
            y = 2000 + int(y_str)
        else: y = int(y_str)

        m, d = int(m_str), int(d_str)
        try:
            date(y, m, d)
        except ValueError as e:
            raise ValueError(f"{u_input} is not a valid date: {e}")
        return m, d, y
    # m/d
    if len(parts) == 2 and all(p.isdigit() for p in parts):
        m, d = int(parts[0]), int(parts[1])
        y = datetime.now().year
        try:
            date(y, m, d)
        except ValueError as e:
            raise ValueError(f"{u_input} is not a valid date: {e}")
        return m, d, y
    
    raise ValueError("Unsupported date format. Use: y-m-d, m/d/y, m/d")

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
    
    start = date(y1, m1, d1)
    end = date(y2, m2, d2)
    
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
    print("\nHW1 - Counting Weekends\nSolution by Aldo Navarro\n")
    print("Format dates as such: y-m-d, m/d/y, m/d (will assume current year)\n")
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