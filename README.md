# School Boundary Merge

This represents a merge of all the attendance areas for the schools in the Chicago Public School System. The source for the final result (the files prefixed with ``all_schools``) is the data from the [City of Chicago Data Portal](https://data.cityofchicago.org/). The files that you get there are broken down by grade so this is an attempt to make one file that contains all the schools regardless of grade. The idea here is not to create a pretty map but to use this information to power other geospatially aware datasets to answer questions like "What kind of crime occurs within the attendance boudary of school X?"

### What you have here is:

1. A few different file type containing the final result of merging all the source data.
2. The source data

The Chicago Public School system also provides data about the attendance boundaries in a few fusion tables, one for each type of school: 

* [Charter Schools](https://www.google.com/fusiontables/DataSource?docid=17Inkq6Z_aPhvIlHSWA9MMX4-d9NkmwQZQELBJY4#map:id=3)
* [Elementary Schools](https://www.google.com/fusiontables/DataSource?docid=1VvtxgksCi6cQHvSsnfnZwn1PrHgkRa8rkWOoHRI#map:id=3)
* [Middle Schools](https://www.google.com/fusiontables/DataSource?docid=1owQoX0Iw1r73jeYpAWotVsp6dBYqOdz0oMTvmMY#map:id=3)
* [Elementary Schools](https://www.google.com/fusiontables/DataSource?docid=1_BkjK_60DUwSvJCozyOO53Q56lkbjrTv2bgpzp8#map:id=3)

You can download the KML files for those maps from those locations (they are also included here in the source data folder). 
