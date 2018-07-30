import pandas as pd
"""
this script receive a dataframe and add infomations about age to the dataframe.
Then return the dataframe.
"""


def getage(birth):
    date = int(pd.to_datetime('2018/4/1').strftime('%Y%m%d'))
    birth = int(pd.to_datetime(birth).strftime('%Y%m%d'))
    return int((date - birth)/10000)

def flag_65(df):
    df['age'] = df['birth'].apply(lambda date: getage(date))
    df['65flag'] = df['age'].apply(lambda age: 1 if age >= 65 else 0)
    return df
