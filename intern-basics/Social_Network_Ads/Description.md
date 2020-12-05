# Social Network ads

Machine Learning technology in social media allows machines to decide which advertisements are to be shown to which audience. They collect data from 
users, analyze it, find out their preferences and accordingly show advertisements which hold their interest


So, in this projet we aim, to get an idea as which customer or how many customers will buy an item like a car, if we advertise our item (i.e. car in this case).
The data is collected of how many customers bought the car, and how many did not.
Along with this information of buying the car and not buying the car, Age and estimated salary of the customer is also collected.

So, in this case, we consider two parameters as the basis to predict whether a customer will buy a car or not, and those two parameters are -

1. Age 
1. Estimated Salary

So, first we import few python libraries and import the dataset.
Then we split the dataset into train and test.

Now, because we will be using kernal SVM, therefore, we need to scale our parameters; as the range of all features should be normalized so that each feature contributes approximately proportionately to the final distance.

After feature scaling we apply our model on the dataset, and predict the outcomes.

