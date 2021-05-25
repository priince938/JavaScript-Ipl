import csv
import json
from collections import defaultdict


def read_csv():
    ''' It read the given csv file from the given location'''
    f = open('./deliveries.csv')
    readed_csv = csv.DictReader(f)
    return readed_csv


def create_dictonary_with_teamname_runs(team_runs_dictonary, readed_csv):
    ''' It create dictonary with keys (team name)
    with values (sum of all runs) '''
    for row in readed_csv:
        team_runs_dictonary[row['batting_team']] += int(row['total_runs'])

    return team_runs_dictonary


def create_abbreviation_name(team_name):
    ''' This fuction create a abbrevation for a given name
     It is Good see team name in abbervation over full name in graph '''
    abbrevation_name = ''
    split_list_team_name = team_name.split(' ')
    for split_name in split_list_team_name:
        abbrevation_name += split_name[0]
    return abbrevation_name


def create_abbrevation_dictonary(team_runs_abbrevation_dictonary,
                                 team_runs_dictonary):
    ''' It generate abbrevation dictonay
     with the help create_abbrevation_name fuction '''
    for team_name_key in team_runs_dictonary.keys():
        # create a new dictonary with abbrevated name
        team_name = team_name_key
        team_run = team_runs_dictonary[team_name_key]
        abbrevated_name = create_abbreviation_name(team_name)
        team_runs_abbrevation_dictonary[abbrevated_name] = team_run
    return team_runs_abbrevation_dictonary


def create_json(teams_dictonary, json_name):
    ''' It create a json array from python dictionary '''
    json_list = []
    for team_name in teams_dictonary:
        temp_list = [team_name, teams_dictonary[team_name]]
        json_list.append(temp_list)
    j = open(json_name, 'w')
    json.dump(json_list, j)


if __name__ == "__main__":
    ''' Only execute when the open is main file '''
    x_axis_label = "Team Names in Abbrivation"
    y_axis_label = "Total Runs in All Ininig"
    readed_csv = read_csv()
    team_runs_dictonary = defaultdict(lambda: 0)
    team_runs_dictonary = create_dictonary_with_teamname_runs(
        team_runs_dictonary, readed_csv
    )
    # To create Abbrevation_dictonary
    team_runs_abbrevation_dictonary = {}
    team_runs_abbrevation_dictonary = create_abbrevation_dictonary(
        team_runs_abbrevation_dictonary, team_runs_dictonary
    )
    # It create json file take two argument list and location
    create_json(team_runs_abbrevation_dictonary, "./json/totalruns.json")
