# DECISION TREES 

## What is a Decision Tree?

<img src = "https://raw.githubusercontent.com/kanchitank/Contribution-program/master/(t3)%20Supervised%20Learning/images/Decision_Trees/1.jpg" width="60%"> 

A **decision tree** is a flowchart-like structure in which:
- Each internal node represents **a test on a feature** (e.g. whether a coin flip comes up heads or tails) , 
- Each leaf node represents **a class label** (decision taken after computing all features) 
- And branches represent **conjunctions of features that lead to those class labels**.
- The paths from root to leaf represent **classification rules**. 

The tree can be explained by two entities, namely decision nodes and leaves. The leaves are the decisions or the final outcomes. And the decision nodes are where the data is split.

### Decision Tree for Rain Forecasting

Below diagram illustrates the basic flow of decision tree for decision making with labels (Rain(**Yes**), No Rain(**No**)):

<img src = "https://raw.githubusercontent.com/kanchitank/Contribution-program/master/(t3)%20Supervised%20Learning/images/Decision_Trees/2.png" width="60%"> 

### Decision tree is one of the predictive modelling approaches used in **statistics, data mining and machine learning**.

### Important Terminology related to Decision Trees

- **Branches** - Division of the whole tree is called branches.
- **Root Node** - Represent the whole sample that is further divided.
- **Splitting** - Division of nodes is called splitting.
- **Terminal Node** - Node that does not split further is called a terminal node.
- **Decision Node** -  It is a node that also gets further divided into different sub-nodes being a sub node. 
- **Pruning** - Removal of subnodes from a decision node.
- **Parent and Child Node** - When a node gets divided further then that node is termed as parent node whereas the divided nodes or the sub-nodes are termed as a child node of the parent node.

<img src = "https://raw.githubusercontent.com/kanchitank/Contribution-program/master/(t3)%20Supervised%20Learning/images/Decision_Trees/5.png" width="80%"> 

Decision trees classify the examples by sorting them down the tree from the root to some leaf/terminal node, with the leaf/terminal node providing the classification of the example.

Each node in the tree acts as a test case for some attribute, and each edge descending from the node corresponds to the possible answers to the test case. This process is recursive in nature and is repeated for every subtree rooted at the new node.

## Types of Decision Trees
There are two main types of Decision Trees:

- **Categorical Variable Decision Tree** <br>
What we’ve seen above is an example of classification tree, where the outcome was either 'Yes' or 'No'. This type of decision tree is called a **Categorical variable decision tree**. 
<br>Below is one more example of Categorical variable decision tree:

<img src = "https://raw.githubusercontent.com/kanchitank/Contribution-program/master/(t3)%20Supervised%20Learning/images/Decision_Trees/3.png" width="60%"> 

- **Continuous Variable Decision Tree** <br>
If the input is numeric types and or is continuous in nature like when we have to predict a house price. Then the used decision tree is called a **Continuous variable decision tree**.
<br>Below is the example of Continuous variable decision tree:

<img src = "https://raw.githubusercontent.com/kanchitank/Contribution-program/master/(t3)%20Supervised%20Learning/images/Decision_Trees/4.png" width="60%"> 

## Algorithms used in Decision Trees

- **ID3** → (extension of D3)
- **C4.5** → (successor of ID3)
- **CART** → (Classification And Regression Tree)
- **CHAID** → (Chi-square automatic interaction detection Performs multi-level splits when computing classification trees)
- **MARS** → (multivariate adaptive regression splines)

## What are the Advantages and Disadvantages of Decision Trees?

### Advantages

- DT is **effective** and is **very simple**.
- DT can be used while **dealing with the missing values** in the dataset.
- DT **can take care of numeric as well as categorical features**.
- Results that are generated from DT **does not require any statistical or mathematics knowledge** to be explained.

### Disadvantages

- Logics get transformed if there are even small changes in training data.
- Larger trees get **difficult to interpret**.
- **Biased** towards tree having more levels.

 
