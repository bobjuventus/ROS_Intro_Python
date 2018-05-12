#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse # you import the service message python classes generated from Empty.srv.
from move_bb8 import MoveBB8

def my_callback(request):
    print "My_callback has been called"
    
    """
    # BB8CustomServiceMessage
    float64 side       # The distance of each side of the square
    int32 repetitions    # The number of times BB-8 has to execute the square movement when the service is called
    ---
    bool success         # Did it achieve it?
    """
    move = MoveBB8()
    
    distance = request.side
    repetitions = request.repetitions
    
    for i in range(repetitions):
        move.square(distance)
    
    
    print "Did move"
    message = BB8CustomServiceMessageResponse()
    message.success = True
    
    return message # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split())) 

rospy.init_node('unit3_services_server') 
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , my_callback) # create the Service called my_service with the defined callback
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