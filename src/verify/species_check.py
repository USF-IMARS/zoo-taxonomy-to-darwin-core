#!/usr/bin/env python3
"""
checks species names in taxonomy-df.pickle
prints ones that do not pass the check
"""
import pickle
# import math
import csv

import numpy
import pandas
from suds import null, WebFault
from suds.client import Client

with open("data/2b_pickles/taxonomy-df.pickle", 'rb') as taxa_file:
    print("loading pickled file...")
    taxonomy_df = pickle.load(taxa_file)

    # print("checking these species w/ WoRMS: {}".format(
    #     taxonomy_df["classification"])
    # )

    # print(taxonomy_df["classification"])
    # print(taxonomy_df["classification"][25:50])
    print(taxonomy_df["classification"][2734:2739])
    # TODO: why is 2736 NaN?!?

    # === break into len=50 chunks b/c of API limit
    all_data = list(taxonomy_df["classification"])
    CHUNK_SIZE = 50
    data_chunks = []  # this will be list of lists
    search_strs=[]
    sp_df = pandas.read_csv("data/1_raw/sp.csv")
    cols = [  # taxa level columns in decending order
        "kingdom", "phylum", "subphylum", "class", "subclass",
        "infraclass", "superorder", "order", "suborder", "family", "genus",
        "species"
    ]
    for classif_str in all_data:
        search_str=""
        print("----------\n",classif_str,"\n---------")
        sp_row = sp_df[sp_df["classification"] == classif_str]
        if len(sp_row)==0:
            # raise KeyError("no row in species map for '{}'".format(classif_str))
            print("no row in species map for '{}'".format(classif_str))
            search_str = classif_str
        elif len(sp_row) > 1:
            raise KeyError("too many rows matching '{}'".format(classif_str))
        # print(sp_row.shape)
        # print(sp_row)
        else:
            for taxa_lvl in cols:
                taxa_label = sp_row[taxa_lvl].item()
                # print("{}={}".format(taxa_lvl, taxa_label))
                if taxa_label == "UNKNOWN" or pandas.isnull(taxa_label):
                    search_str += "% "
                else:
                    search_str += taxa_label + ' '
        if pandas.isnull(search_str):
            search_str = classif_str
        else:
            search_str.replace(" sp.", "%")
            search_str.replace(" sp", "%")
        print(search_str)
        search_strs.append(search_str)

    while (len(search_strs) > 0):
        # === map "classification" to the clarified names in sp.csv
        # print(len(search_strs))
        data_chunks.append(
            [search_strs.pop() for i in range(min(CHUNK_SIZE, len(search_strs)))]
        )

    print("{} species split into {} chunks of len {} + 1 chunk of len {}".format(
        len(taxonomy_df["classification"]),
        len(data_chunks)-1,
        CHUNK_SIZE,
        len(data_chunks[-1])
    ))

    badrows=[]
    for chunk_n, data_chunk in enumerate(data_chunks):
        # print(len(data_chunk))
        print(data_chunk)
        fname = 'data/2c_verify/species_{}.tsv'.format(chunk_n)
        print("creating {}...".format(fname))
        with open(fname, 'w') as csvfile:
            # TODO: write results to file
            csv_writer = csv.writer(csvfile, delimiter='\t')

            # check vs WoRMS
            # based on http://www.marinespecies.org/aphia.php?p=webservice&type=python
            cl = Client('http://www.marinespecies.org/aphia.php?p=soap&wsdl=1')
            scinames = cl.factory.create('scientificnames')
            scinames["_arrayType"] = "string[]"
            scinames["scientificname"] = data_chunk

            array_of_results_array = cl.service.matchAphiaRecordsByNames(
                scinames,
                like="true",
                fuzzy="false",
                marine_only="false"
            )
            print("performing WoRMS lookup...")
            # print("results len={}".format(len(array_of_results_array)))
            assert(len(array_of_results_array) == len(data_chunk))
            for i, results_array in enumerate(array_of_results_array):
                # print("aphia_len={}".format(len(results_array)))
                if (len(results_array) == 0):
                    badrow = [
                        i + chunk_n*CHUNK_SIZE,
                        data_chunk[i],
                        "???","???","???"
                    ]
                    badrows.append(badrow)
                    csv_writer.writerow(badrow)
                else:
                    for aphia_object in results_array:
                        csv_writer.writerow([
                            i + chunk_n*CHUNK_SIZE,
                            data_chunk[i],
                            aphia_object.AphiaID,
                            aphia_object.scientificname,
                            aphia_object.genus
                        ])
            print("chunk {} complete.".format(chunk_n))

print(badrows)
