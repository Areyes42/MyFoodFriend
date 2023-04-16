def load_user_info(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
    f.close()

    user_dict = {}
    for i in range(0, len(lines), 2):
        key = lines[i]
        value = lines[i+1]
        user_dict[key] = value

    return user_dict

def save_user_info(file_name, user_dict):
    with open(file_name, 'w') as f:
        for key, value in user_dict.items():
            f.write(key + '\n')
            f.write(value + '\n')
    f.close()

def edit_settings():
    file_name = 'user_information.txt'
    user_dict = load_user_info(file_name)

    while True:
        print("======Current Settings======")
        for key, value in user_dict.items():
            print(f"{key}: {value}")

        setting = input("Select a setting to edit (or 'q' to quit): ")
        if setting.lower() == 'q':
            break

        if setting not in user_dict:
            print("Invalid setting. Please try again.")
            continue

        new_value = input(f"Enter a new value for '{setting}': ")
        user_dict[setting] = new_value

    save_user_info(file_name, user_dict)
    print("Settings saved.")



def user_info(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    f.close()

    user_dict = {}
    for i in range(0, len(lines), 2):
        key = lines[i]
        value = lines[i + 1]
        user_dict[key] = value

    return user_dict


def display_settings():
    settings = ''


def display_list():
    f = open("allergy_list.txt", "r")
    allergy_list = f.read()
    return allergy_list


def main_menu():
    print("======MyFoodFriend======")
    print("1) List")
    print("2) Scan")
    print("3) Settings")
    print("4) Report")
    print("5) Exit")



f = open("user_information.txt")

def main():
    choice = 0
    while choice != 5:
        main_menu()
        choice = int(input("Enter a choice: "))
        if choice == 1:
            print("I am allergic to:\n"+str(display_list()))
            print()
        elif choice == 2:
            user_upc = input("Enter a UPC file to scan: ")
            temp_file = (open(user_upc, "r"))
            file = open("allergy_list.txt", "r")
            allergy_list = file.read()
            upc_ingredients = temp_file.read().lower().split("\n")
            list_of_allergies = allergy_list.lower().split("\n")
            for allergy in list_of_allergies:
                for ingredient in upc_ingredients:
                    if allergy == ingredient:
                        print("You are allergic to:", allergy, "in", user_upc.replace(".txt", ""))
                        print()


        elif choice == 3:
            edit_settings()
            print()

        elif choice == 4:
            verification = input("Are you sure you want to report an allergic reaction?\nY or N: ")
            if verification.lower() == 'y':
                print("Your emergency contacts have been notified. Try to remain calm.\n")
            else:
                print("Returning...\n")
        elif choice == 5:
            print("Have a nice day. Goodbye!")
        else:
            print("Invalid option")



main()