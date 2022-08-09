#!/usr/bin/env python

import roslib
import rospy

import sys
from select import select

import termios
import tty
import keyboard

from std_msgs.msg import String

msg = """
Reading from the keyboard and Publishing to Twist!
---------------------------
Moving around:
   q    w    e
   a    s    d
   z    x    c

CTRL-C to quit
"""

def key():
    rospy.init_node('keyboard', anonymous=True)
    pub = rospy.Publisher('keyboard_control', String, queue_size=1)
    rate = rospy.Rate(7)
    while not rospy.is_shutdown():
        if keyboard.is_pressed("w"):
            rospy.loginfo("go forward")
            pub.publish("w")
            rate.sleep()
        elif keyboard.is_pressed("a"):
            rospy.loginfo("go left")
            pub.publish("a")
            rate.sleep()
        elif keyboard.is_pressed("s"):
            rospy.loginfo("go backward")
            pub.publish("s")
            rate.sleep()
        elif keyboard.is_pressed("d"):
            rospy.loginfo("go right")
            pub.publish("d")
            rate.sleep()
        else:
            rospy.loginfo("stop")
            pub.publish("0")
            rate.sleep()


if __name__ == '__main__':
    try:
        key()
    except rospy.ROSInterruptException:
        pass
