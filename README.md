# Big data project - University of Liege
In this project we were asked to answer if the University of liege
is a good example in terms of electrical consumption.
## Data
To answer that questions a dataset about the consumption in the university is
required. As our data in confidential, if you want to recreate this project 
you will need data from other sources. In our case the dataset 
was provided by the University.

### Initial data
Initial data consisted in the energetic values generated in the University in
 the range between January and October in 2018.
 
## Pre-processing
In order to do the pre-processing correctly, we have to introduce Input and 
Output path for each task in this section.
These paths have to be configured manually in *settings.py* introducing the root
path for the project. The other paths are connected to this root path.
* ### From .xls to .csv
   **Input path *(xls_path)*:** Folder where .xls are stored in a monthly 
   folder 
structure (1 folder per month and inside files .xls of that month).
    
   **Ouput path *(csv_path)*:** Folder where .csv will be stored with the same 
folder  structure as the input (1 folder per month).

* ### Group total consumption per building
   **Input path *(month_path)*:** Same as *csv_path* because the data came 
separated in months by default.

   **Ouput path *(year_path)*:** One file per building with all the consumption 
year data.

* ### Plots of the year
   **Input path *(year_path)*:** Takes the *year_path* to create the 
   plots, so first we need the data grouped.
   
   **Ouput path *(plots_path)*:** General folder for every plot that will be 
created in the project. Inside plots folder, nested folders for each building 
are created in this section containing 1 plot per variable in the 
consumption data. Example directory: *Plots/Year/Building_01/*

## Initial analysis
## Computing
## Analysis
