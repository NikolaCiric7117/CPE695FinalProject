#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
class scan:
    
        
    def callback(self,msg):
     
      self.laser = msg.ranges
      

    def getLaser(self):
       print(self.laser)
      

a = scan()


