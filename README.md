PokéNav App
============

Authors: Ifty Zubaer, Salah Abdullah, and Ali Hamza  
Group: Ifty Salah Ali  
Course: DIT009 – Fundamentals of Programming  

---

Task Division
-------------
- Task 1: **Ifty** implemented the main menu.  
- Task 2: **Salah** implemented the hashtag detection.  
- Task 3: **Ali** implemented the palindrome detection.  
- Task 4: **Ifty** implemented the acronym feature.  
- Task 5: **Salah** implemented the Pokémon traits feature.  
- Task 6: **Ali** implemented the zodiac and eeveelution feature.  
- Task 7: **Salah** implemented the BMI calculator (average and categorization).  
- Task 8: **Ifty** implemented the fitness and health tracker (average and standard deviation).  
- Task 9: Each member implemented the error handling for their own tasks.  
- Code Review / Project Review: **Ifty** also acted as the reviewer for the project.

---

Program Description
-------------------
This program is an implementation of the PokéNav App as described in the assignment instructions.  
It uses only basic procedural programming concepts:

- Printing
- Input
- Variables
- Conditionals
- For loops
- While loops
- Lists
- String manipulation
- Functions
- (math library is used where required)

The program starts with a main menu and allows the user to choose between 8 different tasks.  
After each task finishes, the program returns to the main menu. The program only ends when the user selects option 1 (Exit).  

---

How to Run
----------
1. Make sure the file name is exactly: **pokenav_app.py**  
2. Run the program with:
   ```
   python pokenav_app.py
   ```
3. The main menu will appear. Type a number between 1 and 8 to select an option.  
4. After each task, you will be returned to the main menu.

---

Examples
--------
Below are examples based on the assignment description:

Task 1: Exit
-------------
Input:
```
1
```
Output:
```
Thank you for playing! See you next time!
```

Task 2: Identify Hashtags
--------------------------
Input:
```
Type your post: Today is a great day for #battle and #catch them all. Love to #battle
```
Output:
```
Hashtags found:
#battle
#catch
```

Task 3: Detect a Palindrome
----------------------------
Input:
```
Type your Pokémon name: Eevee
```
Output:
```
The name 'Eevee' is a palindrome.
```

Input:
```
Type your Pokémon name: Charizard
```
Output:
```
The name 'Charizard' is not a palindrome.
```

Task 4: Create an Acronym
--------------------------
Input:
```
Type your Pokémon name: Crabominable
Type your shortening factor: 4
```
Output:
```
Abbreviated name: BNE
```

Task 5: Get Pokémon Traits
---------------------------
Input:
```
Type your Pokémon name: Squirtle
Type your Pokémon type: Water
```
Output:
```
Squirtle is a Water-type Pokémon! It is strong against Fire-type Pokémons and weak against Grass-type Pokémons.
```

Task 6: Zodiac Sign and Eeveelution
-----------------------------------
Input:
```
Type your birth month: 7
```
Output:
```
Zodiac sign: Cancer
Element: Water
Eeveelution: Vaporeon
```

Task 7: BMI Calculator
-----------------------
Input:
```
Type Pokémon height (m): 1.2
Type Pokémon weight (kg): 100
```
Output:
```
BMI = 69.44. The Pokémon is overweight.
```

Task 8: Fitness and Health Tracker
----------------------------------
Input:
```
Step count per day: 3200, 1400, 5000, 2000, 100, 5000, 1740
```
Output:
```
Steps Statistics: 2634.29 + / - 1718.03 per day.
Most active day: Friday. Least active day: Thursday.
```

---

Error Handling
--------------
The program also includes error handling as required by Task 9.  
Examples:

- Menu:
  ```
  Type your option: 11
  Error - Invalid option. Please input a number between 1 and 8.
  ```

- Hashtags:
  ```
  Type your post: This sentence has no hashtags.
  No hashtags found.
  ```

- Pokémon Traits:
  ```
  Type your Pokémon type: apple
  Error - The Pokémon type provided is not valid. Valid types: Water, Fire, Grass.
  ```

- Zodiac:
  ```
  Type your birth month: 13
  Error - The month index provided is not valid. Choose between 1 and 12.
  ```

- BMI:
  ```
  Type Pokémon height (m): -90
  Type Pokémon weight (kg): 5
  Error - Height must be a positive number.
  ```

- Fitness Tracker:
  ```
  Step count per day: 100, 100, 200
  Error - Invalid input. The program needs 7 numbers; you typed 3 numbers.
  ```

---

Grading Goals
-------------
- Grade 3 (Pass): Tasks 1–7 implemented.
- Grade 4 (Pass with Merit): Task 8 implemented.
- Grade 5 (Pass with Distinction): Tasks 8 and 9 implemented.

This submission includes Tasks 1–8 and full error handling (Task 9), therefore targeting **Grade 5 (Distinction)**.