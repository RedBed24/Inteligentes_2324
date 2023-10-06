import h5py
from asciigrid import AsciiGrid

def create_HDF5(nombre_archivo, file_list):

    with h5py.File(nombre_archivo,"w") as hdf5_file_writer:
        group_names=_get_group_names(file_list)

        for group,file in zip(group_names,file_list):
            # Obtener el mapa de cada fichero
            asciigrid=AsciiGrid(file)
            file_map=asciigrid.get_map()
            _create_group(hdf5_file_writer,group,file_map)

def _get_group_names(file_list)-> list:
    group_names=[]
    # TODO: Obtener el nombre de los cada grupo a través de los archivos .asc
    return group_names

def _create_group(hdf5_file,group_name,file):
    g=hdf5_file.create_group(group_name)
    g.create_dataset("Dataset",data=file)
    # TODO: Añadir los atributos de cada dataset


def get_dataset_properties(ruta_dataset):
    properties=[]
    # TODO: dado la ruta del dataset, leer sus atributos
    return properties

def get_dataset(nombre_archivo,nombre_grupo):
    hdf5_file_reader=h5py.File(nombre_archivo,'r')
    dataset=hdf5_file_reader[f'{nombre_grupo}/Dataset']
    return dataset