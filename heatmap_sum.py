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
sns.set_theme(style="whitegrid", palette="flare", font_scale=0.8)
sns.set_style(
    "whitegrid" ,{
        "grid.linestyle": ":", 'color': 'r', 
        'axes.edgecolor': 'black'
    }
)

# Preparing data
daily_data = pd.read_csv(lexicon.files.processed_daily) 
start = min(daily_data['date'])
end = max(daily_data['date'])

# Setting up the main area for the plots.
figure, axes = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(12,5))
plt.suptitle(f'Activity on furryli.st from {start} to {end}', weight='bold')
figure.supxlabel("Months")
figure.supylabel("Weekday")

# Adding the legends
axes[0].set_title("Furries joining the feed\n", fontsize=12)
axes[1].set_title("Skeets posted\n", fontsize=12)
axes[2].set_title("Like button smashed\n", fontsize=12)

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
    square=True, cbar=1,  cmap=sns.light_palette("xkcd:dull yellow", 16),
    ax=axes[0],
    center=True, robust=True,
    annot_kws={'size': 'x-small', 'alpha': 1, 'color': "black"}
)

axes[0].set(xlabel="", ylabel="")

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
    square=True, cbar=1,  cmap=sns.light_palette("xkcd:dull yellow", 16),
    ax=axes[1],
    center=True, robust=True,
    annot_kws={'size': 'x-small', 'alpha': 1, 'color': "black"}
)

axes[1].set(xlabel="", ylabel="")

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
    square=True, cbar=1,  cmap=sns.light_palette("xkcd:dull yellow", 16),
    ax=axes[2],
    center=True, robust=True,
    annot_kws={'size': 'x-small', 'alpha': 1, 'color': "black"}
)

axes[2].set(xlabel="", ylabel="")

# Rendering
# --------------

figure.tight_layout(pad=1.0)
figure.savefig(lexicon.files.heatmaps_plots)

# Only showing if called from main.
if __name__ == "__main__":
    plt.show()
