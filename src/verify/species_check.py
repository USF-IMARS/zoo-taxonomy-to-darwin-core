#!/usr/bin/env python3
"""
checks species names in taxonomy-df.pickle
prints ones that do not pass the check
"""
import pickle

import pandas
from suds import null, WebFault
from suds.client import Client

cl = Client('http://www.marinespecies.org/aphia.php?p=soap&wsdl=1')
scinames = cl.factory.create('scientificnames')
scinames["_arrayType"] = "string[]"

def check_species(sp_name):
    scinames["scientificname"] = sp_name

    array_of_results_array = cl.service.matchAphiaRecordsByNames(
        scinames,
        # like="true",
        fuzzy="false",
        marine_only="true"
    )
    print("=== WoRMS lookup results:")
    print("results len={}".format(len(array_of_results_array)))
    assert(len(array_of_results_array) == 1)
    for results_array in array_of_results_array:
        print("results={}".format(len(results_array)))
        # assert(len(results_array) == 1)
        return results_array
        # for aphia_object in results_array:
        #     print(aphia_object)
            # print('%s %s %s' % (aphia_object.AphiaID, aphia_object.scientificname, aphia_object.genus))


with open("data/2b_pickles/taxonomy-df.pickle", 'rb') as taxa_file:
    print("loading pickled file...")
    taxonomy_df = pickle.load(taxa_file)

    # check vs WoRMS
    # based on http://www.marinespecies.org/aphia.php?p=webservice&type=python
    count = 0
    for spec_name in taxonomy_df["classification"]:
        print("checking #{}: '{}'...".format(count, spec_name))
        res = check_species(spec_name)
        print(res)
        if len(res) == 1:
            match = res[0]
            print("\t{} | {}\t|{}".format(
                match.AphiaID,
                match.scientificname,
                match.genus
            ))
        elif len(res) == 0:
            print("ERR: not found!")
        else:
            # multiple matches
            print("ERR: choose match from :")
            for match in res:
                print(match)
        count +=1
