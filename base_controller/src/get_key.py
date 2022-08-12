#!/usr/bin/env python

import roslib
import rospy

import sys
from select import select

import termios
import tty
from getkey import getkey, keys

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
        g = getkey(blocking=True)
        if g == 'w':
            rospy.loginfo("forward")
            pub.publish("w")
            rate.sleep()
        elif g == 'q':
            rospy.loginfo("left front")
            pub.publish("q")
            rate.sleep()
        elif keys.name(g) == "a":
            rospy.loginfo("left")
            pub.publish("a")
            rate.sleep()
        elif keys.name(g) == "z":
            rospy.loginfo("left back")
            pub.publish("z")
            rate.sleep()
        elif keys.name(g) == "x":
            rospy.loginfo("backward")
            pub.publish("x")
        elif keys.name(g) == "c":
            rospy.loginfo("right back")
            pub.publish("c")
            rate.sleep()
        elif keys.name(g) == "d":
            rospy.loginfo("go right")
            pub.publish("d")
            rate.sleep()
        elif keys.name(g) == "e":
            rospy.loginfo("right front")
            pub.publish("e")
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

