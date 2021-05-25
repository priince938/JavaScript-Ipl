import csv
from collections import defaultdict
from totalruns import create_json


def read_csv():
    ''' It read the given csv file from the given location'''
    f = open('./umpire.csv')
    readed_csv = csv.DictReader(f)
    return readed_csv


def creta_umpire_dictonary(umpire_count_dictonary):
    ''' It create dictonary with keys
     (contry name) with values (sum of all umpire number) '''
    for row in readed_csv:
        if row['Nationality'] == 'India':
            continue
        else:
            umpire_count_dictonary[row['Nationality']] += 1
    return umpire_count_dictonary


if __name__ == "__main__":
    ''' To only execute only when involved directy'''
    x_axis_label = "Umpire Name"
    y_axis_label = "Number of Umpire each Country"
    readed_csv = read_csv()
    umpire_count_dictonary = defaultdict(lambda: 0)
    umpire_count_dictonary = creta_umpire_dictonary(umpire_count_dictonary)
    # It create json file take two argument list and location
    create_json(umpire_count_dictonary, "./json/umpire.json")
