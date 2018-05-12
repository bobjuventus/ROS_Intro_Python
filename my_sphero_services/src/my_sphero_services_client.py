#! /usr/bin/env python

import rospy
from my_sphero_services.srv import Trigger, TriggerRequest
import sys 
# import rospkg
# rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.
# traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"

class CheckHitWall_Client(object):
    def __init__(self):
        rospy.wait_for_service('/check_hit_wall') # Wait for the service client /gazebo/delete_model to be running
        self.exec_model_service = rospy.ServiceProxy('/check_hit_wall', Trigger) # Create the connection to the service
        self.exec_model_service_object = TriggerRequest()
        rospy.loginfo("Connected to the /check_hit_wall server.")
        
    def feedback(self):
        result = self.exec_model_service(self.exec_model_service_object)
        rospy.loginfo(str(result))
        return str(result.direction)

if __name__ == "__main__":
    rospy.init_node('my_sphero_services_client') # Initialise a ROS node with the name service_client

    TestClient = CheckHitWall_Client()
    rate = rospy.Rate(1)
    
    ctrl_c = False
    def shutdownhook():
        # works better than the rospy.is_shut_down()
        global ctrl_c
        global twist_object
        global pub
        
        rospy.loginfo("shutdown time!")
        
        ctrl_c = True

    rospy.on_shutdown(shutdownhook)
    
    while not ctrl_c:
        result = TestClient.feedback() # Send through the connection the name of the object to be deleted by the service
        rospy.loginfo(str(result))
        rate.sleep()
    
    # rospy.spin()


