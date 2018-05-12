#! /usr/bin/env python

import rospy
import numpy as np
from geometry_msgs.msg import Twist             # Import the Int32 message from the std_msgs package

# rospy.init_node('my_sphero_topics')         # Initiate a Node named 'my_sphero_topics'
# pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)    # Create a Publisher object, that will publish on the /counter topic
                                           #  messages of type Int32
class CmdVelPub(object):
    def __init__(self):
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.vel = Twist()
        self.linearspeed = 0.3
        # the two parameters below combined making the turtlebot turn 90 degrees
        self.angularspeed = 3.2
        self.angulartime = 0.0
        
    def move_robot(self, direction, angle = 0.0):
        if direction == 'forwards':
            self.vel.linear.x = self.linearspeed
            self.vel.angular.z = 0.0
            self.pub.publish(self.vel)
        elif direction == 'backwards':
            self.vel.linear.x = -self.linearspeed
            self.vel.angular.z = 0.0
            self.pub.publish(self.vel)
        elif direction == 'turn':
            self.vel.linear.x = 0.0
            self.vel.angular.z = self.angularspeed*np.sign(angle) # positive is left turn
            self.pub.publish(self.vel)
            self.angulartime = (abs(angle)+0.2)/self.angularspeed
            rospy.sleep(self.angulartime)
            self.vel.angular.z = 0.0
            self.pub.publish(self.vel)
        elif direction == 'stop':
            self.vel.linear.x = 0.0
            self.vel.angular.z = 0.0
            self.pub.publish(self.vel)
        else:
            pass

# if __name__ == "__main__":
#     rospy.init_node('my_turtlebot2_topics')
#     cmd_publisher_object = CmdVelPub()
    
#     rate = rospy.Rate(1)
    
#     ctrl_c = False
#     def shutdownhook():
#         # works better than the rospy.is_shut_down()
#         global ctrl_c
#         global twist_object
#         global pub
        
#         rospy.loginfo("shutdown time!")
        
#         ctrl_c = True
#         cmd_publisher_object.move_robot(direction="stop")
    
#     rospy.on_shutdown(shutdownhook)
    
#     while not ctrl_c:
#         cmd_publisher_object.move_robot(direction="turn", angle=0.2)
#         rospy.sleep(1)
#         rate.sleep()
    