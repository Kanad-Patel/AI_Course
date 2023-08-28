# AI_Course
## Steps for car
### First
Assemble the car as shown in the previous class.

### Second
Make the connections from the Raspberry Pi GPIO pins to the L298n as shown in the photos in the Working_WASD folder of the repository.

### Third
Test your WASD control for the car.

## **Important Error** 
Try running
```console
pi@raspberrypi:~$ _sudo apt-get update && sudo apt-get upgrade_

```

### If you get an error stating 404 No accelerator found,

You will have to change the repository mirror of the Pi.

```console
sudo nano /etc/apt/sources.list

```

Now in that replace the link which is written after _deb_ with http://raspbian.mirror.uk.sargasso.net/raspbian/ 



## Installing OpenCV on your Pi.


