import csv
from os import mkdir, path
from datetime import datetime
import lexicon

# Set-up 
# Creating the directory structure ahead of time.
# --------------------------

if not path.exists(lexicon.folders.processed_folder):
    mkdir(lexicon.folders.processed_folder)
        
# Extracting the raw data
# --------------------------

processed_daily_interactions: list[dict] = []

with open(lexicon.files.raw_daily) as f:
    
    total_furries: int = 0
    for day_passed, row in enumerate(csv.DictReader(f, delimiter=',', quotechar='"')):
        # I can do it late but it's useful to precompute it
        # Numpy can read CSV which can be given to plotting libs.
        date: str = row['date']
        dt: datetime = datetime.fromisoformat(date)
        weekday: str = dt.strftime('%A')
        month: str = dt.strftime('%B')
        day: str = dt.strftime('%d')
        elapsed_day: int = day_passed + 1
        
        # i like consistency lol
        daily_likes: int = int(row['daily_likes'])
        daily_posts: int  = int(row['daily_posts'])
        daily_furries: int = int(row['daily_furries'])
        total_bsky_users: int = int(row['total_bsky_users'])
        
        # Pre-computing the (furries / global_users) ratio
        total_furries += daily_furries 
        furry_ratio: float = round((total_furries/total_bsky_users * 100), 4)

        # I decided to dump everything in the same csv for now. 
        processed_daily_interactions.append(
            {
                "date": date,
                "weekday": weekday,
                "month": month,
                "day": day,
                "daily_likes": daily_likes,
                "daily_posts": daily_posts,
                "daily_furries": daily_furries,
                "elapsed_day":  elapsed_day,
                "total_furries": total_furries,
                "total_bsky_users": total_bsky_users,
                "furry_ratio": furry_ratio
            }
        )


# Exporting the processed data as csv
# --------------------------

# processed_daily_interactions[0].keys() is hacky and unexplicit.
# This also allows re-ordering as dict do not maintain it.
headers_daily = [
    "date", "weekday", "month", "day", "daily_likes", "daily_posts",
    "daily_furries", "elapsed_day", "total_furries",
    "total_bsky_users", "furry_ratio"
]

# removing newline='' add line-break which are icky. thanks :p
with open(lexicon.files.processed_daily, "w", newline='', encoding='utf-8') as f:
    # DictWriter needs the header to map the data from the dict.
    writer = csv.DictWriter(f, fieldnames=headers_daily)
    # Using writeheader to append the header to the file.
    writer.writeheader()
    # Writing all the raws mapping values from the keys.
    writer.writerows(processed_daily_interactions)