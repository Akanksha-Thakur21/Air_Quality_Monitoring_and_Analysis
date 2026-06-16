# Air Quality Monitoring and Analysis in Major Indian Cities

## Overview
This project was developed as part of my Data Analytics Internship at DevElet. The objective of this project is to analyze air quality data from major Indian cities, identify pollution trends, clean missing data, and visualize Air Quality Index (AQI) patterns using Python.

## Project Objectives
- Analyze air quality levels across different Indian cities.
- Handle missing and incomplete AQI data.
- Compare average AQI values between cities.
- Identify the most polluted cities based on AQI.
- Visualize air quality trends using graphs.

## Dataset
The dataset contains air quality measurements of major Indian cities, including pollutants such as:

- PM2.5
- PM10
- NO
- NO₂
- NOx
- NH₃
- CO
- SO₂
- O₃
- Benzene
- Toluene
- Xylene
- AQI
- AQI Bucket

## Technologies Used
- Python
- Pandas
- Matplotlib
- CSV Dataset Handling

## Project Workflow

### 1. Data Collection
- Imported the air quality dataset (`city_day.csv`).

### 2. Data Cleaning
- Checked dataset dimensions and missing values.
- Removed duplicate records.
- Filled missing numerical values using the mean of each column.
- Filled missing AQI categories using the mode (most frequent category).
- Saved the cleaned dataset as `cleaned_air_quality.csv`.

### 3. Data Analysis
- Generated statistical summaries of air pollution data.
- Calculated the average AQI of each city.
- Ranked cities based on their average pollution levels.

### 4. Data Visualization
Created visualizations including:
- Average AQI comparison among cities.
- AQI distribution histogram.
- Top 10 most polluted cities based on average AQI.

## Key Insights
- Cities with higher average AQI indicate more severe pollution levels.
- AQI distribution provides an understanding of pollution frequency.
- The top 10 polluted cities highlight areas requiring greater pollution control measures.


---

## 🙏 Acknowledgement
This project was completed as part of my Data Analytics Internship at **DevElet**, under the guidance and support of **Kishan Tiwari**.
