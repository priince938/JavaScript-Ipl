# To import the fuction read_csv from toralruns
from collections import defaultdict
from totalruns import create_json, read_csv


def create_dictonary_batsman_rcb(readed_csv, dictonary_batsman_rcb):
    ''' It create dictonary with keys
     (Player name of rcb ) with values (sum of all runs)'''
    for row in readed_csv:
        if row['batting_team'] == 'Royal Challengers Bangalore':
            dictonary_batsman_rcb[row['batsman']] += int(row['batsman_runs'])
    return dictonary_batsman_rcb


def top_ten_player(top_ten_player, team_dictonary):
    ''' This fuction will sort the top ten player of rcb '''
    list_top_ten_player = list(team_dictonary.values())
    list_top_ten_player = sorted(list_top_ten_player)
    list_top_ten_player = list_top_ten_player[len(list_top_ten_player)-10:]
    for player_name in team_dictonary.keys():
        if team_dictonary[player_name] in list_top_ten_player:
            top_ten_player[player_name] = team_dictonary[player_name]
    return top_ten_player


if __name__ == '__main__':
    ''' To only execute only when involved directy '''
    x_axis_label = 'R.C.B Top Ten Player'
    y_axis_label = 'Total Runs in All Ininig'
    readed_csv = read_csv()
    dictonary_batsman_rcb = defaultdict(lambda: 0)
    top_ten_player_dictonary = {}
    dictonary_batsman_rcb = create_dictonary_batsman_rcb(readed_csv,
                                                         dictonary_batsman_rcb
                                                         )
    top_ten_player_dictonary = top_ten_player(top_ten_player_dictonary,
                                              dictonary_batsman_rcb
                                              )
    # It create a json file using create_json
    create_json(top_ten_player_dictonary, "./json/batmanrcb.json")
