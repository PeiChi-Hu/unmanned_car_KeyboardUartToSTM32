#!/usr/bin/env python

import rospy
import serial
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import roslib
import time

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=2)
ser.isOpen()
#res= ser.readall()

def cmdcallback(msg):
    #rospy.Publisher('/cmd_vel',Twist)
    rospy.loginfo("Received a /cmd_vel message!")
    rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
    rospy.loginfo("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=2)
   
    if msg.linear.x >= 0.0:
        dc = "p" + str(round(msg.linear.x, 2))
    else:
        dc = str(round(msg.linear.x, 2)) 

    if len(dc) == 4:
        dc = dc + "0"

    if msg.angular.z >= 0.0:
        servo = "p" + str(round(msg.angular.z, 2))
    else:
        servo = str(round(msg.angular.z, 2))
    
    if len(servo) == 4:
        servo = servo + "0"

    data = dc + servo
    print(data)
    ser.write(str.encode(data))
    #ser.write(str.encode('Hello'))
    ser.close
    #s = ser.read(1)
    #print(s)

def listener():
    rospy.init_node('cmd_vel_listener', anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, cmdcallback)
    rospy.spin()

if __name__=="__main__":

