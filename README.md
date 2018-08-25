# Tweetamin

This is a theramin that responds to LIDAR sensor input OR to tweets that include the hashtag #tweetmytheremin.

It is based on John Bryan Moore's VL53L0X Raspberry Pi code (https://github.com/johnbryanmoore/VL53L0X_rasp_python), and in fact, most of the code is just that code! We included a copy of his README here as well, it is called README_VL530X_rasp_python.md.

### Hardware setup:

You need:
* One Adafruit VL53L0X LIDAR sensor
* One Raspberry Pi
* A PiTop or another monitor
* Keyboard and mouse
* Speaker

Wire it up:
This image is taken from https://cdn-learn.adafruit.com/downloads/pdf/adafruit-vl53l0x-micro-lidar-distance-sensor-breakout.pdf:
![VL53L0X_multi_example.py Diagram](https://raw.githubusercontent.com/katiefg/tweetamin/master/VL53L0x_single.png "Wiring for single LIDAR sensor")

Plug in the speaker.

Turn on your Pi and open the terminal.

### Compilation

* To build on raspberry pi, first make sure you have the right tools and development libraries:
```bash
sudo apt-get install build-essential python-dev
```
* Then use following commands to clone the repository and compile:
```bash
cd your_git_directory
git clone https://github.com/katiefg/tweetmytheremin.git
cd VL53L0X_rasp_python
make
```

* Next, make sure Twython is installed:
```sudo pip3 install twython```


# LIDAR theramin:

* Open runthisfirst.rb in Sonic Pi, and run it. This will allow Sonic Pi to listen for your python code.
* Run VL53L0X_example.py. You should be able to hear noise from the speaker that changes the closer you bring your hand.


# Use tweetable theramin:
* Open runthisfirst.rb in Sonic Pi, and run it. This will allow Sonic Pi to listen for your python code.
* Run tweetmytheremin.py
* Tweet with the hashtag #tweetmytheremin or get someone else to do it, and include MIDI notes. You should see the notes print in Sonic Pi, and hear them on the speaker!




