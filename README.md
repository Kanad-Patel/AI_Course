# AI_Course
##  Steps for car
###  a) First
Assemble the car as shown in the previous class.

### b) Second
Make the connections from the Raspberry Pi GPIO pins to the L298n as shown in the photos in the Working_WASD folder of the repository.

### c) Third
Now create and copy paste the code from WASD_control.py file to your pi and test your WASD control for the car. If you have made all the connections correctly then your car should run.

## **Important Error** 
Try running
```console
sudo apt-get update && sudo apt-get upgrade

```

### If you get an error stating 404 No accelerator found,

You will have to change the repository mirror of the Pi. Run this command on your pi terminal.

```console
sudo nano /etc/apt/sources.list

```

Now in that replace the link which is written after _deb_ with _http://raspbian.mirror.uk.sargasso.net/raspbian/_ and save the changes.

You should be able to run the update and upgrade command now.

## Installing OpenCV on your Pi.

To install OpenCV on your Pi follow this video -_https://www.youtube.com/watch?v=QzVYnG-WaM4_ 

Just make sure to use using **pip3 install** instead of **pip install** in the final step of the video.

Other useful link to install both TensorFlow and OpenCV -_https://www.youtube.com/watch?v=vekblEk6UPc_

##  Steps for car with text recognition

Install "picamera[array]" to operate the picamera using python code.
```console
pip3 install "picamera[array]"
```
Install tesseract-ocr and its tools
```console
sudo apt install tesseract-ocr
```
```console
sudo apt install libtesseract-dev
```
```console
sudo pip install pytesseract
```
Check your installations using 
```console
tesseract --version
```
Useful links for tesseract _https://maker.pro/raspberry-pi/tutorial/optical-character-recognizer-using-raspberry-pi-with-opencv-and-tesseract_ , _https://tutorials-raspberrypi.com/raspberry-pi-text-recognition-ocr/_
