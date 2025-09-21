import math

# ------------------- Task 1: Main Menu by Ifty Zubaer -------------------
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
            calculate_bmi()
        elif option == 8:
            track_fitness()
        else:
            print("Error - Invalid option. Please input a number between 1 and 8.")

# ------------------- Task 2: Identify Hashtags by Salah Abdullah -------------------
def identify_hashtags():
    
    post = input("Type your post: ")        
    words = post.split(" ")                 

    hashtags = []                           
        
    for word in words:
        if len(word) > 1 and word[0] == "#":
            if word not in hashtags:
                hashtags.append(word)

    if len(hashtags) == 0:
        print("No hashtags found.")
    else:
        print("Hashtags found:")
        for tag in hashtags:
            print(tag)

# ------------------- Task 3: Detect a Palindrome by Ali Hamza -------------------
def detect_palindrome():
    name = input("Type your Pokemon name: ")
    lower_name = name.lower()
    length = len(lower_name)
    is_palindrome = True

    for i in range(length // 2):
        if lower_name[i] != lower_name[length - 1 - i]:
            is_palindrome = False

    if is_palindrome:
        print(f"The name '{name}' is a palindrome.")
    else:
        print(f"The name '{name}' is not a palindrome.")

# ------------------- Task 4: Create an Acronym by Ifty Zubaer -------------------
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

# ------------------- Task 5: Get Pokemon Traits by Salah Abdullah -------------------
def get_pokemon_traits():
    pokemon_name = input("Type your Pokemon name: ")
    pokemon_trait = input("Type your Pokemon trait: ")
    pokemon_trait = pokemon_trait.lower()
    valid_traits = ["water", "fire", "grass"]

    if pokemon_trait not in valid_traits:
        print("Error - The Pokemon type provided is not valid. Valid types: Water, Fire, Grass.")
        return  
    if pokemon_trait == "water":
        print(
            f"{pokemon_name.upper()} is a {pokemon_trait}-type pokemon!"
            "It is strong against Fire-type Pokemons and weak against Grass-type Pokemons."
        )
    elif pokemon_trait == "fire":
        print(
            f"{pokemon_name.upper()} is a {pokemon_trait}-type pokemon!"
            "It is strong against Grass-type Pokemons and weak against Water-type Pokemons."
        )
    elif pokemon_trait == "grass":
        print(
            f"{pokemon_name.upper()} is a {pokemon_trait}-type pokemon!"
            "It is strong against Water-type Pokemons and weak against Fire-type Pokemons."
        )
        
# ------------------- Task 6: Zodiac Sign and Eeveelution by Ali Hamza -------------------
def zodiac_and_eeveelution():
    month_input = input("Type your birth month: ")

    if not month_input.isdigit():
        print("Error - The month index provided is not valid. Choose between 1 and 12.")
        return

    month = int(month_input)

    if month < 1 or month > 12:
        print("Error - The month index provided is not valid. Choose between 1 and 12.")
        return

    zodiacs = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini",
               "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]

    zodiac_sign = zodiacs[month - 1]

    if zodiac_sign in ["Cancer", "Scorpio", "Pisces"]:
        element = "Water"
        eevee = "Vaporeon"
    elif zodiac_sign in ["Aries", "Leo", "Sagittarius"]:
        element = "Fire"
        eevee = "Flareon"
    elif zodiac_sign in ["Taurus", "Virgo", "Capricorn"]:
        element = "Earth"
        eevee = "Leafeon"
    else:
        element = "Air"
        eevee = "Jolteon"

    print(f"Zodiac sign: {zodiac_sign}")
    print(f"Element: {element}")
    print(f"Eeveelution: {eevee}")

# ------------------- Task 7: BMI Calculator by Salah Abdullah -------------------
def calculate_bmi():
    pokemon_height = float(input("Enter your height in meters: "))
    pokemon_weight = float(input("Enter your weight in kilograms: "))
     
    if pokemon_weight <= 0 and pokemon_height <= 0:
        print("Error - Height and weight must be numbers.")
    
    elif pokemon_weight <= 0:
        print("Error - Weight must be a positive number.")
        return
    
    elif pokemon_height <= 0:
        print("Error - Height must be a positive number.")
        return   
    
    else:
        bmi = pokemon_weight / (pokemon_height ** 2)
        
        if bmi < 29:
            print(f"BMI = {bmi:.2f}. The Pokemon is underweight.")
        
        elif 29 <= bmi < 53:
            print(f"BMI = {bmi:.2f}. The Pokemon is healthy.")
        
        elif 53 <= bmi < 85:
            print(f"BMI = {bmi:.2f}. The Pokemon is overweight.")
        
        else:
            print(f"BMI = {bmi:.2f}. The Pokemon is obese.")
            
# ------------------- Task 8: Fitness and Health Tracker by Ifty Zubaer -------------------
def track_fitness():
    steps_input = input("Step count per day: ")
    steps_str = steps_input.split(",")
    steps = []
    
    if steps_input.strip() == "":
        print("Error - Invalid input. The program needs 7 numbers; you typed 0 numbers.")
        return

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
if __name__ == "__main__":
    main_menu()