# this is my own function from hw1
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
