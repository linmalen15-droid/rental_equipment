
# get data from the user
def get_equipments():
            equipment_name = input("Enter equipment name: ").capitalize()
            while True:
                try:
                    rental_price = float(input("Enter daily rental price: "))
                    if rental_price < 0:
                        print("Price cannot be negative")
                    else:
                        break
                except ValueError:
                    print("Invalid price. Please enter a number such 3.5")
            while True:
                try:
                    available_unit = int(input("Enter available unit: "))
                    if available_unit < 0:
                        print("Stock cannot be negative")
                    else:
                        break
                except ValueError:
                    print("Invalid stock value. Please enter a whole number such 1")

# store data in a dictionary
            rental = {
            "equipment": equipment_name,
            "price": rental_price,
            "unit": available_unit
        }

            return rental
    
#collect the dictionaries of products and store into a list

def collect_equipments():
    list_of_equipments = []
    answer = "yes"
    while True:
        if answer.lower().strip() == "yes":
            rental_equipment = get_equipments()
            list_of_equipments.append(rental_equipment)
        elif answer.lower().strip() == "no":
            break
        else:
            print("Invalid Response. Answer only yes or no")
        answer = input("Do you want to add another equipment? yes/no: ")
    
    return list_of_equipments


# create a function which will display a product summary
def show_equipments(rental_summary):
    print("\n---Equipment Rental Summary---")
    for key, value in rental_summary.items():
        if key == "price":
            print(f"{key.capitalize()}: €{value:.2f}")
        elif key == "unit":
            print(f"{key.capitalize()}: {value} units")
        else:
            print(f"{key.capitalize()}: {value}")

