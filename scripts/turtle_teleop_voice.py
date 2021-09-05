#!/usr/bin/env python
import vcmd
import rospy
from geometry_msgs.msg import Twist
from math import pi

lstep = 1.0 
astep = pi / 4
def send_msg(pub, cmd):
    vel = Twist()
    if '前' in cmd:
        vel.linear.x= lstep
    if '後' in cmd:
        vel.linear.x= -lstep
    if '右' in cmd:
        vel.angular.z = -astep
    if '左' in cmd:
        vel.angular.z = astep
    pub.publish(vel)

def teleop_voice():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('turtle_teleop_voice', anonymous=True)
    while (cmd := vcmd.read()) != "終":
        send_msg(pub, cmd)

if __name__ == '__main__':
    try:
        teleop_voice()
    except rospy.ROSInterruptException:
        pass
