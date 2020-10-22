## Introduction to Layers #1

Hello there. Glad to have you here! I am Goodness Gureje and I want to intimate you with some very helpful details about neural network. Let's ride!

I would begin with the ***different layers of a neural network***.

A typical neural network consists of many layers, which can be grouped in to three: the input, hidden and output layers. Let's start off with the input layer.

**1. Input Layer** 

This is the layer that feeds in the training data into the Neural Network. It is the first layer in the neural network and the number of nodes in this layer depends on the size of the training set. 

For example, if the training set has 5000 training examples and 25 features, the input layer would have 25 nodes. 

The training set, after being fed into the input layer of the network is then processed, the weights and biases determined and then passed into the hidden layer(s) before it gets to the output layer.

The next is the hidden layer(s)

**2. Hidden Layer(s)**

This is the next set of layer(s) in the network. I used layers because typically, a neural netowrk can have more than one hidden layer.

A typical neural network for solving a linear problem would have only one hidden layer; while a neural network for a non-linear problem would have more than one hidden layer. When more than one, the layers are usually connected together before the output layer.

The number of the hidden layers/neurons is usually determined by the programmer either by a rough estimate or applying a flexible formula as discussed in the next subtopic. 

The third category is the output layer.

**3. Output Layer**

A neural network typically has one output layer. But this could contain one node (for binary classification) or multiples nodes (for SoftMax regression), depending on the type of function involved. 

This is the layer that gives the final result or classification after the neural network has learned the parameters and minimized the cost function. 

You can check the diagram below for a little demonstration, and better grasp of the subject matter.

<p align="center">
  <img src = "Image/ANN-1.jpg" />
</p>

Hope you have had an awesome read! 

In the next section, we would discuss the general techniques to choose the number of hidden neurons in a model. 

Catch you there!
