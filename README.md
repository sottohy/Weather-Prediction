# Weather prediction model using Machine Learning

## Regression model for tomorrow's weather in Alexandria, Egypt based on historical weather data

The data was obtained from the NOAA website https://www.ncdc.noaa.gov/cdo-web/ and the csv file is uploaded here. The uploaded data is obtained from multiple stations accross Egypt from 1993 to 2019. 

## Loading, Cleaning, and Prepping the data
The original data contained 111211 records from multiple stations accross egypt with 5 columns (features). The Snow and the Precipitation columns were dropped since their values were missing in most of the records. The remaining rows with missing values were dropped since they were less than 20% of the records, leaving us with 81758 rows. 

The next step was to focus only on one area or station to get accurate results. Therefore, all rows with stations that are not "Alexandria" were dropped, leaving us with 5064 rows.

A target column was then created, where each record (day) had the tmax of the following record, and the very last target record had the same value as the one above it. 

## Training the model
We first define a list of columns to exclude from the predictors and create a list of predictors by excluding these columns from the weather dataset. We then perform the backtesting by creating a function that iterates over the dataset with a start value of 3650 (10 years) and a step size of 90. For each iteration, we train the model on the data up to the current index and make predictions for the next 90 days. The difference between the predicted and actual values for each prediction was calculated and stored in a list. 

## Making Predictions
The backTest function is used to generate predictions for the weather using a Ridge regression model and the predictors we defined earlier. The mean absolute error between the actual and predicted values was 3.2 degrees.

![download (2)](https://github.com/sottohy/Weather-Prediction/assets/91037437/9d00c822-2760-4f9e-a0f3-b32cc12154ba)

## Creating the Website
The website was created using HTML,CSS, and connected to the model using Flask.

https://github.com/sottohy/Weather-Prediction/assets/91037437/2b0e2fb9-e0ce-4076-a368-f937f8632c24



