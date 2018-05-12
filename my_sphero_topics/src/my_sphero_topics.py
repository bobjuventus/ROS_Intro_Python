#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist             # Import the Int32 message from the std_msgs package

# rospy.init_node('my_sphero_topics')         # Initiate a Node named 'my_sphero_topics'
# pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)    # Create a Publisher object, that will publish on the /counter topic
                                           #  messages of type Int32
class CmdVelPub(object):
    def __init__(self):
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.vel = Twist()
        self.linearspeed = 0.03
        self.angularspeed = 0.3
        
    def move_robot(self, direction):
        if direction == 'forwards':
            self.vel.linear.x = self.linearspeed
            self.vel.angular.z = 0.0
        elif direction == 'backwards':
            self.vel.linear.x = -self.linearspeed
            self.vel.angular.z = 0.0
        elif direction == 'left':
            self.vel.linear.x = self.linearspeed
            self.vel.angular.z = -self.angularspeed 
        elif direction == 'right':
            self.vel.linear.x = self.linearspeed
            self.vel.angular.z = self.angularspeed 
        elif direction == 'stop':
            self.vel.linear.x = 0.0
            self.vel.angular.z = 0.0
        else:
            pass
        
        self.pub.publish(self.vel)


if __name__ == "__main__":
    rospy.init_node('my_sphero_topics')
    cmd_publisher_object = CmdVelPub()
    
    rate = rospy.Rate(1)
    
    ctrl_c = False
    def shutdownhook():
        # works better than the rospy.is_shut_down()
        global ctrl_c
        global twist_object
        global pub
        
        rospy.loginfo("shutdown time!")
        
        ctrl_c = True
        cmd_publisher_object.move_robot(direction="stop")
    
    rospy.on_shutdown(shutdownhook)
    
    while not ctrl_c:
        cmd_publisher_object.move_robot(direction="backwards")
        rate.sleep()
    