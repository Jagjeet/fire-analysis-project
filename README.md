# fire-analysis-project

This project's goal is to analyze [fire data](https://www.kaggle.com/rtatman/188-million-us-wildfires) and analyze it with respect to [air quality data](https://www.kaggle.com/epa/epa-historical-air-quality). We will be looking at the following areas:

* Comparing national fire data with California fire data
* Comparing Californa fire data with California annual air quality data
* Looking at the correlation of counties with worse air quality and fires
* Projecting fires (count, counties most impacted, etc.) for the future

All data is taken from [Kaggle](https://www.kaggle.com). See the `Major Findings` below or view the presentation for more details.

## Major Findings

### Comparing national fire data with California fire data

* While the number of fires is trending up nationally, the number of fires in California is trending down
* National and California burn duration/year, average acreage and total acrege burned are trending up

### Comparing Californa fire data with California annual air quality data

* The counties most affected by fires are: Fresno, Lake, San Bernardino, Trinity
* The counties with the worst days of air quality are: Calaveras, Placer, Inyo

### Looking at the correlation of counties with worse air quality and fires

* The worst fire counties are not the same as the worst air quality areas
* The air moves based on wind patterns and affects other counties more

### Projecting fires (count, potential causes, counties most impacted, etc.) for the future

* Due to air patterns, the same counties will continue to be affected by poor air quality
* While the number of fires in California may continue to decrease, the intensity of fires in terms of duration and acreage is likely to get worse.
* At a national level, the number of fires, the intensity of fires in terms of duration and acreage is likely to get worse.

## Project Techical Requirements

The project will meet the following requirements:

* Use Pandas to clean and format your data set(s)
* Create a Jupyter Notebook describing the data exploration and cleanup process
* Create a Jupyter Notebook illustrating the final data analysis
* Use Matplotlib to create a total of 6-8 visualizations of your data (ideally, at least 2 per “question” you ask of your data)
* Save PNG images of your visualizations to distribute to the class and instructional team, and for inclusion in your presentation
* Optionally, use at least one API, if you can find an API with data pertinent to your primary research questions
* Create a write-up summarizing your major findings. This should include a heading for each “question” you asked of your data, and under each heading, a short description of what you found and any relevant plots.

## Project Presentational Requirements

* Be at least 8-10 min. long
* Describe the core message or hypothesis for your project.
* Describe the questions you and your group found interesting, and what motivated you to answer them
* Summarize where and how you found the data you used to answer these questions
* Describe the data exploration and cleanup process (accompanied by your Jupyter Notebook)
* Describe the analysis process (accompanied by your Jupyter Notebook)
* Summarize your conclusions. This should include a numerical summary (i.e., what data did your analysis yield), as well as visualizations of that summary (plots of the final analysis data)
* Discuss the implications of your findings. This is where you get to have an open-ended discussion about what your findings “mean”.
* Tell a good story! Storytelling through data analysis is no different than in literature. Find your narrative and use your analysis and visualization skills to highlight conflict and resolution in your data.

## Prerequisites

To run this project the following tools are needed:

* Python (tested with v3.85, earlier versions may work as well, but have not been tested)
* Jupyter Notebooks and/or Jupyter Labs

## Usage

1. Clone the respository
2. Download fire historical data from [1.88 Million US Wildfires](https://www.kaggle.com/rtatman/188-million-us-wildfires) to the `Resources` directory.
3. Run the `Tools/FireDataExporter.ipynb` from Jupyter Notebook or Jupyter Labs to export the data from SQLLite to `Fires.csv` file which will contain the subset of data used for analysis
4. Download and save the CA air quality data to the `Resources` directory. This can be done by running this helper [Kaggle notebook](https://www.kaggle.com/jagjeetkhalsa/airqualityexporter). Note the following:
    * The notebook uses the BigQuery API and public [Historical Air Quality](https://www.kaggle.com/epa/epa-historical-air-quality) data to generate the CSV data
    * The query can take a few minutes to complete
    * Once it is completed the data used for analysis can be downloaded from the `output folder` in the data menu on the right side
5. Open and run `FireAnalysis.ipynb` from Jupyter Notebook or Jupyter Labs to run the fire related analysis.
6. Open and run `AirQualityCA.ipynb` and `CorrelationOfCountiesAndFire2015` from Jupyter Notebook or Jupyter Labs to run the air quality related analysis.

Analysis can be viewed in the individual cells.

## Known Issues

* In some cases data from previous Jupyter cells are used to calculate values in the current cell. As such make sure to run all above cells to obtain the correct output

## References

The fire analysis made use of the following concepts and links:

### Reference Description

#### FIPS Codes

* https://www.nrcs.usda.gov/wps/portal/nrcs/detail/ca/home/?cid=nrcs143_013696

#### Kaggle - BigQuery Data Limits

* https://www.kaggle.com/product-feedback/48573

#### Kaggle - Saving a DataFrame as a CSV

* https://www.kaggle.com/getting-started/60617

#### Kaggle - Using the BigQuery Helper Package

* https://www.kaggle.com/sohier/introduction-to-the-bq-helper-package

#### SQLite from Python and Pandas

* https://datacarpentry.org/python-ecology-lesson/09-working-with-sql/index.html

