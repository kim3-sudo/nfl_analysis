# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:15:36 2021

@author: kim3
"""

"""
game_id: str, comes from game_id
home_team: str, "ATL", comes from home_team
away_team: str, "PHI", comes from away_team
runplays: int, calculated by number of rushes per game from play_type_nfl within one game
simpleResult: int, calculated by whether result is + or -; if result is +, then home wins, if result is -, then away wins, encoded with loss as 0, win as 1, and tie as 2
"""

import pandas as pd
import warnings
from psutil import virtual_memory
from datetime import datetime
from tqdm import tqdm

print("Checking system compatibility")
compatibleSystem = virtual_memory()
if (compatibleSystem.total < 8589934592):
    raise Exception ("Cannot start - not enough RAM")
else:
    continueConfirm = input("This script REQUIRES at least 8GB of RAM to run and suggests at least 16GB of RAM. Failure to check system compatiblity may result in data loss! To continue, press 1 and Enter, otherwise, press 0 and Enter.")
    if (continueConfirm == '1'):
        # read the old CSV into oldDf
        print('Reading data in')
        oldDf = pd.read_csv("./testdata.csv")
        
        print('Make editable version of data')
        # make an internally editable version of the dataframe
        editDf = pd.DataFrame.copy(oldDf, deep=True)
        
        print('Making output dataframe')
        # create new columns and fit them into a new dataframe
        newColumns = ["game_id", "home_team", "away_team", "run_plays", "simple_result"]
        newDf = pd.DataFrame(columns = newColumns)
        
        # Initialize empty game ID list
        game_id_list = []
        home_team_list = []
        away_team_list = []
        run_tally_list = []
        result_list = []
        # Fill all of the unique games into the newDf dataframe
        for index, row in tqdm(editDf.iterrows(), desc='Progress', total=(editDf.shape[0] + 1), ascii = True):
            new_game_id = editDf.game_id.iloc[index]
            new_home_team = editDf.home_team.iloc[index]
            new_away_team = editDf.away_team.iloc[index]
            result_int = editDf.result.iloc[index]
            list_iterator = 0
            print('Reset temporary run play tally')
            
            
            # Test whether new game ID is the same as the old game ID, if so then the game is the same
            if new_game_id != editDf.game_id.iloc[index - 1]:
                
                print('New game: ', new_game_id)
                print('Adding to dataframe')
                game_id_list.append(new_game_id)
                home_team_list.append(new_home_team)
                away_team_list.append(new_away_team)
                
                if (result_int == 0):
                    print('Game was TIE')
                    result_list.append(2)
                elif (result_int > 0):
                    print('Game was LOSS')
                    result_list.append(1)
                elif (result_int < 0):
                    print('Game was WIN')
                    result_list.append(0)
                else:
                    issue = 'Undefined game outcome: ' + result_int
                    warnings.warn(issue)
                    result_list.append(-1)
                list_iterator += 1
            else:
                print('Same game: ', new_game_id)
                print('Skipping add new entry to dataframe') 
            
        
        print('Adding game_id to output dataframe')
        # Add the computed lists to the dataframe 
        newDf['game_id'] = game_id_list
        print('Adding home_team to output dataframe')
        newDf['home_team'] = home_team_list
        print('Adding away_team to output dataframe')
        newDf['away_team'] = away_team_list
        print('Adding result_list to output dataframe')
        newDf['simple_result'] = result_list
        
        for index, row in tqdm(newDf.iterrows(), desc='Progress', total=(newDf.shape[0] + 1), ascii = True):
            current_game_id = newDf.game_id.iloc[index]
            tempDf = (editDf.game_id == current_game_id) & (editDf.play_type == 'run')
            run_tally_list.append(tempDf.sum())
            
        print('Adding run tally to output dataframe')
        newDf['run_plays'] = run_tally_list

        print('Generating output file')
        now = datetime.now()
        datetime_string = now.strftime("%Y%m%d_%H%M%S")
        outfile = datetime_string + "_NFLDATA.csv"
        pd.DataFrame.to_csv(newDf, path_or_buf="./" + outfile)
        
        print('All done!')
        print("""
        ##### ENCODING LIST #####
        game_id: str, comes from game_id
        home_team: str, e.g. "ATL", comes from home_team
        away_team: str, e.g. "PHI", comes from away_team
        run_plays: int, calculated by number of rushes per game from play_type_nfl within one game
        simple_Result: int, calculated by whether result is + or -; if result is +, then home wins, if result is -, then away wins, encoded with loss as 0, win as 1, and tie as 2
              """
              )
    else:
        raise Exception ("User terminated - not enough RAM")

