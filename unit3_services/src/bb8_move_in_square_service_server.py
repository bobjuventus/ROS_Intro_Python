#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from move_bb8 import MoveBB8

def my_callback(request):
    print "My_callback has been called"
    move = MoveBB8()
    move.square()
    print "Did move"
    return EmptyResponse() # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split())) 

rospy.init_node('unit3_services_server') 
my_service = rospy.Service('/move_bb8_in_square', Empty , my_callback) # create the Service called my_service with the defined callback
rospy.spin() # mantain the service open.

# import rospy
# from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.


# def my_callback(request):
#     print "My_callback has been called"
#     return EmptyResponse() # the service Response class, in this case EmptyResponse
#     #return MyServiceResponse(len(request.words.split())) 

# rospy.init_node('service_server') 
# my_service = rospy.Service('/my_service', Empty , my_callback) # create the Service called my_service with the defined callback
# rospy.spin() # mantain the service open.