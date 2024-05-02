#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Path
import numpy as np


def callbackPath(path):
  global path_length
  path_length = 0
  for i in range(len(path.poses) - 1):
    position_a_x = path.poses[i].pose.position.x
    position_b_x = path.poses[i+1].pose.position.x
    position_a_y = path.poses[i].pose.position.y
    position_b_y = path.poses[i+1].pose.position.y

    path_length += np.sqrt(np.power((position_b_x - position_a_x), 2) + np.power((position_b_y- position_a_y), 2))

  print(path_length)



rospy.init_node("path")
rospy.Subscriber('/move_base/GlobalPlanner/plan',Path,callbackPath)

rospy.spin()