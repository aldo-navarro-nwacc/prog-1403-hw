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



class Model:

    def __init__(self):
        self.model_list = collections.defaultdict(list)
        #for key in brandList.__car_brand_list:
        #    self.model_list[key] = []
        
    def __str__(self):
        return str(self.model_list)
    
    def appendList(self, brand: str, newItem: str):
        self.model_list[brand].append(newItem)
    
    def modelExists(self, model_name, brand: str | None = None):
        if brand:
            return model_name in self.model_list.get(brand, [])
        else:
            return any(model_name in models for models in self.model_list.values())


class Sales:
    
    def __init__(self):
        self.__yearly_sales = {item: [] for item in modelList.model_list}
        print(self.__yearly_sales)

def removeFirstWord(text, word): # remove first word, kinda messy but it works
    words = text.split()
    if words and words[0] == word:
        return ' '.join(words[1:])
    return text

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
                    
                    if car_brand == 'Alfa': # exception for Alfa Romeo
                        car_brand += ' Romeo' 
                        temp_str = str(row[0].split(" ", 1)[1])
                        car_model = removeFirstWord(temp_str, 'Romeo')

                    elif car_brand == 'Land': # exception for Land Rover
                        car_brand += ' Rover'
                        temp_str = str(row[0].split(" ", 1)[1])
                        car_model = removeFirstWord(temp_str, 'Rover')

                    else:
                        car_model = str(row[0].split(" ", 1)[1]) # gives only the model
                        
                    #print(row[1])
                    brandList.appendList(car_brand)
                    modelList.appendList(car_brand, car_model)

    except IOError as e: print(f"!! Error reading file: {e}")


brandList = Brand()
modelList = Model()


# this will all be removed when testing is complete
readFromFile("US Vehicle Model Sales by Month 2025.txt")
salesList = Sales()
print()
print(brandList, '\n')