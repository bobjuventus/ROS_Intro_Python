#! /usr/bin/env python

import rospy
import time
from sensor_msgs.msg import Imu
# from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from my_sphero_services.srv import Trigger, TriggerResponse

class CheckHitWall_Server(object):
    def __init__(self):
        self.sub = rospy.Subscriber('/sphero/imu/data3', Imu, self.my_Imu_callback)
        self.sphero_service = rospy.Service('/check_hit_wall', Trigger, self.my_callback) # create the Service called my_service with the defined callback
        self.threshold = 1.0 # threshold to decide if robot should has crashed
        # self.message = ""
    
    def my_Imu_callback(self, request):
        # print "My_Imu_callback has been called"
        self.accl = request.linear_acceleration
        # print self.accl.x
        # return EmptyResponse() # the service Response class, in this case EmptyResponse
        #return MyServiceResponse(len(request.words.split())) 
    
    
    def my_callback(self, request):
        print "My_callback has been called"
        '''
        #no input
        ---
        string direction
        '''
        message = TriggerResponse()
        message.direction = self.make_turn()
        return message
        
        
    def make_turn(self):
        # if self.accl.x > self.threshold or self.accl.z > self.threshold or self.accl.z < -self.threshold:
        if self.accl.x > self.threshold:
            print self.accl
            self.message = 'backwards'
        elif self.accl.x < -self.threshold:
            print self.accl.x
            self.message = 'forwards'
        elif self.accl.y > self.threshold:
            print self.accl.y
            self.message = 'left'
        elif self.accl.y < -self.threshold:
            print self.accl.y
            self.message = 'right'
        else:
            self.message = 'continue'
            
        return self.message



if __name__ == "__main__":
    rospy.init_node('my_sphero_services_server')
    # cmd_publisher_object = CmdVelPub()
    sphero_service_object = CheckHitWall_Server()
    time.sleep(1)
    
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
        print sphero_service_object.make_turn()
        rate.sleep()
    
    # rospy.spin()