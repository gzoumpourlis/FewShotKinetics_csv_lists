import os

folders = ['train', 'val', 'test']

dict = np.load('CMN_classes.npy')
names_array = np.ndarray.tolist(dict)

for folder_name in folders:
    names_list = names_array[folder_name]

    for el in names_list:
        folder_dir = os.path.join('/home/george/Desktop/ActivityNet/Crawler/Kinetics/dataset', el)
        if not os.path.exists(folder_dir):
            os.mkdir(folder_dir)
        else:
            print('Folder {} already exists.'.format(folder_dir))
