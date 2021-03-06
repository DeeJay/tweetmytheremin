import time
import VL53L0X

# Create a VL53L0X object for device on TCA9548A bus 1
tof1 = VL53L0X.VL53L0X(TCA9548A_Num=1, TCA9548A_Addr=0x70)

# Start ranging on TCA9548A bus 1
tof1.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

timing = tof1.get_timing()
if (timing < 20000):
    timing = 20000
print ("Timing %d ms" % (timing/1000))

for count in range(1,101):
    # Get distance from VL53L0X  on TCA9548A bus 1
    distance = tof1.get_distance()
    if (distance > 0):
        print ("1: %d mm, %d cm, %d" % (distance, (distance/10), count))

    time.sleep(timing/1000000.00)

tof1.stop_ranging()