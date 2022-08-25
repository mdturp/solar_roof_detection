# Data Sheet 

This document contains information on the data and decisions taken by myself
to process and prepare the data.

## Raw Data

**When was the data downloaded?**
The raw data was downloaded on 20.08.2022

**From where was the data downloaded?**
The data was downloaded from the public website from the canton of Zurich 
specifically from http://maps.zh.ch/download/orthofoto/fruehjahr/2021/jpeg/

**Who downloaded the data?**
Maximilian Dennis Turp (maximilian.dennis.turp@gmail.com)

**What does the data contain?**
The data contains satellite imagery of the entire city of Zurich.

**What is the average file size?**
The average file size is ~650mb

**How large is the entire dataset?**
The entire dataset is ~23.1 GB

**Where can I download the raw data?**
https://solarroofdetection.blob.core.windows.net/rawdata/

## Label Ready Data

**What does the data contain?**
The data contains smaller images of size 500x500x3 pixels of satellite imagery
for the entire city of zurich.

**What modifications have been done to the raw data?**
1) The large .tif files have been split into smaller images of size 500x500x3 pixels.
2) The files have been transformed to .jpgs to reduce the cost on storage and to make it easier to work with.

**Where can I find the data?** 
