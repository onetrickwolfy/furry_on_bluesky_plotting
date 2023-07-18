# Assumed imports 
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so

# local imports
import lexicon

# Setting default heme
sns.set_theme(style="darkgrid")

# Creating multiple spots for plots
figure, axes = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(12,5))
plt.suptitle('Actvity on furryli.st since 2023-05-13', weight='bold')
figure.supxlabel("Months")
figure.supylabel("Weekday")
# Loading daily dataset and sorting it by day.
daily_data = pd.read_csv(lexicon.files.processed_daily) 
ordered_daily = daily_data.sort_values(by=["elapsed_day"], ascending=True)

# Creating daily user heat map
daily_users = pd.pivot_table(
    daily_data,
    index='weekday',
    columns='month',
    values='daily_furries',
    aggfunc='sum'
)

sns.heatmap(
    daily_users, annot=True, fmt="d", linewidths=1,
    square=True, cbar=1,  cmap='Blues',ax=axes[0],
    center=True,
    annot_kws={'size': 'x-small', 'alpha': 0.95}
)
axes[0].set(xlabel="", ylabel="")
axes[0].set_title("New furries added to the feed")

# Creating daily posts heat map
weekly_posts = pd.pivot_table(
    daily_data,
    index='weekday',
    columns='month',
    values='daily_posts',
    aggfunc='sum'
)
sns.heatmap(
    weekly_posts, annot=True, fmt="d", linewidths=1,
    square=True, cbar=1,  cmap='Blues',ax=axes[1],
    center=True,
    annot_kws={'size': 'x-small', 'alpha': 0.95}
)
axes[1].set(xlabel="", ylabel="")
axes[1].set_title("Skeets posted")

# Creating daily likes heat map
weekly_likes = pd.pivot_table(
    daily_data,
    index='weekday',
    columns='month',
    values='daily_likes',
    aggfunc='sum',
)
sns.heatmap(
    weekly_likes, annot=True, fmt="d", linewidths=1,
    square=True, cbar=1,  cmap='Blues',ax=axes[2],
    center=True,
    annot_kws={'size': 'x-small', 'alpha': 0.95}
)
axes[2].set(xlabel="", ylabel="")
axes[2].set_title("Total likes")

figure.tight_layout(pad=1.0)
plt.show()