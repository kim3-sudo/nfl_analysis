### NFL Data Analysis
### Josh Katz & Sejin Kim
### STAT 306 S21 @ Kenyon College

### Data Cleansing
### This script: removes unneeded columns, adds in new columns with newly encoded data, removes unneeded or irrelevant observations

### Prerequisites: You have already created a CSV from the combined dataset - see nfl_analysis/src/datawrangling/combineDatasets.R and nfl_analysis_data/scripts/createcsv.R

import pandas as pd
import numpy as np

### Choose the location of your dataset here - use a full (not relative) filepath for best results:
csvdata = "/users/kim3/nfl_analysis_data/nflfastRdata.csv"

data = pd.read_csv(csvdata)

# Prepare to clean all but needed columns
dataColumnsToDrop = data.columns.values.tolist()
dataColumnsToDrop.remove('game_id')
dataColumnsToDrop.remove('game_stadium')
dataColumnsToDrop.remove('weather')
dataColumnsToDrop.remove('play_type')
dataColumnsToDrop.remove('kick_distance')
dataColumnsToDrop.remove('air_yards')
dataColumnsToDrop.remove('cp')
dataColumnsToDrop.remove('cpoe')

# Drop all other columns
data.drop(dataColumnsToDrop, axis = 1)
