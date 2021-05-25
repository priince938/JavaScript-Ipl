# To import required files
import csv
import json
from collections import defaultdict


def read_csv():
    ''' It read the given csv file from the given location'''
    f = open('./matches.csv')
    readed_csv = csv.DictReader(f)
    return readed_csv


def create_season_match_dictonary(season_match_dictornary,
                                  readed_csv, team_name_set):
    ''' It itrate to list which is given by readed_csv '''
    for row in readed_csv:
        if row['season'] in season_match_dictornary.keys():
            team_name_set.add(row['team1'])
            team_name_set.add(row['team2'])
            season_match_dictornary[row['season']][row['team1']] += 1
            season_match_dictornary[row['season']][row['team2']] += 1
        else:
            season_match_dictornary[row['season']] = defaultdict(lambda: 0)
    return season_match_dictornary


def game_played_byteam(season_match_dictonary,
                       game_played_dict, team_name_set):
    ''' It create a dictonary of each teams
    is played in particular season or not
    if not it append zero on data '''
    for team_name in team_name_set:
        # create a dictonary with list as value
        game_played_dict[team_name] = []
    for season in season_match_dictornary:
        for team_name in game_played_dict.keys():
            if team_name in season_match_dictornary[season].keys():
                game_played_dict[team_name].append(
                    season_match_dictornary[season][team_name])
            else:
                game_played_dict[team_name].append(0)
    return game_played_dict


def create_json(game_played_dict, season_match_dictonary):
    ''' It create json file with nested list for stacked bar graph'''
    season_list = list(season_match_dictonary.keys())
    json_list = [season_list, []]
    for team_name in game_played_dict:
        json_dict = {}
        json_dict['name'] = team_name
        json_dict['data'] = game_played_dict[team_name]
        json_list[1].append(json_dict)
    j = open('./json/season.json', 'w')
    json.dump(json_list, j, indent=1)


if __name__ == '__main__':
    x_axis_label = 'Umpire Name'
    y_axis_label = 'Number of Umpire each Country'
    readed_csv = read_csv()
    season_match_dictornary = {}
    team_name_set = set()

    season_match_dictornary = create_season_match_dictonary(
        season_match_dictornary, readed_csv,
        team_name_set)
    game_played_dict = {}
    game_played_dict = game_played_byteam(
        season_match_dictornary, game_played_dict, team_name_set)
    create_json(game_played_dict, season_match_dictornary)
