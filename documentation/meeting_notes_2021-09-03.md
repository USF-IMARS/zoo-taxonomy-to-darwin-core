Get zooplankton DwC help @  bio data standards meeting

* Link to notes:  https://docs.google.com/document/d/1JfXHFXhP0rB8juAK3-KvOtqtwDofPwewoAB_ZyFwSwY
* Link to GitHub:  https://github.com/ioos/bio_data_guide
* Join Zoom Meeting: https://zoom.us/j/4614271978?pwd=dTduaVY0RnlPNThjajQydENZZUg1Zz09 <==

## general 
* 1 file per sample, each file only has one sheet
    * file name should include station name & datetime of the sample separated by an underscore (`_`). example: `MR_2021-09-03T13:36.xlsx`
        * we need a table to map station abbreviation to full name & lat/lon
        * datetime should be in ISO 8601 format (`YYYY-MM-DDTHH:mm:ss`) 
* position of the first row needs to be consistent
* must say `total *plankton` on last row
* need to include `aphia_id` column

## metadata header section
* metadata in the "header" section needs to be in a consistent spot - i.e. "Mesh:" text is the same and value is always in `B5`
* metadata to include
    * volume filtered
    * lat / lon of station - station abbrev in filename
    * datetime of sample - in filename 
    * mesh size
    * method: bongo net tow
    * split size?
    * depth of sample?

## todo items
1. tylar: ask Abby what MoF should we include
1. tylar: how to best add pictures
1. Natalia: write up a little note on what each metadata in the header section is (eg Replicate, Time, etc)
1. Natalia : rm dilution factor column
1. Natalia : add item in header `Notes` for general notes about the sample
2. Natalia : add aphia_id column
