import csv
import collections

class Brand:

    def __init__(self):
        self.__temp_brand_list = set()

    def __str__(self):
        self.finalizeList() # without this it will break
        return str(self.__car_brand_list)
        #return str(list(self.__temp_brand_list).split(" ")) 

    def appendList(self, newItem: str):
        self.__temp_brand_list.add(newItem) # a set doesn't allow duplicates, so no need to check for them

    def finalizeList(self):
        self.__car_brand_list = list(self.__temp_brand_list) # list is mutable, therefore sort works
        self.__car_brand_list.sort(); del self.__temp_brand_list # delete temp to save some memory
        self.__car_brand_list = tuple(self.__car_brand_list) # tuple is hashable



class Model(Brand):

    def __init__(self):
        self.__temp_model_list = {}
        
    def __str__(self):
        self.finalizeList()
        return str(self.__model_list)
    
    def appendList(self, newItem: str):
        ...
    
    def finalizeList(self):
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
                        continue # skip the current (header) row

                if header_flag: # if the flag is set (header has been passed)
                    car_brand = str(row[0].split(" ", 1)[0]) # gives only the brand
                    if car_brand == 'Alfa':
                        car_brand += ' Romeo' # exception for Alfa Romeo
                    if car_brand == 'Land':
                        car_brand += ' Rover' # exception for Land Rover
                    
                    #car_model = str(row[0].split(" ", 1)[1]) # gives only the model

                    brandList.appendList(car_brand)
    except IOError as e: print(f"!! Error reading file: {e}")


brandList = Brand()
readFromFile("US Vehicle Model Sales by Month 2025.txt")
print()
print(brandList)
print()