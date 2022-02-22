We should use event core instead of occurence core.

* The "core" is the first file that is looked at when inpsecting the archive.
* "Occurrence" is a sighting of one or more individuals.

## notes for turning data into 
One occurrence row for each number of species found in each sample.
* 10 individuals in one event (sample), one occurrence row, number of individuals (10) goes in MoF table
* occurrence ID connects the occurrence table row to the MoF table
* event is sampling event in event table - env data goes there or in MoF if necessary
* reference "sampling protocol" in the event file so that all the information doesn't need to be stated in the file
* one big cruise event, one sampling event for each, aliquot count events are not split up into individual events because they do not have unique MoF data for each 

# TODO
* Need to define protocol or else find a reference for the std protocol being used. 
If the protocol is not standard then we should consider publishing to a journal so that it can be referenced here and in the future.
* write a sentence or two on what each column means and what the items at the top mean

## suggested changes to the zooplankton analysis sheet:
1. Ship speed should have uncertainty +/- number.
2. GMT should be UTC
3. move units to their own column or else put them in brackets `[` `]`

## suggested changes for the ship sampling event sheet:
1. units should be in brackets or else in their own column
2. question: what is difference in lat/lon in the lookup table at top vs `LAT in` and `LON in` rows
3. need short description of each column/row 
