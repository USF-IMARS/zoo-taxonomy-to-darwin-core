#!/usr/bin/env python3
"""
checks species names in taxonomy-df.pickle
prints ones that do not pass the check
"""
import pickle

import pandas
from suds import null, WebFault
from suds.client import Client

with open("data/2b_pickles/taxonomy-df.pickle", 'rb') as taxa_file:
    print("loading pickled file...")
    taxonomy_df = pickle.load(taxa_file)

    print("checking these species w/ WoRMS: {}".format(
        taxonomy_df["classification"])
    )

    # TODO: map "classification" to the clarified names in sp.csv

    # check vs WoRMS
    # based on http://www.marinespecies.org/aphia.php?p=webservice&type=python
    cl = Client('http://www.marinespecies.org/aphia.php?p=soap&wsdl=1')
    scinames = cl.factory.create('scientificnames')
    scinames["_arrayType"] = "string[]"
    scinames["scientificname"] = list(taxonomy_df["classification"])

    # TODO: break into len=50 chunks b/c of API limit

    array_of_results_array = cl.service.matchAphiaRecordsByNames(
        scinames,
        like="true",
        fuzzy="false",
        marine_only="false"
    )
    print("=== WoRMS lookup results:")
    print("results len={}".format(len(array_of_results_array)))
    for results_array in array_of_results_array:
        print("aphia_len={}".format(len(results_array)))
        for aphia_object in results_array:
            print('%s %s %s' % (aphia_object.AphiaID, aphia_object.scientificname, aphia_object.genus))
