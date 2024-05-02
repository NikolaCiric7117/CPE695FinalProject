#!/usr/bin/env python3


import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Path

import numpy as np
import math


count = 0
velocity_added=0
average_velocity = 0
path_length=0
final_path_length =[]
laser = []
people_encountered = 0
amount = []


def callbackPath(path):
  global path_length
  global final_path_length

 
  for i in range(len(path.poses) - 1):
    position_a_x = path.poses[i].pose.position.x
    position_b_x = path.poses[i+1].pose.position.x
    position_a_y = path.poses[i].pose.position.y
    position_b_y = path.poses[i+1].pose.position.y

    path_length += np.sqrt(np.power((position_b_x - position_a_x), 2) + np.power((position_b_y- position_a_y), 2))
  final_path_length.append(path_length)
  
def callbackVelo(msg):
  global count
  global velocity_added
  global average_velocity
  
  total_v = math.sqrt(math.pow(msg.linear.x,2)+math.pow(msg.linear.y,2))
  
  if(total_v!=0):
    count+=1

    velocity_added += total_v
  average_velocity = velocity_added/count
  



  

rospy.init_node("get_stats")

rospy.Subscriber("/cmd_vel",Twist,callbackVelo)
rospy.Subscriber("/move_base/GlobalPlanner/plan",Path,callbackPath)

print("Press control C to exit and calcualte the stats")
rospy.sleep(5)
rospy.spin()

print("average velocity",average_velocity)
print("path_length",final_path_length[0])

time_taken_to_goal = final_path_length[0]/average_velocity
print("time taken to goal:",time_taken_to_goal)
