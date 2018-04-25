#! /usr/bin/env python

import rospy
from iri_wam_reproduce_trajectory.srv import ExecTraj # Import the service message used by the service /gazebo/delete_model
import sys 
import rospkg
rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.
traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"

rospy.init_node('unit3_services_client') # Initialise a ROS node with the name service_client
rospy.wait_for_service('/execute_trajectory') # Wait for the service client /gazebo/delete_model to be running
exec_model_service = rospy.ServiceProxy('/execute_trajectory', ExecTraj) # Create the connection to the service
# kk = ExecTraj() # Create an object of type DeleteModelRequest
# kk.file = traj # Fill the variable model_name of this object with the desired value
result = exec_model_service(traj) # Send through the connection the name of the object to be deleted by the service
print result # Print the result given by the service called