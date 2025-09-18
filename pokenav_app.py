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

        word = word.strip(".,!?;:") # Remove this line – punctuation must stay with the word (see example 2)
    
        if len(word) > 1 and word[0] == "#":

            word = word.lower() # Remove this line – hashtags should keep their original case

            if word not in hashtags:
                hashtags.append(word)

    if len(hashtags) == 0:
        print("No hashtags found.")
    elif len(hashtags) == 1: # Remove this elif – always use "Hashtags found:" even if only one hashtag
        print("Hashtag found:", hashtags[0])
    else:
        print("Hashtags found:")
        for tag in hashtags:
            print(tag)

# ------------------- Task 3: Detect a Palindrome by Ali Hamza -------------------
def detect_palindrome():
    print("This is Task 3, Assigned to Ali")

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
    pokemon_name = pokemon_name.upper() # Remove this – we should not force names to uppercase globally
    valid_traits = ["water", "fire", "grass"]
    if pokemon_trait not in valid_traits:
        pokemon_trait = None # Remove this – unnecessary, since you already return after printing error
        print("Error - The Pokemon type provided is not valid. Valid types: Water, Fire, Grass.")
        return  
    if pokemon_trait == "water":
        # pokemon_name.upper is a method, needs () → pokemon_name.upper()
        # Also: keep formatting consistent with Fire/Grass cases
        print(f'{pokemon_name.upper} is a {pokemon_trait}-type pokemon! It is strong against Fire-type Pokemon and weak against Grass-type Pokemons.')
    elif pokemon_trait == "fire":
        # pokemon_name.upper is wrong (missing ())
        # Extra space in "Water -type"
        print(f"{pokemon_name.upper} is a {pokemon_trait}-type pokemon! It is strong against Grass-type Pokemon and weak against Water -type Pokemons.")
    elif pokemon_trait == "grass":
        # Inconsistent formatting: uses pokemon_name.title() instead of same style as others
        print(f"{pokemon_name.title()} is a {pokemon_trait}-type pokemon! It is strong against Water-type Pokemon and weak against Fire-type Pokemons.")
        
# ------------------- Task 6: Zodiac Sign and Eeveelution by Ali Hamza -------------------
def zodiac_and_eeveelution():
    print("This is Task 6, Assigned to Ali")

# ------------------- Task 7: BMI Calculator by Salah Abdullah -------------------
def calculate_bmi():
    pokemon_height = float(input("Enter your height in meters: "))
    pokemon_weight = float(input("Enter your weight in kilograms: "))

    if pokemon_weight <= 0 and pokemon_height <= 0:
        print("Error - Height and weight must be positive number.")
        return
    elif pokemon_weight <= 0:
        print("Error - Weight must be positive a number.")
        return
    elif pokemon_height <= 0:
        print("Error - Height must be positive number.")
        return   
    
    else:
        bmi = pokemon_weight / (pokemon_height ** 2)
    if bmi < 29:
        print(f"BMI = {bmi:.2f}. The Pokemon is underweight.")
    elif 29 <= bmi < 53:
        print(f"BMI = {bmi:.2f}. The Pokemon is normal weight.")
    elif 53 <= bmi < 85:
        print(f"BMI = {bmi:.2f}. The Pokemon is overweight.")
    else:
        print(f"BMI = {bmi:.2f}. The Pokemon is obese.")

# ------------------- Task 8: Fitness and Health Tracker by Ifty Zubaer -------------------
def track_fitness():
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
if __name__ == "__main__":
    main_menu()