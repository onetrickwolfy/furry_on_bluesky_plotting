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
# --------------------------

if not path.exists(lexicon.folders.processed_folder):
    mkdir(lexicon.folders.processed_folder)
        
# Extracting raw datas
# --------------------------

# Loading the dataset
interactions = pd.read_csv(lexicon.files.interactions)
new_furries = pd.read_csv(lexicon.files.new_furries)
users = pd.read_csv(lexicon.files.users)


# Preparing data
# --------------------------

# Merging according to date
daily_data = pd.merge(
    pd.merge(
        interactions,new_furries, left_on='date', right_on='date', suffixes=("", "_drop"), how='left',
    ),
    users, on='date', how='left', suffixes=("", "_drop"),
)

# 0 furries were added these day
daily_data['furries_added'] = daily_data['furries_added'].fillna(0)

# Cumulative sum of the total amount of furries
daily_data['total_furries'] = daily_data['furries_added'].cumsum()


# Cumulative sum of the total amount of furries
daily_data['new_bsk_users'] = daily_data['total_bsky_users'].diff()
daily_data['total_bsky_users'][0] = 0

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
