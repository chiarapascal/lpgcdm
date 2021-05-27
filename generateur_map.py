from random import random

CHR_FILL = "o"
CHR_EMPTY = "."
MAP_DENSITY = 0.3 # pour modifier le ratio pleins/vides
SHOULD_PRINT_IN_FILE = False

def gen_map(x: int, y: int, density: float) -> list[str]:
    map = []
    for i in range(y):
        s = CHR_FILL if random() < density else CHR_EMPTY
        for j in range(x - 1):
            # Notez le if... else: ... en notation raccourcie
            c = CHR_FILL if random() < density else CHR_EMPTY
            s += " " + c
        map.append(s)
    return "\n".join(map) + "\n"

if __name__ == "__main__":
    while True:
        try:
            width = int(input("Entrez la largeur de la map : "))
            height = int(input("Entrez la hauteur de la map : "))
        except ValueError:
            print("Valeurs entières plz")
        else:
            map = gen_map(width, height, MAP_DENSITY)
            break
    if SHOULD_PRINT_IN_FILE:
        while True:
            name = input("Nom de fichier ? ")
            try:
                fo = open(f"{name}.map", "x")
            except FileExistsError:
                print(f"{name}.map existe déjà, veuillez saisir un autre nom")
            else:
                fo.write(map)
                fo.close()
                break
    print(map)
    print("Done")
