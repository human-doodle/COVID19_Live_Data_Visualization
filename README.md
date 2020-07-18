## COVID19 Live Data Visualization - Project Overview

* Created some advanced visualizations of the COVID-19 data India and Maharashtra state.
* Data Source - https://covidindia.org/Maharashtra
* Python Version - 3.8.3
* Libraries used - Geopandas, Matplotlib, Seaborn, Pandas.
* Content referred - https://github.com/theengineeringguy-yt
* Creators - https://github.com/Rahul-Khairnar, https://github.com/human-doodle

## Data Collection & Pre-processing

* The data source is the govt official websites
    * https://covidindia.org/Maharashtra
    * https://www.mygov.in/covid-19
* The data refreses everyday at 8AM and 11PM
* Data collected and stored in a pandas dataframe.
* Shape file imported and converted into a pandas dataframe.
* The state names in the shape file dataframe are adjusted so as to match with our COVID-19 dataframe. Please note, mismatch in names of states will result in the state not visualized on the map.
* The two dataframes are joined so that we can get a single dataframe consisting of all the states, their counts and their location polygons.

## Data Exploration

* The dataframe is checked for NaN values if any.
* Since all states obtained matched with the ones in shape file, there were no NaN values in the dataframe.

## Data Visualization.

* Barplot is plotted for Total Patients Recovered in the various districts in the state of Maharashtra.


![alt text](https://github.com/human-doodle/COVID19_Live_Data_Visualization/blob/master/img/bar_chart.png "Total Patients Recovered")


* Indian map is plotted using the library geopandas.
* The states are colored according to the Total Case counts in that particular state.

![alt text](https://github.com/human-doodle/COVID19_Live_Data_Visualization/blob/master/img/India.png "Indian Map")


* Maps are plotted for Total Number of cases, Total Patients Recovered and Total Deaths in the various districts in the state of Maharashtra.


![alt text](https://github.com/human-doodle/COVID19_Live_Data_Visualization/blob/master/img/maha_total.png "Total COVID-19 Cases")


![alt text](https://github.com/human-doodle/COVID19_Live_Data_Visualization/blob/master/img/maha_death.png "Total Deaths")


![alt text](https://github.com/human-doodle/COVID19_Live_Data_Visualization/blob/master/img/maha_rec.png "Total Patients Recovered")


* Timeseries plot for the state of Maharashtra is plotted from the date 2nd July, 2020 till 13th July, 2020. The timeseries shows the rise in total cases over the period.


![alt text](https://github.com/human-doodle/COVID19_Live_Data_Visualization/blob/master/img/Timeseries_plot.png "Timeseries Plot")


* Area plot is plotted depicting Total Cases, Active Cases, Total Deaths and Total patients recovered.


![alt text](https://github.com/human-doodle/COVID19_Live_Data_Visualization/blob/master/img/Area_plot.png "Area Plot")


* Pie Chart is plotted for depicting the Total Cases, Active Cases, Total Deaths and Total patients recovered.


![alt text](https://github.com/human-doodle/COVID19_Live_Data_Visualization/blob/master/img/pie_chart.png "Piechart")


