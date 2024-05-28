# Weather prediction model using Machine Learning

This project predicts the maximum temperature (TMAX) for the next day using historical weather data. The model is built using ridge regression and evaluated using backtesting to account for the time series nature of the data.


## Project Overview
This project utilizes historical weather data to predict the maximum temperature of the following day. The dataset is cleaned, preprocessed, and a ridge regression model is trained. The model is evaluated using backtesting to simulate how it would perform in a real-world scenario.

## Data Description
The data was obtained from the NOAA website https://www.ncdc.noaa.gov/cdo-web/ and the csv file is uploaded here. The uploaded data is obtained from multiple stations accross Egypt from 1993 to 2019.

It contains daily weather observations, including features such as temperature, precipitation, and snow depth. The dataset is indexed by date and includes the following key columns:
- TMAX: Maximum temperature
- TMIN: Minimum temperature
- NAME: Station name
- STATION: Station identifier


## Dependencies
The project requires the following libraries:

- pandas
- scikit-learn
- pickle


## Data Preprocessing
- Loading Data: The weather data is loaded from a CSV file and the date column is set as the index.
- Handling Missing Values: Columns with a high percentage of missing values are dropped. Remaining missing values are handled by dropping rows with missing values.
- Filtering Data: The dataset is filtered to include only data from a specific weather station.
- Index Conversion: The date index is converted to a datetime type.
- Target Column Creation: A target column is created by shifting the TMAX values by one day to represent the next day's maximum temperature


## Modeling
### Backtesting
Backtesting is used to evaluate the model on time series data:

- Training and Testing: The model is trained on a rolling basis, using 10 years of historical data and making predictions for the next 90 days.
- Predictions: Predictions are made for 90-day intervals and compared with actual values.


### Model Evaluation
- Model: A ridge regression model is used with a specified alpha value.
- Predictors: All columns except the target, station name, and station identifier are used as predictors.
- Evaluation Metric: Mean Absolute Error (MAE) is used to evaluate the model's performance.

### Results
- The mean absolute error between the actual and predicted maximum temperatures is calculated.
- The distribution of prediction errors is visualized using a plot.

![download (2)](https://github.com/sottohy/Weather-Prediction/assets/91037437/9d00c822-2760-4f9e-a0f3-b32cc12154ba)


## Usage
To run this project, follow these steps:

1. Install all depencies.
2. Load the dataset from the specified path.
3. Execute the notebook to preprocess the data, train the model, and evaluate its performance.
4. The trained model is saved using pickle for future use.


## Creating the Website
The website was created using HTML, CSS, and connected to the model using Flask.

https://github.com/sottohy/Weather-Prediction/assets/91037437/62acb41e-2740-4803-98f6-59a6abd43d43

