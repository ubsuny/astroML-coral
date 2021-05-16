# Overview of Data Sources

All data used for various tasks in this project was gathered using the Kepler Space Telescope. The files described below are contained in the zip archive of this directory

## Cumulative Data
Data extracted from all systems observed by the Kepler Mission in provided in the "cumulative.csv" file. It contains information on whether each system contains 
exoplanets and various physical parameters. The information contained therein has not yet been incorporated into any analysis by this project. A more accessible
version of the data (along with relevant information) is available at https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=cumulative


## Raw Light Curves
The bash scripts download data from the Mikulski archive containing raw flux measurements for all candidate systems over a certain run. These were edited and saved as .txt files for ease of use.  
Due to the quantity of data gathered, it is HIGHLY recommended to not run it directly, but to pull light curves from individual systems using the
links provided in the scripts via the method shown in the "Light_Curve_Demo" notebook. Note, the data is provided in the ".fits" format and requires the astropy
package to display.

Futher information about these data is available at https://archive.stsci.edu/missions-and-data/kepler

All other data used or created in the course of this project were too large to include on the github even when zipped. 
