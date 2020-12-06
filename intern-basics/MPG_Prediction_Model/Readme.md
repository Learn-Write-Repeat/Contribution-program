# MPG Prediction Model

This prediction model shows the different factors that affect vehicle mileage. By considering those factors we can predict the miles per Gallon of a vehicle.

To make a prediction model first we have to collect the data. This data set is found in the [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Auto+MPG).
The attributes given in the dataset are 
1. mpg: continuous
2. cylinders: multi-valued discrete
3. displacement: continuous
4. horsepower: continuous
5. weight: continuous
6. acceleration: continuous
7. model year: multi-valued discrete
8. origin: multi-valued discrete
9. car name: string (unique for each instance)

By considering all other attributes we have to predict the mpg value.

In the notebook, you can see that we have compared different models and pick the best model as our prediction model and store the model values in the model.bin folder.
