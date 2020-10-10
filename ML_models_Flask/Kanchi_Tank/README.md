# GENDER CLASSIFICATION WEB APP USING FLASK

<img src = "https://miro.medium.com/max/5120/1*fR5nPplVxFLEBrYG0Z9Afw.jpeg" width="70%">

### This project aims to detect/predict gender of individuals from their names using Machine Learning.

### Algorithms Used:
- **Decision Tree**
- **Naive Bayes**

### Dataset
I have created a dataset "**[Names_dataset.csv](https://raw.githubusercontent.com/kanchitank/Contribution-program/master/ML_models_Flask/ML_applicationmodels_Flask/Kanchi_Tank/data/Names_dataset.csv)**" by combining three different datasets namely [Indian male names](https://mbejda.github.io/), [Indian female names](https://mbejda.github.io/) and [English names](https://www.kaggle.com/kaggle/us-baby-names?select=NationalNames.csv). 

# How to run this model with Flask

## Step 1: Install latest version of [Python](https://www.python.org/downloads/windows/) 

## Step 2: Clone [this repository](https://github.com/Learn-Write-Repeat/Contribution-program) in your systems
<br>

<img src = "https://user-images.githubusercontent.com/65490196/95604600-6cef3700-0a75-11eb-8226-6f8e733ffdc7.png">

## Step 3: Creation of a directory and virtual environment
Type the following commands in the command prompt.
<br>

<img src = "https://user-images.githubusercontent.com/65490196/95605296-61504000-0a76-11eb-8904-e636c2b3090d.png">

The above command **"py -3 -m venv venv"** is for virtual environment creation.

## Step 4: Activation
Now type the following command in the command prompt to activate the virtual environment.
<br>

<img src = "https://user-images.githubusercontent.com/65490196/95605472-a1172780-0a76-11eb-96a3-e42e6898d4fb.png">

## Step 5: Install FLASK
<br>

<img src = "https://user-images.githubusercontent.com/65490196/95605738-01a66480-0a77-11eb-87d0-3c137f708e82.png">

## Step 6: Install the packages
<br>

> **pip install flask_bootstrap** <br><br>
> **pip install pandas** <br><br>
> **pip install sklearn** <br><br>

## Step 7: Set FLASK_APP and run the flask
<br>

<img src = "https://user-images.githubusercontent.com/65490196/95606439-f7d13100-0a77-11eb-975b-1f6d8ba3564e.png">

## Step 8: Go to http://127.0.0.1:5000/ in the browser
After running the above command copy the address provided by the prompt after successful execution of the application and paste it in the browser, click enter to see the output. <br>

#### The output would be the following:
<br>

![image](https://user-images.githubusercontent.com/65490196/95606831-8b0a6680-0a78-11eb-9d00-f8eb330b470b.png)

### Step 9: Enter any name in the input field and click the "Predict" button to see the results
<br>

![image](https://user-images.githubusercontent.com/65490196/95606960-b1c89d00-0a78-11eb-8aa3-87683dc990ed.png)

### RESULT
<br>

![image](https://user-images.githubusercontent.com/65490196/95607243-184dbb00-0a79-11eb-98c5-a29aa3ea0f6d.png)

### And we're done! We've successfully deployed the ML model using FLASK!
