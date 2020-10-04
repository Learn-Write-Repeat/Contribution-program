# Layers and Blocks
* Dense Layer
* Dropout Layer
* Convolution Layer
* LSTM Layer
* Embedded Layer
* Custom Block
* Sequential Block

## Dense layer
Dense layer is deeply/fully connected neural network layer where neurons in a layer are connected to all other neurons in the next layer. This is the most commonly used layer in neural networks.
After extracting features from input data, in order to classify the output into various classes, dense layer is used.

<img src="https://miro.medium.com/max/875/1*eJ36Jpf-DE9q5nKk67xT0Q.jpeg"></img>

Dense layer performs linear operation on input as follows:
`output = activation(dot(input, kernel) + bias)`

`input`- Input feature matrix

`kernel`- Weight matrix

`dot`- Dot product of all input features and its corresponding weights

`bias`- Represents a biased value used in machine learning to optimize the model

`activation`- Activation function


## Dropout Layer
<img src="https://jamesmccaffrey.files.wordpress.com/2018/05/neuralnetworkdropoutlayer.jpg"></img>

Dropout Layer is a neural network layer which drops units(neurons) during each iteration while training the model. Dropout layer works by randomly setting outgoing edges of units(neurons) to zero. So, such units are not considered during a particular training phase.
Dropout layer is used to avoid the model from overfitting.

`tf.keras.layers.Dropout(rate, noise_shape=None, seed=None, **kwargs)`

`rate`- Rate at which units are dropped. Value ranges from 0-1 (0- No dropout, 1- Drop all units)

`noise_shape`- 

`seed`-


## Convolution Layer
Convolution layer is building block of CNN(convolution neural network) and is mostly used while working with 2D image data. It use to extract features from images.
Convolution layer performs a linear operation 'convolution' on input data. This layer applies a filter/kernel on input data to produce feature map. 
The filter is smaller than the input data and element wise matrix multiplication takes place between a filter-sized patch of the input data and the filter/kernel and then the sum is added to the feature map/matrix.

<img src="https://miro.medium.com/max/875/1*cTEp-IvCCUYPTT0QpE3Gjg@2x.png"></img>


After applying given filter to above input, below shown feature map is obtained.<img src="https://miro.medium.com/max/875/1*VVvdh-BUKFh2pwDD0kPeRA@2x.gif"></img>

Here, the input is 5 x 5(N x N) size and filter is 3 x 3(F x F) size so feature map's size is 3 x 3

(N x N) * (F x F) = (N-F+1)x(N-F+1)

(5 x 5) * (3 x 3) = (5-3+1)x(5-3+1) = (3 x 3)


## Sequential Block
A neural network block is described as a single layer, a component which consists of multiple layers, or the entire model itself.
Thus, a sequential block is a block which allows to build model that holds linear stack of layers in the order in which they should be executed. Sequential allows to build predictive models layer by layer either by passing a list of layers to sequential constructor or by using the add() method. `add()`  method allows to append blocks of layers in a sequence. However, sequential does not allow to create models which share layers and have multiple inputs and outputs.


## Custom Block
A custom block is simply a block which allows us to build or code our own custom blocks.
