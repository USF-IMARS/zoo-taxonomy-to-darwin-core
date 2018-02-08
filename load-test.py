#!/usr/bin/env python3
# loads data from the "compiled" excel file
# into a dict.

from datetime import datetime
import math

import pandas
import pprint

xl = pandas.ExcelFile("data/compiled_zoo_taxonomy_Jaimie_31JAN2018.xlsx")

samples = []
for sheet_name in xl.sheet_names:
    EXCLUDED_SHEETS = [
        "Samples for see", "PLANTILLA", "Sheet1",
        "MR1115500"  # TODO: this has no date?!?
    ]
    STATIONS = ["MR", "LK", "WS"]
    print("=== {}".format(sheet_name))
    if sheet_name not in EXCLUDED_SHEETS:
        station = sheet_name[:2]
        cruise_id = sheet_name[2:]
        sample = {
            "station": station,
            "cruise_id": cruise_id
        }
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
        # === datetime
        try:
            sample['datetime'] = datetime.strptime(df.iloc[0,0], "Date:  %m/%d/%Y")
        except:
            sample['datetime'] = datetime.strptime(df.iloc[0,0], "FECHA:  %m/%d/%Y")

        # === lat / lon
        # TODO: get lat/lon from station name (b/c not in most sheets

        # === drag_type
        # sample["drag_type"] # this looks like:
        # Type of trawl Horiz (  )  Oblic (  )  Vert (  )
        # but is not filled out on any of the sheets

        # === Vol filtered  (m³)
        sample['volume_filtered'] = df.iloc[5,0]

        # === Vol sample water
        sample['volume_sample_water'] = df.iloc[5,3]

        # === Counted aliquot
        sample['counted_aliquot'] = df.iloc[5,5]

        # === sub-samples:
        start_row = 6  # species headers on this row
        # load samples as dataframe:
        sample['subsamples'] = pandas.DataFrame(
            data=df.iloc[(start_row+1):, 0:7],
            # columns=df.iloc[start_row],
            # copy=True
        )
        # columns from
        # sample['subsamples'].columns = df.iloc[start_row]
        # actually look like:
        # Clasification | Nº Ind. Aliquot | NaN | Total Ind. Sample | NaN | N° Ind.\ m³ | Sub total G.
        # but we rename these slightly:
        print(sample['subsamples'])
        COL_NAMES = [
            "classification", "n_ind_aliquot", "NaN", "tot_ind_sample", "NaN", "n_ind_per_m3", "sub_tot_g"
        ]
        sample['subsamples'].columns = COL_NAMES

        # # load sample rows until we run out of rows
        # sample['subsamples'] = []
        # species_name = "temporary_string"
        # while not math.isnan(species_name):
        #     # rows:
        #     # Clasification
        #     species_name = df.iloc[row,0]
        #     # TODO: other columns

        samples.append(sample)
    else:
        print("sheet skipped")

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(samples)
