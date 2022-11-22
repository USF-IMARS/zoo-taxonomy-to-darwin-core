This repo is for processing the Zooplankton data collected from S FL MBON cruises in the FL keys so that it can be published to OBIS as a Darwin Core Archive.

The data is segmented annually.

Year | data status & notes                                                                 | raw datasheets link      | OBIS ref   
-----|-------------------------------------------------------------------------------------|--------------------------|------------------------------------------
2018 | rough 1st draft published as occurrence data only. Samples were processed by Jaime. | [from tylar's gdrive](https://drive.google.com/drive/folders/1FcyUnXjqIeh2XF7uhuuvKL8eYGSaJVvZ?usp=sharing) | https://obis.org/dataset/afef5da2-614b-4208-aee6-c2413ed5ab76
2019 | ?                                                                                   | Maybe Enrique knows?     | UNPUBLISHED
2020 | ?                                                                                   | Maybe Enrique knows?     | UNPUBLISHED
2021 | ?                                                                                   | Maybe Enrique knows?     | UNPUBLISHED
2022 | Not yet collected. Samples will be processed by Natalia.                            | .                        | .


## data processing steps
1. collect the data using the sheets (TODO: link the raw data collection spreadsheets here
2. run the relevant scripts to convert the collection sheets into a DwC archive
    - [Zooplankton Ingestion](https://github.com/sebastiandig/obis_zooplankton_setup)
      - Method for ingesting data and metadata, and conversion to DarwinCore
3. upload to OBIS via one of the [IPT](https://github.com/gbif/ipt) nodes listed [here](http://ipt.iobis.org/) (Caribbean?).

## additional links
* [obistools](https://github.com/iobis/obistools).

