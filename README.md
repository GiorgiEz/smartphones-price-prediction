# Smartphone Price Prediction Project

## Overview
This project aims to analyze and predict smartphone prices based on various features such as brand, specifications, and other characteristics. By leveraging machine learning models, we hope to gain insights into the factors influencing smartphone pricing.

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset Description](#dataset-description)
3. [Project Objectives](#project-objectives)
4. [Setup and Installation](#setup-and-installation)
5. [Data Preprocessing](#data-preprocessing)
6. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
7. [Model Training and Evaluation](#model-training-and-evaluation)
8. [Results](#results)
9. [Future Work](#future-work)

## Introduction
With the growing demand for smartphones, understanding pricing strategies is critical for manufacturers and retailers. This project utilizes machine learning models to predict smartphone prices based on various specifications and features provided in a dataset of 980 smartphones.

## Dataset Description
The original dataset can be found here: https://www.kaggle.com/datasets/abhijitdahatonde/real-world-smartphones-dataset

The dataset contains 980 rows and 22 columns, capturing various attributes of smartphones, including:
- **brand_name**: The manufacturer’s name.
- **model**: The specific model of the smartphone.
- **price**: The price of the smartphone in INR.
- **avg_rating**: The average customer rating.
- **5g_or_not**: A Boolean value representing if the phone has 5G support or not.
- **processor_brand**: The brand of the processor used in the smartphone.
- **num_cores**: The number of cores in the smartphone's processor.
- **processor_speed**: The clock speed of the processor in GHz.
- **battery_capacity**: The battery capacity of the smartphone in mAh.
- **fast_charging_available**: Indicates whether the phone supports fast charging (1 for yes, 0 for no).
- **fast_charging**: The wattage of the fast charging feature (if available).
- **ram_capacity**: The amount of RAM in GB.
- **internal_memory**: The internal storage capacity of the smartphone in GB.
- **screen_size**: The diagonal screen size in inches.
- **refresh_rate**: The screen refresh rate in Hz.
- **num_rear_cameras**: The number of rear cameras on the smartphone.
- **os**: The operating system of the smartphone (e.g., Android, iOS).
- **primary_camera_rear**: The resolution of the primary rear camera in megapixels.
- **primary_camera_front**: The resolution of the front camera in megapixels.
- **extended_memory_available**: Indicates whether the phone supports expandable storage (1 for yes, 0 for no).
- **resolution_height**: The height of the screen resolution in pixels.
- **resolution_width**: The width of the screen resolution in pixels.

## Project Objectives
1. **Data Preprocessing**: Clean and preprocess the dataset to handle missing values, outliers, and categorical data.
2. **Exploratory Data Analysis (EDA)**: Visualize and analyze the relationships between features and target variables.
3. **Model Training**: Train machine learning models to predict smartphone price.
4. **Model Evaluation**: Compare the performance of different models and identify the most effective ones.

## Setup and Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/username/smartphone-ml-project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd smartphone-ml-project
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Data Preprocessing
- Handle missing values in columns such as `fast_charging_available`.
- Encode categorical features like `brand_name` and `os` using one-hot encoding.
- Scale continuous variables (e.g., `processor_speed`, `battery_capacity`) to standardize the dataset.
- Split the dataset into training and testing subsets for model training and evaluation.

## Exploratory Data Analysis (EDA)
- Visualize feature distributions (e.g., `price`).
- Analyze relationships between features and target variables (e.g., correlation heatmaps).
- Identify patterns and trends in smartphone specifications.

## Model Training and Evaluation
**Models to be included:**
- Regression Models for Price Prediction

Details of models trained, hyperparameters used, and evaluation metrics will be added here.

## Results
Summarize the findings and performance of the machine learning models. Include key insights and visualizations.

## Future Work
- Expand the dataset with more recent smartphone data.
- Integrate additional features such as market demand or customer reviews.
- Explore advanced models for improved prediction accuracy.

