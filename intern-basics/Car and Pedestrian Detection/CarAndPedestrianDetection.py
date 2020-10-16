import cv2

#Image
img_file = "car2.jpg"
video = cv2.VideoCapture('Driving.mp4')

#Pre-trained  Car and Pedestrian Classifier
car_classifier = "haarcascade_car.xml"
pedestrian_classifier = "haarcascade_pedestrians.xml"

car_tracker = cv2.CascadeClassifier(car_classifier)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_classifier)


while True:

   #Read single frame
   (read_successful,frame) = video.read()

   if read_successful:
      greyscaled_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   else:
      break

   cars = car_tracker.detectMultiScale(greyscaled_frame)
   pedestrians = pedestrian_tracker.detectMultiScale(greyscaled_frame)


   for(x,y,w,h) in cars:
      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

   for(x,y,w,h) in pedestrians:
      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)


   cv2.imshow('Car and Pedestrians Detection System',frame)
   key = cv2.waitKey(1)

   #Stop if 'q' or 'Q' is pressed
   if key==81 or key==113:
      break

video.release()
