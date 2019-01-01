import random

# Program that generates a  9x9 sudoku

fields = {"A1" : random.randint(1,9),
        }


for number in range(1,9):
    field_value = random.randint(1,9)

    while field_value in fields.values():
        field_value = random.randint(1,9)

    fields["A" + str(number + 1)] = field_value

for n in range(1,10):
    print(fields["A" + str(n)])
