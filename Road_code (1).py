"""
File: Road_code.py
Author: Cohen Fourie 
Date:
Description:
"""
def get_guestions():
    # Questions for quiz 

    return [
    "When coming up to a pedestrian crossing without a raised traffic island, what must you do?", 
    "When driving at night on a road with lanes you must be able to stop in half the length of clear road you can see in front of you.",
    "What should you do when you are coming up to traffic signals and the signals change from green to yellow?",
    "You MUST dip the headlights on your vehicle when:",
    "What may you do at traffic signals if there is a green arrow pointing to the right and a red light showing at the same time?",
    "If you have a learner licence can you carry passengers?",
    "What lights should you use if your vehicle has broken down and is being towed?",
    "What is the maximum speed you may drive if you have a 'space saver wheel' fitted? (km/h)",
    "When turning right from a two-laned road into a one-way street that has two lanes, you must turn into the:",
    "When coming up to a roundabout you must give way to all vehicles that will cross your path from your left.?"]


def showing_main_menu():
    # First Menu which will ask whether user wants to continue or choose a different road code test

    print("""Hello, welcome to Cohen's Road Code test. Please choose an option below either 1, 2 or 3 (please input in numerical form)
    1) Run road code program, where you'll answer 10 questions and have a score 
    2) Run road code test, until you get 1 question wrong out of 10 questions
    3) EXIT """)
    
    
def user_main_menu_response():
    # Asking for users answer for first menu

    User_Menu_Choice = input("What is your choice?\n")
    return User_Menu_Choice 


def validate_user_response(menu_response):
    # Validating users response for main menu and ch

    result = "error
    if menu_response == "1":
        return "1"
    elif menu_response == "2":
        return "2"
    elif menu_response == "3":
        return "3"
        
    else:
        print("Invalid try again, please enter a valid number!")
        return "error"

    return result

def main():

    showing_main_menu()

    menu_response = user_main_menu_response()
    validated_response = validate_user_response(menu_response)

    while (validated_response == "error"):
        menu_response = user_main_menu_response()
        validated_response = validate_user_response(menu_response)


    print("the user chose: " + validated_response)


main()