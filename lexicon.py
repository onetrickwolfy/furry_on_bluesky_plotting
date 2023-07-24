"""
    Access to files and folders using the . operator!
    
    I never used this before but 
    it was a sexy alternative to boring ass constants.

    Maybe it's a huge mistake! who knows. 
"""

# "global" imports
# --------------------------
from os import path
from types import SimpleNamespace

# Relative -> Absolute path converstions
# TODO: move the constant if ever required elswere.
# --------------------------

# Hardcoding the rootfolder for consistency
_ROOT: str = path.realpath(r"/home/gabey/furrylist_plot")

# os.path.realpath will remove unnecessary slashes. 
def _absolute_path(relative_path: str) -> str:
    """Take an relative path and make it into an absolute path
    
    Generally I only want to worry about where is the file COMPARED
    to the root folder. Absolute path are very useful for multithreading.
    
    Assumption:
        the ROOT constant is defined
    Args:
        relative_path (str): relative path to a file or folder
    Returns:
        str: an absolute path forged from the relative path.
    """
    
    global _ROOT
    return path.realpath(
        f"{_ROOT}/{relative_path}"
    )

# Building the lexicon
# Basically dictionnaries but using the . operator
# --------------------------

folders = SimpleNamespace(
    processed_folder = _absolute_path("data/processed"),
    raw_folder = _absolute_path("data/raw"),
    plots_folder = _absolute_path("dataplots")
)

files = SimpleNamespace(
    interactions = _absolute_path("data/raw/interactions.csv"),
    new_furries = _absolute_path("data/raw/new_furries.csv"),
    users = _absolute_path("data/raw/users.csv"),
    processed_daily = _absolute_path("data/processed/processed_daily.csv"),
    heatmaps_plots = _absolute_path("data/plots/heatmaps.png"),
    daytoday = _absolute_path("data/plots/daytoday.png")
)
