import random
import time


def cat(eye):
    return f'''/|__/|\\
(={eye}=)
(")(")_|
'''

print("Hello, this is a cat:\n")
print(cat('^.^'))

while True:
    try:
        first_input = int(input("How many cats do you want to appear next to each other? Pick a number between 1 and 10: "))
        if first_input > 0 and first_input <= 10:
            break
        else:
            print("Please enter a number between 1 and 10.")
    except ValueError:
        print("That is not a number. Try again.")


while True:
    try:
        second_input = int(input("How many rows of cats do you want to appear beneath each other? Please pick a number between 1 and 10: "))
        if second_input > 0 and  second_input <= 10:
            break
        else:
            print("Please enter a number between 1 and 10.")
    except ValueError:
        print("That is not a number. Try again.")


third_input = input("Should the cats be in a happy, surprised, sleepy or randomly chosen mood? Please enter 'happy', 'surprised', 'sleepy' or 'random'.")

eye_styles = ['^.^', '°.°', 'o_o', 'O.O', '@_@']
def eye_mood(third_input):
    if third_input == 'happy':
        return '^.^'
    elif third_input == 'surprised':
        return '°.°'
    elif third_input == 'sleepy':
        return '-.-'
    elif third_input == 'random':
        return random.choice(eye_styles)
    else:
        return '^.^'

print("\n Please wait while your cats are generated...\n")
time.sleep(3)

#AI helped me write this segment because I couldn't figure out how to make the cats appear next to each other since they spread over three lines
for r in range(second_input):
    for line in range(3):
        for c in range(first_input):
            eye = eye_mood(third_input)
            if line == 0:
                print('/|__/|\\ ', end='')
            elif line == 1:
                print(f'(={eye}=) ', end='')
            else:
                print('(")(")_| ', end='')
        print()
    print()

print("Thank you for playing!")
