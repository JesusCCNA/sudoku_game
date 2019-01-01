import random
import pygame
# Program that generates a  9x9 sudoku

# Create GUI

"""
(width, height) = (600, 600)
background_color = (252, 238, 220)
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)
pygame.display.set_caption("Sudoku Game - JesusCCNA ")
pygame.display.flip()
"""

def check_validity(key, field_value):
    actual_position = ord(key)
    if actual_position > 65 and actual_position < 68:
        validations_needed = actual_position - 65
        validation_done = 0
    if actual_position >= 68 and actual_position < 71:
        validations_needed = actual_position - 67
        validation_done = 0
        for key_this in fields:
            print(key_this)
            if key_this == key:
                break
            print(key)
            print(len(fields[key]))
            print(fields["A"])
            print(fields["B"])
            print(fields["C"])
            print(fields["D"])
            print(fields["E"])
            print(fields["F"])
            print("field value = " + str(field_value))
            if field_value == fields[key_this][len(fields[key])]:
                print("ERROR")
                print(str(field_value) + "==" + str(fields[key_this][len(fields[key])]))
                return False

    if actual_position >= 71 and actual_position < 73:
        validations_needed = actual_position - 70
        validation_done = 0
        for key_this in fields:
            print(key_this)
            if key_this == key:
                break
            print(key)
            print(len(fields[key]))
            print(fields["A"])
            print(fields["B"])
            print(fields["C"])
            print(fields["D"])
            print(fields["E"])
            print(fields["F"])
            print(fields["G"])
            print("field value = " + str(field_value))
            if field_value == fields[key_this][len(fields[key])]:
                print("MIERDAAA")
                print(str(field_value) + "==" + str(fields[key_this][len(fields[key])]))
                return False




    for validation in range(1, validations_needed + 1):
        if actual_position > 65 and actual_position < 68:
            if field_value not in fields[str(chr(actual_position-1))][x:y + 1] and field_value not in fields[key]:
                #print(fields[str(chr(actual_position-1))][x:y + 1])
                actual_position -= 1
                validation_done += 1
                #print(str(validations_needed) + "/done: " + str(validation_done))

                if validation_done == validations_needed:
                    return True
            else:
                return False
        if actual_position == 68:
            if field_value not in fields[key]:
                actual_position -= 1
                validation_done += 1
                #print(str(validations_needed) + "/done: " + str(validation_done))

                if validation_done == validations_needed:
                    return True
            else:
                return False

        if actual_position > 68 and actual_position < 71:
            if field_value not in fields[str(chr(actual_position-1))][x:y + 1] and field_value not in fields[key]:
                #print(fields[str(chr(actual_position-1))][x:y + 1])
                actual_position -= 1
                validation_done += 1
                #print(str(validations_needed) + "/done: " + str(validation_done))

                if validation_done == validations_needed:
                    return True
            else:
                return False

        if actual_position == 71:
            if field_value not in fields[key]:
                actual_position -= 1
                validation_done += 1
                #print(str(validations_needed) + "/done: " + str(validation_done))

                if validation_done == validations_needed:
                    return True
            else:
                return False

fields = {  "A" : [random.randint(1,9)],
            "B":[], "C": [], "D": [], "E": [], "F": [], "G": [],
        }

for number in range(1,9):
    field_value = random.randint(1,9)

    while field_value in fields["A"]:
        field_value = random.randint(1,9)

    fields["A"].append(field_value)


for key in fields.keys():
    x = 0
    y = 2
    i = 0
    if key == "A":
        continue
    for number in range(1, 4):
        while True:
            field_value = random.randint(1,9)
            if check_validity(key, field_value):
                fields[key].append(field_value)
                i += 1
                if i == 3:
                    x = y + 1
                    y += 3
                    i = 0
                    break



print(fields["A"])
print(fields["B"])
print(fields["C"])
print(fields["D"])
print(fields["E"])
print(fields["F"])
print(fields["G"])
