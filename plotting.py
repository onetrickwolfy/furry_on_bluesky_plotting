# Assumed imports 
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so

# local imports
import lexicon

# Set-up
# --------------

# Setting theme.
sns.set_theme(style="darkgrid")

# Preparing data aqnd extracting infos about them
daily_data = pd.read_csv(lexicon.files.processed_daily) 
start = min(daily_data['date'])
end = max(daily_data['date'])
daily_data = daily_data.drop(
    columns=["date", "total_bsky_users", "furry_ratio", ]
)

# Setting up the main area for the plots.
figure, axes = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(12,5))
plt.suptitle(f'Actvity on furryli.st from {start} to {end}', weight='bold')
figure.supxlabel("Months")
figure.supylabel("Weekday")

# Plotting
# --------------

# User joining
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

# Skeets recorded.
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

# Like button pressed
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

# Rendering
# --------------

figure.tight_layout(pad=1.0)
figure.savefig(lexicon.files.heatmaps_plots)
plt.show()