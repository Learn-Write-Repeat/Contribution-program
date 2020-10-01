### Hello Everyone, I am **Ashish Kumar Panda**, Pursuing my B.tech degree now from College of Engineering and Technology,Bhubaneswar.
### I am interested in Ai & Deep learning and i love programming,you can connect with me on my linkedin <a>https://www.linkedin.com/in/ashish-kumar-panda-123026194/</a> .I also love to write some technical blogs in my free time ,if you want to read the you can check them, on <a>https://dev.to/ashish12</a>

### The topic provided to me is  *Deep Learning Computation*
### The below table consist of the topics which i select to contribuite during this contribution program

| Topic | Sub-Topic |
| ----------- | ----------- |
| Parameter-management | (i)Hyper Parameter Tuning|
|                      | (ii)Custom Input|
|                      | (iii)GridSearchCV|
|                      | (iv)RandomSearch|
| Deferred Initialization | (i)weight initialization in back propagation |
|                      | (ii)b)activation function initialization|
|                      | (iii)Types Of Activation Function|

### First of all Deep learning is a machine learning technique that teaches computers to do what comes naturally to humans.And a simple deep learning model looks like this:
<img src="https://miro.medium.com/max/1200/1*3fA77_mLNiJTSgZFhYnU0Q.png"></img>

#### so basically the model consist of three parts input layer,hidden layers,and output layer.Each layer consits of some neurons.To Increase the accuracy of the model the programmer used to add weights into the model then apply a activation function that will generate the output i.e *y=activation(WxX+b)*

#### instead of adding random layers we allow the machine to learn and select the best provided model from a set of provided inputs ,this process includes weight initialization,activation function initializion etc.And this process is known as **Deep Learning computation**.The method of selection is called as **Parameter management (Hyper parameter tunning),which includes **deffered initializations**

# Hyper Parameter Tunning:
<img src="https://cdn-images-1.medium.com/max/1600/1*kfMWXXwjYAeliuRPbHleiQ.png"></img>
#### you can refer the .ipynb file provided for the coding part.Basically it searches for the best set of layers for which the model will provide highest accuracy and then can be applied on the provided data to get the desired output.
#### now the thing is how to find the best set of datas:
` from keras.wrapper.scikit.learn import KerasClassifier`
#### this will help us to classify our created model (refer to the .ipynb file)
` from sklearn.model_selection import GridSearchCV`
#### this will help to apply the provided set of datas continiously to the tunning function (refer to the .ipynb file)

`from keras.layers import Dense,Activation`
####  this line of code will help us to create different set of layers provided in the keras library (refer to the .ipynb file)
`from keras.models import Sequential`
#### last but not least to create a model this piece of code is required

# DEFERRED INITIALIZATION
<img src="https://cdn-images-1.medium.com/max/1200/1*LB10KFg5J7yK1MLxTXcLdQ.jpeg"></img>


#### as mentioned earlier one layers initialized our model will work in forward direction it will multiply the weights(W) given with input(X) then add some bias(b) into it after this we will get our output(Y),i.e Y=activation(WxX+b).But what if the model will give us less accuracy? Here comes *Back Propagation* here we changes the values of the weights in the reverse manner and then again the model is trained and this process continues till our original output matches with our predicted output.

#### There are several Weight initialization techniques
<br>1)he_uniform</br>
<br>2)he_init</br>
<br>3)he_normal</br>
<br>4)glorot_uniform</br>

#### There are several Activation Functions
<img src="https://cdn-images-1.medium.com/max/1200/1*ZafDv3VUm60Eh10OeJu1vw.png"></img>
#### The major used activation function that i have used during this process is relu.


#### Hope you like this repositpory.
> Name-Ashish Kumar Panda
> slack group-t2-2
> subject-Deep learning Computation
> subtopics-Parameter management & Deferred initialization


                           



