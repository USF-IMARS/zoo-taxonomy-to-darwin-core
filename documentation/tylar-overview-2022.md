This is a summary of how I used the python code here based on what little I can remember and deduce from the code.

[This gdrive folder](https://drive.google.com/drive/folders/1FcyUnXjqIeh2XF7uhuuvKL8eYGSaJVvZ?usp=sharing) contains relevant files not included in this repo.
Some notable files there are:
* `/data/` folder : this folder should be copied to your local. Code here loads and saves into this folder. If it were not so large then it would have been included in this repo.
* `species abbrev mappings` spreadsheet : this spreadsheet contains the manual translations from what the "raw" spreadsheets said to what the actual species label should be.

## The "raw" data
The `/data/1_raw` directory contains what was given to me to convert. Included are:
1. `sp.csv` : an export of the `species abbrev mappings` spreadsheet used to make sense of the various abbreviations used in the raw data.
2. `compiled_zoo_taxonomy_Jaimie_31JAN2018` : taxa counts from the zooplankton samples collected from the towed filter net.
3. `ZOO MBON_Jaimie_APR2017_v2` : same as (2) but for 2017
3. `WSMasterSampleLog` : Water sample information from the Walton Smith R.V. from which samples were taken
4. `zooplankton_consolidated` : details on how the zooplankton net samples were collected

## processing steps

1. `src/ingest/taxonomy-to-df.py` loads the species count spreadsheet (`compiled_zoo_taxonomy_Jaimie_31JAN2018.xlsx`), creates long dataframe containing the data compiled from all the sheets, and saves that dataframe to `taxonomy-df.pickle`.
2. `/src/verify/species_check.py` loads `taxonomy-df.pickle`, checks the species names from the dataframe using WoRMS, and prints the names that come back as unknown.
3. `/src/create-records.py` loads `taxonomy-df.pickle` and creates an `occurrences.csv` DwC (occurrence-core) file.
