import csv
import collections
from typing import List, Dict, Optional

class Brand:

    def __init__(self):
        self.__temp_brand_list = set()
        self.__car_brand_list = None

    def __str__(self):
        self.finalizeList() # without this it will break
        return str(self.__car_brand_list)
        #return str(list(self.__temp_brand_list).split(" ")) 

    def append(self, newItem: str):
        self.__temp_brand_list.add(newItem) # a set doesn't allow duplicates, so no need to check for them

    def finalizeList(self):
        if self.__car_brand_list is not None:
            return
        car_brand_list = list(self.__temp_brand_list)
        car_brand_list.sort()
        self.__temp_brand_list.clear()
        self.__car_brand_list = tuple(car_brand_list)

    @property # getter for the final list
    def items(self):
        self.finalizeList()
        return self.__car_brand_list or tuple() # returns a blank tuple if empty

class Model:

    def __init__(self):
        self.model_list = collections.defaultdict(list)
        # dict{str, List[str]}
        
    def __str__(self):
        return str(self.model_list)
    
    def append(self, brand: str, newItem: str):
        self.model_list[brand].append(newItem)
    
    def modelExists(self, model_name, brand: str | None = None):
        if brand:
            return model_name in self.model_list.get(brand, [])
        return any(model_name in models for models in self.model_list.values())
    
    def getModels(self, brand:str):
        return list(self.model_list.get(brand, []))


class Sales:
    
    def __init__(self):#, model_key):
        self.sales = collections.defaultdict(dict)

    def add(self, brand: str, model: str, monthly: List[Optional[int]]):
        if len(monthly) != 12:
            raise ValueError("Monthly must contain exactly 12 entries")
        self.sales[brand][model] = monthly

    #get sales data for a specific car make and model
    def get_model(self, brand: str, model: str):
        return self.sales.get(brand, {}).get(model)
    
    #get sales data for all models for a specific brand
    def get_brand(self, brand: str):
        return self.sales.get(brand, {})
    
    # yearly sales for one model
    def yearly_total_by_model(self, brand: str, model: str):
        data = self.get_model(brand, model)
        if data is None:
            return None
        return sum(v for v in data if isinstance(v, int))

    # yearly sales for one brand
    def yearly_total_by_brand(self, brand: str):
        return sum(self.monthly_total_by_brand(brand))
    
    def monthly_total_by_brand(self, brand: str):
        models = self.get_brand(brand).values()
        if not models:
            return [0] * 12 # if nothing is found, give zeroes
        totals = [0] * 12
        for arr in models:
            for i, v in enumerate(arr):
                if isinstance(v, int):
                    totals[i] += v
        return totals
    
    def find(self, model: str):
        hits = []
        for b, models in self.sales.items():
            for m in models:
                if m.lower() == model.lower():
                    hits.append((b,m))
        return hits

def _remove_first_word(text, word): # remove first word, kinda messy but it works
    words = text.split()
    if words and words[0] == word:
        return ' '.join(words[1:])
    return text

def _parse_brand_model(cell: str): # used to be in the filereader
    first = cell.split(" ", 1)[0]
    if first == "Alfa":
        brand = "Alfa Romeo"
        model = _remove_first_word(cell.split(" ", 1)[1], "Romeo")
    elif first == "Land":
        brand = "Land Rover"
        model = _remove_first_word(cell.split(" ", 1)[1], "Rover")
    else:
        brand = first
        model = cell.split(" ", 1)[1] if ' ' in cell else ""
    return brand, model

def _parse_months(row: list[str]):
    months = []
    for raw in row[1:13]:
        val = raw or ''.strip()
        if not val or val == '-': # sales with hyphen should return None
            months.append(None)
        else:
            months.append(int(val.replace(",", ""))) # remove commas and save the int
    while len(months) < 12:
        months.append(None)
    return months

def readFromFile(filename:str, brandList: Brand, modelList: Model, salesList: Sales):
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
                    name_cell = row[0].strip()
                    if not name_cell:
                        continue

                    brand, model = _parse_brand_model(name_cell)
                    brandList.append(brand)
                    modelList.append(brand,model)

                    monthly = _parse_months(row)
                    salesList.add(brand, model, monthly)


    except IOError as e: print(f"!! Error reading file: {e}")

