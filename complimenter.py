import cv2
import numpy as np
import random
import os
from pathlib import Path
from playsound import playsound
import time

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml") #dataset to be used for detecting face 

cap = cv2.VideoCapture(0) #

compliments = os.listdir("complimentfiles") #list of the soundfiles of compliments
insults = os.listdir("insultfiles") #list of the soundfiles of insults
datacompfolder = Path("complimentfiles") #path to the folder of compliment sound files
datainsultfolder = Path("insultfiles") #path to the folder of insult sound files

startTime = time.time() #starts timer
times = list() #keeps track of seconds so it doesn't play a sound file again

while True:
    ret, img = cap.read() #reads the frame of the web cam
    num = random.randrange(0,len(compliments)) # generates a random number
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converts the frame to a gray scale image
    faces = face_cascade.detectMultiScale(gray, 1.3,2) #applies face detection onto gray scale image. second parameter(float) determines speed vs accuracy. greater the number greater the speed and lower the accuracy. third parameter(int) is the quality min of a possible detection. higher the number the higher the quality required

    k = cv2.waitKey(30) & 0xff #must press esc and x button to close webcam

    for (x,y,w,h) in faces: #takes the x coord, y coord, width, and height of the face detected
        rect = cv2.rectangle(img, (x,y), (x+w, y+h), (255,122,0),2) #draws a rectangle on the webcam frame using the x and y coord and width and height, and color and thickness of line

    cv2.imshow("img",img) #shows the webcam frame

    endTime = time.time() #seoncds passed 

    if np.any(faces) == True and (round(endTime - startTime)%30 == 0) and (round(endTime - startTime) not in times):#if a face is detected #for every 30 seconds # makes sure only one sound file is played
        playsound(str(datacompfolder / compliments[num]),False)
##        wave_obj = sa.WaveObject.from_wave_file(str(datacompfolder / compliments[num]))
##        play_obj = wave_obj.play()
##        play_obj.wait_done()
    elif np.any(faces) == False and (round(endTime - startTime)%4 == 0) and (round(endTime - startTime) not in times): #if no face is detected #for every four seconds # makes sure only one sound file is played
        playsound(str(datainsultfolder / insults[num]),False)
##        wave_obj = sa.WaveObject.from_wave_file(str(datainsultfolder / insults[num]))
##        play_obj = wave_obj.play()
##        play_obj.wait_done()
    times.append((round(endTime - startTime))) #makes sure that the same second isn't repeated
    if k == 27: #breaks out of while loop
        break




#developed with help based on https://www.youtube.com/watch?v=88HdqNDQsEk&t=557s
