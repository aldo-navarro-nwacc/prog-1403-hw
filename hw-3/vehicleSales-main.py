import vehiclesales as vs

def fmt_int(n: int): # comma separate all integers
    return f"{n:,}" if isinstance(n, int) else "-"

def import_data(brands: vs.Brand, models: vs.Model, sales: vs.Sales):
    filename = 'US Vehicle Model Sales by Month 2025.txt'
    vs.readFromFile(filename, brands, models, sales)
    brands.finalizeList()
    total_brands = len(brands.items)
    total_models = sum(len(models.getModels(b)) for b in brands.items)
    print(f"Import successful: {fmt_int(total_brands)} brands | {fmt_int(total_models)} models\n")
    return True # changes the loaded flag

def ensure_loaded(loaded):
    if not loaded:
        print("!!! No data loaded into the program!\n Choose option 1 first, then retry.\n")
    return loaded

def show_annual_all(brands: vs.Brand, models: vs.Model, sales: vs.Sales):
    print("\n--- Annual sales for All Models (All Brands) ---")
    for brand in brands.items:
        print(f"\n{brand}") # print the brand first
        rows = []
        for m in models.getModels(brand):
            total = sales.yearly_total_by_model(brand, m)
            rows.append((m, 0 if total is None else total))

        rows.sort(key = lambda x: x[1], reverse = True)
        if not rows:
            print(" (no models)")
            continue
        width = max(6, max(len(r[0]) for r in rows))
        for model_name, total in rows:
            print(f"  {model_name:<{width}}  {fmt_int(total)}")

def show_monthly_all(brands: vs.Brand, models: vs.Model, sales: vs.Sales):
    print("\n--- Monthly sales for All Models (All Brands) ---")
    header = ["Model"] + sales.header
    for brand in brands.items:
        print(f"\n{brand}")
        rows = []
        for m in models.getModels(brand):
            monthly = sales.get_model(brand, m) or [None]*12
            rows.append((m, monthly))
        if not rows:
            print("  (no models)")
            continue
        namew = max(5, max(len(r[0]) for r in rows))
        print(" " + f"{header[0]:<{namew}}  " + "  ".join(f"{h:>6}" for h in sales.header))
        for name, arr in rows:
            print(" " + f"{name:<{namew}}  " + "  ".join(f"{fmt_int(v):>6}" for v in arr)) 

def main():
    print("Vehicle Sales")
    brands = vs.Brand()
    models = vs.Model()
    sales = vs.Sales()
    loaded = False # flag to ensure nothing runs if nothing is loaded
    while True:
        try:
            user_input = ""
            print("Menu Items:\n" \
            "1. Import Vehicle Sales Data\n2. Display annual sales for all Models for all Brands\n" \
            "3. Display monthly sales for all Models for all Brands\n" \
            "4. Display annual sales for all Models for one Brand\n" \
            "5. Display monthly sales for all Models for one Brand\n6. Exit")

            user_input = int(input("\nEnter a menu item > "))
            if user_input == 1: # import file
                loaded = import_data(brands, models, sales)
                ...


            if user_input == 2: # annual sales for ALL brands
                if ensure_loaded(loaded):
                    show_annual_all(brands, models, sales)


            if user_input == 3: # month-by-month sales for ALL brands
                if ensure_loaded(loaded):
                    show_monthly_all(brands, models, sales)


            if user_input == 4: # annual sales for ONE brand
                if ensure_loaded(loaded):
                    ...


            if user_input == 5: # month-by-month sales for ONE brand
                if ensure_loaded(loaded):
                    ...

                
            if user_input == 6: 
                print("Goodbye"); break
        except ValueError: print("!!! Invalid menu entry")

if __name__ == "__main__":
    main()