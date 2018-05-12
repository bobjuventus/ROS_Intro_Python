#! /usr/bin/env python

import rospy
import time
from geometry_msgs.msg import Twist             # Import the Int32 message from the std_msgs package
from my_turtlebot2.srv import Trigger, TriggerResponse

# import sys
# # the mock-0.3.1 dir contains testcase.py, testutils.py & mock.py
# sys.path.append('/home/user/catkin_ws/src/my_sphero_topics/src')
from my_turtlebot2_topics import CmdVelPub
# sys.path.append('/home/user/catkin_ws/src/my_sphero_services/src')
from my_turtlebot2_services_server import CheckHitWall_Server
from my_turtlebot2_services_client import CheckHitWall_Client

class robotmaze(object):
    def __init__(self):
        self.cmd_publisher_object = CmdVelPub()
        self.turtlebot2_service_server_object = CheckHitWall_Server()
        time.sleep(1)
        self.turtlebot2_service_client_object = CheckHitWall_Client()
        
    def run(self):
        result = self.turtlebot2_service_client_object.feedback()
        direction = result.direction
        angle = result.angle
        distance = result.distance
        if direction == 'turn':
            self.cmd_publisher_object.move_robot(direction='turn', angle=angle)
            self.cmd_publisher_object.move_robot(direction='forwards')
            rospy.sleep(2)
            self.cmd_publisher_object.move_robot(direction='stop')
            new_result = self.turtlebot2_service_client_object.feedback()
            if new_result.distance > distance:
                self.cmd_publisher_object.move_robot(direction='forwards')
        elif direction == 'forwards':
            self.cmd_publisher_object.move_robot(direction='forwards')
        elif direction == 'backwards':
            self.cmd_publisher_object.move_robot(direction='backwards')
        else:
            pass
        
        # print self.turtlebot2_service_client_object.feedback()


if __name__ == "__main__":
    rospy.init_node('my_turtlebot2_main')
    mainobject = robotmaze()
    mainobject.cmd_publisher_object.move_robot(direction="forwards")
    rospy.sleep(1)
    rate = rospy.Rate(1)
    
    ctrl_c = False
    def shutdownhook():
        # works better than the rospy.is_shut_down()
        global ctrl_c
        global twist_object
        global pub
        
        rospy.loginfo("shutdown time!")
        
        ctrl_c = True
        mainobject.cmd_publisher_object.move_robot(direction="stop")
    
    rospy.on_shutdown(shutdownhook)
    
    while not ctrl_c:
        mainobject.run()
        rospy.sleep(1)

        rate.sleep()
    