#!/usr/bin/env python3
# loads data from the water samples excel file

import pickle

import pandas

xl = pandas.ExcelFile("data/1_raw/WSMasterSampleLog.xlsx")

df = xl.parse(
    sheet_name="All Depths",
    index_col=0  # "Rank" column
)

df.to_csv("data/2a_csv/water-samples.csv")

with open('data/2b_pickles/water-samples-df.pickle', 'wb') as f:
    pickle.dump(df, f)
