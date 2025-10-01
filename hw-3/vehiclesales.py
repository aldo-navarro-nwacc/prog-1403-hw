import csv

class Brand:
    ...


class Model:
    ...


class Sales:
    ...


def readFromFile(filename:str):
    header_flag = False
    try:
        with open(filename, 'r', newline='', encoding="UTF-8") as csvfile:
            filereader = csv.reader(csvfile, delimiter='\t') # this file is tab-delimited
            for row in filereader:
                if not header_flag: # sort out the useless (to this) header
                    if any(cell.strip() == 'May' for cell in row): # May is chosen since its not abbreviated
                        header_flag = True
                        continue # skip the current row
                if header_flag: # if the flag is set (header has been passed)
                    #test = str(row[0].split(" ", 1)[0]) # gives us only the brand
                    print(row)
    except IOError as e: print(f"!! Error reading file: {e}")


readFromFile("US Vehicle Model Sales by Month 2025.txt")