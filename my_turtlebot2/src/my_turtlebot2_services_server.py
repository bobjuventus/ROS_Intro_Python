#! /usr/bin/env python

import rospy
import time
from sensor_msgs.msg import LaserScan
# from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from my_turtlebot2.srv import Trigger, TriggerResponse

class CheckHitWall_Server(object):
    def __init__(self):
        self.sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, self.my_LaserScan_callback)
        self.turtlebot2_service = rospy.Service('/check_hit_wall', Trigger, self.my_callback) # create the Service called my_service with the defined callback
        self.threshold = 0.5 # threshold to determine when to turn
        self.ranges = [] # initilize the ranges
        self.message = 'continue'
    
    def my_LaserScan_callback(self, msg):
        # print "My_LaserScan_callback has been called"
        self.ranges = msg.ranges

        # return EmptyResponse() # the service Response class, in this case EmptyResponse
        #return MyServiceResponse(len(request.words.split())) 
    
    
    def my_callback(self, request):
        # print "My_callback has been called"
        '''
        #no input
        ---
        string direction
        float32 angle
        float32 distance
        '''
        message = TriggerResponse()
        distance = min(self.ranges)
        if distance < self.threshold:
            size = len(self.ranges)
            loca_min = self.ranges.index(min(self.ranges))
            angle_min = loca_min*3.14/size
            loca_max = self.ranges.index(max(self.ranges))
            angle_max = loca_max*3.14/size
            turn_angle = angle_max - 1.57
            message.distance = distance
            message.direction = 'turn'
            message.angle = turn_angle
            
        else:
            message.distance = distance
            message.direction = 'forwards'
            message.angle = 0.0
        
        print message
        return message



# if __name__ == "__main__":
#     rospy.init_node('my_turtlebot2_services_server')
#     my_turtlebot2_service_object = CheckHitWall_Server()
#     time.sleep(1)
    
#     rate = rospy.Rate(1)
    
#     ctrl_c = False
#     def shutdownhook():
#         # works better than the rospy.is_shut_down()
#         global ctrl_c
#         global twist_object
#         global pub
        
#         rospy.loginfo("shutdown time!")
        
#         ctrl_c = True

#     rospy.on_shutdown(shutdownhook)
    
#     while not ctrl_c:
#         rate.sleep()
    
#     # rospy.spin()