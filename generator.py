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


fields = {  "A" : [random.randint(1,9)],
            "B":[]
        }

for number in range(1,9):
    field_value = random.randint(1,9)

    while field_value in fields["A"]:
        field_value = random.randint(1,9)

    fields["A"].append(field_value)

x = 0
y = 2
i = 0
for number in range(1, 4):
    while True:
        field_value = random.randint(1,9)
        if field_value not in fields["A"][x:y] and field_value not in fields["B"]:
            fields["B"].append(field_value)
            i += 1
            if i == 3:
                x = y + 1
                y += 3
                i = 0
                break




print(fields["A"])
print(fields["B"])
