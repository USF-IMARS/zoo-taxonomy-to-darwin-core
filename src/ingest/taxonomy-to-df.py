#!/usr/bin/env python3
"""
Loads data from the "compiled" excel file into a single "long" pandas dataframe.
This script deals with some weirdness in the "raw" data by skipping sheets,
figuring out what row to start on, etc.
The final dataframe is saved as a `.pickle` file.
Based on load-test.py
"""

from datetime import datetime
import math
import pickle

from matplotlib import pyplot
import pandas

xl = pandas.ExcelFile("data/1_raw/compiled_zoo_taxonomy_Jaimie_31JAN2018.xlsx")

samples = pandas.DataFrame()
for sheet_name in xl.sheet_names:
    station = sheet_name[:2]
    cruise_id = sheet_name[2:]
    EXCLUDED_SHEETS = [
        "Samples for see", "PLANTILLA", "Sheet1"
    ]
    STATIONS = ["MR", "LK", "WS"]
    print("=== {}".format(sheet_name))
    if sheet_name not in EXCLUDED_SHEETS:
        if station not in STATIONS:
            raise ValueError("unknown station name for sheet '{}'".format(sheet_name))
        df = xl.parse(
            sheet_name=sheet_name,
            header=None,
            skiprows=1
            # 1st row is either empty or looks like:
            #   Western Sambo	3/14/2016	Only conting copepods
            # we just skip it for consistency's sake
        )

        # === sub-samples:
        start_row = 6  # species headers on this row
        # load samples as dataframe:
        subsample = pandas.DataFrame(
            data=df.iloc[(start_row+1):, 0:7],
            # columns=df.iloc[start_row],
            # copy=True
        )
        # columns from
        # subsample.columns = df.iloc[start_row]
        # actually look like:
        # Clasification | Nº Ind. Aliquot | NaN | Total Ind. Sample | NaN | N° Ind.\ m³ | Sub total G.
        # but we rename these slightly:
        # print(subsample)
        COL_NAMES = [
            "classification", "n_ind_aliquot", "NaN", "tot_ind_sample", "NaN", "n_ind_per_m3", "sub_tot_g"
        ]
        subsample.columns = COL_NAMES

        # === datetime
        try:
            sample_datetime = datetime.strptime(df.iloc[0,0], "Date:  %m/%d/%Y")
        except:
            sample_datetime = datetime.strptime(df.iloc[0,0], "FECHA:  %m/%d/%Y")

        # === lat / lon
        # TODO: get lat/lon from station name (b/c not in most sheets

        subsample = subsample.assign(
            counted_aliquot=df.iloc[5,5],
            volume_sample_water=df.iloc[5,3],
            volume_filtered=df.iloc[5,0],
            datetime=sample_datetime,
            mesh_size=df.iloc[2,5].replace("mesh size:", "").strip(),
            folson=df.iloc[5,1],
            split_size=df.iloc[5,2],
            station=station,
            cruise_id=cruise_id
            # === drag_type
            # TODO:
            # sample["drag_type"] # this looks like:
            # Type of trawl Horiz (  )  Oblic (  )  Vert (  )
            # but is not filled out on any of the sheets

            # TODO: lat & lon
        )
        # samples = samples.append(subsample, ignore_index=True)
        samples = pandas.concat([samples, pandas.DataFrame(subsample)], ignore_index=True)
    else:
        print("sheet skipped")

print(samples.columns)

# example usage of data:
# samples.groupby(by='classification').count()['counted_aliquot'].hist()
# pyplot.show()

samples.to_csv("data/2a_csv/taxonomy.csv")

with open('data/2b_pickles/taxonomy-df.pickle', 'wb') as f:
    pickle.dump(samples, f)
