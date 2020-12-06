# Stock Market Analysis & Prediction
In this project, we used some algorithm to forecast stock market prices for NSE India stock market. Main goal is to compare various algorithms and evaluate models by comparing prediction accuracy. We examined different models - Random Forest, Linear Regression and ARIMA based on the accuracy (RMSE) and predicted the price of different industries.

## Content
A data frame with 8 variables: index, date, time, open, high, low, close and id. For each year from 2013 to 2016, the number of trading data of each minute of given each date. The currency of the price is Indian Rupee (INR).

* Code : market id
* Date : numerical value (Ex. 20151203- to be converted as 2015-12-03)
* Time : factor (Ex. 09:16)
* Open : numeric (opening price)
* High : numeric (high price)
* Low : numeric (low price)
* Close : numeric (closing price)
* Volume : numeric (total volume traded)

## Implementation

Dataset:   
Dataset can be found [here](https://www.kaggle.com/ramamet4/nse-company-stocks).

Code file:   
[Code for Random Forest & Linear Regression](https://github.com/shalakasaraogi/Contribution-program/blob/master/intern-basics/Stock%20Market%20Analysis%20and%20Prediction/Stock_Market_Prediction-%20(Random%20Forest%20%26%20Linear%20Regression).ipynb)  
[Code for ARIMA](https://github.com/shalakasaraogi/Contribution-program/blob/master/intern-basics/Stock%20Market%20Analysis%20and%20Prediction/Stock_Market_Prediction-%20(ARIMA).ipynb)


## Prediction

We have used following algorithm for time series analysis:

* Random Forest
* Linear Regression
* Autoregressive Integrated Moving Average (ARIMA)

## Conclusion

We have compared algorithms by RMSE. We found that ARIMA model gave lowest RMSE and accurate prediction. 
