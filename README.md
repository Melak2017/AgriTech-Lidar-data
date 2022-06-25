# AgriTech - USGS LIDAR

## Background

The USGS 3DEP project (United States Geological Survey 3D Elevation Program) aims at responding to growing needs for high-quality topographic data and a wide range of 3D data representation of the county’s features.

## Content

- [Overview](#overview)
- [Dataset Description](#the-dataset-description)
- [Install](#install)
- [Project Structure](#project-structure)

- [Dashboard](#dashboard)
- [Article](#article)

---

## Overview

- Python module that domain experts and data scientists can use to fetch, visualise, and transform publicly available satellite and LIDAR data.

- LiDAR or Light Detection and Ranging is an active remote sensing system that can be used to measure vegetation height across wide areas.

## The Dataset Description

- Data from the 3DEP repository's lidar point cloud is accessible through the USGS 3D Elevation Program (3DEP). By utilizing cloud computing and storage, 3DEP has made it possible for users to deal with enormous volumes of lidar point cloud data without having to download them first.
- The dataset provides realizations of the 3DEP point cloud data.The point cloud data resource is a public access organization provided freely accessible from AWS in EPT format. Entwine Point Tile (EPT) is a simple and flexible octree-based storage format for point cloud data. The organization of an EPT dataset contains JSON metadata portions as well as binary point data. The JSON file is core metadata required to interpret the contents of an EPT datase.

---

## Install

#### Creating a new environment.

It is good practice to install the geospatial stack in a clean environment starting fresh.

```
conda create -n geo_env
conda activate geo_env
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict
conda install python=3 geopandas

pip install pdal
```

#### Clone the repository and install the required packages.

```
clone https://github.com/Melak2017/AgriTech-Lidar-data.git
cd AgriTech-Lidar-data
pip install -r requirements.txt
```

---

## Project Structure

    .
    ├── .github/workflows              # github actions
    ├── .vscode                        # collection of folders that are opened in a VS Code window.
    ├── assets
    |   └──data_fetch.json             # pipline json file
    |
    ├── data                           # data directory
    ├── docs                           # HTML pages
    ├── notebooks                      # A simple - notebook on how to use the package.
    ├── screenshots                    # A sample screenshots of analysis result.
    ├── scripts                        # script files.
    |    ├── boundaries.py             # python file for boundry setting
    │    ├── ept_info.py               # pyhon file for info ept
    │    ├── elevation_extractor.py    # python file elevation extractor
    │    ├── lidar_fetch_data.py       # python file for data fecthing
    │    └── Lidar_Package.py          # final python module to use
    |
    ├── tests                          # directory for unit testing
    |    └── test_get_data.py          # unit-test file
    ├── requirements.txt               # a text file lsiting the projet's dependancies
    ├── .gitignore                     # files to ignore when committing
    ├── setup.py                       # a configuration file for installing the scripts as a package
    └── README.md                      # Markdown text with explanation of the project and the structure.

---

[back to top](#background)
