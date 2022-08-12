#!/usr/bin/env python

import roslib
import rospy

import sys
from select import select

import termios
import tty
from pynput import keyboard

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
        with keyboard.Events() as events:
            for event in events:
                if event.key == "w":
                    rospy.loginfo("forward")
                    pub.publish("w")
                    rate.sleep()
                elif event.key == "q":
                    rospy.loginfo("left front")
                    pub.publish("q")
                    rate.sleep()
                elif event.key == "a":
                    rospy.loginfo("left")
                    pub.publish("a")
                    rate.sleep()
                elif event.key == "z":
                    rospy.loginfo("left back")
                    pub.publish("z")
                    rate.sleep()
                elif event.key == "x":
                    rospy.loginfo("backward")
                    pub.publish("x")
                    rate.sleep()
                elif event.key == "c":
                    rospy.loginfo("right back")
                    pub.publish("c")
                    rate.sleep()
                elif event.key == "d":
                    rospy.loginfo("go right")
                    pub.publish("d")
                    rate.sleep()
                elif event.key == "e":
                    rospy.loginfo("right front")
                    pub.publish("e")
                    rate.sleep()
                elif event.key == keyboard.Key.esc:
                    break
                else:
                    rospy.loginfo("stop")
                    pub.publish("0")
                    rate.sleep()


if __name__ == '__main__':
    try:
        key()
    except rospy.ROSInterruptException:
        pass

