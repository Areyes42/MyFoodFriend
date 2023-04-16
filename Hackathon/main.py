


def update_allergens():
    return

def update_emergency_contact_information():
    return

def display_list():
    return

def match_list():
    return

def report():
    #are you sure you want to report allergen reaction. Yes or no?
    #emergency services and x have been contacted
    #please input your symptoms
    return

def main_menu():
    print("=====MyFoodFriend=====")
    print("1) List")
    print("2) Scan")
    print("3) Settings")
    print("4) Report")
    print("5) Exit")

f = open("allergy_list.txt", "r")
allergy_list = f.read()

def main():
    choice = 0
    while choice != 5:
        main_menu()
        choice = int(input("Enter a choice: "))
        if choice == 1:
            print("I am allergic to:\n"+str(allergy_list))
        elif choice == 2:
            return true
        elif choice == 3:
            return true
        elif choice == 4:
            return true
        elif choice == 5:
            print("Have a nice day. Goodbye!")
        else:
            print("Invalid option")



main()