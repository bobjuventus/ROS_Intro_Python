#! /usr/bin/env python

import rospy

rospy.init_node("ObiWang")
rate = rospy.Rate(2)               # We create a Rate object of 2Hz
while not rospy.is_shutdown():     # Endless loop until Ctrl + C
   print "Help me Obi-Wan Kenobi, you're my only hope. Test!!"
   rate.sleep()