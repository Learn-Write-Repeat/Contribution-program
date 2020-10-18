# Hyper-parameter Tuning of Machine Learning (ML) Models  

![Header](https://github.com/shalakasaraogi/Contribution-program/blob/master/(t2)%20Deep%20Learning%20Computations/Shalaka_DL_DLComputations/Extras/title.jpg)

When creating a machine learning model, we will be presented with design choices as how to define our model architecture. Often times, we don’t immediately know what the optimal model architecture should be for a given model which result us to explore a range of possibilities. In true machine learning fashion, we will ideally ask the machine to perform this exploration and select the optimal model architecture automatically. 

## What are Hyper-parameters?  

**W**ikipedia states that `“hyperparameter tuning is choosing a set of optimal hyperparameters for a learning algorithm”`. So what is a [hyperparameter](https://en.wikipedia.org/wiki/Hyperparameter_(machine_learning))?

Parameters which define the model architecture are referred to as **Hyper-parameters** and thus this process of searching for the ideal model architecture is referred to as **Hyperparameter Tuning**. 

Two types of parameters exist in machine learning models: one that can be initialized and updated through the data learning process (*e.g. the weights of neurons in neural networks, number of epochs, activation function*), named **Model-parameters**; while other named **Hyper-parameters**, cannot be directly estimated from data learning and must be set before training a Machine learning model because they define the architecture of a machine learning model.  

![model vs hyper](https://github.com/shalakasaraogi/Contribution-program/blob/master/(t2)%20Deep%20Learning%20Computations/Shalaka_DL_DLComputations/Extras/model%20vs.png)

To fit a machine learning model into different problems, its hyper-parameters must be tuned. Selecting the best hyper-parameter configuration for machine learning models has a direct impact on the model’s performance i.e on accuracy and efficiency while training the model. Therefore it needed to be set accurately to get better and efficient results.

> *"A good choice of hyperparameters can really make an algorithm shine"*

### Why are Hyper-parameters essential?

•	 It reduces the human effort required, since many ML developers spend considerable time tuning the hyper-parameters, especially for a large datasets or complex ML algorithms with a large number of hyper-parameters.  

•	 It Improves the performance of ML models. Many ML hyper-parameters have different optimum to achieve best performance in different datasets or problems.

•	 It makes the models and research more reproducible. Only when the same level of hyper-parameter tuning process is implemented can different ML algorithms be compared fairly; hence using a same Hyper-parameter tuning method on different ML algorithms also helps to determine the most suitable ML model for a specific problem.

Let's see some exhaustive search methods or algorithms to optimize the hyper-parameters.

### Some Hyper-parameters tuning algorithms:

**Grid search-**

Grid search is a traditional way to perform hyperparameter optimization.  Grid search is a decision-theoretic approach that involves exhaustively searching for a fixed domain of hyperparameter values.  It trains the algorithm for all combinations by using the two set of hyperparameters (learning rate and number of layers) and measures the performance using “Cross Validation” technique. This validation technique gives assurance that our trained model got most of the patterns from the dataset. One of the best methods to do validation by using “K-Fold Cross Validation” which helps to provide ample data for training the model and ample data for validations.

The Grid search method is a simpler algorithm to use but it suffers if data have high dimensional space called the curse of dimensionality.

**Random Search-**

Randomly samples the search space and evaluates sets from a specified probability distribution. For example, Instead of trying to check all 100,000 samples, we can check 1000 random parameters. The drawback of using the random search algorithm, however, it doesn’t use information from prior experiments to select the next set and also it is very difficult to predict the next of experiments.

![grid-vs-random](https://github.com/shalakasaraogi/Contribution-program/blob/master/(t2)%20Deep%20Learning%20Computations/Shalaka_DL_DLComputations/Extras/Untitled%20design.jpg)

**Bayesian Optimization-**

Bayesian optimization is an iterative algorithm that is popularly used for Hyper-parameter problems. Unlike Grid Search and Random Search, it determines the future
evaluation points based on the previously-obtained results. To determine the next hyper-parameter configuration, Bayesian Optimization uses two key components: a surrogate model and an acquisition function.

**Bayesian Optimization with Gaussian Processes (BO-GP)-**  

Gaussian process (GP) is a standard surrogate model for objective function modeling in Bayesian Optimization. A Gaussian process defines the prior distribution over functions which can be converted into a posterior over functions once we have seen some data. The Gaussian process uses Covariance matrix to ensure that values that are close together. The covariance matrix along with a mean µ function to output the expected value ƒ(x) defines a Gaussian process.

1. Gaussian process will be used as a prior for Bayesian inference
2. To computing the posterior is that it can be used to make predictions for unseen test cases.

![gaussian-prior](https://github.com/shalakasaraogi/Contribution-program/blob/master/(t2)%20Deep%20Learning%20Computations/Shalaka_DL_DLComputations/Extras/GP-prior.png)

Figure: Gaussian Process prior distribution → [Source](http://katbailey.github.io/post/gaussian-processes-for-dummies/)

![guassian-posterior](https://github.com/shalakasaraogi/Contribution-program/blob/master/(t2)%20Deep%20Learning%20Computations/Shalaka_DL_DLComputations/Extras/GP-posteior.png)

Figure: Gaussian Process posterior distribution by applying covariance matrix → [Source](http://katbailey.github.io/post/gaussian-processes-for-dummies/)

**Bayesian Optimization with Tree-structured Parzen Estimator (BO-TPE)-**  

Tree-structured Parzen estimator (TPE) is another common surrogate model for Bayesian Optimization. Instead of defining a predictive distribution used in BO-GP, BO-TPE creates two density functions, l(x) and g(x), to act as the generative models for all domain variables. To apply TPE, the observation results are divided into good results and poor results by a pre-defined percentile y∗, and the two sets of results are modeled by simple Parzen windows:  

![equation](https://github.com/shalakasaraogi/Contribution-program/blob/master/(t2)%20Deep%20Learning%20Computations/Shalaka_DL_DLComputations/Extras/equation.png)

### Some Advantages & Disadvantages of Hyper-parameter Tuning Algorithms:

|Sr.No.| Hyper-parameter Tuning Algorithms | Advantages | Disadvantages|
|------|-----------------------------------|--------------|----------------|
|1.    | Grid Search | Simple to implement| Time Consuming,<br>Efficient only for categorical hyper-parameters |
|2.    | Random Search | More efficient as compare to Grid Search | Require subsets with small budgets to be representative,<br> Not efficient with conditional hyper-parameters |
|3.    | Bayesian Optimization with Gaussian Processes (BO-GP)  | Fast convergence speed for continuous hyper-parameters  | Poor capacity for parallelization,<br> Not efficient with conditional hyper-parameters |
|4.    | Bayesian Optimization with Tree-structured Parzen Estimator (BO-TPE)  | Efficient for all types of hyper-parameters,<br> Keep conditional dependencies | Poor capacity for parallelization |
  
 
---

## Implementation
The sample code for Hyper-parameter tuning of ML models (both for regression & classification problems) is provided in this repository. 

### 1] Sample Code-
**Sample code for Regression Problems**

`Dataset Used:` [Bouston Housing Dataset](https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html)

`Code:` [Shalaka_DL_DLComputations_HPTRegression.ipynb](https://github.com/shalakasaraogi/Contribution-program/blob/master/(t2)%20Deep%20Learning%20Computations/Shalaka_DL_DLComputations/Shalaka_DL_DLComputations_HPTRegression.ipynb)  

`Performance Metric Used:` Mean Square Error (MSE)  


**Sample Code for Classification Problems**  

`Dataset Used:` [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)  

`Code:`  [Shalaka_DL_DLComputations_HPTClassification.ipynb](https://github.com/shalakasaraogi/Contribution-program/blob/master/(t2)%20Deep%20Learning%20Computations/Shalaka_DL_DLComputations/Shalaka_DL_DLComputations_HPTClassification.ipynb)  

`Performance Metric Used:` Classification Accuracy

### 2] Machine Learning/Deep Learning Algorithms Used- 
```
• Random Forest (RF)  
• Support Vector Machine (SVM)  
• K-Nearest Neighbor (KNN)  
• Artificial Neural Network (ANN) 
```

### 3] Hyper-parameter Tuning Algorithms Used-  
```
• Grid search  
• Random Search  
• Bayesian Optimization with Gaussian Processes (BO-GP)  
• Bayesian Optimization with Tree-structured Parzen Estimator (BO-TPE)  
```
---

## Reference 

```
Research Paper Title - On hyperparameter optimization of machine learning algorithms: Theory and practice
Authors- L. Yang and A. Shami
Journal- Neurocomputing
Volume- 415
Page- 295–316
Year- 2020
DOI- https://doi.org/10.1016/j.neucom.2020.07.061
```
---

<p>
  <h6>Created/Written By - Shalaka Saraogi | Thanks to Team members: Roja TV & Sagar Raj Roul | Mentor: Kumari Neha | Open Source Contribution with DevIncept<br>
  Find me here:</h6>  
  <a href="https://github.com/shalakasaraogi"><img src="https://img.shields.io/badge/GitHub--_.svg?style=social&logo=github" alt="GitHub"></a>     
  <a href="https://www.linkedin.com/in/shalaka-saraogi"> <img src="https://img.shields.io/badge/LinkedIn--_.svg?style=social&logo=linkedin" alt="LinkedIn"></a>      
  <a href="mailto:shalakasaraogi@gmail.com"> <img src="https://img.shields.io/badge/Gmail--_.svg?style=social&logo=gmail" title="shalakasaraogi@gmail.com"></a>     
</p> 
 
---
