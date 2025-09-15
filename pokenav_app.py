import math

# ------------------- Task 1: Main Menu -------------------
def main_menu():
    option = 0
    while option != 1:
        print("\nWelcome to the Main Menu. Choose one of the options below:")
        print("1. Exit")
        print("2. Identify hashtags")
        print("3. Detect a palindrome")
        print("4. Create an acronym")
        print("5. Get Pokemon traits")
        print("6. Match zodiac sign and element")
        print("7. BMI calculator")
        print("8. Fitness and health tracker")

        option_input = input("Type your option: ")

        if not option_input.isdigit():
            print("Error - Invalid option. Please input a number between 1 and 8.")
            continue

        option = int(option_input)

        if option == 1:
            print("Thank you for playing! See you next time!")
        elif option == 2:
            identify_hashtags()
        elif option == 3:
            detect_palindrome()
        elif option == 4:
            create_acronym()
        elif option == 5:
            get_pokemon_traits()
        elif option == 6:
            zodiac_and_eeveelution()
        elif option == 7:
            bmi_calculator()
        elif option == 8:
            fitness_tracker()
        else:
            print("Error - Invalid option. Please input a number between 1 and 8.")

# ------------------- Task 2: Identify Hashtags -------------------
def identify_hashtags():
    print("This is Task 2, Assigned to Salah")

# ------------------- Task 3: Detect a Palindrome -------------------
def detect_palindrome():
    print("This is Task 3, Assigned to Ali")

# ------------------- Task 4: Create an Acronym -------------------
def create_acronym():
    name = input("Type your Pokemon name: ")
    factor_input = input("Type your shortening factor: ")

    if not factor_input.isdigit():
        print("Error - Shortening factor must be an integer.")
        return

    factor = int(factor_input)

    acronym = ""
    index = factor - 1

    while index < len(name):
        acronym += name[index].upper()
        index += factor

    print("Abbreviated name:", acronym)

# ------------------- Task 5: Get Pokemon Traits -------------------
def get_pokemon_traits():
    print("This is Task 5, Assigned to Salah")

# ------------------- Task 6: Zodiac Sign and Eeveelution -------------------
def zodiac_and_eeveelution():
    print("This is Task 6, Assigned to Ali")

# ------------------- Task 7: BMI Calculator -------------------
def bmi_calculator():
    print("This is Task 7, Assigned to Salah")

# ------------------- Task 8: Fitness and Health Tracker -------------------
def fitness_tracker():
    steps_input = input("Step count per day: ")
    steps_str = steps_input.split(",")
    steps = []

    for s in steps_str:
        s = s.strip()
        if not s.isdigit():
            print("Error - Invalid input. Steps must be integers.")
            return
        steps.append(int(s))

    if len(steps) != 7:
        print(f"Error - Invalid input. The program needs 7 numbers; you typed {len(steps)} numbers.")
        return

    total = 0
    for value in steps:
        total += value
    avg = total / 7

    variance_sum = 0
    for value in steps:
        variance_sum += (value - avg) ** 2
    variance = variance_sum / 7
    std_dev = math.sqrt(variance)

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    most_index = 0
    least_index = 0
    for i in range(7):
        if steps[i] >= steps[most_index]:
            most_index = i
        if steps[i] <= steps[least_index]:
            least_index = i

    print(f"Steps Statistics: {avg:.2f} + / - {std_dev:.2f} per day.")
    print(f"Most active day: {days[most_index]}. Least active day: {days[least_index]}.")

# ------------------- Run Program -------------------
main_menu()