# What are Contours?
Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity. The contours are a useful tool for shape analysis and object detection and recognition.

For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
findContours function modifies the source image. So if you want source image even after finding contours, already store it to some other variables.
In OpenCV, finding contours is like finding white object from black background. So remember, object to be found should be white and background should be black.

# Let’s see how to find contours of a binary image:   
There are three arguments in **cv2.findContours()** function, first one is source image, second is contour retrieval mode, third is contour approximation method. And it outputs the image, contours and hierarchy. contours is a Python list of all the contours in the image. Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.

# How to Draw Contours?  
To draw the contours, **cv2.drawContours** function is used. It can also be used to draw any shape provided you have its boundary points. Its first argument is source image, second argument is the contours which should be passed as a Python list, third argument is index of contours (useful when drawing individual contour. To draw all contours, pass -1) and remaining arguments are color, thickness etc. 

# Contour Features
**1.) Moment -** 
Image moments help you to calculate some features like center of mass of the object, area of the object etc. 

**2.) Contour Area and Perimeter -** 
Contour area is given by the function cv.contourArea() or from moments .

Contour Perimeter is also called arc length. It can be found out using cv.arcLength() function. Second argument specify whether shape is a closed contour (if passed True), or just a curve. 

**3.a) Contour Approximation -** 
It approximates a contour shape to another shape with less number of vertices depending upon the precision we specify. It is an implementation of Douglas-Peucker algorithm.

**3.b) Convex Hull -** 
Hull means the exterior or the shape of the object.

Therefore, the Convex Hull of a shape or a group of points is a tight fitting convex boundary around the points or the shape.

**4.) Checking Convexity -** 
There is a function to check if a curve is convex or not, cv2.isContourConvex(). It just return whether True or False. Not a big deal. 

**5.a) Straight Bounding Rectangle -** 
It is a straight rectangle, it doesn't consider the rotation of the object. So area of the bounding rectangle won't be minimum. It is found by the function cv.boundingRect().

Let (x,y) be the top-left coordinate of the rectangle and (w,h) be its width and height. 

**5.b) Rotated Rectangle -** 
Here, bounding rectangle is drawn with minimum area, so it considers the rotation also. The function used is cv2.minAreaRect(). It returns a Box2D structure which contains following detals - ( top-left corner(x,y), (width, height), angle of rotation ). But to draw this rectangle, we need 4 corners of the rectangle. It is obtained by the function cv2.boxPoints().  

**6.) Minimum Enclosing Circle -**  
the circumcircle of an object using the function cv.minEnclosingCircle(). It is a circle which completely covers the object with minimum area.  

**7.) Fitting an Ellipse -**
fit an ellipse to an object. It returns the rotated rectangle in which the ellipse is inscribed.

**8.) Fitting a Line -** 
Similarly we can fit a line to a set of points. Below image contains a set of white points. We can approximate a straight line to it.

