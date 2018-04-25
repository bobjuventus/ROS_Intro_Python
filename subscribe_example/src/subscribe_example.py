#! /usr/bin/env python

import rospy                                          
from nav_msgs.msg import Odometry
from std_msgs.msg import Int32

def callback(msg):                                    # Define a function called 'callback' that receives a parameter 
                                                      # named 'msg'
    print msg.pose  

rospy.init_node('topic_subscriber')                   # Initiate a Node called 'topic_subscriber'
sub = rospy.Subscriber('/odom', Odometry, callback)   # Create a Subscriber object that will listen to the /counter
pub = rospy.Publisher('/counter', Int32, queue_size=1)                                                      # topic and will cal the 'callback' function each time it reads
count = Int32()
count.data = 42
# pub.publish(count)

                                 # Print the value 'data' inside the 'msg' parameter

# count = Int32()
# count.data = 0
rate = rospy.Rate(2)
# def increment(msg):
#     count.data += 1
#     rate.sleep()
    

while not rospy.is_shutdown(): 
  pub.publish(count)
  count.data += 1
  rate.sleep()
                                                      # something from the topic
rospy.spin() 