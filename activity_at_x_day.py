# Assumed imports 
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so

# local imports
import lexicon

# Constants
END_DAY = 26

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
daily_data['data'] = pd.to_datetime(daily_data['date'], format='%Y-%m-%d')
# Filtering according the 
daily_data = daily_data.loc[(daily_data['data'].dt.day <= END_DAY)]
start = min(daily_data['date'])
end = max(daily_data['date'])

# Setting up the main area for the plots.
figure, axes = plt.subplots(3, 1, figsize=(16,10))
plt.suptitle(f'Activity on furryli.st from the 1st to the {END_DAY}th of each month.\n', weight='bold')

# Adding the legends
axes[0].set_title("How many times the like button was hit:\n", fontsize=12)
axes[1].set_title("Skeets posted for each day:\n", fontsize=12)
axes[2].set_title("New furries tracked by furryli.st:\n", fontsize=12)

# Like button presse
sns.barplot(daily_data,
    x="day", y="daily_likes", hue="month",
        errorbar=("sd", 0), ax=axes[0]
).set_yscale("log")

# Like button presse
sns.barplot(daily_data,
    x="day", y="daily_posts", hue="month",
        errorbar=("sd", 0), ax=axes[1]
).set_yscale("log")

# Like button presse
sns.barplot(daily_data,
    x="day", y="daily_furries", hue="month",
        errorbar=("sd", 0), ax=axes[2]
).set_yscale("log")

# Fixing legends
# --------------

axes[0].set(xlabel="day of the week", ylabel="Likes (log10)")
axes[1].set(xlabel="day of the week", ylabel="Skeets (log10)")
axes[2].set(xlabel="day of the week", ylabel="New Furries Added (log10)")
axes[0].legend(loc='upper left')
axes[1].legend(loc='upper left')
axes[2].legend(loc='upper left')

# Rendering
# --------------
figure.tight_layout(pad=1)
figure.savefig(lexicon.files.activity_at_x_day)

# Only showing if called from main.
if __name__ == "__main__":
    plt.show()