# AI_Course
## 1) Steps for car
###  a) First
Assemble the car as shown in the previous class.

### b) Second
Make the connections from the Raspberry Pi GPIO pins to the L298n as shown in the photos in the Working_WASD folder of the repository.

### c) Third
Test your WASD control for the car.

## **Important Error** 
Try running
```console
sudo apt-get update && sudo apt-get upgrade

```

### If you get an error stating 404 No accelerator found,

You will have to change the repository mirror of the Pi.

```console
sudo nano /etc/apt/sources.list

```

Now in that replace the link which is written after _deb_ with _http://raspbian.mirror.uk.sargasso.net/raspbian/_ and save the changes.

You should be able to run the update and upgrade command now.

## Installing OpenCV on your Pi.

To install OpenCV on your Pi follow this video -_https://www.youtube.com/watch?v=QzVYnG-WaM4_ 

Just make sure to use using **pip3 install** instead of **pip install** in the final step of the video.

Other useful link to install both TensorFlow and OpenCV -_https://www.youtube.com/watch?v=vekblEk6UPc_


