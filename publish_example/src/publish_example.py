#! /usr/bin/env python

import rospy

from geometry_msgs.msg import Twist             # Import the Int32 message from the std_msgs package

rospy.init_node('PublishExample')         # Initiate a Node named 'topic_publisher'
pub = rospy.Publisher('/cmd_vel', Twist)    # Create a Publisher object, that will publish on the /counter topic
                                           #  messages of type Int32

rate = rospy.Rate(2)                       # Set a publish rate of 2 Hz
var1 = Twist()                            # Create a var of type Int32
var1.linear.x = 0.5
var1.angular.z = 0.5

while not rospy.is_shutdown():             # Create a loop that will go until someone stops the program execution
  pub.publish(var1)                       # Publish the message within the 'count' variable                          # Increment 'count' variable
  rate.sleep()                             # Make sure the publish rate maintains at 2 Hz