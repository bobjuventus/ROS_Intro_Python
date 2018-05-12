#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest # you import the service message python classes generated from Empty.srv.
import sys 
# import rospkg
# rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.
# traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"

rospy.init_node('service_client') # Initialise a ROS node with the name service_client
rospy.wait_for_service('/move_bb8_in_square_custom') # Wait for the service client /gazebo/delete_model to be running
exec_model_service = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage) # Create the connection to the service
exec_model_service_object = BB8CustomServiceMessageRequest()

rospy.loginfo("Start Two Small Squares...")
exec_model_service_object.side = 2.0
exec_model_service_object.repetitions = 2

result = exec_model_service(exec_model_service_object) # Send through the connection the name of the object to be deleted by the service
rospy.loginfo(str(result))

rospy.loginfo("Start One Large Square...")
exec_model_service_object.side = 6.0
exec_model_service_object.repetitions = 1

# kk = ExecTraj() # Create an object of type DeleteModelRequest
# kk.file = traj # Fill the variable model_name of this object with the desired value
result = exec_model_service(exec_model_service_object) # Send through the connection the name of the object to be deleted by the service
rospy.loginfo(str(result))
