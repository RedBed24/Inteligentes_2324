from os import listdir
from os.path import isfile

# Importar una clase de otro archivo
from asciigrid import AsciiGrid

def main():
    DATAFOLDER = "data/"

    filenames = []
    for f in listdir(DATAFOLDER):
        if isfile(f"{DATAFOLDER}/{f}"):
            filenames.append(f"{DATAFOLDER}/{f}")

    ascii_grids = []
    for file in filenames:
        grid = AsciiGrid(file)
        grid.read()
        ascii_grids.append(grid)

    # TODO: juntar todos los grids en un mapa
    

if __name__ == "__main__":
    main()

