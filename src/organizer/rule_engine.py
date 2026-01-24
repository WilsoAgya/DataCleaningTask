'''
Ask the user how they which type of files they want organized
If they want to organize more types of files then it will ask them to enter the prompt again
    1. Ask the user for which choicie they want
    2. If it is a valid choice ask the user if they want to choose another type to organize as well
    3. If the choose selects yes then prompt the user with the menu again
If they want all files to be organized don't ask again
'''


def userprompt():
    user_choices = []
    while True:
        menu = (
        "\nSelect which type of file you would like to organize:\n\n"
        "1. Documents\n"
        "2. Images\n"
        "3. Videos\n"
        "4. Recordings\n"
        "5. Other\n"
        "6. All Files\n"
        )

        menu_choices = {
            1 : "Documents",
            2 : "Images",
            3 : "Videos",
            4 : "Recordings",
            5 : "Other",
            6 : "All Files"
        }

        print(menu)
        file_choice = int(input("Your choice → "))

        '''if not file_choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 6.")'''

        if file_choice in menu_choices:
            selected = menu_choices[file_choice]
            print(f"You selected {selected}")
            user_choices.append(selected)
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


        if 5 >= file_choice >= 1:
            print("\nAre there other files you would also like to organize?")
            choose_again = input("Yes\nNo\n").strip().lower()


            if choose_again not in ('yes', 'y'):
                print(f"The following will be organized {user_choices}")
                break

        if file_choice == 6:
            print("\nAll files will be organized to their own folder")
            print(user_choices)
            break


print("=============DATA CLEANER: CLEAN ALL DATA IN A GIVEN FOLDER============")
userprompt()


