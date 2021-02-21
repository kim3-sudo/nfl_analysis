### NFL Data Analysis
### Josh Katz & Sejin Kim
### STAT 306 S21 @ Kenyon College

### Data Cleansing
### This script: removes unneeded columns, adds in new columns with newly encoded data, removes unneeded or irrelevant observations

### Prerequisites: You have already created a CSV from the combined dataset - see nfl_analysis/src/datawrangling/combineDatasets.R and nfl_analysis_data/scripts/createcsv.R

# Import libraries
import pandas as pd
import numpy as np
import constant
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

### Choose the location of your dataset here - use a full (not relative) filepath for best results:
csvdata = "/home/kim3/nfl_analysis_data/nflfastr_pbp_2010_to_2020.csv"

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

# Create lists that will hold new data
kick_accuracy = []
pass_accuracy = []
altitude = []
humidity = []
temperature = []

# Process the altitude
# To get altitudes, see the stadium reference document
print("Processing altitude data")
for index,rows in tqdm(data.iterrows(), desc='Altitude Progress', total=(data.shape[0], ascii = True)):
  if (data.game_stadium.iloc[index] == 'Edward Jones Dome'):
    altitude.append(EDWARDJAMESDOME)
  elif (data.game_stadium.iloc[index] == 'Heinz Field'):
    altitude.append(HEINZFIELD)
  elif (data.game_stadium.iloc[index] == 'New Meadowlands Stadium'):
    altitude.append(METLIFESTADIUM)
  elif (data.game_stadium.iloc[index] == 'Gillette Stadium'):
    altitude.append(GILLETTESTADIUM)
  elif (data.game_stadium.iloc[index] == 'Raymond James Stadium'):
    altitude.append(RAYMONDJAMESSTADIUM)
  elif (data.game_stadium.iloc[index] == 'FedExField'):
    altitude.append(FEDEXFIELD)
  elif (data.game_stadium.iloc[index] == 'EverBank Field'):
    altitude.append(TIAABANKFIELD)
  elif (data.game_stadium.iloc[index] == 'Soldier Field'):
    altitude.append(SOLDIERFIELD)
  elif (data.game_stadium.iloc[index] == 'Lincoln Financial Field'):
    altitude.append(LINCOLNFINANCIALFIELD)
  elif (data.game_stadium.iloc[index] == 'Reliant Stadium'):
    altitude.append(NRGSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Ralph Wilson Stadium'):
    altitude.append(BILLSSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Louisiana Superdome'):
    altitude.append(MERCEDESBENZSUPERDOME)
  elif (data.game_stadium.iloc[index] == 'LP Field'):
    altitude.append(NISSANSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Arrowhead Stadium'):
    altitude.append(ARROWHEADSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Qwest Field'):
    altitude.append(LUMENFIELD)
  elif (data.game_stadium.iloc[index] == 'Georgia Dome'):
    altitude.append(MERCEDESBENZSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Paul Brown Stadium'):
    altitude.append(PAULBROWNSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Lambeau Field'):
    altitude.append(LAMBEAUFIELD)
  elif (data.game_stadium.iloc[index] == 'Cowboys Stadium'):
    altitude.append(ATTSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Qualcomm Stadium'):
    altitude.append(SDCCUSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Cleveland Browns Stadium'):
    altitude.append(FIRSTENERGYSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Mall of America Field'):
    altitude.append(MALLOFAMERICAFIELD)
  elif (data.game_stadium.iloc[index] == 'Lucas Oil Stadium'):
    altitude.append(LUCASOILSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Ford Field'):
    altitude.append(FORDFIELD)
  elif (data.game_stadium.iloc[index] == 'Invesco Field at Mile High'):
    altitude.append(EMPOWERFIELD)
  elif (data.game_stadium.iloc[index] == 'Oakland-Alameda County Coliseum'):
    altitude.append(RINGCENTRALCOLISEUM)
  elif (data.game_stadium.iloc[index] == 'Bank of America Stadium'):
    altitude.append(BANKOFAMERICASTADIUM)
  elif (data.game_stadium.iloc[index] == 'M&T Bank Stadium'):
    altitude.append(MTBANKSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Sun Life Stadium'):
    altitude.append(HARDROCKSTADIUM)
  elif (data.game_stadium.iloc[index] == 'University of Phoenix Stadium'):
    altitude.append(STATEFARMSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Wembley Stadium'):
    altitude.append(WEMBLEYSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Rogers Centre'):
    altitude.append(ROGERSCENTRE)
  elif (data.game_stadium.iloc[index] == 'TCF Bank Stadium'):
    altitude.append(TCFBANKSTADIUM)
  elif (data.game_stadium.iloc[index] == 'MetLife Stadium'):
    altitude.append(METLIFESTADIUM)
  elif (data.game_stadium.iloc[index] == 'Sports Authority Field at Mile High'):
    altitude.append(EMPOWERFIELD)
  elif (data.game_stadium.iloc[index] == 'Mercedes-Benz Superdome'):
    altitude.append(MERCEDESBENZSUPERDOME)
  elif (data.game_stadium.iloc[index] == 'CenturyLink Field'):
    altitude.append(LUMENFIELD)
  elif (data.game_stadium.iloc[index] == 'O.co Coliseum'):
    altitude.append(RINGCENTRALCOLISEUM)
  elif (data.game_stadium.iloc[index] == 'FirstEnergy Stadium'):
    altitude.append(FIRSTENERGYSTADIUM)
  elif (data.game_stadium.iloc[index] == 'AT&T Stadium'):
    altitude.append(ATTSTADIUM)
  elif (data.game_stadium.iloc[index] == 'NRG Stadium'):
    altitude.append(NRGSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Levi\'s Stadium'):
    altitude.append(LEVISSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Nissan Stadium'):
    altitude.append(NISSANSTADIUM)
  elif (data.game_stadium.iloc[index] == 'U.S. Bank Stadium'):
    altitude.append(USBANKSTADIUM)
  elif (data.game_stadium.iloc[index] == 'New Era Field'):
    altitude.append(BILLSSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Los Angeles Memorial Coliseum'):
    altitude.append(LAMEMORIALCOLISEUM)
  elif (data.game_stadium.iloc[index] == 'Hard Rock Stadium'):
    altitude.append(HARDROCKSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Twickenham Stadium'):
    altitude.append(TWICKENHAMSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Azteca Stadium'):
    altitude.append(AZTECASTADIUM)
  elif (data.game_stadium.iloc[index] == 'Mercedes-Benz Stadium'):
    altitude.append(MERCEDESBENZSTADIUM)
  elif (data.game_stadium.iloc[index] == 'StubHub Center'):
    altitude.append(DIGNITYHEALTHSPORTSPARK)
  elif (data.game_stadium.iloc[index] == 'State Farm Stadium'):
    altitude.append(STATEFARMSTADIUM)
  elif (data.game_stadium.iloc[index] == 'TIAA Bank Stadium'):
    altitude.append(TIAABANKSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Ring Central Coliseum'):
    altitude.append(RINGCENTRALCOLISEUM)
  elif (data.game_stadium.iloc[index] == 'Empower Field at Mile High'):
    altitude.append(EMPOWERFIELD)
  elif (data.game_stadium.iloc[index] == 'Tottenham Stadium'):
    altitude.append(TOTTENHAMSTADIUM)
  elif (data.game_stadium.iloc[index] == 'SoFi Stadium'):
    altitude.append(SOFISTADIUM)
  elif (data.game_stadium.iloc[index] == 'Allegiant Stadium'):
    altitude.append(ALLEGIANTSTADIUM)
  elif (data.game_stadium.iloc[index] == 'Lumen Field'):
    altitude.append(LUMENFIELD)
  else:
    altitude.append('')


print("Processing weather data")
for index,rows in tqdm(data.iterrows(), desc='Humidity Progress', total=(data.shape[0], ascii = True)):
  humidity.append(getHumidity(data.weather.iloc[index])
for index,rows in tqdm(data.iterrows(), desc='Temperature Progress', total=(data.shape[0], ascii = True)):
  humidity.append(getTemperature(data.weather.iloc[index])

