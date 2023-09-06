import RPi.GPIO as GPIO    
import cv2
import pytesseract
from pytesseract import Output

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

in1 = 24
in2 = 23
ena = 25
in3 = 17
in4 = 27
enb = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
q=GPIO.PWM(enb,1000)
p=GPIO.PWM(ena,1000)
p.start(50)
q.start(50)

while True():
    ret, frame = cap.read()
    x = pytesseract.image_to_data(frame, output_type=Output.DICT)
    text = len(x['text'])
    for i in range(text):

        if int(x['conf'][i]) > 60:

            d = x['text'][i]

            if d=='f':
                print("forward")
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                GPIO.output(in3,GPIO.HIGH)
                GPIO.output(in4,GPIO.LOW)
            
GPIO.cleanup()
