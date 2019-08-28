import os

cmd_train = 'python download.py data/kinetics-100_train.csv ./dataset'
cmd_val = 'python download.py data/kinetics-100_val.csv ./dataset'
cmd_test = 'python download.py data/kinetics-100_test.csv ./dataset'

os.system(cmd_train)
os.system(cmd_val)
os.system(cmd_test)
