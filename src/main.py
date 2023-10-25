import mapa
import hdf5_data_handler as hdf5

def main():
    DATAFOLDER = "data/"
    
    map = mapa.Mapa(DATAFOLDER + "LaGomera.hdf5")


if __name__ == "__main__":
    main()

