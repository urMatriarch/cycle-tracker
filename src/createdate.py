import datetime as dt
from confirmation import confirmation
from dateutil.relativedelta import relativedelta

def create_date():
    #TODO create function to allow easy datetime creation
    pass

def create_deltatime():
    print(f"Create complex or simple duration?")
    choice = input("--> ").lower()
    match choice:
        case "simple" | "sim" | "s":
            print(f"Simple duration selected.")
            print(f"How many days long should the duration be?")
            return dt.timedelta(int(input("--> ")))
        case "complex" | "com" | "c":
            valid_input = False
            while valid_input == False:
                print(f"Please enter the task duration in the following format. Enter 0 if duration is less than month or year.")
                print(f"YEARS, MONTHS, DAYS")
                units = input("--> ").split(",")
                if len(units) != 3:
                    raise Exception("Invalid format submitted. Please use the following format: YEARS, MONTHS, DAYS")
                else:
                    for unit in units:
                        unit.strip()
                    #This feels like a silly solution :/
                    return relativedelta(years = int(units[0]), months = int(units[1]),days = int(units[2]))

        case default:
            print(f"Bad input detected")
            return