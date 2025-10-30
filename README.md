# Bijplaatsingen afval - Amsterdam
In this repo we load the Amsterdam data about dumpings near undergruond trash containers. We then have some basic Python code to analyze the data and create a map.

[You can download the data here](https://data.amsterdam.nl/catalogus/aanpak_bijplaatsingen_v1/?tab=info). The data description [can be found here](https://api.data.amsterdam.nl/v1/docs/datasets/huishoudelijkafval.html#bijplaatsingen).

## Output 
The result of the analysis can be found in this repo as well, so you do not need to run the code yourself. `all_bins.csv` includes all the underground trash bins in Amsterdam that have been checked at least once. There's data for how many illegal dumpings have been done at each of these (`totaal_bijplaatsingen`), and how many times there were big items place (`aantal_grofvuil`). Also, the amount of times an item with address information was found, and most likely somebody got a fine, is included (`aantal_handhavingen`). 

N.B. This analysis was done on October 30th 2025, with the data that was at hand *at that time*. By now, the numbers might have risen.

[Browse an interactive map here](https://jorisheijkant.github.io/afval-amsterdam/map).

## Requirements
In order to run the code yourself, you'll need a modern version of python and some libraries (see `requirements.txt`). These are best installed in a separate python environment like venv or Conda. Use `pip install -r requirements.txt` to do that. 

## Running the script
Then you'll need the source csv from the Amsterdam government mentioned above. If that's correctly placed in the data folder, you can run the `parse_csv.py` script to run the analysis and re-render the csv and map. Make sure to check the file paths in that script before running it. 

Creating the map is an experimental feature and might take a long time depending on your pc hardware.
