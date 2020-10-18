# Sequence to Sequence architecture for machine translation


### What is Sequence to Sequence learning ???

Sequence-to-sequence learning (Seq2Seq) is about training models to convert sequences from one domain.
A typical sequence to sequence model has two parts :

* Encoder 
* Decoder

Both the parts are practically two different neural network models combined into one giant network. 
The task of an encoder network is to understand the input sequence, and create a smaller dimensional representation of it. 
This representation is then forwarded to a decoder network which generates a sequence of its own that represents the output. 

Eg: 

`"the cat sat on the mat" -> [Seq2Seq model] -> "le chat etait assis sur le tapis"`

This can be used for machine translation or for free-from question answering (generating a natural language answer given a natural language question) -- in general, it is applicable any time you need to generate text.

![image](https://blog.keras.io/img/seq2seq/addition-rnn.png)

When both input sequences and output sequences have the same length, you can implement such models simply with a Keras LSTM or GRU layer (or stack thereof). This is the case in this example script that shows how to teach a RNN to learn to add numbers, encoded as character strings

One caveat of this approach is that it assumes that it is possible to generate target[...t] given input[...t]. That works in some cases (e.g. adding strings of digits) but does not work for most use cases. In the general case, information about the entire input sequence is necessary in order to start generating the target sequence.

### Canonical Sequence-to-Sequence :

In the general case, input sequences and output sequences have different lengths (e.g. machine translation) and the entire input sequence is required in order to start predicting the target. This requires a more advanced setup, which is what people commonly refer to when mentioning "sequence to sequence models" with no further context. Here's how it works:

* A RNN layer (or stack thereof) acts as "encoder": it processes the input sequence and returns its own internal state. Note that we discard the outputs of the encoder RNN, only recovering the state. This state will serve as the "context", or "conditioning", of the decoder in the next step.

* Another RNN layer (or stack thereof) acts as "decoder": it is trained to predict the next characters of the target sequence, given previous characters of the target sequence. Specifically, it is trained to turn the target sequences into the same sequences but offset by one timestep in the future, a training process called "teacher forcing" in this context. Importantly, the encoder uses as initial state the state vectors from the encoder, which is how the decoder obtains information about what it is supposed to generate. Effectively, the decoder learns to generate targets[t+1...] given targets[...t], conditioned on the input sequence.

![image](https://blog.keras.io/img/seq2seq/seq2seq-teacher-forcing.png)

In inference mode, i.e. when we want to decode unknown input sequences, we go through a slightly different process:

* Encode the input sequence into state vectors.
* Start with a target sequence of size 1 (just the start-of-sequence character).
* Feed the state vectors and 1-char target sequence to the decoder to produce predictions for the next character.
* Sample the next character using these predictions (we simply use argmax).
* Append the sampled character to the target sequence
* Repeat until we generate the end-of-sequence character or we hit the character limit.

![image](https://blog.keras.io/img/seq2seq/seq2seq-inference.png)

## References :

* [The Keras Blog](https://blog.keras.io/index.html)
* [Analytics Vidhya](https://www.analyticsvidhya.com/blog/)
