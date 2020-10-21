# What is Attention Mechanism?

While reading/listening about a certain topic, it is possible for our brain to recognise one part of the context better than the other. 
In the same way, an Attention Mechanism model would provide a somewhat higher weight to one part than the other, simply meaning that its attention is 
focused in that area.

I’ll try to make this clearer with the help of an example. Say, you have to prepare for an open book examination. For this purpose, 10 mins before the exam, 
you are provided a single sheet of a document containing a brief description about Arrays. You as a newbie, go through the document, understanding some parts 
and missing out on some. The exam commences and it consists of a single question ‘What are Arrays’. You quickly go back to the document in your hand and try to 
find the definition of Arrays. Your ATTENTION is focused on searching for an answer to the question at hand. Being the smart person you are, you answer the 
question and receive a full grade. 

An Attention mechanism model takes in the input from one end, the question from the other end, and only focuses on the parts in the input that might help 
in answering the question. 

We can also describe Attention Mechanism as a method in Deep learning which is used to represent what part of input data some layer should focus or a mechanism 
used to create a corresponding output for this kind of focused input data. 


## Why Attention Mechanism?
Why are we using Attention Mechanism in Deep learning or NLP? Simply because when implemented, the result obtained is better. Attention Mechanism models were able
to give a substantially better result when applied to text translation, image captioning , etc. 

Let us understand the purpose of this model in RNN

### Attention Mechanism in RNN
Attention Mechanism models are applied to Recurrent Neural Networks, which are used in NLP and Computer Vision.

A neural network model consists of an encoder and a decoder. The encoder maps discrete inputs into a continuous one and the decoder generates an output of 
sequence one at a time. 

**Encoder**
*It is a stack of RNN units such as LSTM, where each of these units accepts a single element of the input sequence.
*It then collects the information linked to that element and subsequently passes it forward.

**Decoder**
*A decoder consists of a stack of RNN where each units predicts an output.

 A key benefit of the encoder-decoder models is its ability to train the model directly on the source and also handle inputs and outputs of variable lengths. 
Encoder-Decoder models are widely used in Neural Machine translation. 

## Neural Machine Translation
In an NMT system, the meaning of the sentence or text input is mapped to a fixed length vector representation and a translation is generated based on this vector. 
NMT’s work by encoding a sentence to a vector form by using RNN and then decoding the particular sentence, also using RNN. 

This is a form of unsupervised learning where we allow decoder to focus on only a few parts of the input at each step of the generation. The results obtained 
from tase models are usually more accurate. 


***References***
1. http://www.wildml.com/2016/01/attention-and-memory-in-deep-learning-and-nlp/
2. Attention is all you need.— Ashish et.al. 
3. https://machinelearningmastery.com/how-does-attention-work-in-encoder-decoder-recurrent-neural-networks/

