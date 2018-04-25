#! /usr/bin/env python

import rospy                                          
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

# def shortest_distance(msg):                                    # Define a function called 'callback' that receives a parameter 
#                                                       # named 'msg'
#     return msg.range_min, msg.range_max  

rospy.init_node('wall_avoid')                   # Initiate a Node called 'topic_subscriber'

# try:
#     a = 3
# except KeyboardInterrupt:
#     print "Shutting down ROS Image feature detector module"
    
class avoid_wall:
    def __init__(self):
        self.min_range = None
        self.max_range = None
        self.ranges = [0,0,0]
        # self.sub = None
        
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, self.callback)
        
    def callback(self, msg):
        self.min_range = msg.range_min
        self.max_range = msg.range_max
        self.ranges = msg.ranges
        # self.sub = self.max_range - self.min_range
        # print self.min_range

    def distance_angle(self):
        size = len(self.ranges)
        loca = self.ranges.index(min(self.ranges))
        angle = loca*180.0/size
        distance = min(self.ranges)

        print "distance is {}".format(distance)
        print "angle is {}".format(angle)
        
        return distance, angle
        

    
    
test_avoid_wall = avoid_wall()


# def callback(msg):                                    # Define a function called 'callback' that receives a parameter 
#     minx = msg.range_min       
#                                                       # named 'msg'
#     return minx

# mind, maxd = rospy.Subscriber('/kobuki/laser/scan', LaserScan, shortest_distance)   # Create a Subscriber object that will listen to the /counter
# sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)   # Create a Subscriber object that will listen to the /counter
# print(minx)
# print(mind)
# print(maxd)
# pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)      

if __name__ == '__main__':
    vel = Twist()
    vel.linear.x = 0.0
    vel.angular.z = 0.0
                                     # Print the value 'data' inside the 'msg' parameter
    rate = rospy.Rate(2)
    # def increment(msg):
    #     count.data += 1
    #     rate.sleep()

    while not rospy.is_shutdown(): 
      dist, angle = test_avoid_wall.distance_angle()
      
      if dist < 2 and angle > 0.1 and angle < 70:
          vel.linear.x = 0.0
          vel.angular.z = 0.5
          test_avoid_wall.pub.publish(vel)
      elif dist < 2 and angle > 110 and angle < 180:
          vel.linear.x = 0.0
          vel.angular.z = -0.5
          test_avoid_wall.pub.publish(vel)
      elif dist < 2 and angle >= 70 and angle <= 90:
          vel.linear.x = 0.5
          vel.angular.z = 0.5
          test_avoid_wall.pub.publish(vel)
      elif dist < 2 and angle >= 90 and angle <= 110:
          vel.linear.x = 0.5
          vel.angular.z = -0.5
          test_avoid_wall.pub.publish(vel)
      else:
          vel.linear.x = 0.5
          vel.angular.z = 0.5
          test_avoid_wall.pub.publish(vel)
#   print test_avoid_wall.max_range
      rate.sleep()
          
                                                          # something from the topic
    rospy.spin() 