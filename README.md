# NASA Psyche Capstone 19A: Visualizing Space Data Footprints (Copper Class - 2022)

- [NASA Psyche Capstone 19A: Visualizing Space Data Footprints (Copper Class - 2022)](#nasa-psyche-capstone-19a-visualizing-space-data-footprints-copper-class---2022)
  - [Project Description](#project-description)
  - [Team](#team)
  - [Installation](#installation)
    - [Set up the environment](#set-up-the-environment)
  - [Usage](#usage)
  - [How-to?](#how-to)
  - [Credits](#credits)
    - [SPICE](#spice)
    - [SpiceyPy](#spiceypy)
  - [License](#license)

## Project Description
## Team
## Installation

### Set up the environment

``` bash
$ conda create --name <env name> --file requirements.txt
$ conda activate <env name>
```

## Usage

To run the app with GUI,
``` bash
$ python app.py
```
This will create a localhost server on http://127.0.0.1:5000/ (or some other port)

To run the app with CLI,
```bash
$ python -m psyche [file name(s)]
```

## How-to?

Update package dependencies?
```
$ conda install <package name>
$ conda list --explicit > requirements.txt
```
Push this new requirements.txt to git
Make sure to do `conda env update --name <env name> --file requirements.txt --prune` with every git pull.

## Credits

### SPICE

    Acton, C.H.; "Ancillary Data Services of NASA's Navigation and Ancillary Information Facility;" Planetary and Space Science, Vol. 44, No. 1, pp. 65-70, 1996.

    Charles Acton, Nathaniel Bachman, Boris Semenov, Edward Wright; A look toward the future in the handling of space science mission geometry; Planetary and Space Science (2017);
    DOI 10.1016/j.pss.2017.02.013
    https://doi.org/10.1016/j.pss.2017.02.013 

### SpiceyPy

    Annex et al., (2020). SpiceyPy: a Pythonic Wrapper for the SPICE Toolkit. Journal of Open Source Software, 5(46), 2050, https://doi.org/10.21105/joss.02050

## License

MIT
