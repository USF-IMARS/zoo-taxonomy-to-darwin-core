Scripts from [IOOS data workshop 2018](https://github.com/ioos/BioData-Training-Workshop) to align IMaRS zooplankton data from Walton Smith cruises to Darwin Core.

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
        12. Folson
        13. split size

2. `WSMasterSampleLog.xlsx` - CTD water samples for all stations
3. `zooplankton_consolidated.xlsx` - details of sampling methods for each sample in (1)
4. `ZOO MBON_Jaimie_APR2017_v2.xlsx` - older version of (1)

### DwC alignment notes
* "Event" is used for cruise, station, sample, subsample from (3)?
* "ExtendedMeasurementOrFacts" are added from (2), (3)
* "Occurence Extension" is used for each species from (1)
