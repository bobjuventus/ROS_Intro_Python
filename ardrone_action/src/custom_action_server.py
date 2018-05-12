#! /usr/bin/env python
import rospy
import time
import actionlib

from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from ardrone_action.msg import CustomActionMsgAction, CustomActionMsgResult, CustomActionMsgFeedback

class MoveUpDownClass(object):
    
    # create messages that are used to publish feedback/result
    _feedback = CustomActionMsgFeedback()
    _result   = CustomActionMsgResult()
  
    def __init__(self):
      # creates the action server
      self._as = actionlib.SimpleActionServer("custom_drone_as", CustomActionMsgAction, self.goal_callback, False)
      self._as.start()
      self.ctrl_c = False
      self.rate = rospy.Rate(1)
    
    def publish_once_in_cmd_vel(self, cmd):
        """
        This is because publishing in topics sometimes fails teh first time you publish.
        In continuos publishing systems there is no big deal but in systems that publish only
        once it IS very important.
        """
        while not self.ctrl_c:
            connections = self._move.get_num_connections()
            if connections > 0:
                self._move.publish(cmd)
                rospy.loginfo("Publish in cmd_vel...")
                break
            else:
                self.rate.sleep()
              
    # function that stops the drone from any movement
    def stop_drone(self):
      rospy.loginfo("Stopping...")
      self._move_msg.linear.z = 0.0
      self._move_msg.angular.z = 0.0
      self.publish_once_in_cmd_vel(self._move_msg)
      
    # function that makes the drone move up
    def move_up_drone(self):
      rospy.loginfo("Moving up...")
      self._move_msg.linear.z = 1.0
      self._move_msg.angular.z = 0.0
      self.publish_once_in_cmd_vel(self._move_msg)
      
    # function that makes the drone move down
    def move_down_drone(self):
      rospy.loginfo("Moving down...")
      self._move_msg.linear.z = -1.0
      self._move_msg.angular.z = 0.0
      self.publish_once_in_cmd_vel(self._move_msg)
      
    # main program
    def goal_callback(self, goal):
  # this callback is called when the action server is called.
  # this is the function that computes the Fibonacci sequence
  # and returns the sequence to the node that called the action server
  
  # helper variables
      success = True
      
      self._move = rospy.Publisher('/cmd_vel', Twist, queue_size=1) #Create a Publisher to move the drone
      self._move_msg = Twist() #Create the message to move the drone
      self._takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1) #Create a Publisher to takeoff the drone
      self._takeoff_msg = Empty() #Create the message to takeoff the drone
      self._land = rospy.Publisher('/drone/land', Empty, queue_size=1) #Create a Publisher to land the drone
      self._land_msg = Empty() #Create the message to land the drone
      
      
      i=0
      while not i == 3:
        self._takeoff.publish(self._takeoff_msg)
        rospy.loginfo('Taking off...')
        time.sleep(1)
        i += 1
    
      # define the direction to move the drone and seconds to move
      direction = goal.goal
      moveSeconds = 2.0
      
      i = 0
      
      # check that preempt (cancelation) has not been requested by the action client
      if self._as.is_preempt_requested():
        rospy.loginfo('The goal has been cancelled/preempted')
        # the following line, sets the client in preempted state (goal cancelled)
        self._as.set_preempted()
        success = False
  
      # Logic that makes the robot move forward and turn
      
      if direction == 'UP':
        self.move_up_drone()
        self._feedback.feedback = 'UP'
        self._as.publish_feedback(self._feedback)
        time.sleep(moveSeconds)
        self.stop_drone()
      elif direction == 'DOWN':
        self.move_down_drone()
        self._feedback.feedback = 'DOWN'
        self._as.publish_feedback(self._feedback)
        time.sleep(moveSeconds)
        self.stop_drone()
      else:
        self.stop_drone()
    
      # the sequence is computed at 1 Hz frequency
      self.rate.sleep()
    
    # at this point, either the goal has been achieved (success==true)
    # or the client preempted the goal (success==false)
    # If success, then we publish the final result
    # If not success, we do not publish anything in the result
  
      if success:
          self._result = Empty()
          self._as.set_succeeded(self._result)
          # make the drone stop and land
          self.stop_drone()
          i=0
          while not i == 3:
              self._land.publish(self._land_msg)
              rospy.loginfo('Landing...')
              time.sleep(1)
              i += 1 
      
if __name__ == '__main__':
  rospy.init_node('custom_action_server')
  MoveUpDownClass()
  rospy.spin()