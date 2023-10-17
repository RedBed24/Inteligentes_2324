import h5py
import math

def get_datasets_hdf5_file(hdf5_file_name):
    datasets_names=[]
    with h5py.File(hdf5_file_name,"r") as hdf5_file:
        _get_group_structure(hdf5_file,datasets_names)
        _order_datasets(hdf5_file,datasets_names)
    return datasets_names

def _order_datasets(hdf5_file, datasets_names):
    ordered_datasets = [datasets_names[0]]
    for i in range(1, len(datasets_names)):
        dataset_attrs=get_dataset_attrs(hdf5_file, datasets_names[i])
        for j in range(0, len(ordered_datasets)):
            ordered_dataset_attrs=get_dataset_attrs(hdf5_file, ordered_datasets[j])

            end=False
            if (dataset_attrs['ysup'] > ordered_dataset_attrs['ysup'] and not end):
                ordered_datasets.insert(j,datasets_names[i])
                end=True   
            elif (dataset_attrs['ysup'] == ordered_dataset_attrs['ysup'] and not end):
                if (dataset_attrs['xinf'] < ordered_dataset_attrs['xinf']):
                   ordered_datasets.insert(j,datasets_names[i]) 
                   end=True
            else:
                ordered_datasets.append(datasets_names[i])

    datasets_names[:]=ordered_datasets       

def _get_group_structure(group,datasets_names):
    # Recorre los subgrupos en el grupo actual de forma recursiva
    for item_name in group.keys():
        item = group[item_name] 
        if isinstance(item, h5py.Group): # Si el item es un grupo, se buscan datasets dentro de el recursivamente
            _get_group_structure(item,datasets_names)
        elif isinstance(item,h5py.Dataset): # Si el item es un dataset, se almacena su "ruta"
            datasets_names.append(f"{group.name}{'' if group.name == '/' else '/'}{item_name}")

def get_dataset_attrs(hdf5_file_name, dataset_path):
    dataset_attrs = {}  
    # Devuelve un diccionario con los atributos de un dataset en particular
    with h5py.File(hdf5_file_name, "r") as hdf5_file:
        dataset_attrs_names = hdf5_file[dataset_path].attrs.keys()
        for attr_name in dataset_attrs_names:
            dataset_attrs[attr_name] = hdf5_file[dataset_path].attrs[attr_name]
    return dataset_attrs

def get_dataset_data(hdf5_file_name,dataset_path):
     
     with h5py.File(hdf5_file_name, "r") as hdf5_file:
        dataset = hdf5_file[dataset_path]
        return dataset[()]

def check_umt_coordinate_in_dataset(hdf5_file_name,dataset_path,y,x):
    dataset_attrs=get_dataset_attrs(hdf5_file_name,dataset_path)

    if dataset_attrs['yinf']<y and y<dataset_attrs['ysup'] and dataset_attrs['xinf']<x and dataset_attrs['xsup']:
        dataset_data=get_dataset_data(hdf5_file_name,dataset_path)
        xsol=math.floor((x-dataset_attrs['xinf'])/dataset_attrs['cellsize'])
        ysol=math.floor((y-dataset_attrs['yinf'])/dataset_attrs['cellsize'])
        return dataset_data[ysol,xsol]
    
    return dataset_attrs['nodata_value']


'''def clone_hdf5(src_file_name,dest_file_name):
    src_file=h5py.File(src_file_name,"r")
    dest_file=h5py.File(dest_file_name,"w")
    _clone_group(src_file,dest_file)
    src_file.close()
    dest_file.close()

 
def _clone_group(src_group,dest_group):
    for name, item in src_group.items():
        if isinstance(item, h5py.Group):
            new_group = dest_group.create_group(name)
            _clone_group(item, new_group)
        elif isinstance(item, h5py.Dataset):
            dest_group.create_dataset(name, data=item[()])
'''

def modify_dataset_attr(hdf5_file_name,dataset_path,attr_name,new_value):
    with h5py.File(hdf5_file_name, "r+") as hdf5_file:
        hdf5_file[dataset_path].attrs[attr_name]=new_value

'''def modify_dataset_data(hdf5_file_name,dataset_path,new_data):
    with h5py.File(hdf5_file_name,"r+") as hdf5_file:
        dataset=hdf5_file[dataset_path]
        dataset[...]=new_data'''

