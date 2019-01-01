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
    validations_needed = actual_position - 65
    validation_done = 0
    for validation in range(1, validations_needed + 1):
        if field_value not in fields[str(chr(actual_position-1))][x:y + 1] and field_value not in fields[key]:
            #print(fields[str(chr(actual_position-1))][x:y + 1])
            actual_position -= 1
            validation_done += 1
            #print(str(validations_needed) + "/done: " + str(validation_done))

            if validation_done == validations_needed:
                return True
        else:
            return False


fields = {  "A" : [random.randint(1,9)],
            "B":[], "C": [],
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
