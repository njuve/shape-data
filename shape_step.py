import pandas as pd
"""
Description : we get a (long-format) dataframe and return a (wide-format) dataframe
              with monthly step data or step data from start day.
"""

def get_step_from_startday(df):
    """
    一度pivot tableで月ごとの平均にした後、meltして、ない月は消して、番号振って、もう一回pivot
    絶対改善の余地がある
    """
    df_pivot = df.pivot_table(index = 'ID', columns = 'sokutei_m', values = 'step')
    df_pivot = df_pivot.reset_index()
    df_melt = df_pivot.melt(id_vars = 'ID', var_name = 'sokutei_m', value_name='step')
    df_melt = df_melt.dropna(subset = ['step'])
    df_melt['No'] = df_melt.groupby('ID').cumcount()+1
    df_pivot2 = df_melt.pivot_table(index = 'ID', columns = 'No', values = 'step')
    return df_pivot2

def get_monthly_step(df):
    df_pivot = df.pivot_table(index = 'ID', columns = 'sokutei_m', values = 'step')

    return df_pivot
