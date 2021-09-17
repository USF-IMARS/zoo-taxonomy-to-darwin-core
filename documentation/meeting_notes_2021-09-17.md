Similar crosswalk from prev work with Digna: https://www.sciencebase.gov/catalog/item/6049252cd34eb120311ad2a5.

Boat is in motion dragging the net at tow speed of ~2 knots.

Depth: Always in upper 50m or less. Net is dropped to 25 meters then slowly brought up to surface to sample full water column.

## DwC Occurrence File:

column          | DwC term                           |  source                 |
--------------- | ---------------------------------- | ----------------------- |
Species Name    | aphiaID                            | aphiaID column from taxa using WoRMS
DateTime        | datetime                           | from filename
lat/lon         | decimalLatitude & decimalLongitude | station ID in filename using ID->lat/lon mapping (TODO: mapping file)
mesh size       | MoF (see below)                    | sheet header section
method (bongo)  | MoF (see below)                    | same for all samples
depth           | minDepth & maxDepth                | assumed for all samples 0m - 50m
NA              | coordinate_uncertainty_in_meters   | estimated for all samples
Filtered Volume | MoF (see below)                    | sheet header section 

## MoFs

* device aperture: http://vocab.nerc.ac.uk/collection/Q01/current/Q0100012/
* mesh size:  http://vocab.nerc.ac.uk/collection/P01/current/MSHSIZE1/
* bongo net method : ???
