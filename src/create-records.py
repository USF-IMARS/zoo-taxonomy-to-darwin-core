#!/usr/bin/env python3
# creates DwC record files from dataframes
import pickle

import pandas

with \
    open("data/2b_pickles/sample-details-df.pickle", 'rb') as sample_file,\
    open("data/2b_pickles/taxonomy-df.pickle",       'rb') as taxa_file,  \
    open("data/2b_pickles/water-samples-df.pickle",  'rb') as water_file  :
    sample_detail_df = pickle.load(sample_file)
    taxonomy_df      = pickle.load(taxa_file)
    water_sample_df  = pickle.load(water_file)

    # === Event record(s)
    events = pandas.DataFrame()
    institutionCode,
    collectionCode,
    catalogNumber,
    occurrenceID,
    eventDate,
    decimalLongitude,
    decimalLatitude,
    scientificName,
    scientificNameID,
    occurrenceStatus,
    basisOfRecord
