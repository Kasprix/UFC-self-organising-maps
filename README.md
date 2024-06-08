
# UFC Self-Organising Maps

This repository contains scripts and data for creating self-organising maps (SOMs) to analyse UFC fighter statistics. The goal is to visualise and cluster fighters based on their performance metrics.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Data Preparation](#data-preparation)
  - [Running the SOM](#running-the-som)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview

Self-organising maps are a type of artificial neural network used to produce a low-dimensional representation of high-dimensional data. This project uses SOMs to cluster UFC fighters based on various performance metrics. The analysis includes data scraping, preprocessing, and visualisation of results.

## Installation

To use this project, clone the repository and install the required Python packages:

```bash
git clone https://github.com/yourusername/UFC-self-organising-maps.git
cd UFC-self-organising-maps
pip install -r requirements.txt
```

## Usage

### Data Preparation

1. **FightMetricToDataframe.py**: This script scrapes fight metrics data and converts it into a pandas DataFrame.
2. **MultiplefighterURLS.py**: This script collects URLs for multiple fighters to be used in data scraping.

To run these scripts, execute:

```bash
python FightMetricToDataframe.py
python MultiplefighterURLS.py
```

### Running the SOM

1. **SomCreate.py**: This script takes the prepared data and runs the self-organising map algorithm to create clusters.

To run the SOM:

```bash
python SomCreate.py
```

## Results

The results of the SOM analysis are stored in the `Results` directory. This includes various visualisations and CSV files showing the clustered data.

### Example Results

- **all heatmaps.png**: Heatmaps representing different clusters.
- **sensitivity.png**: Sensitivity analysis of the SOM.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
