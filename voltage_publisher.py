#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher():

    pub_volt_0 = rospy.Publisher('volt0', String, queue_size=10)
    pub_volt_1 = rospy.Publisher('volt1', String, queue_size=10)
    pub_volt_2 = rospy.Publisher('volt2', String, queue_size=10)

    rospy.init_node('tx_voltage_publisher', anonymous=True)
    rate = rospy.Rate(0.1)  # 0.1hz 10s period

    while not rospy.is_shutdown():

        volt0 = open('/sys/bus/i2c/drivers/ina3221x/0-0040/iio_device/in_voltage0_input').read()
        volt1 = open('/sys/bus/i2c/drivers/ina3221x/0-0040/iio_device/in_voltage1_input').read()
        volt2 = open('/sys/bus/i2c/drivers/ina3221x/0-0040/iio_device/in_voltage2_input').read()

        pub_volt_0.publish(volt0)
        pub_volt_1.publish(volt1)
        pub_volt_2.publish(volt2)

        rospy.loginfo("Voltage [mV]: " + volt0 + ", " + volt1 + ", " + volt2)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass