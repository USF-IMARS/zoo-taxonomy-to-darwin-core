#!/usr/bin/env python3
# loads data from the water samples excel file

import pickle

import pandas

xl = pandas.ExcelFile("data/1_raw/zooplankton_consolidated.xlsx")

df = xl.parse(
    sheet_name="Sheet1",
    skiprows=9
)

# TODO: split each `mesh_size = 200 / 500` row into two rows

# TODO: add these:
# Area of the net(m^2)	Net diameter (mm)
# 0.20	0.5

df.to_csv("data/2a_csv/sample-details.csv")

with open('data/2b_pickles/sample-details-df.pickle', 'wb') as f:
    pickle.dump(df, f)

print(df)
