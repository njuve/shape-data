import numpy as np
import pandas as pd
"""
Input : (wide-format)dataframe
Output : a series of baseline steps
Description ： we get a dataframe and compute baseline steps.
"""

def produce_baseline(df):
    """
    Description : this script compute baseline steps as Series.

     i:ID指定(行)
     j:日付指定(列)

     初めて1000歩を超えた日から7日間の平均歩数を求める
    """
    result = [] #baseline歩数用

    for i in range(len(df)): #IDの数だけ回す
        steps = [] #7日間の歩数用
        j = 1 #1列目指定
        if(len(df.iloc[i,1:]) < 7 or np.max(df.iloc[i,1:]) < 1000): #歩数データ数7未満または最大歩数1000未満のIDのbaselineを0にする
            steps = 0
        else:
            while df.iat[i,j] < 1000: #1000歩を超えた列の位置を取得
                j += 1

            while len(steps) < 7: #7日分数えるまで回す
                if j == len(df.columns):
                    break
                if df.iat[i,j] >= 300: #300歩以上の歩数を取得
                    steps.append(df.iat[i,j])
                j += 1

        result.append(np.mean(steps))

    return result

def get_baseline(df):
    """
    Description : Using produce_baseline, this produce series of baseline steps.
    """
    baseline = produce_baseline(df)
    baseline_series = pd.Series(baseline, index = df.index)

    return baseline_series
