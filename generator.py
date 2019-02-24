from random import randint

rows = {  "A" : [7,8,9,1,2,3,4,5,6],
            "B":[], "C": [], "D": [], "E": [], "F": [], "G": [], "H": [], "I": [],
        }

second_row = 65 # Esto puede cambiar ya que no tiene mucho sentido que sean estas letras en específico
third_row = 66
for n in range(2,10,3): # Crear varias listas, llenar las listas segun 3 casos de datos posibles
    second_row += 2 # c,e,g
    third_row += 2 # d,f,h
    if rows["A"][n] == 9:
        rows[chr(second_row)] = [x for x in range(1,4)]
        rows[chr(third_row)] = [x for x in range(4,7)]
    if rows["A"][n] == 3:
        rows[chr(second_row)] = [x for x in range(rows["A"][n] + 1, rows["A"][n] + 4)]
        rows[chr(third_row)] = [x for x in range(rows["A"][n] + 4, rows["A"][n] + 7)]
    if rows["A"][n] == 6:
        rows[chr(second_row)] = [x for x in range(rows["A"][n] + 1, rows["A"][n] + 4)]
        rows[chr(third_row)] = [x for x in range(1,4)]


# Juntando todos los valores de las 3 filas "c,e,g" en una sola
for n in range(0,3):
    rows["B"].append(rows["C"][n])

for n in range(0,3):
    rows["B"].append(rows["E"][n])

for n in range(0,3):
    rows["B"].append(rows["G"][n])

rows["C"] = [] # Vacío la lista porque la lista C toma valores por los numeros usados en la variable "second row"

# Juntando todos los valores de las 3 filas "d,f,h" en una sola
for n in range(0,3):
    rows["C"].append(rows["D"][n])

for n in range(0,3):
    rows["C"].append(rows["F"][n])

for n in range(0,3):
    rows["C"].append(rows["H"][n])

rows["D"] = []  # Vacío la lista porque están ya poseen valores que no son necesarios actualmente
rows["E"] = []
rows["F"] = []
rows["G"] = []
rows["H"] = []
rows["I"] = []

for letter in range(67,71,3): # Esto define los dos valores de las letras a utilizar (D y G)
    for x in range(3):
        letter += 1
        for n in range(2,10,3):                 # Para que realice el procedimiento con los 3 cuadros
            if x != 2:
                rows[chr(letter)].append(rows[chr(letter-3)][n])
                rows[chr(letter)].append(rows[chr(letter-2)][n-2])
                if rows[chr(letter)][-1] != 9:                              # Para las tercera fila de cada cuadro, si el numero anterior a lo de la linea de codigo de abajo es 9, entonces colocar 1
                    rows[chr(letter)].append(rows[chr(letter)][-1] + 1)
                else:
                    rows[chr(letter)].append(1)
            else:
                if n == 2 or n == 5 or n == 8:
                    if rows[chr(letter-1)][n] == 9: # Si el ultimo numero de la anterior fila es 9, entonces añade uno como siguiente valor
                        rows[chr(letter)].append(1)
                    else:
                        rows[chr(letter)].append(rows[chr(letter-1)][n] + 1) # Si el ultimo numero de la fila anterior no es 9, entonces añade el mismo valor + 1

                if rows[chr(letter)][n-2] != 9: # Esto es para el caso de que valga 9 el numero anterior
                    rows[chr(letter)].append(rows[chr(letter)][n-2] + 1) # Añadir valor siguiente al anterior en la fila
                else:
                    rows[chr(letter)].append(1)
                if rows[chr(letter)][n-1] != 9: # Esto es para el caso de que valga 9 el numero anterior
                    rows[chr(letter)].append(rows[chr(letter)][n-1] + 1) # Añadir valor siguiente al anterior en la fila
                else:
                    rows[chr(letter)].append(1)

for n in range(10): # Cambia 5 pares de numeros de posición (podría cambiar varias veces el mismo par de números)
    random_number_1 = randint(1,9)
    random_number_2 = randint(1,9)
    for letter in range(65,74): # Cambiar las posiciones de dos numeros para hacer más difícil el sudoku
        a, b = rows[chr(letter)].index(random_number_1), rows[chr(letter)].index(random_number_2)
        rows[chr(letter)][b], rows[chr(letter)][a] = rows[chr(letter)][a], rows[chr(letter)][b]

for letter in range(65,74): # Print all letters (rows)
    print(rows[chr(letter)])
