#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
import sys 
# import rospkg
# rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.
# traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"

rospy.init_node('service_client') # Initialise a ROS node with the name service_client
rospy.wait_for_service('/move_bb8_in_square') # Wait for the service client /gazebo/delete_model to be running
exec_model_service = rospy.ServiceProxy('/move_bb8_in_square', Empty) # Create the connection to the service
# kk = ExecTraj() # Create an object of type DeleteModelRequest
# kk.file = traj # Fill the variable model_name of this object with the desired value
result = exec_model_service() # Send through the connection the name of the object to be deleted by the service
print result # Print the result given by the service called