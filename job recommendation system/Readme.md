# job Recommendation system
## What is Recommendation system?

*Recommender systems are an important class of machine learning algorithms that offer "relevant" suggestions to users. Categorized as either collaborative filtering or a content-based system, check out how these approaches work along with implementations to follow from example code. By George Seif, AI / Machine Learning Engineer*

## Types of Recommendation system
**There are three basic, commonly used, types of recommender systems**
* collaborative filtering
* content-based filtering
* hybrid recommendation systems.

## For this project we are going  to use Content based Filtering system.
## What is content based filtering?

*The point of content-based filtering system is to know the content of both user and item. Usually it constructs and then compare user-profile and item-profile using the content of shared attribute space*

<img src = "https://image.slidesharecdn.com/crabintroduction-111002094330-phpapp02/95/crab-a-python-framework-for-building-recommender-systems-42-728.jpg?cb=1317548872"></img>

# WorkFlow

# User side data

| id | Name | Skills | Applied job | Experience |
| ----------- | ----------- | ----- | ----------- | ----------- |
| 1 | swayam |python | software developer| 2 | 
| 2 | ashish | java| Android developer| 0 | 


# Company side data

| company name | required post | minimum experience |
| -------------- | --------- | ------------ |
| x | software developer | 1 |


*as we know Content filtering works by matching strings of characters. When the strings match, the content is not allowed through. Content filters are often part of Internet firewalls. In such a usage content filtering is serving a security purpose, but content filtering is also used to implement company policies related to information system usage*

* it will predict according to the data given by the user
* it gets trained on the user data
* so if a user is applying for specific post in a company then it will recommend all the similar posts of different companies
* simmilarly for companies it will suggest them the user id applying for the soimilar kind of post 
