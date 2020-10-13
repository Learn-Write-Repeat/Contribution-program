# Machine Learning Models Using Flask
### Why Flask?
- Easy to use.
- Built in development server and debugger.
- Integrated unit testing support.
- RESTful request dispatching.
- Extensively documented.
### Algorithm Used:
  - I will be using linear regression to predict the sales value in the third month using rate of interest and sales of the first two months.
### Dataset Used:
  - I created a custom sales [dataset](https://github.com/anillko1108/Contribution-program/blob/master/ML_models_Flask/Anil%20Kumar%20Mishra%20AI/sales.csv) for this project which has four columns — rate of interest, sales in first month, sales in second month and sales in third month.
### Project Structure
This Project has 4 parts:
  - model.py — This contains code for the machine learning model to predict sales in the third month based on the sales in the first two months.
  - app.py — This contains Flask APIs that receives sales details through GUI or API calls, computes the predicted value based on our model and returns it.
  - request.py — This uses requests module to call APIs defined in app.py and displays the returned value.
  - HTML/CSS — This contains the HTML template and CSS styling to allow user to enter sales detail and displays the predicted sales in the third month.
### Results:
![](https://github.com/anillko1108/Contribution-program/blob/master/ML_models_Flask/Anil%20Kumar%20Mishra%20AI/result.png)
#### Conclusion:
  - I used linear regression to predict sales value in the third month using rate of interest and sales in first two months. 
