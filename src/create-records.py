#!/usr/bin/env python3
"""
creates DwC record files from dataframes
"""
import pickle

import pandas

with \
    open("data/2b_pickles/sample-details-df.pickle", 'rb') as sample_file,\
    open("data/2b_pickles/taxonomy-df.pickle",       'rb') as taxa_file,  \
    open("data/2b_pickles/water-samples-df.pickle",  'rb') as water_file  :
    sample_detail_df = pickle.load(sample_file)
    taxonomy_df      = pickle.load(taxa_file)
    water_sample_df  = pickle.load(water_file)

    # TODO: (???) join on:
    # taxa:
    #   1. cruise_id    3165002
    #   2. datetime     2017-04-24
    #   3. station      WS
    # water-samples
    #   1. Cruise       WS1418
    #   2. date         2014-12-01
    #   2. Time (GMT)   13:23:00
    #   4a. latitude    25.6449733333
    #   4b. longitude   25.6449733333
    # sample-details
    #   3. station      Molasses Reef
    #   2. Date         2015-04-13
    #   2. Local Time   16:00:00


    # === Event record(s)
    # map created from averages in water-samples
    station_map = {
        "MR": {
            "lat": 25.00607727,
            "lon": -80.37953386
        },
        "WS":{
            "lat": 24.47605506,
            "lon": -81.71532752
        },
        "LK":{
            "lat": -81.41464542,
            "lon": 24.53862793
        }
    }
    occurrences = pandas.DataFrame()
    institution_code = "USF_IMaRS"
    collection_code = "compiled_zoo_taxonomy_jaimie"
    catalog_number = "2018_01_31"
    occurrences = occurrences.assign(
        occurrenceID = [
            ':'.join([
                "urn:catalog",
                institution_code,
                collection_code,
                catalog_number,
                str(row)
            ]) for row in taxonomy_df.index.values
        ],
        eventDate = taxonomy_df["datetime"],
        decimalLongitude = [station_map[st]["lon"] for st in taxonomy_df["station"]],
        decimalLatitude = [station_map[st]["lat"] for st in taxonomy_df["station"]],
        scientificName=taxonomy_df["classification"],
        scientificNameID="TODO: worms lookup", #taxonomy_df["classification"],
    )
    occurrences = occurrences.assign(
        basisOfRecord="HumanObservation",
        collectionCode = collection_code,
        catalogNumber = catalog_number,
        occurrenceStatus="present",
        institutionCode = institution_code
    )

    occurrences.to_csv("data/3_records/occurences.csv")
