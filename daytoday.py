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
        'axes.edgecolor': 'black', 'patch.edgecolor': 'r'
    }
)

# Preparing data
daily_data = pd.read_csv(lexicon.files.processed_daily) 
start = min(daily_data['date'])
end = max(daily_data['date'])

# Setting up the main area for the plots.
figure, axes = plt.subplots(3, 3, figsize=(4*3,3*3))
plt.suptitle(f'Activity on furryli.st from {start} to {end}', weight='bold', fontsize=16)
figure.supxlabel("Elapsed Days", fontsize=16)

# Adding the legends
axes[0, 0].set_title("Prediction\n", fontsize=14)
axes[0, 1].set_title("Day to day activity\n", fontsize=14)
axes[0, 2].set_title("Cumulated\n", fontsize=14)


# Plotting regressions (first row)
# --------------

sns.regplot(data=daily_data, x="elapsed_day", y="daily_posts", 
            ax = axes[0, 0], lowess=True, 
            scatter_kws={'s': 5, 'alpha': 0.7}, 
            label="Predicted New Skeets"
).legend()

sns.regplot(data=daily_data, x="elapsed_day", y="daily_likes", 
            ax = axes[1, 0], lowess=True, 
            scatter_kws={'s': 5, 'alpha': 0.7},
            label="Predicted New Likes"
).legend()

sns.regplot(data=daily_data, x="elapsed_day", y="daily_furries",
            ax = axes[2, 0], lowess=True,
            scatter_kws={'s': 5, 'alpha': 0.7},
            label="Predicted New Users"
).legend()

# Every day variation
# --------------

sns.lineplot(data=daily_data, x="elapsed_day", y="daily_posts", 
             ax = axes[0, 1], label="New Skeets"
)

sns.lineplot(data=daily_data, x="elapsed_day", y="daily_likes",
            ax = axes[1, 1], label="New Likes"
)

sns.lineplot(data=daily_data, x="elapsed_day", y="daily_furries",
            ax = axes[2, 1], label="New Users"
)

# Cummulated
# --------------

sns.lineplot(data=daily_data, x="elapsed_day", y="total_posts", 
             ax = axes[0, 2] , label="Total Skeets"
)

sns.lineplot(data=daily_data, x="elapsed_day", y="total_likes",
            ax = axes[1, 2], label="Total Likes"
)

sns.lineplot(data=daily_data, x="elapsed_day", y="total_furries",
            ax = axes[2, 2], label="Total Users"
)

# Removing labels
# --------------

axes[2, 0].set(xlabel="", ylabel="Users")
axes[2, 1].set(xlabel="", ylabel="")
axes[2, 2].set(xlabel="", ylabel="")

axes[1, 0].set(xlabel="", ylabel="Likes")
axes[1, 1].set(xlabel="", ylabel="")
axes[1, 2].set(xlabel="", ylabel="")

axes[0, 0].set(xlabel="", ylabel="Posts")
axes[0, 1].set(xlabel="", ylabel="")
axes[0, 2].set(xlabel="", ylabel="")


# Rendering
# --------------

figure.tight_layout(pad=1.5)
figure.savefig(lexicon.files.daytoday)

# Only showing if called from main.
if __name__ == "__main__":
    plt.show()
