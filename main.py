### Functions

def matches_played(ipl, team):
    count = 0
    for i in range(ipl.shape[0]):
        if ipl['team1'].iloc[i] == team or ipl['team2'].iloc[i] == team:
            count += 1
    return count
    
def most_played_venue(ipl, team):
    venues = []
    for i in range(ipl.shape[0]):
        if ipl['team1'].iloc[i] == team or ipl['team2'].iloc[i] == team:
            venues.append(ipl['venue'].iloc[i])
    return statistics.mode(venues)
    
def no_toss_win_and_loose(ipl, team):
    win, lose = 0, 0
    for i in range(ipl.shape[0]):
        if ipl['team1'].iloc[i] == team or ipl['team2'].iloc[i] == team:
            if ipl['toss_winner'].iloc[i] == team or ipl['toss_winner'].iloc[i] == team:
                win += 1
            else:
                lose += 1
    return (win, lose) 
          
def most_player_of_match(ipl, team):
    players = []
    for i in range(ipl.shape[0]):
        if ipl['team1'].iloc[i] == team or ipl['team2'].iloc[i] == team:
            players.append(ipl['player_of_match'].iloc[i])
    return statistics.mode(players)
    
# UI function  
def ui_code(team, query):
    if query in 'Number of matches played':
        op = matches_played(ipl, team)
        return op
    
    elif query in 'Most Played Venue':
        op = most_played_venue(ipl, team)
        return op
    
    elif query in 'Number of Toss win and loose':
        win, lose = no_toss_win_and_loose(ipl, team)
        return win, lose    
            
    elif query in 'Player with most player_of_match award':
        op = most_player_of_match(ipl, team)    
        return op
          
        
### Libraries

import json
import statistics
import pandas as pd
import gradio as gr
from time import time
          
          
### Main code

start_time = time()

# Read files
ipl = pd.read_csv('IPL Matches 2008-2020.csv')
config = pd.read_json('config.json')

# ipl file team names
ipl_teams = []
for i in range(ipl.shape[0]):
    ipl_teams.append(ipl['team1'].iloc[i])
ipl_teams = list(set(ipl_teams))

# Problem statements
problem_statements = ["Number of matches played", "Most Played Venue", "Number of Toss win and loose", 
                      "Player with most player_of_match award"]


# UI Code
iface = gr.Interface(
                     fn=ui_code, 
                     inputs=[
                         gr.inputs.Dropdown(ipl_teams),
                         gr.inputs.Dropdown(problem_statements)
                     ], 
                     outputs="text"
                    )

iface.launch()