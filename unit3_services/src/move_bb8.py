#! /usr/bin/env python

import rospy
from iri_wam_reproduce_trajectory.srv import ExecTraj # Import the service message used by the service /gazebo/delete_model
import sys
import time

from geometry_msgs.msg import Twist             # Import the Int32 message from the std_msgs package

# rospy.init_node('unit3_services') # This should not be here!

class MoveBB8:
  def __init__(self):
    self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    self.ctrl_c = False
    rospy.on_shutdown(self.shutdownhook)
    self.rate = rospy.Rate(10) # 10hz
    
  def publish_once_in_cmd_vel(self, cmd):
    while not self.ctrl_c:
            connections = self.pub.get_num_connections()
            # print "connections: {}".format(connections)
            if connections > 1:
                self.pub.publish(cmd)
                # print "Cmd Published"
                break
            else:
                self.rate.sleep()  
  
  def shutdownhook(self):
      self.stop_bb8()
      self.ctrl_c = True
      
  def stop_bb8(self):
      cmd = Twist()
      cmd.linear.x = 0.0
      cmd.angular.z = 0.0
      self.publish_once_in_cmd_vel(cmd)
      
  def move_x_time(self, moving_time, linear_speed=0.2, angular_speed=0.2):
      cmd = Twist()
      cmd.linear.x = linear_speed
      cmd.angular.z = angular_speed
      self.publish_once_in_cmd_vel(cmd)
      time.sleep(moving_time)
      self.stop_bb8()
      
  
  def square(self):
      i = 0
      
      while not self.ctrl_c and i < 4:
          #Move forward
          self.move_x_time(moving_time=2.0, linear_speed=0.22, angular_speed=0.0)
          # Stop
          self.move_x_time(moving_time=4.0, linear_speed=0.0, angular_speed=0.0)
          # Turn 
          self.move_x_time(moving_time=3.0, linear_speed=0.0, angular_speed=0.3)
          # Stop
          self.move_x_time(moving_time=0.1, linear_speed=0.0, angular_speed=0.0)
          i += 1
      

if __name__ == '__main__':
    rospy.init_node('move_bb8_test', anonymous=True)
    movebb8_object = MoveBB8()
    try:
        movebb8_object.square()
    except rospy.ROSInterruptException:
        pass