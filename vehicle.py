# OpenCV Python program to detect cars in video frame 
# import libraries of python OpenCV  
import cv2 
from tkinter import *
import numpy as np


def vehicle():

	# capture frames from a video 
	cap = cv2.VideoCapture('video.avi') 
	  
	# Trained XML classifiers describes some features of some object we want to detect 
	car_cascade = cv2.CascadeClassifier('self_created_cars.xml') 
	  
	# loop runs if capturing has been initialized. 
	while True: 
	    # reads frames from a video 
	    ret, frames = cap.read() 
	      
	    # convert to gray scale of each frames 
	    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) 
	      
	  
	    # Detects cars of different sizes in the input image 
	    cars = car_cascade.detectMultiScale(gray, 3.1,2)

	    cars = np.array(cars)
	    
	    print(cars.shape)
	    if len(cars) == 0:
	    	print("No cars found!")
	    	
	    else:
	    	print(type(cars))
	    	print(cars)
	    	print("Number of cars detected :"+ str(cars.shape[0]))
	    
	    
	    # To draw a rectangle in each cars 
	    for (x,y,w,h) in cars:
	    	cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
	    	cv2.rectangle(frames, ((0,frames.shape[0] -25)),(270, frames.shape[0]), (255,255,255), -1)
	    	cv2.putText(frames, "Number of cars detected: " + str(cars.shape[0]), (0,frames.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
	   
	   
	   # Display frames in a window  
	    	cv2.imshow('video2', frames)
	      
	    # Wait for Esc key to stop 
	    if cv2.waitKey(33) == 27:
	    	break
	  
	# De-allocate any associated memory usage 
	cv2.destroyAllWindows() 

window = Tk()
window.geometry('800x600')
button1 = Button(window, text=" Vehicle Detection", command=vehicle).pack()
button2 = Button(window,text='Quit',command=quit).pack()
window.mainloop()

