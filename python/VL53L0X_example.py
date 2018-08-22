#!/usr/bin/python

# MIT License
# 
# Copyright (c) 2017 John Bryan Moore
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
import VL53L0X
from pythonosc import udp_client

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

# Create a VL53L0X object
tof = VL53L0X.VL53L0X()

# Start ranging
tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

timing = tof.get_timing()
if (timing < 20000):
    timing = 20000
print ("Timing %d ms" % (timing/1000))

while True:
    distance = tof.get_distance()
    if (distance > 0):
        print ("%d mm, %d cm" % (distance, (distance/10)))
        if (distance < 100):
            sender.send_message('/play_this', 69)
        elif (distance < 200):
            sender.send_message('/play_this', 71)
        elif (distance < 300):
            sender.send_message('/play_this', 60)
        elif (distance < 400):
            sender.send_message('/play_this', 62)
        elif (distance < 500):
            sender.send_message('/play_this', 64)
        elif (distance < 600):
            sender.send_message('/play_this', 65)
        elif (distance < 700):
            sender.send_message('/play_this', 67)
    time.sleep(0.5)
            
    time.sleep(timing/1000000.00)

tof.stop_ranging()

