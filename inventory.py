#Import system form os , used to clear console
from os import system, path

LENGHTS :tuple = () 

#========The beginning of the class==========
class Shoe:

    def __init__(self, country: str, code: str, product: str, cost: int, quantity: int):
        '''Initialiser for shoe class'''
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)


    def get_cost(self):
        '''Returns cost property of shoe'''
        return self.cost


    def get_quantity(self):
        '''Returns quantity property of shoe'''
        return self.quantity


    def __str__(self) -> str:
        '''Returns string of shoe class'''
        global LENGHTS
        country_lenght = LENGHTS[0]
        code_lenght = LENGHTS[1]
        prod_lenght = LENGHTS[2]
        cost_lenght = LENGHTS[3]
        qty_lenght = LENGHTS[4]

        return f"| {self.product}".ljust(prod_lenght) + f"| {self.code}".ljust(code_lenght) +\
            f"| {self.quantity}".ljust(qty_lenght) + f"| {self.cost}".ljust(cost_lenght) +\
                f"| {self.country}".ljust(country_lenght) + " |"

#=============Shoe list===========
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data() -> list:
    ''''Read shoe data from "invetory.txt", return error message and exit if file not found'''

    shoe_data = []
    try:
        with open(f"{path.dirname(__file__)}\inventory.txt", "r") as data:
            for nr, line in enumerate(data):
                #Skip first line form "inventory.txt"
                if nr == 0:
                    continue
                #Proccess line form "invetory.txt" and append to shoe_data
                shoe_data.append(line.strip("\n").split(","))
        return shoe_data

    except FileNotFoundError:
        exit("The file 'invetory.txt' cannot be found, please create and place in directory")


def capture_shoes(shoe_data: list) -> list:
    '''Create Shoe class based on shoe_data and store objects in shoe_list'''
    [shoe_list.append(Shoe(shoe[0], shoe[1], shoe[2], shoe[3], shoe[4])) for shoe in shoe_data]


def get_max_string_lenght(shoe_data: list) -> tuple:
    '''Find max sting length of items in shoe_data to help build table'''

    max_country_lenght = len("| Country ")
    max_code_lenght = len("| Code ")
    max_prod_lenght = len("| Prod ")
    max_cost_lenght = len("| Cost ")
    max_qty_lenght = len("| Qty ")

    for shoe in shoe_data:
        if len(shoe[0]) > max_country_lenght:
            max_country_lenght = len(shoe[0]) + 3
        if len(shoe[1]) > max_code_lenght:
            max_code_lenght = len(shoe[1]) + 3
        if len(shoe[2]) > max_prod_lenght:
            max_prod_lenght = len(shoe[2]) + 3
        if len(shoe[3]) > max_cost_lenght:
            max_cost_lenght = len(shoe[3]) + 3
        if len(shoe[4]) > max_qty_lenght:
            max_qty_lenght = len(shoe[4]) + 3
    
    global LENGHTS
    LENGHTS = (max_country_lenght, max_code_lenght, max_prod_lenght, max_cost_lenght, max_qty_lenght)


def header(line_lenght=0) -> str:
    '''Prints heaeder into console, provided max string lenghts for columns'''

    global LENGHTS
    #Assign lenghts to variables for easy placement in string
    country_lenght = LENGHTS[0]
    code_lenght = LENGHTS[1]
    prod_lenght = LENGHTS[2]
    cost_lenght = LENGHTS[3]
    qty_lenght = LENGHTS[4]

    #Build Header string
    header_str = "\033[4m" + "| Product".ljust(prod_lenght) + "| Code".ljust(code_lenght) \
        + "| Qty".ljust(qty_lenght) + "| Cost".ljust(cost_lenght) + "| Country".ljust(country_lenght) + " |"

    #Build line string
    if line_lenght == 0:
        line_lenght = (len(header_str) - 4)

    line = ("_" * line_lenght)

    return f"{line}\n{header_str}"


def view_all() -> None:
    '''Prints table of all shoes in shoe_list in table format, provided max lenghts for columns'''
    #Print header
    print(header())

    #Loop through shoe_list and print out string of each shoe object
    for shoe in shoe_list:
        print(shoe.__str__())

    #Stop underlining text in console output 
    print("\033[0m")


def add_tag(tag: str) -> str:
    '''Creates a tag to print  ex. ---[ text ]--- '''
    #Calculate line lenght for tag
    line = int((len(header()) / 2) / 2) - int(len(tag) / 2)

    return f"{('-' * line)}[{tag}]{'-' * line}"


def search_shoe(shoe_code: str) -> None:
    '''Print shoe based on Code'''

    #Get shoe using list comprehension based in shoe.code
    shoe = [shoe for shoe in shoe_list if shoe.code == shoe_code]
    if len(shoe) == 0:
        print(f"\n >>> Shoe with code: '{shoe_code}' was not found !! <<< \n")
    else:
        print(add_tag(shoe_code))
        print(header())
        print(shoe[0].__str__())
        print("\033[0m")


def value_per_item() -> None:
    '''Calculates and prints out value per item for all shoes'''
    
    #Add extra column to table " Value / Item "
    value_str = " Value / Item "
    column_len =  len(value_str)

    #Calculate column width
    len_line = (int(len(header()) / 2)) + len(value_str.ljust(column_len) + "|")

    #Print header for table
    print(header(len_line) + value_str.ljust(column_len) + "  |")

    #Calculate all total valules for each shoe and print out in table
    for shoe in shoe_list:
        shoe_total_value = shoe.cost * shoe.quantity
        print(shoe.__str__() + " " + str(shoe_total_value).ljust(column_len) + " |")

    #Stop underlining text in console output 
    print("\033[0m")   


def re_stock() -> None:
    '''Get Shoe that is lowest in stock and print out'''

    print(add_tag("LOW ON STOCK"))
    #Get shoe with the minimum qty from shoes
    min_qty = min(shoe.quantity for shoe in shoe_list)

    #Call search shoe and print out shoe with the minimum qty from shoes
    [search_shoe(shoe.code) for shoe in shoe_list if shoe.quantity == min_qty]


def highest_qty():
    '''Prints out Shoe with highest qty and that is on sale'''

    print(add_tag("ON SALE"))

    #Calcualte which shoe should go on sale, and print out by calling search_shoe
    max_qty = max(shoe.quantity for shoe in shoe_list)
    [search_shoe(shoe.code) for shoe in shoe_list if shoe.quantity == max_qty]


def update_database():
    '''Calls other functions to build database'''

    #If there is already data in database will clear to prevent duplication
    if len(shoe_list) > 0:
        shoe_list.clear()

    #Call read_shoes_data to get list of shoes
    shoe_data = read_shoes_data()

    #Call capture_shoes to create Shoe objects form shoe_data
    capture_shoes(shoe_data)

    #Call get_max_string_lenght to get column widths for table
    get_max_string_lenght(shoe_data)

    print(f"\n >>> {len(shoe_list)} shoes were loaded from 'inventory.txt' <<< \n")


def main():
    '''Main function , calls other functions base on user input'''

    system("cls")
    print(">>> Starting Shoe Inventory Managemnet System <<<")
    update_database()

    while True:
        print("Shoe Inventory Managemnet System: ")
        print("  1. Update Shoes from 'inventory.txt'.")
        print("  2. View Shoes in database.")
        print("  3. Show 'Low Stock' shoe.")
        print("  4. Put 'Sale' on highest qty shoe.")
        print("  5. Calculate total value / shoe.")
        print("  6. Search for shoe.")
        print("  0. Exit.")

        user_input = input("\n >>> ")
        system("cls")

        if user_input == "1":
            update_database()

        elif user_input == "2":
            view_all()

        elif user_input == "3":
            re_stock()

        elif user_input == "4":
            highest_qty()

        elif user_input == "5":
            value_per_item()

        elif user_input == "6":
            shoe_code = input("Shoe Code: ").upper()
            search_shoe(shoe_code)

        elif user_input == "0":
            exit("\n >>> Bye Bye !!  <<< \n")

        else:
            print(f"\n >>> Wrong choice try again !! <<< \n")

#==========Main Menu=============
main()