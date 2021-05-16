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
The repository contains two Jupyter notebooks which currently serve as proof-of-concept for deeper analysis. An example of methods created for
analysis is in the third "example" notebook. The "Data" directory contains the txt files that are used for data procurement. Unfortunately, the processed datasets are too large to store on github even when zipped. The "Random" directory contains a few pieces of in-progress code. Note: unless your machine contains absurd amounts of RAM, the Feature Extraction notebook is unsafe to run over more than  ~2000 rows of data.

The Tools folder contains data processing functionality for various parts of the project. 

WARNING: minimum specs to safely run everything at 8GB RAM and at least 10GB local storage. If testing things yourself, please pay very close attention to target files. Big data sets in memory can easily crash your machine. Also highly recommended is a good ethernet cable. Run at your own risk


This repository currently exists as a proof of concept on whether machine learning allows for satisfactory analysis of astronomical data.
Future work will be mainly focused on implementing proper signal analysis on raw data sets, and reworking the algorithms to ingest identified features.


***

Any parts of this project can be reused for whatever purposes. If it's being included in something important, please reconsider and come up with better alternatives to the spaghetti within. 
