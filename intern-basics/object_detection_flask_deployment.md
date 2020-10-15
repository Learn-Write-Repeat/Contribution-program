# Object Dtection Deployment Using Flask

## *main.py* file for the flask application
- This file would consist the code that will be used to connect through flask.
- To make different root. 
- There are three root that are created.First one to display opening template. Then for uploading the image that needed to be processed and other for displaying the output.
- The second root consist the code for object detection. 
- Simple stop sign detection code has been written using the haarcascade library. 
- The image that was generated has type of *<numpy.ndarray>* which is converted to *<str>* class and a .jpg format using the *Pillow* Library. 
- The image that is uploaded is saved in a  static/upload folder. Both the detected image and test image is stored in the sam folder. 

## The result after detection

[!Detected image]()
