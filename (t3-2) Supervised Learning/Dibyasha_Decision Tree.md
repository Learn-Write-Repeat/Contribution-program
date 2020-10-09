# Decision Tree Algorithm :thinking:

Before going down to the topic, lets learn about **Machine Learning**:
## What is Machine Learning? :confused:
<br>As per the name Machine(Computers) learn about the data. They apply tools, techniques and algorithms to study(Learning) the patterns hidden in the data to make accurate predictions and deliver the output to the users.
<br>To learn from the data, there are various ways or types.
### Types of Machine Learning: :shushing_face:
1)**Supervised Learning**: 
The basic idea that goes with is that there is a teacher or supervisor who guides the whole process, Similarly, here we train the machine with labeled to predict the outcome for a newly unseen data. Labeled data means data is already paired with some correct answers.
<br>2) **Unsupervised Learning**:
Here, we do not train the machine rather we leave the machine to study on its own and discover the hidden patterns in the data. Unsupervised Learning deals with unlabeled data. 

<br>As mentioned above machine apply some algorithms to study the data, these two types of learning have some algorithms. So, we are here today to learn about **Decision Tree Algorithm** which is a supervised learning.

## Decision Tree Algorithm :deciduous_tree:
<br>The **Decision Tree Algorithm** is similar to the if-else statements in looping. Decision Tree is the graphical representation of answers to our own problems which we come across daily in our life based upon some conditions.

## Example of Decision Tree:
<img src="images/pic2.png">

In this example, we want to predict whether a person is fit or unfit with the information provided about their age, eating habits, physical activity, etc. The parent node is the question about his age 'Age < 30?'.The internal nodes are the questions like ‘Does he exercise?’, ‘Does he eat a lot of pizzas’? And the leaves represent outcomes like either ‘fit’, or ‘unfit’.
## Types of Decision Trees:
**1)Classification Trees**:
<br>The above example is an example of Classification Tree. The outcome variables 'fit' or 'unfit'are the Categorical Variables.
The tree is built through a process called binary recursive partitioning which is an iterative process of splitting the data into partitions, and then splitting it up further on each of the branches.

<img src="images/pic3.png">

**2)Regression Trees**:
<br>In this type of decision trees the target variable can take continuous values or real numbers. Examples:the price of a house, or a patient’s length of stay in a hospital.

<img src="images/pic4.png">

## Creation of Decision Tree:
The basic algorithm used in decision trees is known as the ID3 algorithm which uses a top-down, greedy approach.
<br>**Steps of the Algorithms**:
<br>1)Select the best attribute → A 
<br>2)Assign A as the decision attribute (test case) for the NODE. 
<br>3)For each value of A, create a new descendant of the NODE.
<br>4)Sort the training examples to the appropriate descendant node leaf. 
<br>5)If examples are perfectly classified, then STOP else iterate over the new leaf nodes.

The next thing that comes to mind is how to choose the best attribute.

## Attribute Selection Measures:
**1)Entropy**: This tells how messy is our data. It controls how a decision tree decides to split the data. Its value ranges from 0 to 1. The entropy is 0 if all samples of a node belong to the same class (not good for training dataset), and the entropy is maximal if we have a uniform class distribution (good for training dataset). 
<br>Entropy(D) = Σ - pi(log2(pi))
<br>Here also p is probability.

**2)Information Gain**: measures how much “information” a feature gives us about the class. The information gain is based on the decrease in entropy after a dataset is split on an attribute. It is the main parameter used to construct a Decision Tree. An attribute with the highest Information gain will be tested/split first. It is the difference between the original information requirement and the new requirement.
<br>Gain(D,A) = Entropy(D) - Σ(((Dj)/D)*Entropy(Dj))
<br>D is the given data partition
<br>A is attribute, an attribute can have V distinct values.

## Pros of Decision Tree:
<br>1)Decision trees are easy to visualize and interpret.
<br>2)It can easily capture non — linear patterns.
<br>3)It can handle both numerical and categorical data.

## Cons of Decision Tree:
<br>1)Overfitting is one of the most practical difficulties for decision tree models.
<br>2)Low accuracy for continuous variables
<br>3)It is unstable, meaning that a small change in the data can lead to a large change in the structure of the optimal decision tree.
<br>4)Decision trees are biased with imbalance dataset, so it is recommended that balance out the dataset before creating the decision tree.

For coding part refer Dibyasha_DesicionTree.ipnyb

Thanks for reading :heart:
<br> Contributed by **Dibyasha Panda**

<br>Reach me out at:
<br><a href="https://linkedin.com/"><img src = "https://github.com/DibyashaPanda/dibyasha-panda/blob/master/images/linkedin.png" width = "48" height = "48"></a>
<a href="https://gmail.com/"><img src = "https://github.com/DibyashaPanda/dibyasha-panda/blob/master/images/gmail.jpg" width = "48" height = "48"></a>
