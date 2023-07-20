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

# Setting up the main area for the plots.
figure, axes = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(12,5))
plt.suptitle(f'Actvity on furryli.st from {start} to {end}', weight='bold')
figure.supxlabel("Months")
figure.supylabel("Weekday")



sns.set_theme(style="darkgrid")
g = sns.jointplot(x="total_bill", y="tip", data=daily_data,
                  kind="reg", truncate=False,
                  xlim=(0, 60), ylim=(0, 12),
                  color="m", height=7)

# Rendering
# --------------

figure.tight_layout(pad=1.0)
figure.savefig(lexicon.files.heatmaps_plots)


# Only showing if called from main.
if __name__ == "__main__":
    plt.show()
