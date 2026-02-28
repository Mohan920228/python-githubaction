hours_in_day = 24
units = "hours"

user_input = input("Enter your number:\n")


def units_to_hours(no_of_days):
    return f"you have entered {no_of_days}, the calculated value is {no_of_days * hours_in_day} {units}"


def validate_execute():
    # if user_input.isdigit():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculate_value = units_to_hours(user_input_number)
            print(calculate_value)
        elif user_input_number < 0:
            print("You have entered a negative number")
        elif int(user_input) == 0:
            print("you have entered Zero")
    # else:
    except ValueError:
        print("You have entered an invalid number")


validate_execute()
