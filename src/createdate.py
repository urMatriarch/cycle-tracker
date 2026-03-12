import datetime as dt

def create_date():
    #TODO create function to allow easy datetime creation
    pass

def create_deltatime():
    print(f"Create complex or simple duration?")
    choice = input("--> ")
    match choice:
        case "simple" | "sim" | "s":
            print(f"Simple duration selected.")
            print(f"How many days long should the duration be?")
            return dt.timedelta(int(input("--> ")))
        case "complex" | "com" | "c":
            #TODO
            pass
        case default:
            print(f"Bad input detected")
            return