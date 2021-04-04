# Machine Learning for exoplanet Identification


### Introduction
***
The field of astrophysics, where large datasets need to be processed rather quickly and efficiently, is a golden opportunity
for the application of machine learning. Over the past decade or so, advances have been steadily growing in the field, with various
algorithms used to process data. Specific applications range from identifying quasars, to mapping large scale galactic structures, to 
searching for signals from a sufficiently advanced extrasolar civilizations. A particular use case that initially seemed appropriate
for a semester-long project was using machine learning to parse data from the Kepler Space Telescope for the purpose of identifying
star systems containing exoplanets. Further theory is discussed in the wiki.

### Repo Organization
***
The repository contains two Jupyter notebooks which currently serve as proof-of-concept for deeper analysis. The "Data" directory contains
a zip archive of .csv files of the data sets used in the code, along with descriptions of each. The "Random" directory contains a few pieces
of in-progress code. Note: unless your machine contains absurd amounts of RAM, the Feature Extraction notebook is unsafe to run over more than 
~2000 rows of data.

This repository currently exists as a proof of concept on whether machine learning allows for satisfactory analysis of astronomical data.
Future work will be mainly focused on implementing proper signal analysis on raw data sets, and reworking the algorithms to ingest identified features.
