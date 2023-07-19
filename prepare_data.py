import csv
from os import mkdir, path
from datetime import datetime
import lexicon


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so

# Set-up 
# Creating the directory structure ahead of time.
# TODO: Prepare data with NUMPY.
# --------------------------

if not path.exists(lexicon.folders.processed_folder):
    mkdir(lexicon.folders.processed_folder)
        
# Extracting raw datas
# --------------------------

# Loading the dataset
interactions = pd.read_csv(lexicon.files.interactions)
new_furries = pd.read_csv(lexicon.files.interactions)
users = pd.read_csv(lexicon.files.interactions)


# Preparing data
# --------------------------

# Merging according to date
daily_data = pd.merge(
    pd.merge(
        interactions,new_furries, left_on='date', right_on='date', suffixes=("", "_drop"), how='inner',
    ),
    users, on='date', how='left', suffixes=("", "_drop"),
)

# Removing duplicate
daily_data.drop(
    [col for col in daily_data.columns if 'drop' in col], axis=1, inplace=True
)

# Parsing date s
daily_data['elapsed_day'] = daily_data.reset_index().index
daily_data['date'] = pd.to_datetime(daily_data['date'])
daily_data['weekday'] = daily_data['date'].dt.day_name()
daily_data['month'] = daily_data['date'].dt.month_name()
daily_data['day'] = daily_data['date'].dt.day



# Exporiting data
# --------------------------

daily_data.to_csv(
    lexicon.files.processed_daily,
    index=False
)
