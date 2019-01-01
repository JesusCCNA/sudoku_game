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


fields = {"A1" : random.randint(1,9),
        }

for number in range(1,9):
    field_value = random.randint(1,9)

    while field_value in fields.values():
        field_value = random.randint(1,9)

    fields["A" + str(number + 1)] = field_value

for number in range(1, 9):
    field_value = random.randint(1,9)
    i = 0
    d = 0
    while True:
        field_value = random.randint(1,9)
        dict_values = str(fields.values()).strip("dict_values([])")
        print(dict_values)


    fields["B" + str(number + 1)] = field_value

for n in range(1, 10):
    print(fields["A" + str(n)], end=" ")
