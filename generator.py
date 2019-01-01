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


fields = {"A" : [random.randint(1,9)],
        }

for number in range(1,9):
    field_value = random.randint(1,9)

    while field_value in fields["A"]:
        field_value = random.randint(1,9)

    fields["A"].append(field_value)

"""
for number in range(1, 9):
    field_value = random.randint(1,9)
    while True:
        field_value = random.randint(1,9)



    fields["B"].append(field_value)
"""

print(fields["A"])
