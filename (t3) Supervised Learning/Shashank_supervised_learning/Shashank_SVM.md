# Support Vector Machines
***Introduction***
* SVM offers very high accuracy compared to other classifiers such as logistic regression, and decision trees.
  It is known for its kernel trick to handle nonlinear input spaces.
  It is used in a variety of applications such as face detection, intrusion detection, classification of emails,
  news articles and web pages, classification of genes, and handwriting recognition.
  SVM is an exciting algorithm and the concepts are relatively simple.
  The classifier separates data points using a hyperplane with the largest amount of margin.
  That's why an SVM classifier is also known as a discriminative classifier. SVM finds an optimal hyperplane which helps in classifying new data points
  
 #### In this file, we are going to cover following topics:
  
 * Support Vector Machines
 *	How does it work?
 *	Kernels
 *	Classifier building in Scikit-learn
 *	Tuning Hyperparameters
 *	Advantages and Disadvantages
  
## What is Support Vector Machine

* Generally, Support Vector Machines is considered to be a classification approach, it but can be employed in both types of classification and regression problems.
  It can easily handle multiple continuous and categorical variables. SVM constructs a hyperplane in multidimensional space to separate different classes.
  SVM generates optimal hyperplane in an iterative manner, which is used to minimize an error.
  The core idea of SVM is to find a maximum marginal hyperplane(MMH) that best divides the dataset into classes.
  
* Support Vectors
    Support vectors are the data points, which are closest to the hyperplane. These points will define the separating line better by calculating margins.
    These points are more relevant to the construction of the classifier.
    
* Hyperplane
   A hyperplane is a decision plane which separates between a set of objects having different class memberships.
   
* Margin
  A margin is a gap between the two lines on the closest class points. This is calculated as the perpendicular distance from the line to support vectors or
  closest points. If the margin is larger in between the classes, then it is considered a good margin, a smaller margin is a bad margin.
  
## How does SVM work?

 * The main objective is to segregate the given dataset in the best possible way. The distance between the either nearest points is known as the margin.
   The objective is to select a hyperplane with the maximum possible margin between support vectors in the given dataset. SVM searches for the maximum
   marginal hyperplane in the following steps:
1. Generate hyperplanes which segregates the classes in the best way. Left-hand side figure showing three hyperplanes black, blue and orange.
    Here, the blue and orange have higher classification error, but the black is separating the two classes correctly.
2. Select the right hyperplane with the maximum segregation from the either nearest data points

## SVM Kernels

* The SVM algorithm is implemented in practice using a kernel. A kernel transforms an input data space into the required form. SVM uses a technique called the kernel trick.
  Here, the kernel takes a low-dimensional input space and transforms it into a higher dimensional space.
  
* In other words, you can say that it converts nonseparable problem to separable problems by adding more dimension to it. It is most useful in non-linear separation problem.
  Kernel trick helps you to build a more accurate classifier.
  
1. ***Linear Kernel*** A linear kernel can be used as normal dot product any two given observations. 
  The product between two vectors is the sum of the multiplication of each pair of input values.
                  K(x, xi) = sum(x * xi)  
2. ***Polynomial Kernel*** A polynomial kernel is a more generalized form of the linear kernel. The polynomial kernel can distinguish curved or nonlinear input space.
                                   K(x,xi) = 1 + sum(x * xi)^d
   Where d is the degree of the polynomial. d=1 is similar to the linear transformation. The degree needs to be manually specified in the learning algorithm.
   
3. ***Radial Basis Function Kernel*** The Radial basis function kernel is a popular kernel function commonly used in support vector machine classification. 
   RBF can map an input space in infinite dimensional space.
                                          K(x,xi) = exp(-gamma * sum((x – xi^2))
   Here gamma is a parameter, which ranges from 0 to 1. A higher value of gamma will perfectly fit the training dataset, which causes over-fitting.
   Gamma=0.1 is considered to be a good default value. The value of gamma needs to be manually specified in the learning algorithm.  
 
 ## Classifier Building in Scikit-learn
 
* Until now, you have learned about the theoretical background of SVM. Now you will learn about its implementation in Python using scikit-learn.

* In the model the building part, you can use the cancer dataset, which is a very famous multi-class classification problem. This dataset is computed
  from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image.

* The dataset comprises 30 features (mean radius, mean texture, mean perimeter, mean area, mean smoothness, mean compactness, mean concavity, mean concave points,
  mean symmetry, mean fractal dimension, radius error, texture error, perimeter error, area error, smoothness error, compactness error, concavity error, concave
  points error, symmetry error, fractal dimension error, worst radius, worst texture, worst perimeter, worst area, worst smoothness, worst compactness, worst concavity,
  worst concave points, worst symmetry, and worst fractal dimension) and a target (type of cancer).
  
* Tuning Hyperparameters

1. Kernel: The main function of the kernel is to transform the given dataset input data into the required form. There are various types of functions such as linear, polynomial,
   and radial basis function (RBF). Polynomial and RBF are useful for non-linear hyperplane. Polynomial and RBF kernels compute the separation line in the higher dimension. In
   some of the applications, it is suggested to use a more complex kernel to separate the classes that are curved or nonlinear. This transformation can lead to more accurate
   classifiers.

2. Regularization: Regularization parameter in python's Scikit-learn C parameter used to maintain regularization. Here C is the penalty parameter, which represents
   misclassification or error term. The misclassification or error term tells the SVM optimization how much error is bearable. This is how you can control the trade-off between
   decision boundary and misclassification term. A smaller value of C creates a small-margin hyperplane and a larger value of C creates a larger-margin hyperplane.

3. Gamma: A lower value of Gamma will loosely fit the training dataset, whereas a higher value of gamma will exactly fit the training dataset, which causes over-fitting. In
   other words, you can say a low value of gamma considers only nearby points in calculating the separation line, while the a value of gamma considers all the data points in the
   calculation of the separation line.


* Advantages
  SVM Classifiers offer good accuracy and perform faster prediction compared to Naïve Bayes algorithm. They also use less memory because they use a subset of
  training points in the decision phase. SVM works well with a clear margin of separation and with high dimensional space.

* Disadvantages
  SVM is not suitable for large datasets because of its high training time and it also takes more time in training compared to Naïve Bayes. It works poorly
  with overlapping classes and is also sensitive to the type of kernel used.
 
