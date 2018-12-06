Scripts from [IOOS data workshop 2018](https://github.com/ioos/BioData-Training-Workshop) (and follow-up work) to align IMaRS zooplankton data from Walton Smith cruises to Darwin Core.

The inputs are described in the **data** section below, the output should align with the standards outlined [here](http://rs.gbif.org/); a similar example of this format can be accessed [via DwC-A button here](http://ipt.vliz.be/eurobis/resource?r=deltaresbenthos).

The resulting output will be uploaded to OBIS via one of the [IPT](https://github.com/gbif/ipt) nodes listed [here](http://ipt.iobis.org/) (Caribbean?).

## data
1. `compiled_zoo_taxonomy_Jaimie_31JAN2018.xlsx` - species counts for each sampling
    1. (sheet name) == station & cruise ID
        1. classification
        2. n_ind_aliquot
        3. tot_ind_sample
        4. n_ind_per_m3
        5. sub_tot_g
        6. drag_type (! empty !)
        7. counted_aliquot
        8. volume_sample_water
        9. volume_filtered
        10. date
        11. mesh_size
        12. folson
        13. split size
2. `WSMasterSampleLog.xlsx` - CTD water samples for all stations
    1. Rank
    1. Keyfield
    1. Cruise
    1. Date (GMT)
    1. Temperature
    1. Salinity
    1. Latitude Deg
    1. Latitude Min
    1. Latitude Decimal
    1. Longitude Deg
    1. Longitude Min
    1. Longitude Decimal
    1. Time (GMT)
    1. Station
    1. F or CTD
    1. Depth
    1. Chlorophyll Tube #
    1. Avg chl a (ug/L)
    1. Avg Phaeophytin (ug/L)
    1. Nutrients Tube #
    1. NH4  (uM)
    1. PO4  (uM)
    1. NO3+NO2 (uM)
    1. NO3   (uM)
    1. NO2  (uM)
    1. Si    (uM)
    1. DIC Bottle # Manzello
    1. TA with CRM Correction (uequiv/kg)
    1. CRM Corrected TCO2 (µmol/kg)
    1. DIC Bottle # Wanninkhof
    1. DIC (umol/kg)
    1. pH
    1. Oxygen
    1. Notes
    1. Seapoint Chl Fluorometer Voltage
    1. Seapoint Chl Fluorometer Calculated Conc
    1. Seapoint Chl Fluorometer Gain
    1. Turner C7 Chlorophyll-a Raw Fluoresence Units
    1. Turner C7 CDOM Raw Fluoresence Units
    1. Turner C7 Turbidity Raw Fluoresence Units

3. `zooplankton_consolidated.xlsx` - details of sampling methods for each sample in (1) | NOTE: data from this doesn't necessarily need to be included b/c values in (1) use these values in calculations
    1. global metadata:
        1. Area of the net(m^2)
        2. Net diameter (mm)
    1. per sample:
        1. Station
        1. mesh size (um)
        1. Date
        1. Local time (EST)
        1. flowmeter in
        1. LAT in
        1. LON in
        1. Tow time (min)
        1. Flowmeter out
        1. Ship speed (knots)
        1. inpeller constant
        1. distance (m)
        1. tow speed (m min-1)
        1. split size
        1. formalin vol. (ml)
        1. Vol filtered (m^3)
4. `ZOO MBON_Jaimie_APR2017_v2.xlsx` - older version of (1)

### DwC alignment notes
* "Event" is used for cruise, station, sample, subsample from (3)?
* "ExtendedMeasurementOrFacts" are added from (2), (3)
* "Occurence Extension" is used for each species from (1)

### DwC alignment table
Mapping the variables above to Darwin Core is outlined in [this spreadsheet](https://docs.google.com/spreadsheets/d/13jiEv32KN0AcX6ppZOSt6kZboKRG_ZxmC3VhnHSXEhE/edit?usp=sharing).
In this sheet the `raw data item id` is reference to numbered lists above.
