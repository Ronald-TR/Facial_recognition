# Facial_recognition
Using OpenCV library to find faces and eyes

## Required ##

**OpenCV for Python**

**numpy**

**haarcascade facial and eye detection xml (available in https://github.com/opencv/opencv/tree/master/data/haarcascades)**

*The definied function in the utils write rectangles in face and eyes detected by the image passed by parameter, like the example in OpenCV docs, but... you can do anything with the cordinates wich **detectMultiScale** brings to you.*

This return a numpy array with each position like this:
**>>** [x_axis, y_axis, width, heigth]

With the x_axis the top left point.
and y_axis the top left point too.

I use this coordinates to write a rectangle to expose the detection area, but think in the possibilities, they're awesome! :')
