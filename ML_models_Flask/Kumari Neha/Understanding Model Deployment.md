# MACHINE LEARNING MODEL DEPLOYMENT USING FLASK
---
![images.jpg](attachment:images.jpg)







# What Does it Mean to Deploy A Machine Learning Model?



 - Integrating a machine learning model into an existing production environment where it can take in an input and return an output is called **model deployment**,the purpose of deploying your model is so that you can make the predictions from a trained ML model available to others, whether that be users, management, or other systems. 
 
 **For example**-You have to build a model that predicts whether to approve a loan for a customer or not. The model is trained on features like salary, dependents, loan amount and several other features then the model will be able to make predictions when you give input of these fields to the model. You have to give entries of features on which the model is trained then only it would be able to make predictions.
 
 
 ![flask1.png](attachment:flask1.png)
 
 
 ### Points to keep in mind before deploying model-
 
 - **Portability**: this refers to the ability of your software to be transferred from one machine or system to another. A portable model is one with a relatively low response time and one that can be rewritten with minimal effort.
 
 - **Scalability**: this refers to how large your model can scale. A scalable model is one that doesn’t need to be redesigned to maintain its performance.
 
 
 
### Factors to Consider When Determining Your Method of Deployment

There are a number of factors and implications that one should consider when deciding how to deploy an ML model. These factors include the following:


- How frequently predictions will be generated and how urgent the results are needed
- If predictions should be generated individually or by batches
- The latency requirements of the model, the computing power capabilities that one has, and the desired SLA
- The operational implications and costs required to deploy and maintain the model



# What is Flask?
Flask is a web application framework written in Python. It has multiple modules that make it easier for a web developer to write applications without having to worry about the details like protocol management, thread management, etc.

Flask gives is a variety of choices for developing web applications and it gives us the necessary tools and libraries that allow us to build a web application.


![download.png](attachment:download.png)




# Why Flask??

1. feature-rich micro framework
1. fast template
1. strong WSGI features
1. and extensive documentation
1. vast no of extension




After building different predictive models now it’s time to understand how to use them in real-time to make predictions. You can always check your model ability to generalize when you deploy it in production. For example, if you have built a predictive model that predicts whether a customer will default or not then you will realize how good it is for your model to predict the same when you deploy it in real-time and start predicting for new coming data. 






# STEPS FOR DEPLOYING MODEL

1. Prepare your machine learning model
1. Save your model
1. choose a Web Server, **flask**
1. choose a cloud service provider,**Heroku**



![flask.jpg](attachment:flask.jpg)


# HEROKU
Heroku: www.heroku.com

Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
Heroku is also said to be a polyglot platform as it has features for a developer to build, run and scale applications in a similar manner across most languages.It allows software developers to build and run complex web applications without having to worry about the underlying hardware or the networking aspects of it.



![download.jpg](attachment:download.jpg)


# Why HEROKU?

1.  User-Friendly Tool
1.  No Infrastructure Needed
1. incredible Command Line Interface
1. Multi-Language Support
1. Huge Toolbelt of Add-Ons
1. Deploy from Different Sources

and many more...


```python

```
