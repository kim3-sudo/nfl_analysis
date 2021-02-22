### NFL Data Analysis
### Josh Katz & Sejin Kim
### STAT 306 S21 @ Kenyon College

### Data Cleansing
### This script: removes unneeded columns, adds in new columns with newly encoded data, removes unneeded or irrelevant observations

### Prerequisites: You have already created a CSV from the combined dataset - see nfl_analysis/src/datawrangling/combineDatasets.R and nfl_analysis_data/scripts/createcsv.R

# Import libraries
import pandas as pd
import numpy as np
from constant import *
import re
from tqdm import tqdm

# Function definitions
def getHumidity(weather):
  try:
    humidity = re.split('\d\d%', weather)
    humidity = humidity[:-1]
    humidity = int(humidity)
    return humidity
  except:
    try:
      humidity = re.split('\d%', weather)
      humidity = humidity[:-1]
      humidity = int(humidity)
      return humidity
    except:
      return ''

def getTemperature(weather):
  try:
    temperature = re.split('\d\d° F', weather)
    temperature = temperature[:-3]
    temperature = int(temperature)
    return temperature
  except:
    try:
      temperature = re.split('\d° F', weather)
      temperature = temperature[:-3]
      temperature = int(temperature)
      return temperature
    except:
      return ''

print("Importing CSV data")

### Choose the location of your dataset here - use a full (not relative) filepath for best results:
csvdata = "/home/kim3/nfl_analysis_data/nflfastr_pbp_2010_to_2020.csv"

print("Reading CSV data")
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
print("Removing unneeded columns")
data.drop(columns = dataColumnsToDrop, inplace = True)

# Create lists that will hold new data
print("Creating lists for new data")
kick_accuracy = []
altitude = []
humidity = []
temperature = []

# Process the altitude
# To get altitudes, see the stadium reference document
print("Processing altitude data")
for index,rows in tqdm(data.iterrows(), desc='Altitude Progress', total=(data.shape[0]), ascii = True):
  game_stadium = data.game_stadium.iloc[index]
  if (game_stadium == 'Edward Jones Dome'):
    altitude.append(EDWARDJAMESDOME)
  elif (game_stadium == 'Heinz Field'):
    altitude.append(HEINZFIELD)
  elif (game_stadium == 'New Meadowlands Stadium'):
    altitude.append(METLIFESTADIUM)
  elif (game_stadium == 'Gillette Stadium'):
    altitude.append(GILLETTESTADIUM)
  elif (game_stadium == 'Raymond James Stadium'):
    altitude.append(RAYMONDJAMESSTADIUM)
  elif (game_stadium == 'FedExField'):
    altitude.append(FEDEXFIELD)
  elif (game_stadium == 'EverBank Field'):
    altitude.append(TIAABANKFIELD)
  elif (game_stadium == 'Soldier Field'):
    altitude.append(SOLDIERFIELD)
  elif (game_stadium == 'Lincoln Financial Field'):
    altitude.append(LINCOLNFINANCIALFIELD)
  elif (game_stadium == 'Reliant Stadium'):
    altitude.append(NRGSTADIUM)
  elif (game_stadium == 'Ralph Wilson Stadium'):
    altitude.append(BILLSSTADIUM)
  elif (game_stadium == 'Louisiana Superdome'):
    altitude.append(MERCEDESBENZSUPERDOME)
  elif (game_stadium == 'LP Field'):
    altitude.append(NISSANSTADIUM)
  elif (game_stadium == 'Arrowhead Stadium'):
    altitude.append(ARROWHEADSTADIUM)
  elif (game_stadium == 'Qwest Field'):
    altitude.append(LUMENFIELD)
  elif (game_stadium == 'Georgia Dome'):
    altitude.append(MERCEDESBENZSTADIUM)
  elif (game_stadium == 'Paul Brown Stadium'):
    altitude.append(PAULBROWNSTADIUM)
  elif (game_stadium == 'Lambeau Field'):
    altitude.append(LAMBEAUFIELD)
  elif (game_stadium == 'Cowboys Stadium'):
    altitude.append(ATTSTADIUM)
  elif (game_stadium == 'Qualcomm Stadium'):
    altitude.append(SDCCUSTADIUM)
  elif (game_stadium == 'Cleveland Browns Stadium'):
    altitude.append(FIRSTENERGYSTADIUM)
  elif (game_stadium == 'Mall of America Field'):
    altitude.append(MALLOFAMERICAFIELD)
  elif (game_stadium == 'Lucas Oil Stadium'):
    altitude.append(LUCASOILSTADIUM)
  elif (game_stadium == 'Ford Field'):
    altitude.append(FORDFIELD)
  elif (game_stadium == 'Invesco Field at Mile High'):
    altitude.append(EMPOWERFIELD)
  elif (game_stadium == 'Oakland-Alameda County Coliseum'):
    altitude.append(RINGCENTRALCOLISEUM)
  elif (game_stadium == 'Bank of America Stadium'):
    altitude.append(BANKOFAMERICASTADIUM)
  elif (game_stadium == 'M&T Bank Stadium'):
    altitude.append(MTBANKSTADIUM)
  elif (game_stadium == 'Sun Life Stadium'):
    altitude.append(HARDROCKSTADIUM)
  elif (game_stadium == 'University of Phoenix Stadium'):
    altitude.append(STATEFARMSTADIUM)
  elif (game_stadium == 'Wembley Stadium'):
    altitude.append(WEMBLEYSTADIUM)
  elif (game_stadium == 'Rogers Centre'):
    altitude.append(ROGERSCENTRE)
  elif (game_stadium == 'TCF Bank Stadium'):
    altitude.append(TCFBANKSTADIUM)
  elif (game_stadium == 'MetLife Stadium'):
    altitude.append(METLIFESTADIUM)
  elif (game_stadium == 'Sports Authority Field at Mile High'):
    altitude.append(EMPOWERFIELD)
  elif (game_stadium == 'Mercedes-Benz Superdome'):
    altitude.append(MERCEDESBENZSUPERDOME)
  elif (game_stadium == 'CenturyLink Field'):
    altitude.append(LUMENFIELD)
  elif (game_stadium == 'O.co Coliseum'):
    altitude.append(RINGCENTRALCOLISEUM)
  elif (game_stadium == 'FirstEnergy Stadium'):
    altitude.append(FIRSTENERGYSTADIUM)
  elif (game_stadium == 'AT&T Stadium'):
    altitude.append(ATTSTADIUM)
  elif (game_stadium == 'NRG Stadium'):
    altitude.append(NRGSTADIUM)
  elif (game_stadium == 'Levi\'s Stadium'):
    altitude.append(LEVISSTADIUM)
  elif (game_stadium == 'Nissan Stadium'):
    altitude.append(NISSANSTADIUM)
  elif (game_stadium == 'U.S. Bank Stadium'):
    altitude.append(USBANKSTADIUM)
  elif (game_stadium == 'New Era Field'):
    altitude.append(BILLSSTADIUM)
  elif (game_stadium == 'Los Angeles Memorial Coliseum'):
    altitude.append(LAMEMORIALCOLISEUM)
  elif (game_stadium == 'Hard Rock Stadium'):
    altitude.append(HARDROCKSTADIUM)
  elif (game_stadium == 'Twickenham Stadium'):
    altitude.append(TWICKENHAMSTADIUM)
  elif (game_stadium == 'Azteca Stadium'):
    altitude.append(AZTECASTADIUM)
  elif (game_stadium == 'Mercedes-Benz Stadium'):
    altitude.append(MERCEDESBENZSTADIUM)
  elif (game_stadium == 'StubHub Center'):
    altitude.append(DIGNITYHEALTHSPORTSPARK)
  elif (game_stadium == 'State Farm Stadium'):
    altitude.append(STATEFARMSTADIUM)
  elif (game_stadium == 'TIAA Bank Stadium'):
    altitude.append(TIAABANKFIELD)
  elif (game_stadium == 'Ring Central Coliseum'):
    altitude.append(RINGCENTRALCOLISEUM)
  elif (game_stadium == 'Empower Field at Mile High'):
    altitude.append(EMPOWERFIELD)
  elif (game_stadium == 'Tottenham Stadium'):
    altitude.append(TOTTENHAMSTADIUM)
  elif (game_stadium == 'SoFi Stadium'):
    altitude.append(SOFISTADIUM)
  elif (game_stadium == 'Allegiant Stadium'):
    altitude.append(ALLEGIANTSTADIUM)
  elif (game_stadium == 'Lumen Field'):
    altitude.append(LUMENFIELD)
  else:
    altitude.append('')

# Process weather data
print("Processing weather data")
print("Processing humidity data")
for index,rows in tqdm(data.iterrows(), desc='Humidity Progress', total=data.shape[0], ascii = True):
  humidity.append(getHumidity(data.weather.iloc[index]))
print("Processing temperature data")
for index,rows in tqdm(data.iterrows(), desc='Temperature Progress', total=data.shape[0], ascii = True):
  temperature.append(getTemperature(data.weather.iloc[index]))
  
# Process kick accuracy data
print("Processing kick accuracy data")
for index, rows in tqdm(data.iterrows(), desc='Kick Accuracy Progress', total=data.shape[0], ascii = True):
  accuracy = 
  kick_accuracy.append()
  
# Append data
print("Appending altitude data")
data['altitude'] = altitude
print("Appending humidity data")
data['humidity'] = humidity
print("Appending temperature data")
data['temperature'] = temperature
print("Appending kick accuracy data")
data['kick_accuracy'] = kick_accuracy

# Drop irrelevant observations
print("Removing irrelevant observations")
removalList = []
originalLen = data.shape[0]
for index,rows in tqdm(data.iterrows(), desc='Row Processing', total = data.shape[0], ascii = True):
  play_type = data.play_type.iloc[index]
  if (play_type == 'pass'):
    continue
  elif (play_type == 'field_goal'):
    continue
  elif (play_type == 'punt'):
    continue
  elif (play_type == 'kickoff'):
    continue
  elif (play_type == 'extra_point'):
    continue
  else:
    removalList.append(index)
print('Removing', len(removalList), 'out of', originalLen,'rows')
data.drop(data.index[removalList], axis = 0, inplace = True)
print('Done.')



# Write data out
print("Writing file out to .")
data.to_csv(path_or_buf = './nflfastr_2010_2020_kicks_passes.csv')
