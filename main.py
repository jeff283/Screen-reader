#This is a python program that reads what is it 'sees'
#Credits @Jeff

import cv2 as cv
import pytesseract
import  
from PIL import ImageGrab
import numpy as np
import time

print("Initiallizing..")
time.sleep(3)
print("Starting..")
time.sleep(2)


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

engine = pyttsx3.init()



while True:
	img = ImageGrab.grab()
	img = np.array(img)
	frame = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	text = pytesseract.image_to_string(frame, config='--psm 11')
	print(text)
	engine.say(text)
	engine.runAndWait()
	cv.waitKey(1)

cv.destroyAllWindows()
