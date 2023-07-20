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

sns.set_theme(style="darkgrid")
sns.lineplot(data=daily_data, y="furries_added", x="elapsed_day", label="new Furries")
sns.lineplot(data=daily_data, y="new_bsk_users", x="elapsed_day", label="New Bluesky Users")
# sns.lineplot(data=daily_data, y="daily_likes", x="elapsed_day", label="Posts Liked")
# sns.lineplot(data=daily_data, y="furries_added", x="elapsed_day", label="Furries Added")

plt.legend()

# likes_according_to_posts.set_axis_labels("Daily Posts", "Daily Likes")

# Rendering
# --------------

# Only showing if called from main.
if __name__ == "__main__":
    plt.show()
