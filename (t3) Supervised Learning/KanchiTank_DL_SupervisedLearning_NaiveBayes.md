# NAIVE BAYES CLASSIFIER

## What is a Classifier?

<img src = "https://raw.githubusercontent.com/kanchitank/Contribution-program/master/(t3)%20Supervised%20Learning/images/Naive_Bayes/1.jpg" width="60%"> 

A **classifier** is a **machine learning model** that is used to discriminate different objects based on certain features.

## Principle of Naive Bayes Classifier

A **Naive Bayes classifier** is a probabilistic machine learning model that’s used for classification task. The crux of the classifier is based on the Bayes theorem.

## Bayes Theorem

<img src = "https://raw.githubusercontent.com/kanchitank/Contribution-program/master/(t3)%20Supervised%20Learning/images/Naive_Bayes/2.png" width="60%"> 

Using **Bayes theorem**, we can find the **probability** of **A** happening, given that **B** has occurred. Here, **B** is the **evidence** and **A** is the **hypothesis**.<br>
The assumption made here is that the predictors/features are independent. That is presence of one particular feature does not affect the other. <br>
Hence it is called **naive**. <br>

### Example:
Let us take an example to get some better intuition. Consider the problem of playing golf. The dataset is represented as below.

<img src = "https://raw.githubusercontent.com/kanchitank/Contribution-program/master/(t3)%20Supervised%20Learning/images/Naive_Bayes/3.png" width="60%"> 

We **classify whether the day is suitable for playing golf**, given the features of the day. <br> 
The **columns represent these features** and the **rows represent individual entries**. <br>
If we take the first row of the dataset, we can observe that is not suitable for playing golf if the outlook is rainy, temperature is hot, humidity is high and it is not windy. <br>
We make two assumptions here:
- One as stated above we consider that these **predictors are independent**. That is, if the temperature is hot, it does not necessarily mean that the humidity is high. 
- Another assumption made here is that **all the predictors have an equal effect on the outcome**. That is, the day being windy does not have more importance in deciding to play golf or not.

According to this example, Bayes theorem can be rewritten as:

<img src = "https://raw.githubusercontent.com/kanchitank/Contribution-program/master/(t3)%20Supervised%20Learning/images/Naive_Bayes/4.png">

The variable **y is the class variable(play golf)**, which represents if it is suitable to play golf or not given the conditions. Variable **X represent the parameters/features**.

## Types of Naive Bayes Classifier

- **Multinomial Naive Bayes:** <br>
This is mostly used for **document classification problem**, i.e whether a document belongs to the category of sports, politics, technology etc. The features/predictors used by the classifier are the **frequency** of the words present in the document.

- **Bernoulli Naive Bayes:** <br>
This is similar to the multinomial naive bayes but the predictors are **boolean variables**. The parameters that we use to predict the class variable take up only values yes or no, for example if a word occurs in the text or not.

- **Gaussian Naive Bayes:** <br>
When characteristic values are **continuous** in nature then an assumption is made that the values linked with each class are dispersed according to Gaussian that is **Normal Distribution**.

<img src = "https://raw.githubusercontent.com/kanchitank/Contribution-program/master/(t3)%20Supervised%20Learning/images/Naive_Bayes/6.png" width="60%"> 

## Data Preparation For Naive Bayes

<img src = "https://raw.githubusercontent.com/kanchitank/Contribution-program/master/(t3)%20Supervised%20Learning/images/Naive_Bayes/8.jpg" width="60%"> 

- **Categorical Inputs:** <br>
Naive Bayes assumes label attributes such as binary, categorical or nominal.
- **Gaussian Inputs:** <br>
If the input variables are real-valued, a Gaussian distribution is assumed. In which case the algorithm will perform better if the univariate distributions of your data are Gaussian or near-Gaussian. This may require removing outliers (e.g. values that are more than 3 or 4 standard deviations from the mean).
- **Classification Problems:** <br>
Naive Bayes is a classification algorithm suitable for binary and multiclass classification.
- **Log Probabilities:** <br>
The calculation of the likelihood of different class values involves multiplying a lot of small numbers together. This can lead to an underflow of numerical precision. As such it is good practice to use a log transform of the probabilities to avoid this underflow.
- **Kernel Functions:** <br>
Rather than assuming a Gaussian distribution for numerical input values, more complex distributions can be used such as a variety of kernel density functions.
- **Update Probabilities:** <br>
When new data becomes available, you can simply update the probabilities of your model. This can be helpful if the data changes frequently.

## Applications of Naive Bayes Algorithms

<img src = "https://raw.githubusercontent.com/kanchitank/Contribution-program/master/(t3)%20Supervised%20Learning/images/Naive_Bayes/7.jpeg" width="60%"> 

- **Real time Prediction:** <br>
Naive Bayes is an eager learning classifier and it is sure fast. Thus, it could be used for **making predictions in real time**.
- **Multi class Prediction:** <br>
This algorithm is also well known for **multi class prediction feature**. Here we can **predict the probability of multiple classes of target variable**.
- **Text classification/ Spam Filtering/ Sentiment Analysis:** <br>
Naive Bayes classifiers mostly used in **text classification** (due to better result in multi class problems and independence rule) have higher success rate as compared to other algorithms. As a result, it is widely used in **Spam filtering** (identify spam e-mail) and **Sentiment Analysis** (in social media analysis, to identify positive and negative customer sentiments)
- **Recommendation System:** <br>
Naive Bayes Classifier and Collaborative Filtering together builds a **Recommendation System** that uses machine learning and data mining techniques to filter unseen information and predict whether a user would like a given resource or not.

## What are the Advantages and Disadvantages of Naive Bayes Classifier?

### Advantages
- When the assumption of independent predictors holds true, a Naive Bayes classifier performs better as compared to other models. If the Naive Bayes conditional independence assumption holds, then it will converge quicker than discriminative models like logistic regression.
- Naive Bayes **requires a small amount of training data** to estimate the test data. So the training period takes less time.
- Very **simple**, **easy to implement**, and **fast**. It can make probabilistic predictions.
- It is **highly scalable**. It scales linearly with the number of predictor features and data points.
- Can be **used for both binary and multi-class classification problems**.
- Handles **continuous and discrete data** and is not sensitive to irrelevant features. <br>

<img src = "https://raw.githubusercontent.com/kanchitank/Contribution-program/master/(t3)%20Supervised%20Learning/images/Naive_Bayes/5.jpeg" width="40%"> 

### Disadvantages
- The main limitation of Naive Bayes is the **assumption of independent predictor features**. Naive Bayes implicitly assumes that all the attributes are mutually independent. In real life, it’s almost impossible that we get a set of predictors that are completely independent or one another.
- If a categorical variable has a category in the test dataset, which was not observed in training dataset, then the model will assign a 0 (zero) probability and will be unable to make a prediction. This is often known as **Zero Frequency**. To solve this, we can use a **smoothing technique**. 
