# Layers and Blocks
* Dense Layer
* Dropout Layer
* Convolution Layer
* LSTM Layer
* Embedded Layer
* Sequential Block
* Custom Block

&nbsp;
## Dense layer
Dense layer is a deeply/fully connected neural network layer where each neuron in a layer is connected to all the other neurons in the next layer. This is the most commonly used layer in neural networks.
After extracting features from input data, in order to classify the output into various classes, dense layer is used.

<img src="https://miro.medium.com/max/875/1*eJ36Jpf-DE9q5nKk67xT0Q.jpeg"></img>

Dense layer performs linear operation on input as follows:
`output = activation(dot(input, kernel) + bias)`

`input`- Input feature matrix

`kernel`- Weight matrix

`dot`- Dot product of all input features and its corresponding weights

`bias`- Represents a biased value used in machine learning to optimize the model

`activation`- Activation function

*Refer the .ipynb file to understand operation of Dense Layer.*

&nbsp;
## Dropout Layer
<img src="https://jamesmccaffrey.files.wordpress.com/2018/05/neuralnetworkdropoutlayer.jpg"></img>

Dropout Layer is a neural network layer that drops units(neurons) during each iteration while training the model. The Dropout layer works by randomly setting outgoing edges of
units(neurons) to zero. So, such units are not considered during a particular training phase.
The Dropout layer is used to avoid the model from overfitting.

`tf.keras.layers.Dropout(rate, noise_shape=None, seed=None, **kwargs)`

`rate`- Fraction of units to be dropped. Value ranges from 0-1 (0- No dropout, 1- Drop all units)

`noise_shape`- 1D integer tensor representing the shape of the binary dropout mask that will be multiplied with the input.

`seed`- integer to use as random seed

Training Phase: For each hidden layer, for each training sample, for each iteration, ignore a random fraction, p, of units and its corresponding activations.

Testing Phase: Use all activations, but reduce them by a factor p to account for the missing activations during training.


&nbsp;
## Convolution Layer
Convolution layer is the building block of CNN(convolution neural network) and is mostly used while working with 2D image data. It is used to extract features from images.
The Convolution layer performs a linear operation 'convolution' on input data. This layer applies a filter/kernel on input data to produce a feature map. 
The filter is smaller than the input data and the operation involves element-wise matrix multiplication between the filter-sized patch of the input data and the filter/kernel
and then the sum is added to the feature map/matrix.

<img src="https://miro.medium.com/max/875/1*cTEp-IvCCUYPTT0QpE3Gjg@2x.png"></img>


After applying given filter to above input, below shown feature map is obtained.<img src="https://miro.medium.com/max/875/1*VVvdh-BUKFh2pwDD0kPeRA@2x.gif"></img>

Here, the input is 5 x 5(N x N) size and filter is 3 x 3(F x F) size so feature map's size is (3 x 3)

(N x N) * (F x F) = (N-F+1) x (N-F+1)

(5 x 5) * (3 x 3) = (5-3+1) x (5-3+1) = (3 x 3)

&nbsp;
## Embedding Layer
Embedding layer is a layer that transforms positive integers(indexes) into dense vectors of fixed size. Embedding layer is used in neural networks which involves large input
textual data.
It requires that the input data should be integer encoded ie. each word in the text should be represented by a unique integer.
Consider an example where there are 5000 unique words in a text which needs to be classified. After preprocessing(one-hot encoding) this textual data, a sparse matrix of large
dimensions(5000 dimensional vector for each word) will be generated and this will be used to feed the neural network model. This will require a huge amount of memory and time
and hence this approach is inefficient. So, embedding layer is used where *high-dimensional vectors are translated to low-dimensional vectors*.


*Refer the .ipynb file to understand working of Embedding Layer.*
 
&nbsp;
## LSTM Layer
LSTM stands for *Long Short Term Memory*. LSTM network is a kind of recurrent neural network. Recurrent neural networks can remember the characteristics of its recent previous
inputs and outputs but does not have the capability to remember the past inputs and outputs for too long. In some cases, it may not be sufficient for the network to rely on
recent or immediate previous inputs and outputs for predictions. This is known as Long term dependency. LSTM deals with this long term dependency problem of RNNs.

LSTM networks have *`LSTM cells`* in place of standard neural network layers. LSTM's have an internal mechanism called gates that control the flow of information. These gates
consist of an input gate, forget gate and an output gate. These gates learn which data should be retained as important and which data should be discarded.

<img src="https://i1.wp.com/adventuresinmachinelearning.com/wp-content/uploads/2017/09/LSTM-diagram.png?w=669&ssl=1"></img>

In the above diagram, new word or sequence value x<sub>t</sub> is added to the output of previous LSTM cell h<sub>t-1</sub>. This combined input is passed via the tanh layer to
the input gate which consists of the sigmoid function. These input gates can discard any input vector that is not required.
LSTM cells have an internal state variable s<sub>t</sub>. The variable s<sub>t-1</sub> is added to the input data to create an effective layer of recurrence. This addition
operation helps to reduce the risk of vanishing gradients. However, this recurrence loop is controlled by a forget gate which works similarly to the input gate, but instead
helps the network to learn which state variables should be remembered or forgotten.

&nbsp;
## Sequential Block
A neural network block is described as a single layer, a component that consists of multiple layers, or the entire model itself.
Thus, a sequential block is a block that allows us to build models that hold a linear stack of layers in the order in which they should be executed. Sequential allows us to
build predictive models layer by layer either by passing a list of layers to the sequential constructor or by using the add() method. `add()`  method allows to append blocks of
layers in a sequence. However, sequential does not allow to create models that share layers and have multiple inputs and outputs.

<img src="https://d2l.ai/_images/blocks.svg"></img>

In the above figure, multiple layers are combined into blocks, forming repeating patterns of larger models.

*Refer the .ipynb file to understand working of Sequential Block.*

&nbsp;
## Custom Block
A custom block is simply a block which allows us to build or code our own custom models and blocks. In order to create a custom block or model, the block class must be extended and its methods `init` and `forward` should be overridden to define parameters of the model and forward function, respectively.

*Refer the .ipynb file to understand how to implement our own Custom Block.*

&nbsp;
&nbsp;
### Contribution By- Rutuja Dharankar


