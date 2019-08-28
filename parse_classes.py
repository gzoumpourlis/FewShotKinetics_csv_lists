import numpy as np
import glob
import os
import pandas as pd

save_csv = True

######################################################
# Kinetics-100 splits, used in CMN paper

train_list_100_path = 'data_splits/train.list'
val_list_100_path = 'data_splits/val.list'
test_list_100_path = 'data_splits/test.list'

######################################################
# Kinetics-100 splits, to be written

if not os.path.exists('data_splits_100'):
    os.mkdir('data_splits_100')
train_list_100_csv_path = 'data_splits_100/kinetics-100_train.csv'
val_list_100_csv_path = 'data_splits_100/kinetics-100_val.csv'
test_list_100_csv_path = 'data_splits_100/kinetics-100_test.csv'

######################################################
# Kinetics-400 splits, used in original Kinetics paper

train_list_400_csv_path = 'data_splits_400/kinetics-400_train.csv'
val_list_400_csv_path = 'data_splits_400/kinetics-400_val.csv'
test_list_400_csv_path = 'data_splits_400/kinetics-400_test.csv'

######################################################
# Read Kinetics-400 CSV files

df_train_400 = pd.read_csv(train_list_400_csv_path)
df_val_400 = pd.read_csv(val_list_400_csv_path)
df_test_400 = pd.read_csv(test_list_400_csv_path)

# columns : ['label', 'youtube_id', 'time_start', 'time_end', 'split', 'is_cc']
column_names = df_train_400.columns.values.tolist()

video_class_column_name = column_names[0]
video_id_column_name = column_names[1]
video_start_column_name = column_names[2]
video_end_column_name = column_names[3]
video_split_column_name = column_names[4]
video_cc_column_name = column_names[5]

video_ids_train = list(df_train_400[video_id_column_name].values)
video_ids_val = list(df_val_400[video_id_column_name].values)
video_ids_test = list(df_test_400[video_id_column_name].values)

vid_classes = {'train' : list(df_train_400[video_class_column_name].values),
               'val' : list(df_val_400[video_class_column_name].values)}
vid_ids = {'train' : list(df_train_400[video_id_column_name].values),
               'val' : list(df_val_400[video_id_column_name].values)}
vid_starts = {'train' : list(df_train_400[video_start_column_name].values),
               'val' : list(df_val_400[video_start_column_name].values)}
vid_ends = {'train' : list(df_train_400[video_end_column_name].values),
               'val' : list(df_val_400[video_end_column_name].values)}
vid_splits = {'train' : list(df_train_400[video_split_column_name].values),
               'val' : list(df_val_400[video_split_column_name].values)}
vid_ccs = {'train' : list(df_train_400[video_cc_column_name].values),
               'val' : list(df_val_400[video_cc_column_name].values)}

######################################################
# Read CMN train split

video_classes = list(df_train_400[video_class_column_name].values)
video_ids = list(df_train_400[video_id_column_name].values)
video_starts = list(df_train_400[video_start_column_name].values)
video_ends = list(df_train_400[video_end_column_name].values)
video_splits = list(df_train_400[video_split_column_name].values)
video_ccs = list(df_train_400[video_cc_column_name].values)

print('###############################')
print('Parsing train set')
print(' ')

classes_train = []
cnt = 0
cnt_error = 0
file = open(train_list_100_path, 'r')
for line in file:
    rest_info = line.split('/')[1]
    id = rest_info[:11]
    line = line.split('/')[0]
    if line not in classes_train:
        classes_train.append(line)
    ##############################
    if id in video_ids:
        index = video_ids.index(id)
        row_class = video_classes[index]
        row_id = video_ids[index]
        row_start = video_starts[index]
        row_end = video_ends[index]
        row_split = video_splits[index]
        row_cc = video_ccs[index]
    elif id in video_ids_val:
        index = video_ids_val.index(id)
        cnt_error += 1
        row_class = vid_classes['val'][index]
        row_id = vid_ids['val'][index]
        row_start = vid_starts['val'][index]
        row_end = vid_ends['val'][index]
        row_split = vid_splits['val'][index]
        row_cc = vid_ccs['val'][index]
    else:
        cnt_error += 1
        print('Train set error {:07d} : video_id {} could not be found'.format(cnt_error, id))
        quit()

    video_data_list = [[row_class, row_id, row_start, row_end, row_split, row_cc]]
    if cnt==0:
        df_train_100 = pd.DataFrame(video_data_list, columns=column_names)
    else:
        df_train_100 = df_train_100.append(video_data_list, ignore_index=True)
    ##############################
    cnt += 1
print('Found %03d train classes' % len(classes_train))
if save_csv==True:
    df_train_100.to_csv(train_list_100_csv_path, index=False)

######################################################
# Read CMN val split

video_classes = list(df_val_400[video_class_column_name].values)
video_ids = list(df_val_400[video_id_column_name].values)
video_starts = list(df_val_400[video_start_column_name].values)
video_ends = list(df_val_400[video_end_column_name].values)
video_splits = list(df_val_400[video_split_column_name].values)
video_ccs = list(df_val_400[video_cc_column_name].values)

print(' ')
print('###############################')
print('Parsing val set')
print(' ')

classes_val = []
cnt = 0
cnt_error = 0
file = open(val_list_100_path, 'r')
for line in file:
    rest_info = line.split('/')[1]
    id = rest_info[:11]
    line = line.split('/')[0]
    if line not in classes_val:
        classes_val.append(line)
    ##############################
    if id in video_ids:
        index = video_ids.index(id)
        row_class = video_classes[index]
        row_id = video_ids[index]
        row_start = video_starts[index]
        row_end = video_ends[index]
        row_split = video_splits[index]
        row_cc = video_ccs[index]
    elif id in video_ids_train:
        index = video_ids_train.index(id)
        cnt_error += 1
        row_class = vid_classes['train'][index]
        row_id = vid_ids['train'][index]
        row_start = vid_starts['train'][index]
        row_end = vid_ends['train'][index]
        row_split = vid_splits['train'][index]
        row_cc = vid_ccs['train'][index]
    else:
        cnt_error += 1
        print('Val set error {:07d} : video_id {} could not be found'.format(cnt_error, id))
        quit()

    video_data_list = [[row_class, row_id, row_start, row_end, row_split, row_cc]]
    if cnt == 0:
        df_val_100 = pd.DataFrame(video_data_list, columns=column_names)
    else:
        df_val_100 = df_val_100.append(video_data_list, ignore_index=True)
    ##############################
    cnt += 1
print('Found %03d val classes' % len(classes_val))
if save_csv==True:
    df_val_100.to_csv(val_list_100_csv_path, index=False)

######################################################
# Read CMN test split

video_ids = list(df_test_400[video_id_column_name].values)
video_starts = list(df_test_400[video_start_column_name].values)
video_ends = list(df_test_400[video_end_column_name].values)
video_splits = list(df_test_400[video_split_column_name].values)

print(' ')
print('###############################')
print('Parsing test set')
print(' ')

classes_test = []
cnt = 0
cnt_error = 0
file = open(test_list_100_path, 'r')
for line in file:
    rest_info = line.split('/')[1]
    id = rest_info[:11]
    line = line.split('/')[0]
    if line not in classes_test:
        classes_test.append(line)
    ##############################
    if id in video_ids:
        index = video_ids.index(id)
        row_class = line
        row_id = video_ids[index]
        row_start = video_starts[index]
        row_end = video_ends[index]
        row_split = video_splits[index]
        row_cc = 1
    elif id in video_ids_train:
        index = video_ids_train.index(id)
        cnt_error += 1
        row_class = vid_classes['train'][index]
        row_id = vid_ids['train'][index]
        row_start = vid_starts['train'][index]
        row_end = vid_ends['train'][index]
        row_split = vid_splits['train'][index]
        row_cc = vid_ccs['train'][index]
    elif id in video_ids_val:
        index = video_ids_val.index(id)
        cnt_error += 1
        row_class = vid_classes['val'][index]
        row_id = vid_ids['val'][index]
        row_start = vid_starts['val'][index]
        row_end = vid_ends['val'][index]
        row_split = vid_splits['val'][index]
        row_cc = vid_ccs['val'][index]
    else:
        cnt_error += 1
        print('Test set error {:07d} : video_id {} could not be found'.format(cnt_error, id))
        quit()

    video_data_list = [[row_class, row_id, row_start, row_end, row_split, row_cc]]
    if cnt == 0:
        df_test_100 = pd.DataFrame(video_data_list, columns=column_names)
    else:
        df_test_100 = df_test_100.append(video_data_list, ignore_index=True)
    ##############################
    cnt += 1
print('Found %03d test classes' % len(classes_test))
if save_csv==True:
    df_test_100.to_csv(test_list_100_csv_path, index=False)

######################################
# Write dictionary of 100 kept classes

print('-------- Train --------')
print(classes_train)

print('-------- Val --------')
print(classes_val)

print('-------- Test --------')
print(classes_test)

class_dict = {'train' : classes_train,
              'val' : classes_val,
              'test' : classes_test}
np.save('CMN_classes.npy', class_dict)
