"""

This module provides parsers for period tracker data. The functions take a data source as input, and return a
Pandas dataframe with a common structure.

Output table columns:
* cycle n.
* length of period in days
* # days with heavy period
* # days with heavy period
* # days with light period
* # days with cramps

"""

import datetime
import json
import pandas as pd

headers = ['Day', 'Heavy', 'Medium', 'Light', 'Cramps']


def parse_clue_data(data):

    period_data = []

    period_lookup = {'heavy': [1, 0, 0],
                     'medium': [0, 1, 0],
                     'light': [0, 0, 1]}

    for day_data in data['data']:

        if 'period' in day_data.keys() and day_data['period'] != "spotting":

            data_list = list()
            data_list.append(day_data['day'])

            for i in period_lookup[day_data['period']]:
                data_list.append(i)

            cramps = 1 if 'cramps' in day_data['pain'] else 0

            data_list.append(cramps)

            if len(data_list) != 5:
                raise Exception('wrong length of list')

            period_data.append(data_list)

    df = pd.DataFrame(period_data, columns=headers)

    df = df.sort_values(by=['Day']).reset_index(drop=True)

    df['Day'] = pd.to_datetime(df['Day'])

    counter = 0

    df.loc[0, 'Period'] = counter

    for record_index in list(range(1, len(df))):
        if df.loc[record_index]['Day'] - df.loc[record_index-1]['Day'] > datetime.timedelta(days=1):
            counter += 1

        df.loc[record_index, 'Period'] = counter

    return df.groupby('Period').agg({'Day': 'count',
                                     'Heavy': 'sum',
                                     'Medium': 'sum',
                                     'Light': 'sum',
                                     'Cramps': 'sum'})


if __name__ == '__main__':

    filename_clue = "fixture.cluedata"

    import pdb; pdb.set_trace()
    with open(filename_clue) as f:
        data_clue = json.load(f)

    print(parse_clue_data(data_clue))
