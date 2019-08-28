### Parsing the dataset of "Compound Memory Networks for Few-shot Video Classification"

The data splits of the dataset (let's call it "Kinetics-100" for convenience) that was introduced by the publication "Compound Memory Networks for Few-shot Video Classification - ECCV 2018", in text format, as given by the authors in their github repo, can be found in `data_splits` folder. (source : https://github.com/ffmpbgrnn/CMN )
These data splits are re-written in .csv format (the same format with that of the data splits of the full Kinetics-400 dataset), in `data_splits_100` folder, by executing `parse_classes.py`.

The data splits of the Kinetics-400 dataset, can be found in .csv format, in `data_splits_400` folder. ( source : https://github.com/activitynet/ActivityNet/tree/master/Crawler/Kinetics/data )

To download the dataset splits of Kinetics-100, you'll need the Kinetics crawler, and the splits in .csv format (as mentioned above, you can find the splits in the `data_splits_100` folder) :
1. Clone the Kinetics dataset crawler:
``
git clone https://github.com/activitynet/ActivityNet/tree/master/Crawler/Kinetics
``

2. Copy the .csv files from the `data_splits_100` folder, to the `data` folder of the crawler's repo

3. Copy the `download_Kinetics_100.py` file to the root directory of the crawler's repo, i.e. in the same directory with the crawler's `download.py` file

4. Create the folder where the  Kinetics-100 will be downloaded and stored.
``
mkdir dataset
``

5. Run the script to download the train/val/test splits of Kinetics-100
``
python download_Kinetics_100.py
``
