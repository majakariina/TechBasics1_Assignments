# Assignment 2: python text game

print("Let's learn about the world!")

# Europe
print("We are currently in Europe.\n What is the smallest country in Europe? \n 1. San Marino \n 2. Monaco \n 3. Andorra \n 4. Vatican City  ")

question_1 = (input("Please choose the correct answer."))

if question_1 == "4.":
    print("Your answer is correct! Vatican City is the smallest country in Europe!")
elif question_1 == "1." or "2." or "3.":
    print("False. Vatican City is the smallest country in Europe!")
else:
    print("Invalid choice. Pleas choose between 1. and 4.")

#Africa
print("We have now left Europe and have now arrived in Asia!")
print("What is the name of the biggest lake in Africa? \n 1. Lake Victoria \n 2. Lake Malawi \n 3. Lake Tanganyika \n 4. Lake Turkana")

question_1 = (input("Please choose the correct answer."))

if question_1 == "1.":
    print("Your answer is correct!")
elif question_1 == "2." or "3." or "4.":
    print("False. The correct answer is Lake Victoria!")
else:
    print("Invalid choice. Pleas choose between 1. and 4.")

# Asia
print("We have now left Europe and have now arrived in Asia!")
print("Naypyidaw is the capital of which country in Asia? \n 1. Mongolia \n 2. Tajikistan \n 3. Myanmar \n 4. East Timor")

question_2 = (input("Please choose the correct answer."))

if question_2 == "3.":
    print("Your answer is correct! Naypyidaw is the capital of Myanmar!")
elif question_1 == "1." or "2." or "4.":
    print("False. Naypyidaw is the capital of Myanmar!")
else:
    print("Invalid choice. Pleas choose between 1. and 4.")

# Oceania
print("We have now arrived in Oceania!")
print("In which of the following countries is rugby not the national sport? \n 1. New Zealand \n 2. Australia \n 3. Samoa \n 4. Fiji")

question_2 = (input("Please choose the correct answer."))

if question_2 == "2.":
    print("Your answer is correct! Australia's national sport is not rugby but cricket!")
elif question_1 == "1." or "3." or "4.":
    print("False. The correct answer is Australia.")
else:
    print("Invalid choice. Pleas choose between 1. and 4.")

# North and Central America
print("We are now on North and Central America!")
print("What is the currency in Mexico? \n 1. Mexican peso \n 2. Mexican dollar \n 3. Mexican quetzal \n 4. US dollar")

question_2 = (input("Please choose the correct answer."))

if question_2 == "1.":
    print("Your answer is correct!")
elif question_1 == "2." or "3." or "4.":
    print("False. The correct answer is Mexican peso.")
else:
    print("Invalid choice. Pleas choose between 1. and 4.")

# South America
print("Only two continents left! We are now in South America")
print("Which country are the Easter Islands located in? \n 1. Peru \n 2. Ecuador \n 3. Chile \n 4. Argentina")

question_2 = (input("Please choose the correct answer."))

if question_2 == "3.":
    print("Your answer is correct!")
elif question_1 == "1." or "2." or "4.":
    print("False. The correct answer is Chile.")
else:
    print("Invalid choice. Pleas choose between 1. and 4.")

# Antarctica
print("It's cold now! We are in Antarctica")
print("Which of these animals do not appear in Antarctica? \n 1. Penguins \n 2. Whales \n 3. Seals \n 4. Polar Bears")

question_2 = (input("Please choose the correct answer."))

if question_2 == "4.":
    print("Your answer is correct!")
elif question_1 == "1." or "2." or "3.":
    print("False. The correct answer is polar bears. \n You have now visited all continents! Thank you for playing!")
else:
    print("Invalid choice. Pleas choose between 1. and 4.")


