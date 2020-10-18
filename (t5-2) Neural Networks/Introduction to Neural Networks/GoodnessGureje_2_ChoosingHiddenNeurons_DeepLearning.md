## Introduction to Layers #2

Hello! Welcome back! In this part, we would be addressing ***general techniques of choosing the number of hidden neurons in a model***.

The choice the number of hidden neurons/layers in a network can be made randomly, depending on the problem at hand.

However, a simple equation below can be applied generally to give an estimate. But frankly speaking, there is no hard and fast rule to it! 

Observe the variables you are working with. If they are linearly separable, use one hidden neuron. If the data are not linearly seperable, then opt in for two or more hidden neurons. The number of hidden neurons in this case would depend on the order or type of the function.

Here is the formula you can use: <br>
N_h = N_s/((α * (N_i + N_o)))

where: <br>
N_h = number of input neurons <br>
N_o = number of output neurons <br>
N_s = number of samples in training data set <br>
α = an arbitrary scaling factor, usually 2-10 <br>

Remember it is not a hard and fast rule. Feel free to try out your own choices to give you the model of your dream!

Up next, we would consider layers of Keras API. See you!
