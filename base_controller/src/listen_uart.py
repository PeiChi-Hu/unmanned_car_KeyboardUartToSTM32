#!/usr/bin/env python

import rospy
import serial
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import roslib
import time

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=2)
ser.isOpen()

def cmdcallback(msg):
    rospy.loginfo("Received a /keyboard message!")
    rospy.loginfo("%s", msg.data)
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=2)
   

    print(msg.data)
    ser.write(str.encode(msg.data))
    ser.close

def listener():
    rospy.init_node('keyboard_listener', anonymous=True)
    rospy.Subscriber('keyboard_control', String, cmdcallback)
    rospy.spin()

if __name__=="__main__":
        listener()

