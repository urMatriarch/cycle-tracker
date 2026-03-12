def confirmation(response, num_attempts = 3, custom = None):
    if custom == None:
        print(f"Confirm input: {response}?")
    else:
        print(f"{custom} {response}")
    ans = input("y/n --> ").lower()
    match ans:
        case "y" | "ye" | "yes":
            return True
        case "n" | "no":
            return False
        case default:
            if num_attempts == 0:
                raise Exception("Too many invalid attempts")
            print("Try again...")
            num_attempts -= 1
            confirmation(response, num_attempts, custom)