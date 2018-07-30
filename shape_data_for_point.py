import pandas as pd
import numpy as np
import function_baseline
import shape_step
import adding_information
"""
Input: a (long-format) csv file
Output: a excel file composed of two sheet:
        1st sheet - monthly step data
        2nd sheet - left justified step data
"""


"""
入力データ指定
"""
# データ読み込み
df = pd.read_csv('kitaibaraki_step.csv', encoding='SHIFT-JIS')

"""
dataframeの分割
"""
# 年齢と65歳フラグ追加
df = adding_information.flag_65(df)
# 基本情報df
df_info = df[['ID', 'birth', 'dantai','tiki','age','65flag']]
df_info = df_info.set_index('ID')
df_info = df_info.drop_duplicates()

# baseline計算用df
df_base = df.pivot_table(index = 'ID', columns = 'sokutei_date', values = 'step')

"""
歩数計算とピボットテーブル,結合
"""
# 開始月歩数のdf
df_step_from_startday = shape_step.get_step_from_startday(df)
# 月ごと歩数のdf
df_monthly_step = shape_step.get_monthly_step(df)

# baseline計算(as Series)
baseline = function_baseline.get_baseline(df_base)
df_baseline = baseline.to_frame()
df_baseline.columns = ['baseline']
df_with_baseline = df_baseline.join(df_step_from_startday)

df_monthly_with_info = df_info.join(df_monthly_step)
df_with_baseline_with_info = df_info.join(df_with_baseline)


"""
書き出し
"""
with pd.ExcelWriter('kitaibaraki_for_analysis.xlsx') as writer:
    df_monthly_with_info.to_excel(writer, sheet_name = '2018年n月歩数')
    df_with_baseline_with_info.to_excel(writer, sheet_name = 'nヶ月目歩数')
